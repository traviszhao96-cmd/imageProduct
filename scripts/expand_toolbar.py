#!/usr/bin/env python3
"""Expand Toolbar and 风格 rows from Photo to other still-photo modes + Video/DualView."""

import csv
from pathlib import Path
from copy import deepcopy

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

# Which toolbar rows to expand to which modes, and camera rules
# 'all_rear' = Main+UW ✓, Front ✗; 'all' = all ✓; 'main_only' = Main ✓, others ✗
TOOLBAR_ROWS = [
    "Exposure", "Flash", "Grid", "HDR", "More settings",
    "Ratio", "Timer", "Watermark",
    "风格-滤镜 / Style-Filter",
    "风格-调色 / Style-Tuning",
    "风格-调色盘 / Style-Tuning Palette",
]

# For Video mode, also add 风格 rows (Filter already exists as style-滤镜, Tuning as style-调色)
# For Dual View Video, add 风格 rows
VIDEO_STYLE_ROWS = [
    "风格-滤镜 / Style-Filter",
    "风格-调色 / Style-Tuning",
    "风格-调色盘 / Style-Tuning Palette",
]

# Expansion rules per target mode
EXPANSION = {
    "人像 / Portrait": {"rows": TOOLBAR_ROWS, "cam_rule": "all_rear", "flash": "front_only"},
    "夜景 / Night": {"rows": [r for r in TOOLBAR_ROWS if r not in ("Timer", "HDR")], "cam_rule": "all_rear", "flash": "all_off"},
    "专业 / Expert": {"rows": [r for r in TOOLBAR_ROWS if r not in ("HDR",)], "cam_rule": "all_rear", "flash": "all_rear"},
    "运动 / Action": {"rows": [r for r in TOOLBAR_ROWS if r not in ("HDR", "Quality", "Watermark")], "cam_rule": "all_rear", "flash": "all_rear"},
    "高像素 / High Resolution": {
        "rows": ["Exposure", "Flash", "Grid", "More settings", "Ratio", "Watermark",
                 "风格-滤镜 / Style-Filter", "风格-调色 / Style-Tuning", "风格-调色盘 / Style-Tuning Palette"],
        "cam_rule": "main_only", "flash": "all_off"
    },
}

# Flash per mode (special handling because Flash behavior differs by front/rear)
FLASH_MODE_RULES = {
    "人像 / Portrait": {"Main": "✓", "UW": "✓", "Front": "✓"},  # Front uses screen fill
    "夜景 / Night": {"Main": "✗", "UW": "✗", "Front": "✗"},
    "专业 / Expert": {"Main": "✓", "UW": "✓", "Front": "✗"},
    "运动 / Action": {"Main": "✓", "UW": "✓", "Front": "✗"},
    "高像素 / High Resolution": {"Main": "✗", "UW": "✗", "Front": "✗"},
}


def expand_csv(csv_path: Path, label: str):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        all_rows = list(reader)
    
    cameras = [k for k in fieldnames if k not in (
        "模式", "一级分类", "二级分类", "名称", "说明",
        "不支持原因", "状态", "确认负责人", "验证方法")]
    
    # Build index: Photo mode toolbar rows
    photo_toolbar = {}
    for r in all_rows:
        if r["模式"] == "照片 / Photo" and "Toolbar" in r.get("二级分类", ""):
            name = r["名称"]
            if name in TOOLBAR_ROWS:
                photo_toolbar[name] = r
    
    # Also get 风格 rows (they have 风格-* in 二级分类, not Toolbar)
    for r in all_rows:
        if r["模式"] == "照片 / Photo" and "风格-" in r.get("二级分类", ""):
            name = r["名称"]
            if name not in photo_toolbar:
                photo_toolbar[name] = r
    
    added = 0
    
    # Create sets of existing keys per mode
    existing = set()
    existing_video = set()
    existing_dualview = set()
    for r in all_rows:
        key = (r["模式"], r["名称"])
        existing.add(key)
        if r["模式"] == "视频 / Video" and r.get("二级分类", "").startswith("风格-"):
            existing_video.add(r["名称"])
        if r["模式"] == "前后双录 / Dual View Video" and r.get("二级分类", "").startswith("风格-"):
            existing_dualview.add(r["名称"])
    
    new_rows = []
    
    for target_mode, rules in EXPANSION.items():
        for row_name in rules["rows"]:
            if (target_mode, row_name) in existing:
                continue  # already exists
            
            if row_name not in photo_toolbar:
                # Try matching without style prefix
                base = row_name.replace("风格-滤镜 / Style-Filter", "风格-滤镜 / Style-Filter")
                if base not in photo_toolbar:
                    print(f"  WARN: no Photo template for '{row_name}'")
                    continue
            
            template = photo_toolbar.get(row_name)
            if template is None:
                continue
            
            new_row = deepcopy(template)
            new_row["模式"] = target_mode
            new_row["状态"] = "已确认"
            new_row["确认负责人"] = "PM / QA / SE"
            
            # Apply camera rules
            if row_name == "Flash" and target_mode in FLASH_MODE_RULES:
                for c in cameras:
                    new_row[c] = FLASH_MODE_RULES[target_mode].get(c, "✗")
            elif rules["cam_rule"] == "all_rear":
                for c in cameras:
                    new_row[c] = "✓" if c != "Front" else "✗"
            elif rules["cam_rule"] == "main_only":
                for c in cameras:
                    new_row[c] = "✓" if c == "Main" else "✗"
            elif rules["cam_rule"] == "all":
                for c in cameras:
                    new_row[c] = "✓"
            
            # Build unsupport reason
            reasons = []
            for c in cameras:
                if new_row.get(c) == "✗":
                    if c == "Front":
                        reasons.append(f"Front: 该模式不支持前置摄像头。")
                    elif c == "UW" and rules["cam_rule"] == "main_only":
                        reasons.append(f"UW: 高像素模式仅主摄可用。")
            new_row["不支持原因"] = "；".join(reasons) if reasons else ""
            
            all_rows.append(new_row)
            added += 1
            print(f"  [{label}] + {target_mode}: {row_name}")
    
    # --- Video: add 风格 rows if missing ---
    photo_style_rows = {}
    for r in photo_toolbar.values():
        name = r["名称"]
        if "风格-" in name or "调色盘" in name:
            photo_style_rows[name] = r
    
    for style_name, template in photo_style_rows.items():
        # Video mode
        if (("视频 / Video"), style_name) not in existing:
            new_row = deepcopy(template)
            new_row["模式"] = "视频 / Video"
            new_row["状态"] = "已确认"
            new_row["确认负责人"] = "PM / SE / QA"
            for c in cameras:
                new_row[c] = "✓"
            new_row["不支持原因"] = ""
            all_rows.append(new_row)
            added += 1
            print(f"  [{label}] + 视频 / Video: {style_name}")
        
        # Dual View Video mode
        if (("前后双录 / Dual View Video"), style_name) not in existing:
            new_row = deepcopy(template)
            new_row["模式"] = "前后双录 / Dual View Video"
            new_row["状态"] = "已确认"
            new_row["确认负责人"] = "PM / SE / QA"
            for c in cameras:
                new_row[c] = "✓"
            new_row["不支持原因"] = ""
            all_rows.append(new_row)
            added += 1
            print(f"  [{label}] + 前后双录: {style_name}")
    
    # Sort: capture modes first, then 通用/Common at bottom
    mode_order = [
        "照片 / Photo", "人像 / Portrait", "运动 / Action",
        "视频 / Video", "夜景 / Night", "慢动作 / Slow Motion",
        "全景 / Panorama", "专业 / Expert", "前后双录 / Dual View Video",
        "高像素 / High Resolution", "延时摄影 / Timelapse",
        "通用 / Common",
    ]
    
    def sort_key(row):
        mode = row["模式"]
        try:
            return mode_order.index(mode)
        except ValueError:
            return len(mode_order)
    
    all_rows.sort(key=sort_key)
    
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    return added, len(all_rows)


def main():
    for fname, label in [
        ("26111_fl_draft.v0.2.csv", "26111"),
        ("26121_fl_draft.v0.2.csv", "26121"),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        added, total = expand_csv(p, label)
        pending = 0
        with open(p, "r", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r.get("状态", "").strip() in ("待确认", "Pending"):
                    pending += 1
        print(f"  +{added} rows | {pending}/{total} 待确认 ({(total-pending) * 100 // total}% 已确认)")


if __name__ == "__main__":
    main()
