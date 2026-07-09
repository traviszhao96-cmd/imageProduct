#!/usr/bin/env python3
"""Clean up old naming references in 说明 / 不支持原因 / 验证方法 fields."""

import csv
from pathlib import Path

REPLACEMENTS = [
    # Photo Style → 照片影调 in 说明 and 验证方法
    ("Photo Style PRD", "照片影调 PRD"),
    ("Photo Style 与 Filter、Tuning", "照片影调 / Image Tone 与 风格-滤镜、风格-调色"),
    ("Photo Style、Tuning、Preset", "照片影调 / Image Tone、风格-调色 / Style-Tuning、Preset"),
    
    # Tuning/Tuning Palette → 风格 naming in 说明
    ("Tuning / Tuning Palette 调色能力", "风格-调色 / 风格-调色盘能力"),
    ("Filter 与 Tuning 暂不合并", "风格-滤镜 与 风格-调色 暂不合并"),
    ("Style / Filter+Tuning", "风格 / 风格-滤镜+风格-调色"),
    
    # Filter/Tuning/Style in 验证方法 of 照片影调 rows
    ("Tuning、Preset 的互斥/叠加顺序", "风格-调色、风格-调色盘、Preset 的互斥/叠加顺序"),
    
    # Not video style, but tuning reference
    ("Filter/Tuning/Style 的风格化效果", "风格-滤镜/风格-调色/风格-调色盘 的风格化效果"),
    
    # Tuning-Palette reference
    ("Filter/Tuning，因为仅 1080P pipeline", "风格-滤镜/风格-调色，因为仅 1080P pipeline"),
]


def process_csv(input_path: Path):
    with open(input_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    changes = 0
    for row in rows:
        for field in ["说明", "验证方法", "不支持原因"]:
            if field not in row:
                continue
            original = row[field]
            for old, new in REPLACEMENTS:
                if old in (row[field] or ""):
                    row[field] = row[field].replace(old, new)
            if row[field] != original:
                changes += 1
                print(f"  [{field}] {original[:60]}...")

    with open(input_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return changes


def main():
    base = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")
    for fname, label in [
        ("26111_fl_draft.v0.2.csv", "26111"),
        ("26121_fl_draft.v0.2.csv", "26121"),
    ]:
        p = base / fname
        print(f"\n=== Cleaning {label} ===")
        n = process_csv(p)
        print(f"  {n} field updates")


if __name__ == "__main__":
    main()
