#!/usr/bin/env python3
"""Parse photo_info rows from an exploded camera event table into a compact SQLite table."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path


PATTERNS = {
    "photo_mode": re.compile(r"photoMode:([^;]+)"),
    "camera_id": re.compile(r"camera_id:([0-9]+)"),
    "zoom_ratio": re.compile(r"zoom_ratio:([0-9.]+)"),
    "lux": re.compile(r"lux:([0-9.]+)"),
    "adrc": re.compile(r"adrc:([0-9.]+)"),
    "cct": re.compile(r"cct:([0-9.]+)"),
    "exp_time_ns": re.compile(r"exp_time:([0-9.]+)"),
    "shot_algo": re.compile(r"shot_algo:([^;]+)"),
    "face_count": re.compile(r"face_count:([0-9]+)"),
    "orientation": re.compile(r"orientation:([0-9]+)"),
    "exposure_adjust": re.compile(r"exposure_adjust:([0-9\\-]+)"),
    "nightmode": re.compile(r"nightmode:([0-9]+)"),
    "preset": re.compile(r"preset:([^;]+)"),
    "watermark": re.compile(r"watermark:([0-9]+)"),
    "retouching": re.compile(r"retouching:([0-9]+)"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse photo_info rows from camera_events_raw.")
    parser.add_argument("--db", required=True, help="SQLite db path")
    parser.add_argument("--source-table", default="camera_events_raw")
    parser.add_argument("--target-table", default="photo_events_parsed")
    parser.add_argument("--batch-size", type=int, default=5000)
    return parser.parse_args()


def extract(pattern_name: str, text: str) -> object:
    match = PATTERNS[pattern_name].search(text)
    if not match:
        return None
    value = match.group(1).strip()
    if pattern_name in {"camera_id", "face_count", "orientation", "exposure_adjust", "nightmode", "watermark", "retouching"}:
        return int(value)
    if pattern_name in {"zoom_ratio", "lux", "adrc", "cct", "exp_time_ns"}:
        return float(value)
    return value


def create_table(connection: sqlite3.Connection, target_table: str) -> None:
    connection.execute(f'DROP TABLE IF EXISTS "{target_table}"')
    connection.execute(
        f'''
        CREATE TABLE "{target_table}" (
            event_date TEXT,
            exact_time TEXT,
            user_pseudo_id TEXT,
            model_name TEXT,
            country TEXT,
            raw_photo_info TEXT,
            photo_mode TEXT,
            camera_id INTEGER,
            zoom_ratio REAL,
            lux REAL,
            adrc REAL,
            cct REAL,
            exp_time_ns REAL,
            shot_algo TEXT,
            face_count INTEGER,
            orientation INTEGER,
            exposure_adjust INTEGER,
            nightmode INTEGER,
            preset TEXT,
            watermark INTEGER,
            retouching INTEGER
        )
        '''
    )
    connection.commit()


def main() -> int:
    args = parse_args()
    db_path = Path(args.db)
    if not db_path.exists():
        raise FileNotFoundError(db_path)

    select_sql = f'''
        SELECT event_date, exact_time, user_pseudo_id, model_name, geo_country, string_value
        FROM "{args.source_table}"
        WHERE event_key = 'photo_info'
          AND string_value IS NOT NULL
    '''
    insert_sql = f'''
        INSERT INTO "{args.target_table}" (
            event_date, exact_time, user_pseudo_id, model_name, country, raw_photo_info,
            photo_mode, camera_id, zoom_ratio, lux, adrc, cct, exp_time_ns, shot_algo,
            face_count, orientation, exposure_adjust, nightmode, preset, watermark, retouching
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    with sqlite3.connect(db_path) as connection:
        create_table(connection, args.target_table)
        cursor = connection.execute(select_sql)
        batch = []
        total = 0
        for event_date, exact_time, user_pseudo_id, model_name, country, raw in cursor:
            row = (
                event_date,
                exact_time,
                user_pseudo_id,
                model_name,
                country,
                raw,
                extract("photo_mode", raw),
                extract("camera_id", raw),
                extract("zoom_ratio", raw),
                extract("lux", raw),
                extract("adrc", raw),
                extract("cct", raw),
                extract("exp_time_ns", raw),
                extract("shot_algo", raw),
                extract("face_count", raw),
                extract("orientation", raw),
                extract("exposure_adjust", raw),
                extract("nightmode", raw),
                extract("preset", raw),
                extract("watermark", raw),
                extract("retouching", raw),
            )
            batch.append(row)
            if len(batch) >= args.batch_size:
                connection.executemany(insert_sql, batch)
                connection.commit()
                total += len(batch)
                batch.clear()
        if batch:
            connection.executemany(insert_sql, batch)
            connection.commit()
            total += len(batch)

    print(f"Parsed {total} rows into {args.target_table} at {db_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
