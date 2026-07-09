#!/usr/bin/env python3
"""Transform 26111/26121 FL draft v0.2: 风格 restructure + remove 多帧 rows."""

import csv
import sys
from pathlib import Path

STYLE_RULES = {
    # Remove these rows entirely
    "remove_names": {"多帧", "多帧 + 滤镜"},
    # Rename name field
    "rename": {
        "Photo Style": "照片影调 / Image Tone",
        "Filter": "风格-滤镜 / Style-Filter",
        "Tuning": "风格-调色 / Style-Tuning",
        "Style": "风格-调色 / Style-Tuning",  # Video Style row
    },
    # Rename 二级分类 when name matches
    "secondary_rename": {
        "Filter": "风格-滤镜 / Style-Filter",
        "Tuning": "风格-调色 / Style-Tuning",
        "Style": "风格-调色 / Style-Tuning",
    },
}

# New row to insert after Tuning in Photo mode
TUNING_PALETTE_ROW = {
    "模式": "照片 / Photo",
    "一级分类": "功能 / Feature",
    "二级分类": "风格-调色盘 / Style-Tuning Palette",
    "名称": "风格-调色盘 / Style-Tuning Palette",
    "说明": "风格功能下的调色盘子能力：Palette Mode 视觉化调色界面，支持滑块/色轮直观调节，与 7 参数精调和 Filter/LUT 互斥并行。",
    "Main": "✓",
    "UW": "✓",
    "Front": "✗",
    "不支持原因": "Front: Photo Style PRD 当前范围为后置自然/鲜明风格，前置风格未纳入本期。",
    "状态": "已确认",
    "确认负责人": "PM / Tuning",
    "验证方法": "在照片模式打开 Toolbar → 风格，进入调色盘界面，验证色轮/滑块交互、与调色参数互斥关系、Preset 保存恢复。",
}

# For 26121, add Tele column
def insert_tele(cameras, value="✓"):
    """Insert Tele column after UW."""
    out = {}
    keys = list(cameras.keys())
    uw_idx = keys.index("UW") if "UW" in keys else -1
    for i, k in enumerate(keys):
        out[k] = cameras[k]
        if i == uw_idx:
            out["Tele"] = value
    return out


def process_csv(input_path: Path, output_path: Path, has_tele: bool = False):
    """Process a single FL CSV."""
    with open(input_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    new_rows = []
    removed = 0
    renamed = 0
    inserted = False  # track Tuning Palette insertion

    for row in rows:
        name = row.get("名称", "").strip()

        # 1. Remove unwanted rows
        if name in STYLE_RULES["remove_names"]:
            removed += 1
            continue

        # 2. Rename
        if name in STYLE_RULES["rename"]:
            old_name = name
            row["名称"] = STYLE_RULES["rename"][name]
            renamed += 1
            print(f"  RENAME: '{old_name}' -> '{row['名称']}'  [{row['模式']}]")

        # 3. Update 二级分类 for style items
        if name in STYLE_RULES["secondary_rename"]:
            row["二级分类"] = STYLE_RULES["secondary_rename"][name]

        new_rows.append(row)

        # 4. Insert Tuning Palette after Tuning row in Photo mode
        if not inserted and name == "Tuning" and "Photo" in row.get("模式", ""):
            palette = dict(TUNING_PALETTE_ROW)
            if has_tele:
                palette = insert_tele(palette, "✓")
            new_rows.append(palette)
            inserted = True
            print(f"  INSERT: 风格-调色盘 after Tuning [Photo]")

    # Write output
    with open(output_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)

    return len(new_rows), removed, renamed


def main():
    base_dir = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

    for fname, has_tele, label in [
        ("26111_fl_draft.v0.2.csv", False, "26111"),
        ("26121_fl_draft.v0.2.csv", True, "26121"),
    ]:
        inp = base_dir / fname
        out = base_dir / fname.replace(".csv", ".restyled.csv")
        print(f"\n=== Processing {label} ===")
        n, removed, renamed = process_csv(inp, out, has_tele)
        print(f"  Output: {n} rows ({removed} removed, {renamed} renamed)")
        print(f"  Saved: {out}")

    print("\n✅ Done. Review the .restyled.csv files before replacing originals.")


if __name__ == "__main__":
    main()
