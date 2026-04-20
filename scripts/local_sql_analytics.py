#!/usr/bin/env python3
"""Import exported analytics files into SQLite and query them with SQL."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sqlite3
import sys
from pathlib import Path
from typing import Iterable, Iterator, Sequence


SQLITE_TYPE_INTEGER = "INTEGER"
SQLITE_TYPE_REAL = "REAL"
SQLITE_TYPE_TEXT = "TEXT"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a local SQLite database from exported analytics files."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    import_parser = subparsers.add_parser("import", help="Import files into a table")
    import_parser.add_argument("--db", required=True, help="SQLite database path")
    import_parser.add_argument("--table", required=True, help="Destination table name")
    import_parser.add_argument(
        "--source",
        required=True,
        nargs="+",
        help="One or more CSV, JSON, or JSONL files",
    )
    import_parser.add_argument(
        "--if-exists",
        choices=("replace", "append"),
        default="append",
        help="Replace or append the destination table",
    )
    import_parser.add_argument(
        "--sample-size",
        type=int,
        default=200,
        help="How many rows to sample for schema inference",
    )

    query_parser = subparsers.add_parser("query", help="Run SQL against the database")
    query_parser.add_argument("--db", required=True, help="SQLite database path")
    query_parser.add_argument(
        "--sql",
        help="Inline SQL to execute. Mutually exclusive with --sql-file",
    )
    query_parser.add_argument(
        "--sql-file",
        help="Path to a .sql file to execute. Mutually exclusive with --sql",
    )
    query_parser.add_argument(
        "--limit",
        type=int,
        default=200,
        help="Maximum rows to print when the statement returns data",
    )

    tables_parser = subparsers.add_parser("tables", help="List tables and row counts")
    tables_parser.add_argument("--db", required=True, help="SQLite database path")

    return parser.parse_args()


def sanitize_identifier(value: str) -> str:
    cleaned = re.sub(r"\W+", "_", value.strip()).strip("_").lower()
    if not cleaned:
        cleaned = "column"
    if cleaned[0].isdigit():
        cleaned = f"c_{cleaned}"
    return cleaned


def flatten_record(record: dict, prefix: str = "") -> dict[str, object]:
    flattened: dict[str, object] = {}
    for key, value in record.items():
        clean_key = sanitize_identifier(key)
        final_key = f"{prefix}_{clean_key}" if prefix else clean_key
        if isinstance(value, dict):
            flattened.update(flatten_record(value, prefix=final_key))
        elif isinstance(value, list):
            flattened[final_key] = json.dumps(value, ensure_ascii=True)
        else:
            flattened[final_key] = value
    return flattened


def read_json_records(path: Path) -> list[dict[str, object]]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".jsonl":
        rows = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
        return [normalize_row(row, path) for row in rows]

    parsed = json.loads(text)
    if isinstance(parsed, list):
        return [normalize_row(row, path) for row in parsed]
    if isinstance(parsed, dict):
        return [normalize_row(parsed, path)]
    raise ValueError(f"Unsupported JSON structure in {path}")


def read_csv_records(path: Path) -> list[dict[str, object]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return [normalize_row(row, path) for row in reader]


def iter_csv_records(path: Path) -> Iterator[dict[str, object]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            yield normalize_row(row, path)


def normalize_row(row: object, path: Path) -> dict[str, object]:
    if not isinstance(row, dict):
        raise ValueError(f"Expected object rows in {path}, got {type(row).__name__}")
    flattened = flatten_record(row)
    normalized: dict[str, object] = {}
    for key, value in flattened.items():
        normalized[sanitize_identifier(key)] = normalize_value(value)
    return normalized


def normalize_value(value: object) -> object:
    if value is None:
        return None
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        text = value.strip()
        if text == "":
            return None
        if re.fullmatch(r"[-+]?\d+", text):
            try:
                return int(text)
            except ValueError:
                return text
        if re.fullmatch(r"[-+]?\d*\.\d+", text):
            try:
                return float(text)
            except ValueError:
                return text
        return text
    return json.dumps(value, ensure_ascii=True)


def load_records(path: Path) -> list[dict[str, object]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return read_csv_records(path)
    if suffix in {".json", ".jsonl"}:
        return read_json_records(path)
    raise ValueError(f"Unsupported file type: {path}")


def supports_streaming(path: Path) -> bool:
    return path.suffix.lower() == ".csv"


def infer_column_types(
    rows: Sequence[dict[str, object]], sample_size: int
) -> dict[str, str]:
    types: dict[str, str] = {}
    for row in rows[:sample_size]:
        for key, value in row.items():
            current = types.get(key)
            value_type = infer_sqlite_type(value)
            types[key] = merge_sqlite_types(current, value_type)
    return types


def infer_sqlite_type(value: object) -> str:
    if value is None:
        return SQLITE_TYPE_TEXT
    if isinstance(value, int):
        return SQLITE_TYPE_INTEGER
    if isinstance(value, float):
        return SQLITE_TYPE_REAL
    return SQLITE_TYPE_TEXT


def merge_sqlite_types(existing: str | None, incoming: str) -> str:
    if existing is None:
        return incoming
    ordered = [SQLITE_TYPE_INTEGER, SQLITE_TYPE_REAL, SQLITE_TYPE_TEXT]
    return ordered[max(ordered.index(existing), ordered.index(incoming))]


def ensure_same_columns(rows: Sequence[dict[str, object]]) -> list[str]:
    columns: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                columns.append(key)
    return columns


def create_table(
    connection: sqlite3.Connection,
    table: str,
    columns: Sequence[str],
    column_types: dict[str, str],
    if_exists: str,
) -> None:
    quoted_table = quote_identifier(table)
    if if_exists == "replace":
        connection.execute(f"DROP TABLE IF EXISTS {quoted_table}")
    definitions = ", ".join(
        f"{quote_identifier(column)} {column_types.get(column, SQLITE_TYPE_TEXT)}"
        for column in columns
    )
    connection.execute(f"CREATE TABLE IF NOT EXISTS {quoted_table} ({definitions})")


def insert_rows(
    connection: sqlite3.Connection,
    table: str,
    rows: Sequence[dict[str, object]],
    columns: Sequence[str],
) -> None:
    quoted_columns = ", ".join(quote_identifier(column) for column in columns)
    placeholders = ", ".join("?" for _ in columns)
    sql = (
        f"INSERT INTO {quote_identifier(table)} ({quoted_columns}) "
        f"VALUES ({placeholders})"
    )
    payload: Iterable[tuple[object, ...]] = (
        tuple(row.get(column) for column in columns) for row in rows
    )
    connection.executemany(sql, payload)


def insert_rows_in_batches(
    connection: sqlite3.Connection,
    table: str,
    rows: Iterable[dict[str, object]],
    columns: Sequence[str],
    batch_size: int = 5000,
) -> int:
    quoted_columns = ", ".join(quote_identifier(column) for column in columns)
    placeholders = ", ".join("?" for _ in columns)
    sql = (
        f"INSERT INTO {quote_identifier(table)} ({quoted_columns}) "
        f"VALUES ({placeholders})"
    )
    batch: list[tuple[object, ...]] = []
    total = 0
    for row in rows:
        batch.append(tuple(row.get(column) for column in columns))
        if len(batch) >= batch_size:
            connection.executemany(sql, batch)
            connection.commit()
            total += len(batch)
            batch.clear()
    if batch:
        connection.executemany(sql, batch)
        connection.commit()
        total += len(batch)
    return total


def sample_stream_rows(path: Path, sample_size: int) -> tuple[list[dict[str, object]], bool]:
    rows: list[dict[str, object]] = []
    iterator = iter_csv_records(path)
    exhausted = True
    for _ in range(sample_size):
        try:
            rows.append(next(iterator))
        except StopIteration:
            exhausted = True
            break
        exhausted = False
    else:
        exhausted = False
    return rows, exhausted


def quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def import_files(args: argparse.Namespace) -> int:
    db_path = Path(args.db)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    source_paths = [Path(raw_path) for raw_path in args.source]
    if len(source_paths) == 1 and supports_streaming(source_paths[0]):
        return import_large_csv(args, source_paths[0])

    all_rows: list[dict[str, object]] = []
    for path in source_paths:
        if not path.exists():
            raise FileNotFoundError(path)
        rows = load_records(path)
        if not rows:
            print(f"Skipped empty file: {path}")
            continue
        all_rows.extend(rows)
        print(f"Loaded {len(rows)} rows from {path}")

    if not all_rows:
        print("No rows imported.")
        return 0

    table = sanitize_identifier(args.table)
    columns = ensure_same_columns(all_rows)
    column_types = infer_column_types(all_rows, args.sample_size)

    with sqlite3.connect(db_path) as connection:
        create_table(connection, table, columns, column_types, args.if_exists)
        insert_rows(connection, table, all_rows, columns)
        connection.commit()

    print(
        f"Imported {len(all_rows)} rows into table '{table}' at {db_path}"
    )
    return 0


def import_large_csv(args: argparse.Namespace, path: Path) -> int:
    if not path.exists():
        raise FileNotFoundError(path)

    db_path = Path(args.db)
    table = sanitize_identifier(args.table)
    sample_rows, _ = sample_stream_rows(path, args.sample_size)
    if not sample_rows:
        print("No rows imported.")
        return 0

    columns = ensure_same_columns(sample_rows)
    column_types = infer_column_types(sample_rows, args.sample_size)

    with sqlite3.connect(db_path) as connection:
        create_table(connection, table, columns, column_types, args.if_exists)
        inserted = insert_rows_in_batches(
            connection,
            table,
            iter_csv_records(path),
            columns,
        )

    print(f"Imported {inserted} rows into table '{table}' at {db_path}")
    return 0


def fetch_sql(args: argparse.Namespace) -> str:
    if bool(args.sql) == bool(args.sql_file):
        raise ValueError("Use exactly one of --sql or --sql-file")
    if args.sql:
        return args.sql
    return Path(args.sql_file).read_text(encoding="utf-8")


def run_query(args: argparse.Namespace) -> int:
    sql = fetch_sql(args)
    with sqlite3.connect(args.db) as connection:
        cursor = connection.execute(sql)
        if cursor.description is None:
            connection.commit()
            print("Statement executed.")
            return 0

        headers = [column[0] for column in cursor.description]
        rows = cursor.fetchmany(args.limit)
        print_tsv(headers, rows)
        if len(rows) == args.limit:
            print(f"... truncated to {args.limit} rows", file=sys.stderr)
    return 0


def print_tsv(headers: Sequence[str], rows: Sequence[Sequence[object]]) -> None:
    print("\t".join(headers))
    for row in rows:
        print("\t".join("" if value is None else str(value) for value in row))


def list_tables(args: argparse.Namespace) -> int:
    sql = """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name
    """
    with sqlite3.connect(args.db) as connection:
        tables = [row[0] for row in connection.execute(sql)]
        if not tables:
            print("No tables found.")
            return 0

        print("table_name\trow_count")
        for table in tables:
            count = connection.execute(
                f"SELECT COUNT(*) FROM {quote_identifier(table)}"
            ).fetchone()[0]
            print(f"{table}\t{count}")
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "import":
        return import_files(args)
    if args.command == "query":
        return run_query(args)
    if args.command == "tables":
        return list_tables(args)
    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
