#!/usr/bin/env python3
"""Parse photo/video rows from a semi-structured camera_events_raw table into standard parsed tables."""

from __future__ import annotations

import argparse
import re
import sqlite3
from pathlib import Path


PHOTO_PATTERNS = {
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

VIDEO_PATTERNS = {
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
    "camera_id",
    "face_count",
    "orientation",
    "exposure_adjust",
    "nightmode",
    "watermark",
    "retouching",
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
    "zoom_ratio",
    "lux",
    "adrc",
    "cct",
    "exp_time_ns",
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
    parser = argparse.ArgumentParser(description="Parse semi-structured camera_events_raw into standard parsed tables.")
    parser.add_argument("--db", required=True, help="SQLite db path")
    parser.add_argument("--source-table", default="camera_events_raw")
    parser.add_argument("--batch-size", type=int, default=5000)
    return parser.parse_args()


def extract(patterns: dict[str, re.Pattern[str]], name: str, text: str | None) -> object:
    if not text:
        return None
    match = patterns[name].search(text)
    if not match:
        return None
    value = match.group(1).strip()
    if name in INT_FIELDS:
        return int(float(value))
    if name in FLOAT_FIELDS:
        return float(value)
    return value


def create_photo_table(connection: sqlite3.Connection) -> None:
    connection.execute('DROP TABLE IF EXISTS "photo_events_parsed"')
    connection.execute(
        '''
        CREATE TABLE "photo_events_parsed" (
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


def create_video_table(connection: sqlite3.Connection) -> None:
    connection.execute('DROP TABLE IF EXISTS "video_events_parsed"')
    connection.execute(
        '''
        CREATE TABLE "video_events_parsed" (
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

    with sqlite3.connect(db_path) as connection:
        create_photo_table(connection)
        select_sql = f'''
            SELECT event_date, event_timestamp, user_pseudo_id, project_name, geo_country,
                   photo_info_raw, photo_mode, camera_id, zoom_ratio, exposure_adjust,
                   face_count, orientation, retouching, watermark, preset
            FROM "{args.source_table}"
            WHERE photo_info_raw IS NOT NULL
        '''
        insert_sql = '''
            INSERT INTO "photo_events_parsed" (
                event_date, exact_time, user_pseudo_id, model_name, country, raw_photo_info,
                photo_mode, camera_id, zoom_ratio, lux, adrc, cct, exp_time_ns, shot_algo,
                face_count, orientation, exposure_adjust, nightmode, preset, watermark, retouching
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor = connection.execute(select_sql)
        batch = []
        for row in cursor:
            (
                event_date, event_timestamp, user_pseudo_id, project_name, country, raw,
                photo_mode, camera_id, zoom_ratio, exposure_adjust,
                face_count, orientation, retouching, watermark, preset
            ) = row
            batch.append((
                event_date,
                str(event_timestamp) if event_timestamp is not None else None,
                user_pseudo_id,
                project_name,
                country,
                raw,
                photo_mode or extract(PHOTO_PATTERNS, "photo_mode", raw),
                int(camera_id) if camera_id not in (None, "") else extract(PHOTO_PATTERNS, "camera_id", raw),
                zoom_ratio if zoom_ratio not in (None, "") else extract(PHOTO_PATTERNS, "zoom_ratio", raw),
                extract(PHOTO_PATTERNS, "lux", raw),
                extract(PHOTO_PATTERNS, "adrc", raw),
                extract(PHOTO_PATTERNS, "cct", raw),
                extract(PHOTO_PATTERNS, "exp_time_ns", raw),
                extract(PHOTO_PATTERNS, "shot_algo", raw),
                face_count if face_count not in (None, "") else extract(PHOTO_PATTERNS, "face_count", raw),
                orientation if orientation not in (None, "") else extract(PHOTO_PATTERNS, "orientation", raw),
                exposure_adjust if exposure_adjust not in (None, "") else extract(PHOTO_PATTERNS, "exposure_adjust", raw),
                extract(PHOTO_PATTERNS, "nightmode", raw),
                str(preset) if preset not in (None, "") else extract(PHOTO_PATTERNS, "preset", raw),
                int(watermark) if watermark not in (None, "") else extract(PHOTO_PATTERNS, "watermark", raw),
                int(retouching) if retouching not in (None, "") else extract(PHOTO_PATTERNS, "retouching", raw),
            ))
            if len(batch) >= args.batch_size:
                connection.executemany(insert_sql, batch)
                connection.commit()
                batch.clear()
        if batch:
            connection.executemany(insert_sql, batch)
            connection.commit()

        create_video_table(connection)
        select_sql = f'''
            SELECT event_date, event_timestamp, user_pseudo_id, project_name, geo_country,
                   video_info_raw
            FROM "{args.source_table}"
            WHERE video_info_raw IS NOT NULL
        '''
        insert_sql = '''
            INSERT INTO "video_events_parsed" (
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
        cursor = connection.execute(select_sql)
        batch = []
        for event_date, event_timestamp, user_pseudo_id, project_name, country, raw in cursor:
            batch.append((
                event_date,
                str(event_timestamp) if event_timestamp is not None else None,
                user_pseudo_id,
                project_name,
                country,
                raw,
                extract(VIDEO_PATTERNS, "video_mode", raw),
                extract(VIDEO_PATTERNS, "exposure_adjust", raw),
                extract(VIDEO_PATTERNS, "video_length", raw),
                extract(VIDEO_PATTERNS, "nightmode", raw),
                extract(VIDEO_PATTERNS, "video_hdr", raw),
                extract(VIDEO_PATTERNS, "if_hlg", raw),
                extract(VIDEO_PATTERNS, "action_mode", raw),
                extract(VIDEO_PATTERNS, "flash", raw),
                extract(VIDEO_PATTERNS, "quality", raw),
                extract(VIDEO_PATTERNS, "rec_light", raw),
                extract(VIDEO_PATTERNS, "glyph_mirror", raw),
                extract(VIDEO_PATTERNS, "filter_name", raw),
                extract(VIDEO_PATTERNS, "filter_strength", raw),
                extract(VIDEO_PATTERNS, "tuning_apply", raw),
                extract(VIDEO_PATTERNS, "tuning_contrast", raw),
                extract(VIDEO_PATTERNS, "tuning_saturation", raw),
                extract(VIDEO_PATTERNS, "tuning_warmth", raw),
                extract(VIDEO_PATTERNS, "tuning_tint", raw),
                extract(VIDEO_PATTERNS, "tuning_shapen", raw),
                extract(VIDEO_PATTERNS, "tuning_grain", raw),
                extract(VIDEO_PATTERNS, "tuning_vignette", raw),
                extract(VIDEO_PATTERNS, "first_zoom_ratio", raw),
                extract(VIDEO_PATTERNS, "last_zoom_ratio", raw),
                extract(VIDEO_PATTERNS, "speed", raw),
                extract(VIDEO_PATTERNS, "preset", raw),
                extract(VIDEO_PATTERNS, "first_orientation", raw),
                extract(VIDEO_PATTERNS, "last_orientation", raw),
                extract(VIDEO_PATTERNS, "first_lux", raw),
                extract(VIDEO_PATTERNS, "last_lux", raw),
                extract(VIDEO_PATTERNS, "first_adrc", raw),
                extract(VIDEO_PATTERNS, "last_adrc", raw),
                extract(VIDEO_PATTERNS, "first_cct", raw),
                extract(VIDEO_PATTERNS, "last_cct", raw),
                extract(VIDEO_PATTERNS, "first_face_count", raw),
                extract(VIDEO_PATTERNS, "last_face_count", raw),
                extract(VIDEO_PATTERNS, "auto_fps", raw),
            ))
            if len(batch) >= args.batch_size:
                connection.executemany(insert_sql, batch)
                connection.commit()
                batch.clear()
        if batch:
            connection.executemany(insert_sql, batch)
            connection.commit()

    print(f"Parsed photo_events_parsed and video_events_parsed at {db_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
