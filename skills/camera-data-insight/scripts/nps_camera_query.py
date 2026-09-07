#!/usr/bin/env python3
"""Query Camera telemetry with an NPS deviceId (Android ID / Athena items.aid)."""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import time
from datetime import date
from pathlib import Path
from typing import Any


DEFAULT_DATABASE = "dc_database"
DEFAULT_TABLE = "data_mobile_behavior"
DEFAULT_WORKGROUP = "ad_hoc"
POLL_INTERVAL_SECONDS = 2
POLL_TIMEOUT_SECONDS = 300


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("日期必须使用 YYYY-MM-DD 格式") from exc


def sql_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def masked_device_id(device_id: str) -> str:
    return f"{device_id[:4]}…{device_id[-4:]}"


def build_sql(args: argparse.Namespace) -> str:
    device_id = args.device_id.lower()
    project_filter = ""
    if args.project:
        project_filter = f"\n    AND project_name = {sql_literal(args.project)}"

    base = f"""WITH matched AS (
  SELECT
    event_date,
    from_unixtime(event_timestamp / 1000) AS event_time,
    project_name,
    device.model_name AS model_name,
    device.sw_build_info AS sw_build_info,
    element_at(filter(event_params, x -> x.key = 'photo_info'), 1).string_value AS photo_info,
    element_at(filter(event_params, x -> x.key = 'video_info'), 1).string_value AS video_info,
    element_at(filter(event_params, x -> x.key = 'activate_type'), 1).string_value AS activate_type,
    element_at(filter(event_params, x -> x.key = 'enter_method'), 1).string_value AS enter_method
  FROM {args.database}.{args.table}
  WHERE event_date BETWEEN {sql_literal(args.start_date.isoformat())} AND {sql_literal(args.end_date.isoformat())}
    AND event_name = 'NTCamera'
    AND lower(element_at(filter(items, x -> lower(x.key) = 'aid'), 1).string_value) = {sql_literal(device_id)}{project_filter}
)"""

    if args.mode == "detail":
        return base + f"""
SELECT
  event_date,
  event_time,
  project_name,
  model_name,
  sw_build_info,
  photo_info,
  video_info,
  activate_type,
  enter_method
FROM matched
ORDER BY event_time
LIMIT {args.limit}
"""

    return base + """
SELECT
  event_date,
  project_name,
  model_name,
  sw_build_info,
  count(*) AS camera_events,
  count_if(photo_info IS NOT NULL) AS photo_events,
  count_if(video_info IS NOT NULL) AS video_events,
  min(event_time) AS first_event_time,
  max(event_time) AS last_event_time
FROM matched
GROUP BY 1,2,3,4
ORDER BY event_date, camera_events DESC
"""


def make_session(args: argparse.Namespace) -> Any:
    try:
        import boto3
    except ImportError as exc:
        raise RuntimeError("缺少 boto3，请先执行：python3 -m pip install boto3") from exc

    profile = args.profile or os.environ.get("AWS_PROFILE")
    if profile:
        return boto3.Session(profile_name=profile, region_name=args.region)
    return boto3.Session(region_name=args.region)


def poll_query(athena: Any, query_id: str) -> dict[str, Any]:
    deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        execution = athena.get_query_execution(QueryExecutionId=query_id)["QueryExecution"]
        state = execution["Status"]["State"]
        if state in {"SUCCEEDED", "FAILED", "CANCELLED"}:
            return execution
        time.sleep(POLL_INTERVAL_SECONDS)
    athena.stop_query_execution(QueryExecutionId=query_id)
    raise RuntimeError(f"查询超过 {POLL_TIMEOUT_SECONDS} 秒，已停止：{query_id}")


def fetch_rows(athena: Any, query_id: str) -> tuple[list[str], list[list[str]]]:
    raw_rows: list[list[str]] = []
    token: str | None = None
    while True:
        request: dict[str, Any] = {"QueryExecutionId": query_id, "MaxResults": 1000}
        if token:
            request["NextToken"] = token
        response = athena.get_query_results(**request)
        for row in response["ResultSet"]["Rows"]:
            raw_rows.append([cell.get("VarCharValue", "") for cell in row.get("Data", [])])
        token = response.get("NextToken")
        if not token:
            break

    if not raw_rows:
        return [], []
    headers = raw_rows[0]
    width = len(headers)
    rows = [row + [""] * (width - len(row)) for row in raw_rows[1:]]
    return headers, rows


def default_output(args: argparse.Namespace) -> Path:
    safe_id = f"{args.device_id[:4]}-{args.device_id[-4:]}"
    name = f"nps-camera-{safe_id}-{args.start_date}-{args.end_date}-{args.mode}.csv"
    return Path.cwd() / name


def write_csv(path: Path, headers: list[str], rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        if headers:
            writer.writerow(headers)
            writer.writerows(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="使用 NPS deviceId 查询 Athena 中对应的相机埋点（匹配 items.aid）"
    )
    parser.add_argument("--device-id", required=True, help="NPS 返回的 16 位 deviceId / Android ID")
    parser.add_argument("--start-date", required=True, type=parse_date, help="开始日期，YYYY-MM-DD")
    parser.add_argument("--end-date", required=True, type=parse_date, help="结束日期，YYYY-MM-DD")
    parser.add_argument(
        "--region",
        required=True,
        choices=("ap-south-1", "eu-north-1"),
        help="印度用 ap-south-1；其他全球数据用 eu-north-1",
    )
    parser.add_argument("--project", help="可选：项目名，例如 SuperContra")
    parser.add_argument("--mode", choices=("summary", "detail"), default="summary")
    parser.add_argument("--limit", type=int, default=5000, help="detail 模式最大行数，默认 5000")
    parser.add_argument("--output", type=Path, help="CSV 输出路径")
    parser.add_argument("--profile", default=os.environ.get("AWS_PROFILE", "nothing"), help="AWS profile")
    parser.add_argument("--database", default=DEFAULT_DATABASE)
    parser.add_argument("--table", default=DEFAULT_TABLE)
    parser.add_argument("--workgroup", default=DEFAULT_WORKGROUP)
    parser.add_argument("--dry-run", action="store_true", help="只打印 SQL，不连接 Athena")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not re.fullmatch(r"[0-9a-fA-F]{16}", args.device_id):
        print("错误：deviceId 应为 16 位十六进制 Android ID", file=sys.stderr)
        return 2
    if args.start_date > args.end_date:
        print("错误：开始日期不能晚于结束日期", file=sys.stderr)
        return 2
    if args.limit < 1 or args.limit > 100000:
        print("错误：limit 必须在 1～100000 之间", file=sys.stderr)
        return 2

    sql = build_sql(args)
    if args.dry_run:
        print(sql)
        return 0

    try:
        session = make_session(args)
        athena = session.client("athena", region_name=args.region)
        response = athena.start_query_execution(
            QueryString=sql,
            QueryExecutionContext={"Database": args.database},
            WorkGroup=args.workgroup,
        )
        query_id = response["QueryExecutionId"]
        print(f"已提交查询：{query_id}")
        print(f"设备：{masked_device_id(args.device_id)}；区域：{args.region}")

        execution = poll_query(athena, query_id)
        state = execution["Status"]["State"]
        if state != "SUCCEEDED":
            reason = execution["Status"].get("StateChangeReason", "未知原因")
            print(f"查询失败：{state} - {reason}", file=sys.stderr)
            return 1

        headers, rows = fetch_rows(athena, query_id)
        output = (args.output or default_output(args)).expanduser().resolve()
        write_csv(output, headers, rows)
        scanned = execution.get("Statistics", {}).get("DataScannedInBytes", 0)
        print(f"查询完成：{len(rows)} 行；扫描 {scanned / 1024**3:.2f} GB")
        print(f"结果：{output}")
        return 0
    except Exception as exc:
        print(f"查询失败：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
