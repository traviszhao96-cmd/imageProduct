#!/usr/bin/env python3
"""Query the remote SQLite query service from a local machine."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Remote analytics query client")
    subparsers = parser.add_subparsers(dest="command", required=True)

    query_parser = subparsers.add_parser("query", help="Run SQL against remote service")
    query_parser.add_argument("--base-url", help="Service base URL")
    query_parser.add_argument("--token", help="Bearer token")
    query_parser.add_argument("--sql", help="Inline SQL")
    query_parser.add_argument("--sql-file", help="SQL file path")
    query_parser.add_argument("--max-rows", type=int, default=200, help="Returned row limit")

    tables_parser = subparsers.add_parser("tables", help="List remote tables")
    tables_parser.add_argument("--base-url", help="Service base URL")
    tables_parser.add_argument("--token", help="Bearer token")

    return parser.parse_args()


def resolve_base_url(raw: str | None) -> str:
    value = str(raw or os.environ.get("ANALYTICS_QUERY_BASE_URL") or "").strip().rstrip("/")
    if not value:
        raise RuntimeError("missing_base_url")
    return value


def resolve_token(raw: str | None) -> str:
    return str(raw or os.environ.get("ANALYTICS_QUERY_TOKEN") or "").strip()


def read_sql(inline_sql: str | None, sql_file: str | None) -> str:
    if inline_sql and sql_file:
        raise RuntimeError("use_sql_or_sql_file_not_both")
    if inline_sql:
        return inline_sql
    if sql_file:
        return Path(sql_file).expanduser().read_text(encoding="utf-8")
    raise RuntimeError("missing_sql")


def request_json(url: str, method: str, token: str, payload: dict | None = None) -> dict:
    data = None
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, method=method, headers=headers, data=data)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"http_{exc.code}: {detail}") from exc


def render_table(columns: list[str], rows: list[dict]) -> str:
    if not columns:
        return "(no columns)"
    widths = {column: len(column) for column in columns}
    for row in rows:
        for column in columns:
            widths[column] = max(widths[column], len(str(row.get(column, ""))))
    header = " | ".join(column.ljust(widths[column]) for column in columns)
    divider = "-+-".join("-" * widths[column] for column in columns)
    body = [
        " | ".join(str(row.get(column, "")).ljust(widths[column]) for column in columns)
        for row in rows
    ]
    return "\n".join([header, divider, *body])


def main() -> int:
    args = parse_args()
    base_url = resolve_base_url(getattr(args, "base_url", None))
    token = resolve_token(getattr(args, "token", None))

    if args.command == "tables":
        result = request_json(f"{base_url}/tables", "GET", token)
        if not result.get("ok"):
            raise RuntimeError(str(result))
        rows = result.get("tables", [])
        print(render_table(["table", "row_count"], rows))
        return 0

    if args.command == "query":
        sql = read_sql(args.sql, args.sql_file)
        result = request_json(
            f"{base_url}/query",
            "POST",
            token,
            payload={"sql": sql, "max_rows": int(args.max_rows)},
        )
        if not result.get("ok"):
            raise RuntimeError(str(result))
        print(render_table(result.get("columns", []), result.get("rows", [])))
        if result.get("truncated"):
            print(f"\n(truncated at {result.get('max_rows')} rows)")
        return 0

    raise RuntimeError("unsupported_command")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"error={exc}", file=sys.stderr)
        raise SystemExit(1)
