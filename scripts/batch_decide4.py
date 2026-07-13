#!/usr/bin/env python3
"""Batch 4: video spec front camera decisions."""

import csv
from pathlib import Path

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

# 26111 Front: max 1080P HLG (OV32D lower spec)
# 26121 Front: 1080P30 HLG + 4K30 HLG (KD1)
FRONT_VIDEO_26111 = {
    "1080P 30FPS": "✓",
    "1080P 30FPS HLG": "✓",
    "1080P 60FPS": "✗",
    "1080P 60FPS HLG": "✗",
    "4K 30FPS": "✗",
    "4K 30FPS HLG": "✗",
    "4K 60FPS": "✗",
    "4K 60FPS HLG": "✗",
}
FRONT_VIDEO_26121 = {
    "1080P 30FPS": "✓",
    "1080P 30FPS HLG": "✓",
    "4K 30FPS": "✓",
    "4K 30FPS HLG": "✓",
    "1080P 60FPS": "TBD",
    "1080P 60FPS HLG": "TBD",
    "4K 60FPS": "✗",
    "4K 60FPS HLG": "✗",
}
FRONT_UNSUPPORT_26111 = "Front: 26111 前置 OV32D 规格较低，最高支持 1080P HLG，不支持 4K/1080P60。"
FRONT_UNSUPPORT_26121 = "Front: 26121 前置最高支持 4K30 HLG，不支持 4K60。"

# Also update HLG/HDR 规格 algorithm row
HLG_26111 = {"Main": "✓", "UW": "✓", "Front": "✓"}
HLG_26121 = {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✓"}


def process_csv(csv_path: Path, label: str, front_map, front_reason):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    updates = 0
    for row in rows:
        name = row.get("名称", "").strip()
        mode = row.get("模式", "").strip()
        cameras = [k for k in row if k not in (
            "模式", "一级分类", "二级分类", "名称", "说明",
            "不支持原因", "状态", "确认负责人", "验证方法")]

        # --- Video specs: Front camera ---
        if name in front_map and "Front" in cameras:
            old = row.get("Front", "")
            new_val = front_map[name]
            if old in ("TBD", "") or old != new_val:
                row["Front"] = new_val
                # Update unsupport reason for Front
                existing_reason = row.get("不支持原因", "") or ""
                if "Front:" not in existing_reason and new_val == "✗":
                    if existing_reason:
                        row["不支持原因"] = existing_reason + "；" + front_reason
                    else:
                        row["不支持原因"] = front_reason
                updates += 1
                print(f"  [{label}] {name}: Front {old} → {new_val}")

        # --- HLG/HDR 规格 algorithm ---
        if name == "HLG / HDR 规格":
            old_status = row.get("状态", "").strip()
            if old_status == "待确认":
                for c in cameras:
                    if c == "Front":
                        row[c] = "✓"
                row["状态"] = "已确认"
                row["确认负责人"] = "SE / IQA"
                updates += 1
                print(f"  [{label}] HLG/HDR: Front → ✓")

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return updates


def main():
    for fname, label, front_map, front_reason in [
        ("26111_fl_draft.v1.0.csv", "26111", FRONT_VIDEO_26111, FRONT_UNSUPPORT_26111),
        ("26121_fl_draft.v1.0.csv", "26121", FRONT_VIDEO_26121, FRONT_UNSUPPORT_26121),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        n = process_csv(p, label, front_map, front_reason)
        pending = 0
        total = 0
        with open(p, "r", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                total += 1
                if r.get("状态", "").strip() in ("待确认", "Pending"):
                    pending += 1
        print(f"  {n} rows updated | {pending}/{total} 待确认 ({(total-pending) * 100 // total}% 已确认)")


if __name__ == "__main__":
    main()
