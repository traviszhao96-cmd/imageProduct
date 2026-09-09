#!/usr/bin/env python3
"""Batch-query Camera telemetry using NPS deviceIds mapped to Athena items.aid."""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import time
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Iterable


DEVICE_ID_RE = re.compile(r"^[0-9a-fA-F]{16}$")
DEFAULT_DATABASE = "dc_database"
DEFAULT_TABLE = "data_mobile_behavior"
DEFAULT_WORKGROUP = "ad_hoc"
POLL_INTERVAL_SECONDS = 2
POLL_TIMEOUT_SECONDS = 300
MAX_DEVICES = 500


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("日期必须使用 YYYY-MM-DD 格式") from exc


def normalize_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def sql_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def find_column(headers: Iterable[str], candidates: set[str]) -> str | None:
    for header in headers:
        if normalize_header(header) in candidates:
            return header
    return None


def load_mapping(path: Path) -> tuple[list[str], dict[str, list[str]], list[str]]:
    with path.expanduser().open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("映射 CSV 没有表头")
        device_col = find_column(reader.fieldnames, {"deviceid", "aid", "androidid"})
        refid_col = find_column(reader.fieldnames, {"refid", "ledgerid"})
        status_col = find_column(reader.fieldnames, {"status", "result", "lookupresult"})
        if not device_col:
            raise ValueError("映射 CSV 中找不到 Device ID 列")

        refids_by_device: dict[str, list[str]] = defaultdict(list)
        invalid: list[str] = []
        devices: list[str] = []
        seen: set[str] = set()
        for row_number, row in enumerate(reader, start=2):
            if status_col and row.get(status_col, "").strip().lower() not in {"", "found", "success"}:
                continue
            device_id = row.get(device_col, "").strip().lower()
            if not device_id:
                continue
            if not DEVICE_ID_RE.fullmatch(device_id):
                invalid.append(f"第 {row_number} 行：{device_id}")
                continue
            if device_id not in seen:
                devices.append(device_id)
                seen.add(device_id)
            if refid_col:
                refid = row.get(refid_col, "").strip()
                if refid and refid not in refids_by_device[device_id]:
                    refids_by_device[device_id].append(refid)
        return devices, dict(refids_by_device), invalid


def collect_devices(args: argparse.Namespace) -> tuple[list[str], dict[str, list[str]]]:
    devices: list[str] = []
    refids_by_device: dict[str, list[str]] = {}
    invalid: list[str] = []

    if args.mapping_csv:
        mapped, refids_by_device, invalid = load_mapping(args.mapping_csv)
        devices.extend(mapped)

    for raw in args.device_id or []:
        value = raw.strip().lower()
        if not DEVICE_ID_RE.fullmatch(value):
            invalid.append(value)
        elif value not in devices:
            devices.append(value)

    if invalid:
        preview = ", ".join(invalid[:5])
        suffix = " …" if len(invalid) > 5 else ""
        raise ValueError(f"发现 {len(invalid)} 个无效 deviceId：{preview}{suffix}")
    if not devices:
        raise ValueError("没有可查询的 deviceId")
    if len(devices) > MAX_DEVICES:
        raise ValueError(f"单次最多查询 {MAX_DEVICES} 个唯一 deviceId，当前为 {len(devices)} 个")
    return devices, refids_by_device


def build_sql(args: argparse.Namespace, device_ids: list[str]) -> str:
    id_list = ", ".join(sql_literal(value) for value in device_ids)
    project_filter = ""
    if args.project:
        project_filter = f"\n    AND project_name = {sql_literal(args.project)}"

    base = f"""WITH matched AS (
  SELECT
    lower(element_at(filter(items, x -> lower(x.key) = 'aid'), 1).string_value) AS aid,
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
    AND lower(element_at(filter(items, x -> lower(x.key) = 'aid'), 1).string_value) IN ({id_list}){project_filter}
)"""

    if args.mode == "detail":
        return base + f"""
SELECT aid, event_date, event_time, project_name, model_name, sw_build_info,
       photo_info, video_info, activate_type, enter_method
FROM matched
ORDER BY aid, event_time
LIMIT {args.limit}
"""

    return base + """
SELECT aid, event_date, project_name, model_name, sw_build_info,
       count(*) AS camera_events,
       count_if(photo_info IS NOT NULL) AS photo_events,
       count_if(video_info IS NOT NULL) AS video_events,
       min(event_time) AS first_event_time,
       max(event_time) AS last_event_time
FROM matched
GROUP BY 1,2,3,4,5
ORDER BY aid, event_date, camera_events DESC
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


def enrich_with_refids(
    headers: list[str], rows: list[list[str]], refids_by_device: dict[str, list[str]]
) -> tuple[list[str], list[list[str]]]:
    if not refids_by_device or not headers or "aid" not in headers:
        return headers, rows
    aid_index = headers.index("aid")
    enriched = []
    for row in rows:
        aid = row[aid_index].lower() if aid_index < len(row) else ""
        enriched.append([";".join(refids_by_device.get(aid, []))] + row)
    return ["refids"] + headers, enriched


def default_output(args: argparse.Namespace) -> Path:
    return Path.cwd() / f"nps-camera-{args.start_date}-{args.end_date}-{args.mode}.csv"


def write_csv(path: Path, headers: list[str], rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        if headers:
            writer.writerow(headers)
            writer.writerows(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="批量使用 NPS deviceId 查询 Athena Camera 埋点（items.aid）"
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--device-id", action="append", help="16 位 deviceId，可重复传入")
    source.add_argument("--mapping-csv", type=Path, help="NPS 系统导出的 refid/deviceId CSV")
    parser.add_argument("--start-date", required=True, type=parse_date)
    parser.add_argument("--end-date", required=True, type=parse_date)
    parser.add_argument(
        "--region", required=True, choices=("ap-south-1", "eu-north-1"),
        help="印度用 ap-south-1；其他全球数据用 eu-north-1",
    )
    parser.add_argument("--project", help="可选项目名，例如 SuperContra")
    parser.add_argument("--mode", choices=("summary", "detail"), default="summary")
    parser.add_argument("--limit", type=int, default=10000, help="detail 模式最大行数")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--profile", default=os.environ.get("AWS_PROFILE", "nothing"))
    parser.add_argument("--database", default=DEFAULT_DATABASE)
    parser.add_argument("--table", default=DEFAULT_TABLE)
    parser.add_argument("--workgroup", default=DEFAULT_WORKGROUP)
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.start_date > args.end_date:
        print("错误：开始日期不能晚于结束日期", file=sys.stderr)
        return 2
    if args.limit < 1 or args.limit > 100000:
        print("错误：limit 必须在 1～100000 之间", file=sys.stderr)
        return 2

    try:
        device_ids, refids_by_device = collect_devices(args)
        sql = build_sql(args, device_ids)
        if args.dry_run:
            print(f"-- unique_device_ids: {len(device_ids)}")
            print(sql)
            return 0

        session = make_session(args)
        athena = session.client("athena", region_name=args.region)
        response = athena.start_query_execution(
            QueryString=sql,
            QueryExecutionContext={"Database": args.database},
            WorkGroup=args.workgroup,
        )
        query_id = response["QueryExecutionId"]
        print(f"已提交查询：{query_id}；设备数：{len(device_ids)}；区域：{args.region}")
        execution = poll_query(athena, query_id)
        state = execution["Status"]["State"]
        if state != "SUCCEEDED":
            reason = execution["Status"].get("StateChangeReason", "未知原因")
            raise RuntimeError(f"{state} - {reason}")

        headers, rows = fetch_rows(athena, query_id)
        headers, rows = enrich_with_refids(headers, rows, refids_by_device)
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
