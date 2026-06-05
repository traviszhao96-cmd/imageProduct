#!/usr/bin/env python3
"""
Athena Query CLI for OpenClaw Camera Analytics.

A thin wrapper around boto3 that handles the full Athena query lifecycle:
  auth → submit → poll → fetch → render

Credential sources (checked in order):
  1. --profile / AWS_PROFILE env var
  2. Environment variables: AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY
  3. ~/.aws/credentials + ~/.aws/config
  4. --access-key / --secret-key / --session-token CLI args

Usage:
  # Smoke test auth + connectivity
  python3 scripts/athena_query_cli.py smoke

  # Run a query (auto-polls until complete)
  python3 scripts/athena_query_cli.py query --sql "SELECT * FROM dc_database.data_mobile_behavior LIMIT 10"

  # Run query from file
  python3 scripts/athena_query_cli.py query --sql-file query.sql

  # Poll an existing query
  python3 scripts/athena_query_cli.py poll --query-id "abc123..."

  # Describe a table
  python3 scripts/athena_query_cli.py describe --table data_mobile_behavior

  # List databases
  python3 scripts/athena_query_cli.py databases

  # List tables in a database
  python3 scripts/athena_query_cli.py tables --database dc_database

  # Setup credentials interactively
  python3 scripts/athena_query_cli.py setup
"""

from __future__ import annotations

import argparse
import configparser
import json
import os
import sys
import time

# ── 启动检查：boto3 必须可用 (否则快速失败，不挂起) ──────
try:
    import boto3
except ImportError:
    print("❌ boto3 未安装，请通过 wrapper 执行:", file=sys.stderr)
    print("   scripts/athena_query.sh query --sql ...", file=sys.stderr)
    sys.exit(1)

from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / ".athena_config.json"

# ── Defaults ────────────────────────────────────────────────────────
DEFAULT_REGION = "eu-north-1"      # 全球数据默认斯德哥尔摩; 印度用 ap-south-1
DEFAULT_DATABASE = "dc_database"
DEFAULT_WORKGROUP = "ad_hoc"        # 单次 <1TB 用 ad_hoc; >1TB 用 BigData
MAX_POLL_SECONDS = 300
POLL_INTERVAL_SECONDS = 2


# ── Credential Resolution ───────────────────────────────────────────

def _get_boto3_session(args: argparse.Namespace) -> Any:
    """Build a boto3 session from available credential sources."""
    import boto3

    # 1. CLI --profile / env AWS_PROFILE
    profile = args.profile or os.environ.get("AWS_PROFILE")
    if profile:
        return boto3.Session(profile_name=profile, region_name=args.region or DEFAULT_REGION)

    # 2. Try saved config file
    if CONFIG_FILE.exists():
        cfg = json.loads(CONFIG_FILE.read_text())
        if cfg.get("profile"):
            return boto3.Session(
                profile_name=cfg["profile"],
                region_name=cfg.get("region", DEFAULT_REGION),
            )
        if cfg.get("access_key_id") and cfg.get("secret_access_key"):
            return boto3.Session(
                aws_access_key_id=cfg["access_key_id"],
                aws_secret_access_key=cfg["secret_access_key"],
                aws_session_token=cfg.get("session_token"),
                region_name=cfg.get("region", DEFAULT_REGION),
            )
    if profile:
        return boto3.Session(profile_name=profile, region_name=args.region or DEFAULT_REGION)

    # 3. Env vars (AWS_ACCESS_KEY_ID etc.)
    if os.environ.get("AWS_ACCESS_KEY_ID") and os.environ.get("AWS_SECRET_ACCESS_KEY"):
        return boto3.Session(region_name=args.region or DEFAULT_REGION)

    # 4. CLI args directly
    if args.access_key and args.secret_key:
        return boto3.Session(
            aws_access_key_id=args.access_key,
            aws_secret_access_key=args.secret_key,
            aws_session_token=args.session_token,
            region_name=args.region or DEFAULT_REGION,
        )

    # 5. Fall back to default credential chain (~/.aws, instance profile, etc.)
    return boto3.Session(region_name=args.region or DEFAULT_REGION)


# ── Command: smoke ───────────────────────────────────────────────────

def cmd_smoke(session: Any, args: argparse.Namespace) -> int:
    """Verify auth, connectivity, and workgroup access."""
    try:
        sts = session.client("sts")
        identity = sts.get_caller_identity()
        print(f"✅ 身份验证成功")
        print(f"   Account: {identity['Account']}")
        print(f"   Arn: {identity['Arn']}")

        region = args.region or DEFAULT_REGION
        athena = session.client("athena", region_name=region)
        database = args.database or DEFAULT_DATABASE
        workgroup = args.workgroup or DEFAULT_WORKGROUP

        # Run lightweight query
        sql = "SELECT CURRENT_DATE AS query_date, CURRENT_TIMESTAMP AS query_timestamp"
        resp = athena.start_query_execution(
            QueryString=sql,
            QueryExecutionContext={"Database": database},
            WorkGroup=workgroup,
        )
        query_id = resp["QueryExecutionId"]

        # Poll until complete
        status = _poll_until_done(athena, query_id)

        if status == "SUCCEEDED":
            result = athena.get_query_results(QueryExecutionId=query_id, MaxResults=5)
            data = _render_result(result)
            stats_bytes = _get_stats(athena, query_id)
            print(f"✅ Athena smoke query 成功")
            print(f"   QueryId: {query_id}")
            print(f"   DataScanned: {stats_bytes}")
            print(f"   Result:")
            for line in data:
                print(f"     {line}")
        else:
            reason = _get_status_reason(athena, query_id)
            print(f"❌ Query 失败: {status} - {reason}")
            return 1

        # Verify table access
        try:
            sql2 = f"SELECT * FROM {database}.data_mobile_behavior LIMIT 0"
            resp2 = athena.start_query_execution(
                QueryString=sql2,
                QueryExecutionContext={"Database": database},
                WorkGroup=workgroup,
            )
            qid2 = resp2["QueryExecutionId"]
            status2 = _poll_until_done(athena, qid2)
            if status2 == "SUCCEEDED":
                result2 = athena.get_query_results(QueryExecutionId=qid2, MaxResults=2)
                cols = [c.get("Label", c.get("Name", "?")) for c in result2["ResultSet"]["ResultSetMetadata"]["ColumnInfo"]]
                print(f"✅ 表结构验证成功: {database}.data_mobile_behavior")
                print(f"   列数: {len(cols)}")
                print(f"   列名: {', '.join(cols[:15])}{'...' if len(cols) > 15 else ''}")
            else:
                reason2 = _get_status_reason(athena, qid2)
                print(f"⚠️  表验证失败: {status2} - {reason2}")
        except Exception as e:
            print(f"⚠️  表验证异常: {e}")

        return 0
    except Exception as e:
        print(f"❌ Smoke test 失败: {e}", file=sys.stderr)
        return 1


# ── Command: query ───────────────────────────────────────────────────

def cmd_query(session: Any, args: argparse.Namespace) -> int:
    """Submit SQL, poll until done, print results."""
    region = args.region or DEFAULT_REGION
    athena = session.client("athena", region_name=region)
    database = args.database or DEFAULT_DATABASE
    workgroup = args.workgroup or DEFAULT_WORKGROUP
    max_rows = args.max_rows or 200

    # Resolve SQL
    if args.sql:
        sql = args.sql
    elif args.sql_file:
        sql = Path(args.sql_file).expanduser().read_text(encoding="utf-8")
    else:
        print("❌ 需要提供 --sql 或 --sql-file", file=sys.stderr)
        return 1

    # Submit (workgroup already has output location configured)
    try:
        kwargs = {
            "QueryString": sql,
            "QueryExecutionContext": {"Database": database},
            "WorkGroup": workgroup,
        }
        resp = athena.start_query_execution(**kwargs)
        query_id = resp["QueryExecutionId"]
    except Exception as e:
        print(f"❌ 提交查询失败: {e}", file=sys.stderr)
        return 1

    if args.async_mode:
        print(query_id)
        return 0

    # Poll
    print(f"📊 QueryId: {query_id}", file=sys.stderr)
    status = _poll_until_done(athena, query_id)

    if status != "SUCCEEDED":
        reason = _get_status_reason(athena, query_id)
        stats = _get_full_stats(athena, query_id)
        print(f"❌ 查询失败 ({status}): {reason}", file=sys.stderr)
        print(f"   Stats: {stats}", file=sys.stderr)
        return 1

    # Fetch & render
    stats = _get_full_stats(athena, query_id)
    print(f"📊 {stats}", file=sys.stderr)

    all_rows = _fetch_all_results(athena, query_id, max_rows)
    if not all_rows:
        print("(empty result set)")
        return 0

    # Print as TSV for easy piping
    columns = list(all_rows[0].keys())
    if not args.json_output:
        print("\t".join(columns))
    for row in all_rows:
        if args.json_output:
            print(json.dumps(row, ensure_ascii=False, default=str))
        else:
            print("\t".join(str(row.get(c, "")) for c in columns))

    print(f"\n📊 返回 {len(all_rows)} 行 (限制 {max_rows})", file=sys.stderr)
    return 0


# ── Command: poll ────────────────────────────────────────────────────

def cmd_poll(session: Any, args: argparse.Namespace) -> int:
    region = args.region or DEFAULT_REGION
    athena = session.client("athena", region_name=region)
    query_id = args.query_id
    max_rows = args.max_rows or 200

    status = _poll_until_done(athena, query_id)

    if status == "SUCCEEDED":
        stats = _get_full_stats(athena, query_id)
        print(f"✅ 状态: {status} | {stats}", file=sys.stderr)
        all_rows = _fetch_all_results(athena, query_id, max_rows)
        if all_rows:
            columns = list(all_rows[0].keys())
            print("\t".join(columns))
            for row in all_rows:
                print("\t".join(str(row.get(c, "")) for c in columns))
            print(f"\n📊 返回 {len(all_rows)} 行", file=sys.stderr)
        else:
            print("(empty result set)")
        return 0
    else:
        reason = _get_status_reason(athena, query_id)
        print(f"❌ {status}: {reason}")
        return 1


# ── Command: describe ────────────────────────────────────────────────

def cmd_describe(session: Any, args: argparse.Namespace) -> int:
    region = args.region or DEFAULT_REGION
    athena = session.client("athena", region_name=region)
    database = args.database or DEFAULT_DATABASE
    workgroup = args.workgroup or DEFAULT_WORKGROUP

    table = args.table
    sql = f"DESCRIBE {database}.{table}"

    resp = athena.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={"Database": database},
        WorkGroup=workgroup,
    )
    query_id = resp["QueryExecutionId"]

    print(f"🔍 查询 {database}.{table} 结构... QueryId: {query_id}", file=sys.stderr)
    status = _poll_until_done(athena, query_id)

    if status != "SUCCEEDED":
        reason = _get_status_reason(athena, query_id)
        print(f"❌ DESCRIBE 失败: {status} - {reason}", file=sys.stderr)
        return 1

    all_rows = _fetch_all_results(athena, query_id, 500)
    if not all_rows:
        print("(no columns found)")
        return 0

    for row in all_rows:
        print(f"{row.get('col_name',''):40s} {row.get('data_type',''):20s} {row.get('comment','')}")
    print(f"\n📊 {len(all_rows)} 列", file=sys.stderr)
    return 0


# ── Command: databases / tables ──────────────────────────────────────

def cmd_databases(session: Any, args: argparse.Namespace) -> int:
    region = args.region or DEFAULT_REGION
    athena = session.client("athena", region_name=region)
    workgroup = args.workgroup or DEFAULT_WORKGROUP

    sql = "SHOW DATABASES"
    resp = athena.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={"Catalog": "AwsDataCatalog"},
        WorkGroup=workgroup,
    )
    query_id = resp["QueryExecutionId"]
    _poll_until_done(athena, query_id)
    for row in _fetch_all_results(athena, query_id, 100):
        print(list(row.values())[0])
    return 0


def cmd_tables(session: Any, args: argparse.Namespace) -> int:
    region = args.region or DEFAULT_REGION
    athena = session.client("athena", region_name=region)
    database = args.database or DEFAULT_DATABASE
    workgroup = args.workgroup or DEFAULT_WORKGROUP

    sql = f"SHOW TABLES IN {database}"
    resp = athena.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={"Database": database},
        WorkGroup=workgroup,
    )
    query_id = resp["QueryExecutionId"]
    print(f"📊 列出 {database} 中的表...", file=sys.stderr)
    _poll_until_done(athena, query_id)
    for row in _fetch_all_results(athena, query_id, 200):
        print(list(row.values())[0])
    return 0


# ── Command: setup ───────────────────────────────────────────────────

def cmd_setup(session: Any, args: argparse.Namespace) -> int:
    """Interactive credential configuration."""
    import getpass

    print("=== Athena 凭证配置 ===\n")

    choice = input("凭证方式: [1] AWS Profile [2] Access Key: ").strip()
    cfg = {}

    if choice == "1":
        profile = input("Profile 名称 (默认 default): ").strip() or "default"
        region = input(f"Region (默认 {DEFAULT_REGION}): ").strip() or DEFAULT_REGION
        cfg = {"profile": profile, "region": region}
    elif choice == "2":
        access_key = input("AWS_ACCESS_KEY_ID: ").strip()
        secret_key = getpass.getpass("AWS_SECRET_ACCESS_KEY: ").strip()
        session_token = getpass.getpass("AWS_SESSION_TOKEN (可选): ").strip()
        region = input(f"Region (默认 {DEFAULT_REGION}): ").strip() or DEFAULT_REGION
        cfg = {
            "access_key_id": access_key,
            "secret_access_key": secret_key,
            "region": region,
        }
        if session_token:
            cfg["session_token"] = session_token
    else:
        print("❌ 无效选择", file=sys.stderr)
        return 1

    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))
    print(f"✅ 凭证已保存到 {CONFIG_FILE}")
    return 0


# ── Helpers ──────────────────────────────────────────────────────────

def _poll_until_done(athena: Any, query_id: str) -> str:
    elapsed = 0
    while elapsed < MAX_POLL_SECONDS:
        resp = athena.get_query_execution(QueryExecutionId=query_id)
        status = resp["QueryExecution"]["Status"]["State"]
        if status in ("SUCCEEDED", "FAILED", "CANCELLED"):
            return status
        time.sleep(POLL_INTERVAL_SECONDS)
        elapsed += POLL_INTERVAL_SECONDS
        if elapsed % 10 == 0:
            print(f"   ⏳ 轮询中... {elapsed}s", file=sys.stderr)
    return "TIMEOUT"


def _get_status_reason(athena: Any, query_id: str) -> str:
    try:
        resp = athena.get_query_execution(QueryExecutionId=query_id)
        return resp["QueryExecution"]["Status"].get("StateChangeReason", "unknown")
    except Exception:
        return "unknown"


def _get_stats(athena: Any, query_id: str) -> str:
    try:
        resp = athena.get_query_execution(QueryExecutionId=query_id)
        stats = resp["QueryExecution"].get("Statistics", {})
        scanned = stats.get("DataScannedInBytes", 0)
        if scanned >= 1_000_000_000:
            return f"{scanned / 1_000_000_000:.2f} GB"
        if scanned >= 1_000_000:
            return f"{scanned / 1_000_000:.2f} MB"
        if scanned >= 1_000:
            return f"{scanned / 1_000:.2f} KB"
        return f"{scanned} B"
    except Exception:
        return "N/A"


def _get_full_stats(athena: Any, query_id: str) -> str:
    try:
        resp = athena.get_query_execution(QueryExecutionId=query_id)
        stats = resp["QueryExecution"].get("Statistics", {})
        scanned = stats.get("DataScannedInBytes", 0)
        runtime = stats.get("EngineExecutionTimeInMillis", 0) / 1000
        if scanned >= 1_000_000_000:
            size = f"{scanned / 1_000_000_000:.2f}GB"
        elif scanned >= 1_000_000:
            size = f"{scanned / 1_000_000:.2f}MB"
        else:
            size = f"{scanned / 1_000:.2f}KB"
        return f"扫描 {size} | 耗时 {runtime:.1f}s"
    except Exception:
        return "N/A"


def _fetch_all_results(athena: Any, query_id: str, max_rows: int) -> list[dict]:
    all_rows: list[dict] = []
    next_token: str | None = None

    while len(all_rows) < max_rows:
        kwargs = {"QueryExecutionId": query_id, "MaxResults": min(1000, max_rows - len(all_rows))}
        if next_token:
            kwargs["NextToken"] = next_token

        resp = athena.get_query_results(**kwargs)
        result_set = resp["ResultSet"]
        columns = [c.get("Label", c.get("Name", "?")) for c in result_set["ResultSetMetadata"]["ColumnInfo"]]

        data = result_set.get("Rows", [])
        if len(data) <= 1:
            break  # header only

        for row in data[1:]:  # skip header
            values = row.get("Data", [])
            all_rows.append({columns[i]: values[i].get("VarCharValue", "") if i < len(values) else "" for i in range(len(columns))})

        next_token = resp.get("NextToken")
        if not next_token:
            break

    return all_rows


def _render_result(result: dict) -> list[str]:
    result_set = result["ResultSet"]
    columns = [c.get("Label", c.get("Name", "?")) for c in result_set["ResultSetMetadata"]["ColumnInfo"]]
    lines = []
    for row in result_set.get("Rows", [])[:10]:
        values = [v.get("VarCharValue", "") for v in row.get("Data", [])]
        lines.append(" | ".join(values))
    return lines


# ── Main ─────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Athena Query CLI for OpenClaw Camera Analytics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s smoke                               # Verify auth + connectivity
  %(prog)s query --sql "SELECT * FROM dc_database.data_mobile_behavior LIMIT 10"
  %(prog)s query --sql-file analysis.sql --json-output
  %(prog)s query --sql "..." --async-mode      # Submit and return query-id
  %(prog)s poll --query-id "abc..."            # Poll existing query
  %(prog)s describe --table data_mobile_behavior
  %(prog)s databases                            # List all databases
  %(prog)s tables --database dc_database        # List tables
  %(prog)s setup                                # Configure credentials
""",
    )

    subparsers = parser.add_subparsers(dest="command")

    # smoke
    p_smoke = subparsers.add_parser("smoke", help="Verify auth + connectivity")

    # query
    p_query = subparsers.add_parser("query", help="Run SQL and fetch results")
    p_query.add_argument("--sql", help="Inline SQL to execute")
    p_query.add_argument("--sql-file", help="Path to SQL file")
    p_query.add_argument("--async-mode", action="store_true", help="Submit query and return QueryExecutionId only")
    p_query.add_argument("--max-rows", type=int, default=200, help="Maximum rows to return (default: 200)")
    p_query.add_argument("--json-output", action="store_true", help="Output results as JSON Lines")

    # poll
    p_poll = subparsers.add_parser("poll", help="Poll an existing query for results")
    p_poll.add_argument("--query-id", required=True, help="QueryExecutionId")
    p_poll.add_argument("--max-rows", type=int, default=200, help="Maximum rows to return (default: 200)")

    # describe
    p_desc = subparsers.add_parser("describe", help="Describe a table")
    p_desc.add_argument("--table", required=True, help="Table name")

    # databases
    subparsers.add_parser("databases", help="List databases")

    # tables
    p_tables = subparsers.add_parser("tables", help="List tables in a database")

    # setup
    subparsers.add_parser("setup", help="Configure AWS credentials")

    # Common args for all commands
    for p in [p_smoke, p_query, p_poll, p_desc, p_tables]:
        p.add_argument("--profile", help="AWS profile name")
        p.add_argument("--access-key", help="AWS access key ID")
        p.add_argument("--secret-key", help="AWS secret access key")
        p.add_argument("--session-token", help="AWS session token")
        p.add_argument("--region", default=DEFAULT_REGION, help=f"AWS region (default: {DEFAULT_REGION})")
        p.add_argument("--database", default=DEFAULT_DATABASE, help=f"Athena database (default: {DEFAULT_DATABASE})")
        p.add_argument("--workgroup", default=DEFAULT_WORKGROUP, help=f"Athena workgroup (default: {DEFAULT_WORKGROUP})")
        if p != p_query:
            p.add_argument("--output", help="S3 output location")

    for p in [p_query, p_poll]:
        pass  # already have their specific args

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == "setup":
        return cmd_setup(None, args)  # type: ignore[arg-type]

    try:
        session = _get_boto3_session(args)
    except Exception as e:
        print(f"❌ 无法创建 AWS session: {e}", file=sys.stderr)
        print("   请先运行 setup 命令配置凭证，或设置 AWS_PROFILE 环境变量", file=sys.stderr)
        return 1

    commands = {
        "smoke": cmd_smoke,
        "query": cmd_query,
        "poll": cmd_poll,
        "describe": cmd_describe,
        "databases": cmd_databases,
        "tables": cmd_tables,
    }

    return commands[args.command](session, args)


if __name__ == "__main__":
    sys.exit(main())
