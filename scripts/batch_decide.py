#!/usr/bin/env python3
"""Apply batch decisions to 26111 FL draft."""

import csv
from pathlib import Path

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

# Decision 1: ASD — all modes, all cameras ✓, owner=SE / IQA
# Decision 2: 人脸检测 — all modes, all cameras ✓, owner=SE / IQA
# Decision 3: 脏污检测 — only 照片+人像 ✓, other modes ✗

RULES = [
    {
        "match_name": ["ASD / AI场景检测", "ASD / AI场景检测 (功能行)"],
        "action": "all_yes",
        "owner": "SE / IQA",
        "desc_update": None,
    },
    {
        "match_name": ["人脸检测"],
        "action": "all_yes",
        "owner": "SE / IQA",
        "desc_update": None,
    },
    {
        "match_name": ["脏污检测"],
        "action": "photo_portrait_only",
        "owner": "Product / SE / SQA",
        "unsupport_reason": "脏污检测仅在照片和人像模式生效，其他模式不支持。",
        "desc_update": None,
    },
]


def apply_rules(csv_path: Path, label: str):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    updates = 0

    for row in rows:
        name = row.get("名称", "").strip()
        mode = row.get("模式", "").strip()

        for rule in RULES:
            if name not in rule["match_name"]:
                continue

            cameras = [k for k in row if k not in (
                "模式", "一级分类", "二级分类", "名称", "说明",
                "不支持原因", "状态", "确认负责人", "验证方法")]
            
            old_status = row["状态"]
            old_cams = {c: row.get(c, "") for c in cameras}

            if rule["action"] == "all_yes":
                for c in cameras:
                    row[c] = "✓"
                row["不支持原因"] = ""
                row["状态"] = "已确认"
                row["确认负责人"] = rule["owner"]

            elif rule["action"] == "photo_portrait_only":
                is_photo_portrait = any(m in mode for m in ["照片", "人像", "Photo", "Portrait"])
                if is_photo_portrait:
                    for c in cameras:
                        row[c] = "✓"
                    row["不支持原因"] = ""
                else:
                    for c in cameras:
                        row[c] = "✗"
                    row["不支持原因"] = rule["unsupport_reason"]
                row["状态"] = "已确认"
                row["确认负责人"] = rule["owner"]

            new_cams = {c: row.get(c, "") for c in cameras}
            if old_status != row["状态"] or old_cams != new_cams:
                updates += 1
                print(f"  [{label}] {mode} | {name}: {old_cams} → {new_cams} | {old_status} → {row['状态']}")

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return updates


def main():
    for fname, label in [
        ("26111_fl_draft.v1.0.csv", "26111"),
        ("26121_fl_draft.v1.0.csv", "26121"),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        n = apply_rules(p, label)
        print(f"  {n} rows updated")

    # Count pending rows
    for fname, label in [
        ("26111_fl_draft.v1.0.csv", "26111"),
        ("26121_fl_draft.v1.0.csv", "26121"),
    ]:
        with open(BASE / fname, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        pending = sum(1 for r in rows if r.get("状态", "").strip() in ("待确认", "Pending"))
        total = len(rows)
        print(f"\n{label}: {pending}/{total} 待确认 ({(total-pending) / total * 100:.0f}% 已确认)")


if __name__ == "__main__":
    main()
