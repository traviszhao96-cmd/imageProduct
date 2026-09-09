#!/usr/bin/env python3
"""Resolve NPS refids to deviceIds through the authorized NPS lookup API."""

from __future__ import annotations

import argparse
import base64
import csv
import getpass
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


REFID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)
DEVICE_ID_RE = re.compile(r"^[0-9a-fA-F]{16}$")
DEFAULT_ENDPOINT = "https://push-backend.nothingtech.link/push/nps/executions/lookup"
MAX_BATCH_SIZE = 500


def normalize_header(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def find_refid_column(headers: list[str], requested: str | None) -> str:
    if requested:
        if requested not in headers:
            raise ValueError(f"找不到指定的 refid 列：{requested}")
        return requested
    for header in headers:
        if normalize_header(header) in {"refid", "ledgerid"}:
            return header
    raise ValueError("输入 CSV 中找不到 refid 列")


def load_refids(path: Path, requested_column: str | None) -> tuple[list[str], int]:
    with path.expanduser().open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("输入 CSV 没有表头")
        column = find_refid_column(reader.fieldnames, requested_column)
        raw = [(row.get(column) or "").strip() for row in reader]

    invalid = [value for value in raw if value and not REFID_RE.fullmatch(value)]
    if invalid:
        raise ValueError(f"发现 {len(invalid)} 个格式无效的 refid")
    unique = list(dict.fromkeys(value.lower() for value in raw if value))
    if not unique:
        raise ValueError("输入 CSV 中没有可查询的 refid")
    return unique, len(raw) - len(unique)


def lookup_batch(
    endpoint: str,
    username: str,
    password: str,
    refids: list[str],
    timeout: int,
) -> list[dict[str, object]]:
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
    request = urllib.request.Request(
        endpoint,
        data=json.dumps({"refids": refids}).encode(),
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.load(response)
    if payload.get("code") != "00000" or not isinstance(payload.get("data"), list):
        raise RuntimeError(payload.get("msg") or "NPS lookup 返回异常")
    rows = payload["data"]
    if len(rows) != len(refids):
        raise RuntimeError("NPS lookup 返回数量与请求数量不一致")
    for expected, row in zip(refids, rows):
        if not isinstance(row, dict) or row.get("refid", "").lower() != expected:
            raise RuntimeError("NPS lookup 返回顺序或 refid 不一致")
    return rows


def write_mapping(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["refid", "device_id", "device_id_raw", "mapping_status"])
        for row in rows:
            device_id = str(row.get("deviceId") or "").strip().lower()
            found = bool(row.get("found"))
            valid = bool(DEVICE_ID_RE.fullmatch(device_id))
            if found and valid:
                status = "found"
            elif found and not device_id:
                status = "found_no_device_id"
            elif found:
                status = "device_id_invalid"
            else:
                status = "not_found"
            writer.writerow(
                [row.get("refid", ""), device_id if valid else "", device_id, status]
            )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="批量查询 NPS refid 对应的 deviceId")
    parser.add_argument("--input-csv", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--refid-column")
    parser.add_argument("--username", default=os.environ.get("NPS_USERNAME"))
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--batch-size", type=int, default=MAX_BATCH_SIZE)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--retries", type=int, default=2)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.username:
        print("错误：请通过 --username 或 NPS_USERNAME 提供用户名", file=sys.stderr)
        return 2
    if not 1 <= args.batch_size <= MAX_BATCH_SIZE:
        print(f"错误：batch-size 必须在 1～{MAX_BATCH_SIZE} 之间", file=sys.stderr)
        return 2
    password = os.environ.get("NPS_PASSWORD") or getpass.getpass("NPS password: ")

    try:
        refids, duplicate_rows = load_refids(args.input_csv, args.refid_column)
        results: list[dict[str, object]] = []
        for offset in range(0, len(refids), args.batch_size):
            batch = refids[offset : offset + args.batch_size]
            for attempt in range(args.retries + 1):
                try:
                    results.extend(
                        lookup_batch(
                            args.endpoint, args.username, password, batch, args.timeout
                        )
                    )
                    break
                except (urllib.error.URLError, TimeoutError, RuntimeError):
                    if attempt >= args.retries:
                        raise
                    time.sleep(2**attempt)
            print(f"已查询 {min(offset + len(batch), len(refids))}/{len(refids)}")

        output = args.output_csv.expanduser().resolve()
        write_mapping(output, results)
        mapped = sum(bool(row.get("found")) and bool(DEVICE_ID_RE.fullmatch(str(row.get("deviceId") or ""))) for row in results)
        found_no_device = sum(bool(row.get("found")) and not str(row.get("deviceId") or "").strip() for row in results)
        invalid_device = sum(
            bool(row.get("found"))
            and bool(str(row.get("deviceId") or "").strip())
            and not bool(DEVICE_ID_RE.fullmatch(str(row.get("deviceId") or "").strip()))
            for row in results
        )
        not_found = sum(not bool(row.get("found")) for row in results)
        unique_devices = len(
            {
                str(row.get("deviceId")).lower()
                for row in results
                if row.get("found") and DEVICE_ID_RE.fullmatch(str(row.get("deviceId") or ""))
            }
        )
        print(
            f"完成：唯一 refid {len(refids)}；输入重复行 {duplicate_rows}；"
            f"mapped {mapped}；found 但无 deviceId {found_no_device}；"
            f"deviceId 格式异常 {invalid_device}；not found {not_found}；"
            f"唯一标准 deviceId {unique_devices}"
        )
        print(f"映射文件：{output}")
        return 0
    except Exception as exc:
        print(f"查询失败：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
