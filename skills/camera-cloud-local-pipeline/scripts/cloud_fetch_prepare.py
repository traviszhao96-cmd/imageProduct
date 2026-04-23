#!/usr/bin/env python3
"""Fetch camera exports from remote storage and prepare a local SQLite database."""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


DEFAULT_WORKSPACE = Path("/Users/travis.zhao/imageProduct")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a remote camera export and prepare a local analytics SQLite DB."
    )
    parser.add_argument("--source", required=True, help="Remote or local source path")
    parser.add_argument(
        "--workspace-root",
        default=str(DEFAULT_WORKSPACE),
        help="Workspace root used to derive raw and db paths",
    )
    parser.add_argument("--filename", help="Override destination filename")
    parser.add_argument(
        "--db-name",
        help="Override output db filename, default derived from fetched filename",
    )
    parser.add_argument(
        "--table",
        help="Override imported source table name",
    )
    parser.add_argument(
        "--skip-parse-photo",
        action="store_true",
        help="Skip building photo_events_parsed even for exploded event exports",
    )
    parser.add_argument(
        "--if-exists",
        choices=("replace", "append"),
        default="replace",
        help="Import behavior for source table",
    )
    return parser.parse_args()


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def source_kind(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        return "http"
    if source.startswith("/") or source.startswith("./") or source.startswith("../"):
        return "local"
    if "@" in source and ":" in source:
        return "remote"
    if ":" in source and not parsed.scheme:
        return "remote"
    return "local"


def derive_filename(source: str, override: str | None) -> str:
    if override:
        return override
    parsed = urlparse(source)
    if parsed.scheme in {"http", "https"}:
        name = Path(parsed.path).name
        if name:
            return name
    return Path(source).name


def fetch_source(source: str, dest: Path) -> None:
    kind = source_kind(source)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if kind == "http":
        run(["curl", "-L", "--fail", source, "-o", str(dest)])
        return
    if kind == "remote":
        run(["rsync", "-av", source, str(dest)])
        return
    shutil.copy2(source, dest)


def read_header(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        return next(reader)


def choose_table_name(header: list[str], override: str | None) -> str:
    if override:
        return override
    header_set = set(header)
    if {"event_key", "string_value"}.issubset(header_set):
        return "camera_events_raw"
    if {"raw_photo_info", "photo_mode", "camera_id"}.intersection(header_set):
        return "photo_events_raw"
    return "raw_import"


def main() -> int:
    args = parse_args()
    workspace_root = Path(args.workspace_root)
    raw_dir = workspace_root / "docs/00_inbox/shared/raw_data"
    db_dir = workspace_root / "outputs/local_analytics"
    importer = workspace_root / "scripts/local_sql_analytics.py"
    parser = workspace_root / "scripts/parse_camera_event_table.py"

    filename = derive_filename(args.source, args.filename)
    fetched_path = raw_dir / filename
    fetch_source(args.source, fetched_path)

    header = read_header(fetched_path)
    table = choose_table_name(header, args.table)

    db_name = args.db_name or (Path(filename).stem.replace(":", "_") + ".db")
    db_path = db_dir / db_name
    db_dir.mkdir(parents=True, exist_ok=True)

    run(
        [
            sys.executable,
            str(importer),
            "import",
            "--db",
            str(db_path),
            "--table",
            table,
            "--source",
            str(fetched_path),
            "--if-exists",
            args.if_exists,
        ]
    )

    parsed_table = ""
    if table == "camera_events_raw" and not args.skip_parse_photo:
        run(
            [
                sys.executable,
                str(parser),
                "--db",
                str(db_path),
                "--source-table",
                table,
                "--target-table",
                "photo_events_parsed",
            ]
        )
        parsed_table = "photo_events_parsed"

    print(f"fetched_file={fetched_path}")
    print(f"db_path={db_path}")
    print(f"source_table={table}")
    if parsed_table:
        print(f"parsed_table={parsed_table}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
