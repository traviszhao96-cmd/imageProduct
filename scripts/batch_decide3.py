#!/usr/bin/env python3
"""Batch 3: OIS hardware, Glyph, Grid/More/Ratio, Slow motion specs."""

import csv
from pathlib import Path

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

# 26111 hardware: no OIS on any camera
# 26121 hardware: Main (IMX896 OIS) ✓, Tele (JN5 OIS) ✓, UW ✗, Front ✗
OIS_26111 = {"Main": "✗", "UW": "✗", "Front": "✗"}
OIS_26121 = {"Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✗"}

OIS_UNSUPPORT = "该摄像头无 OIS 硬件。"

# Glyph: 26121 has large Glyph → ✓, 26111 no → ✗
GLYPH_26111 = {"Main": "✗", "UW": "✗", "Front": "✗"}
GLYPH_26121 = {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✓"}  # Wait, user said 26121 supports it
# Actually Glyph Mirror uses rear cameras for selfie with Glyph LED preview.
# All rear cameras ✓ for 26121 (has Glyph hardware), Front ✗ (front is not using Glyph mirror)

# But wait, the user said "26121是有大尺寸格里的，这个是支持的，26111就不支持"
# Glyph Mirror is about using rear cameras with Glyph LED. So for 26121: rear cameras ✓, front ✗
# For 26111: all ✗

GLYPH_UNSUPPORT_26111 = "26111 无大尺寸 Glyph LED 硬件，不支持 Glyph Mirror。"
GLYPH_UNSUPPORT_26121_FRONT = "Glyph Mirror 使用后置摄像头+Glyph LED，前置不适用。"

# Slow motion for 26111:
# All except front: 1080P120 ✓, 1080P240 ✓, 720P120 ✓, 720P240 ✓
# Front: all ✗
# 1080P30 and 720P480: keep TBD (not confirmed)
SLOWMO_SPECS_26111 = {
    "1080P 120FPS": {"Main": "✓", "UW": "✓", "Front": "✗"},
    "1080P 240FPS": {"Main": "✓", "UW": "✓", "Front": "✗"},
    "720P 120FPS": {"Main": "✓", "UW": "✓", "Front": "✗"},
    "720P 240FPS": {"Main": "✓", "UW": "✓", "Front": "✗"},
}
SLOWMO_UNSUPPORT_FRONT = "前置不支持慢动作模式。"

# For 26121, more complex (has Tele). Let me apply same Main/UW, Tele TBD, Front ✗
SLOWMO_SPECS_26121 = {
    "1080P 120FPS": {"Main": "✓", "UW": "✓", "Tele": "TBD", "Front": "✗"},
    "1080P 240FPS": {"Main": "✓", "UW": "✓", "Tele": "TBD", "Front": "✗"},
    "720P 120FPS": {"Main": "✓", "UW": "✓", "Tele": "TBD", "Front": "✗"},
    "720P 240FPS": {"Main": "✓", "UW": "✓", "Tele": "TBD", "Front": "✗"},
}

# Basic toolbar that's always ✓
BASIC_TOOLBAR = {"Grid", "More settings", "Ratio", "Watermark"}


def process_csv(csv_path: Path, label: str, ois_map, glyph_map, glyph_reason, slowmo_specs):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    updates = 0
    for row in rows:
        name = row.get("名称", "").strip()
        cameras = [k for k in row if k not in (
            "模式", "一级分类", "二级分类", "名称", "说明",
            "不支持原因", "状态", "确认负责人", "验证方法")]

        # --- OIS ---
        if name == "OIS" and row.get("状态", "").strip() in ("待确认", "Pending"):
            for c in cameras:
                val = ois_map.get(c, "✗")
                row[c] = val
            reasons = [f"{c}: {OIS_UNSUPPORT}" for c, v in ois_map.items() if v == "✗"]
            row["不支持原因"] = "；".join(reasons)
            row["状态"] = "已确认"
            row["确认负责人"] = "影像 SE"
            updates += 1
            print(f"  [{label}] OIS: {row['模式']} → 已确认")

        # --- Glyph Mirror ---
        if name == "Glyph Mirror":
            for c in cameras:
                row[c] = glyph_map.get(c, "✗")
            row["不支持原因"] = glyph_reason
            row["状态"] = "已确认"
            row["确认负责人"] = "PM / QA / SE"
            updates += 1
            print(f"  [{label}] Glyph Mirror: → 已确认")

        # --- Basic toolbar ---
        if name in BASIC_TOOLBAR:
            old_status = row.get("状态", "").strip()
            if old_status == "待确认":
                for c in cameras:
                    row[c] = "✓"
                row["不支持原因"] = ""
                row["状态"] = "已确认"
                row["确认负责人"] = "PM / QA / SE"
                updates += 1
                print(f"  [{label}] {name}: → 已确认")

        # --- Slow motion specs ---
        if name in slowmo_specs:
            old_status = row.get("状态", "").strip()
            if old_status == "待确认":
                spec = slowmo_specs[name]
                for c in cameras:
                    row[c] = spec.get(c, "TBD")
                reasons = []
                if "Front" in cameras and spec.get("Front") == "✗":
                    reasons.append(f"Front: {SLOWMO_UNSUPPORT_FRONT}")
                row["不支持原因"] = "；".join(reasons) if reasons else ""
                row["状态"] = "已确认" if all(v != "TBD" for v in spec.values()) else "待确认"
                row["确认负责人"] = "PM / SE / QA"
                updates += 1
                print(f"  [{label}] {name}: {spec} → {row['状态']}")

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return updates


def main():
    glyph_26111 = {c: "✗" for c in ["Main", "UW", "Front"]}
    glyph_26121 = {"Main": "✓", "UW": "✓", "Tele": "✓", "Front": "✗"}

    for fname, label, ois_map, glyph_map, glyph_reason, slowmo in [
        ("26111_fl_draft.v0.2.csv", "26111", OIS_26111,
         glyph_26111, GLYPH_UNSUPPORT_26111, SLOWMO_SPECS_26111),
        ("26121_fl_draft.v0.2.csv", "26121", OIS_26121,
         glyph_26121, GLYPH_UNSUPPORT_26121_FRONT, SLOWMO_SPECS_26121),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        n = process_csv(p, label, ois_map, glyph_map, glyph_reason, slowmo)
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
