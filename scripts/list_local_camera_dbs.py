#!/usr/bin/env python3
"""Summarize local imaging-related SQLite databases for query routing."""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path


DEFAULT_ROOTS = [
    Path(__file__).resolve().parents[1] / "outputs" / "local_analytics",
    Path("/Users/travis.zhao/nt_cam_pulse/data"),
]

SUMMARY_TABLES = [
    "photo_events_parsed",
    "photo_events_raw",
    "camera_events_raw",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan known local SQLite databases and print a routing summary."
    )
    parser.add_argument(
        "--root",
        action="append",
        default=[],
        help="Extra root to scan for .db files.",
    )
    return parser.parse_args()


def get_db_files(extra_roots: list[str]) -> list[Path]:
    roots = [*DEFAULT_ROOTS, *(Path(item) for item in extra_roots)]
    files: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.db")):
            if path in seen:
                continue
            seen.add(path)
            files.append(path)
    return files


def fetchone(cur: sqlite3.Cursor, sql: str) -> tuple | None:
    try:
        return cur.execute(sql).fetchone()
    except sqlite3.DatabaseError:
        return None


def fetchall(cur: sqlite3.Cursor, sql: str) -> list[tuple]:
    try:
        return cur.execute(sql).fetchall()
    except sqlite3.DatabaseError:
        return []


def summarize_db(path: Path) -> dict:
    summary = {
        "path": str(path),
        "tables": [],
    }
    try:
        con = sqlite3.connect(path)
    except sqlite3.DatabaseError as exc:
        summary["error"] = str(exc)
        return summary
    try:
        cur = con.cursor()
        tables = [
            row[0]
            for row in cur.execute(
                "select name from sqlite_master where type='table' order by 1"
            ).fetchall()
        ]
        summary["tables"] = tables
        summaries: list[dict] = []
        for table in SUMMARY_TABLES:
            if table not in tables:
                continue
            table_summary: dict[str, object] = {"table": table}
            row = fetchone(cur, f"select count(*) from {table}")
            if row:
                table_summary["row_count"] = row[0]
            if table == "photo_events_parsed":
                date_row = fetchone(
                    cur,
                    f"select min(event_date), max(event_date) from {table}",
                )
                if date_row:
                    table_summary["date_range"] = {
                        "min": date_row[0],
                        "max": date_row[1],
                    }
                table_summary["models"] = [
                    {"value": value, "count": count}
                    for value, count in fetchall(
                        cur,
                        f"select model_name, count(*) c from {table} "
                        "group by 1 order by c desc limit 10",
                    )
                ]
                table_summary["countries"] = [
                    {"value": value, "count": count}
                    for value, count in fetchall(
                        cur,
                        f"select country, count(*) c from {table} "
                        "group by 1 order by c desc limit 10",
                    )
                ]
            summaries.append(table_summary)
        if summaries:
            summary["summaries"] = summaries
    finally:
        con.close()
    return summary


def main() -> int:
    args = parse_args()
    dbs = [summarize_db(path) for path in get_db_files(args.root)]
    print(json.dumps(dbs, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
