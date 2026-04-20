#!/usr/bin/env python3
"""Serve a local SQLite database over a small read-only HTTP API."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


DEFAULT_MAX_ROWS = 500


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only SQLite query service")
    parser.add_argument("--db", required=True, help="SQLite database path")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host")
    parser.add_argument("--port", type=int, default=8765, help="Bind port")
    parser.add_argument(
        "--token",
        help="Bearer token. Falls back to ANALYTICS_QUERY_TOKEN env var.",
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=DEFAULT_MAX_ROWS,
        help="Maximum returned rows per query",
    )
    return parser.parse_args()


def normalize_sql(sql: str) -> str:
    return re.sub(r"\s+", " ", sql.strip())


def validate_sql(sql: str) -> None:
    normalized = normalize_sql(sql).lower()
    if not normalized:
        raise ValueError("empty_sql")
    if ";" in normalized.rstrip(";"):
        raise ValueError("multi_statement_not_allowed")
    allowed = ("select ", "with ", "pragma table_info", "pragma table_xinfo")
    if not normalized.startswith(allowed):
        raise ValueError("only_readonly_select_allowed")
    blocked_keywords = [
        "insert ",
        "update ",
        "delete ",
        "drop ",
        "alter ",
        "create ",
        "replace ",
        "attach ",
        "detach ",
        "vacuum",
        "reindex",
        "truncate ",
    ]
    if any(keyword in normalized for keyword in blocked_keywords):
        raise ValueError("write_keyword_detected")


def run_query(db_path: Path, sql: str, max_rows: int) -> dict[str, Any]:
    validate_sql(sql)
    connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        cursor = connection.execute(sql)
        rows = cursor.fetchmany(max_rows + 1)
        columns = [item[0] for item in (cursor.description or [])]
        truncated = len(rows) > max_rows
        payload_rows = rows[:max_rows]
        return {
            "columns": columns,
            "rows": [dict(row) for row in payload_rows],
            "row_count": len(payload_rows),
            "truncated": truncated,
            "max_rows": max_rows,
        }
    finally:
        connection.close()


def list_tables(db_path: Path) -> dict[str, Any]:
    sql = """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
    """
    connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        table_names = [row["name"] for row in connection.execute(sql).fetchall()]
        tables = []
        for name in table_names:
            count_sql = f'SELECT COUNT(*) AS cnt FROM "{name}"'
            row_count = connection.execute(count_sql).fetchone()["cnt"]
            tables.append({"table": name, "row_count": row_count})
        return {"tables": tables}
    finally:
        connection.close()


def make_handler(db_path: Path, token: str, max_rows: int):
    class QueryHandler(BaseHTTPRequestHandler):
        server_version = "SQLiteQueryService/0.1"

        def _write_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status.value)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _require_auth(self) -> bool:
            expected = token.strip()
            if not expected:
                return True
            auth_header = str(self.headers.get("Authorization", "")).strip()
            if auth_header == f"Bearer {expected}":
                return True
            self._write_json(HTTPStatus.UNAUTHORIZED, {"ok": False, "error": "unauthorized"})
            return False

        def do_GET(self) -> None:  # noqa: N802
            if not self._require_auth():
                return
            if self.path == "/health":
                self._write_json(
                    HTTPStatus.OK,
                    {"ok": True, "db_path": str(db_path), "max_rows": max_rows},
                )
                return
            if self.path == "/tables":
                try:
                    payload = list_tables(db_path)
                except Exception as exc:  # noqa: BLE001
                    self._write_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"ok": False, "error": str(exc)})
                    return
                self._write_json(HTTPStatus.OK, {"ok": True, **payload})
                return
            self._write_json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "not_found"})

        def do_POST(self) -> None:  # noqa: N802
            if not self._require_auth():
                return
            if self.path != "/query":
                self._write_json(HTTPStatus.NOT_FOUND, {"ok": False, "error": "not_found"})
                return
            try:
                content_length = int(self.headers.get("Content-Length", "0"))
                raw = self.rfile.read(content_length)
                payload = json.loads(raw.decode("utf-8"))
                sql = str(payload.get("sql", "")).strip()
                limit = int(payload.get("max_rows") or max_rows)
                result = run_query(db_path, sql, max(1, min(limit, max_rows)))
            except ValueError as exc:
                self._write_json(HTTPStatus.BAD_REQUEST, {"ok": False, "error": str(exc)})
                return
            except Exception as exc:  # noqa: BLE001
                self._write_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"ok": False, "error": str(exc)})
                return
            self._write_json(HTTPStatus.OK, {"ok": True, **result})

        def log_message(self, format: str, *args: object) -> None:  # noqa: A003
            return

    return QueryHandler


def main() -> int:
    args = parse_args()
    db_path = Path(args.db).expanduser().resolve()
    if not db_path.exists():
        raise FileNotFoundError(f"db_not_found: {db_path}")
    token = str(args.token or os.environ.get("ANALYTICS_QUERY_TOKEN") or "").strip()
    handler = make_handler(db_path, token, max_rows=max(1, int(args.max_rows)))
    server = ThreadingHTTPServer((args.host, int(args.port)), handler)
    print(f"sqlite_query_service_host={args.host}")
    print(f"sqlite_query_service_port={args.port}")
    print(f"sqlite_query_service_db={db_path}")
    print(f"sqlite_query_service_token_configured={int(bool(token))}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
