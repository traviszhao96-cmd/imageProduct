#!/usr/bin/env python3
"""Parse video_info rows from an exploded camera event table into a compact SQLite table."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path


PATTERNS = {
    "video_mode": re.compile(r"video_mode:([^;]+)"),
    "exposure_adjust": re.compile(r"exposure_adjust:([0-9\\-]+)"),
    "video_length": re.compile(r"video_length:([0-9.]+)"),
    "nightmode": re.compile(r"nightmode:([0-9]+)"),
    "video_hdr": re.compile(r"video_hdr:([0-9]+)"),
    "if_hlg": re.compile(r"if_HLG:([0-9]+)"),
    "action_mode": re.compile(r"action_mode:([0-9]+)"),
    "flash": re.compile(r"flash:([0-9]+)"),
    "quality": re.compile(r"quality:([^;]+)"),
    "rec_light": re.compile(r"Rec_light:([0-9]+)"),
    "glyph_mirror": re.compile(r"glyph_mirror:([0-9]+)"),
    "filter_name": re.compile(r"filter:([^;]+)"),
    "filter_strength": re.compile(r"filter_strength:([0-9.\\-]+)"),
    "tuning_apply": re.compile(r"tuning_apply:([0-9]+)"),
    "tuning_contrast": re.compile(r"tuning_contrast:([0-9.\\-]+)"),
    "tuning_saturation": re.compile(r"tuning_saturation:([0-9.\\-]+)"),
    "tuning_warmth": re.compile(r"tuning_warmth:([0-9.\\-]+)"),
    "tuning_tint": re.compile(r"tuning_tint:([0-9.\\-]+)"),
    "tuning_shapen": re.compile(r"tuning_shapen:([0-9.\\-]+)"),
    "tuning_grain": re.compile(r"tuning_grain:([0-9.\\-]+)"),
    "tuning_vignette": re.compile(r"tuning_vignette:([0-9.\\-]+)"),
    "first_zoom_ratio": re.compile(r"first_zoom_ratio:([0-9.\\-]+)"),
    "last_zoom_ratio": re.compile(r"last_zoom_ratio:([0-9.\\-]+)"),
    "speed": re.compile(r"speed:([0-9\\-]+)"),
    "preset": re.compile(r"preset:([^;]+)"),
    "first_orientation": re.compile(r"first_orientation:([0-9]+)"),
    "last_orientation": re.compile(r"last_orientation:([0-9]+)"),
    "first_lux": re.compile(r"first_lux:([0-9.\\-]+)"),
    "last_lux": re.compile(r"last_lux:([0-9.\\-]+)"),
    "first_adrc": re.compile(r"first_adrc:([0-9.\\-]+)"),
    "last_adrc": re.compile(r"last_adrc:([0-9.\\-]+)"),
    "first_cct": re.compile(r"first_cct:([0-9.\\-]+)"),
    "last_cct": re.compile(r"last_cct:([0-9.\\-]+)"),
    "first_face_count": re.compile(r"first_face_count:([0-9]+)"),
    "last_face_count": re.compile(r"last_face_count:([0-9]+)"),
    "auto_fps": re.compile(r"auto_fps:([^;]+)"),
}

INT_FIELDS = {
    "exposure_adjust",
    "nightmode",
    "video_hdr",
    "if_hlg",
    "action_mode",
    "flash",
    "rec_light",
    "glyph_mirror",
    "tuning_apply",
    "speed",
    "first_orientation",
    "last_orientation",
    "first_face_count",
    "last_face_count",
}

FLOAT_FIELDS = {
    "video_length",
    "filter_strength",
    "tuning_contrast",
    "tuning_saturation",
    "tuning_warmth",
    "tuning_tint",
    "tuning_shapen",
    "tuning_grain",
    "tuning_vignette",
    "first_zoom_ratio",
    "last_zoom_ratio",
    "first_lux",
    "last_lux",
    "first_adrc",
    "last_adrc",
    "first_cct",
    "last_cct",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse video_info rows from camera_events_raw.")
    parser.add_argument("--db", required=True, help="SQLite db path")
    parser.add_argument("--source-table", default="camera_events_raw")
    parser.add_argument("--target-table", default="video_events_parsed")
    parser.add_argument("--batch-size", type=int, default=5000)
    return parser.parse_args()


def extract(pattern_name: str, text: str) -> object:
    match = PATTERNS[pattern_name].search(text)
    if not match:
        return None
    value = match.group(1).strip()
    if pattern_name in INT_FIELDS:
        return int(value)
    if pattern_name in FLOAT_FIELDS:
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
            raw_video_info TEXT,
            video_mode TEXT,
            exposure_adjust INTEGER,
            video_length REAL,
            nightmode INTEGER,
            video_hdr INTEGER,
            if_hlg INTEGER,
            action_mode INTEGER,
            flash INTEGER,
            quality TEXT,
            rec_light INTEGER,
            glyph_mirror INTEGER,
            filter_name TEXT,
            filter_strength REAL,
            tuning_apply INTEGER,
            tuning_contrast REAL,
            tuning_saturation REAL,
            tuning_warmth REAL,
            tuning_tint REAL,
            tuning_shapen REAL,
            tuning_grain REAL,
            tuning_vignette REAL,
            first_zoom_ratio REAL,
            last_zoom_ratio REAL,
            speed INTEGER,
            preset TEXT,
            first_orientation INTEGER,
            last_orientation INTEGER,
            first_lux REAL,
            last_lux REAL,
            first_adrc REAL,
            last_adrc REAL,
            first_cct REAL,
            last_cct REAL,
            first_face_count INTEGER,
            last_face_count INTEGER,
            auto_fps TEXT
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
        WHERE event_key = 'video_info'
          AND string_value IS NOT NULL
    '''
    insert_sql = f'''
        INSERT INTO "{args.target_table}" (
            event_date, exact_time, user_pseudo_id, model_name, country, raw_video_info,
            video_mode, exposure_adjust, video_length, nightmode, video_hdr, if_hlg,
            action_mode, flash, quality, rec_light, glyph_mirror, filter_name,
            filter_strength, tuning_apply, tuning_contrast, tuning_saturation,
            tuning_warmth, tuning_tint, tuning_shapen, tuning_grain, tuning_vignette,
            first_zoom_ratio, last_zoom_ratio, speed, preset, first_orientation,
            last_orientation, first_lux, last_lux, first_adrc, last_adrc,
            first_cct, last_cct, first_face_count, last_face_count, auto_fps
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                extract("video_mode", raw),
                extract("exposure_adjust", raw),
                extract("video_length", raw),
                extract("nightmode", raw),
                extract("video_hdr", raw),
                extract("if_hlg", raw),
                extract("action_mode", raw),
                extract("flash", raw),
                extract("quality", raw),
                extract("rec_light", raw),
                extract("glyph_mirror", raw),
                extract("filter_name", raw),
                extract("filter_strength", raw),
                extract("tuning_apply", raw),
                extract("tuning_contrast", raw),
                extract("tuning_saturation", raw),
                extract("tuning_warmth", raw),
                extract("tuning_tint", raw),
                extract("tuning_shapen", raw),
                extract("tuning_grain", raw),
                extract("tuning_vignette", raw),
                extract("first_zoom_ratio", raw),
                extract("last_zoom_ratio", raw),
                extract("speed", raw),
                extract("preset", raw),
                extract("first_orientation", raw),
                extract("last_orientation", raw),
                extract("first_lux", raw),
                extract("last_lux", raw),
                extract("first_adrc", raw),
                extract("last_adrc", raw),
                extract("first_cct", raw),
                extract("last_cct", raw),
                extract("first_face_count", raw),
                extract("last_face_count", raw),
                extract("auto_fps", raw),
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
