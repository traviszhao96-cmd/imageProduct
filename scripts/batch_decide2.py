#!/usr/bin/env python3
"""Batch 2: split AE/AF + confirm 变焦."""

import csv
from pathlib import Path

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

# FF cameras: UW is always FF. Front is FF. Main has AF. Tele has AF.
FF_CAMERAS = {"Front"}  # UW is front — wait, UW is ultrawide
# For 26111: Main=AF, UW=FF (IMX355), Front=FF (OV32D)
# For 26121: Main=AF, UW=FF (IMX355), Tele=AF (JN5), Front=FF (KD1)

CAM26111_AF = {"Main": True, "UW": False, "Front": False}
CAM26121_AF = {"Main": True, "UW": False, "Tele": True, "Front": False}

# 变焦说明更新
ZOOM_DESC = (
    "变焦栏位于模式栏上方，默认变焦点应覆盖硬件光学点，并覆盖可用 In-Sensor Zoom 点。"
    "变焦方式：双指缩放变焦 或 滑动变焦条变焦（不同模式支持形式不同，详见验证方法）。"
    "SAT 平滑镜头切换、硬切镜头切换、纯数码变焦按项目/模式/摄像头组合判断。"
)


def process_csv(csv_path: Path, label: str, af_map: dict):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    new_rows = []
    updates = 0

    for row in rows:
        name = row.get("名称", "").strip()

        # --- AE/AF split ---
        if name == "自动对焦-自动曝光":
            mode = row.get("模式", "")
            cat1 = row.get("一级分类", "")
            cat2 = row.get("二级分类", "")
            cameras = [k for k in row if k not in (
                "模式", "一级分类", "二级分类", "名称", "说明",
                "不支持原因", "状态", "确认负责人", "验证方法")]

            # AE row: all cameras ✓
            ae_row = dict(row)
            ae_row["名称"] = "AE / 自动曝光"
            ae_row["说明"] = "包含自动曝光、点按测光、人脸测光、曝光补偿（-2EV~+2EV）等预览基础 AE 能力。所有摄像头支持。"
            for c in cameras:
                ae_row[c] = "✓"
            ae_row["不支持原因"] = ""
            ae_row["状态"] = "已确认"
            ae_row["确认负责人"] = "Product / SE / SQA"
            ae_row["验证方法"] = "短按/长按预览区域，确认 AE 调节 UI、曝光补偿和锁定功能。"
            new_rows.append(ae_row)

            # AF row: only AF cameras ✓
            af_row = dict(row)
            af_row["名称"] = "AF / 自动对焦"
            af_row["说明"] = "包含 CAF 连续自动对焦、Touch AF、Face AF、Touch AF Lock 等能力。FF（定焦）摄像头仅支持 AE，不支持 AF。"
            for c in cameras:
                if af_map.get(c, False):
                    af_row[c] = "✓"
                else:
                    af_row[c] = "✗"
            # Build unsupport reason for FF cameras
            reasons = []
            for c in cameras:
                if not af_map.get(c, False):
                    reasons.append(f"{c}: FF 定焦摄像头，仅支持 AE，不支持 AF。")
            af_row["不支持原因"] = "；".join(reasons) if reasons else ""
            af_row["状态"] = "已确认"
            af_row["确认负责人"] = "Product / SE / SQA"
            af_row["验证方法"] = "点击预览、人脸入镜、长按锁定、移动被摄体，确认 CAF/Touch AF/Face AF/Lock 行为；FF 摄像头确认仅 AE 生效。"
            new_rows.append(af_row)

            updates += 1
            print(f"  [{label}] SPLIT AE/AF: {mode}")
            continue

        # --- 变焦 → all ✓ ---
        if name == "变焦":
            cameras = [k for k in row if k not in (
                "模式", "一级分类", "二级分类", "名称", "说明",
                "不支持原因", "状态", "确认负责人", "验证方法")]
            old_status = row["状态"]
            old_cams = {c: row.get(c, "") for c in cameras}

            for c in cameras:
                row[c] = "✓"
            row["不支持原因"] = ""
            row["状态"] = "已确认"
            row["确认负责人"] = "Product / SE / SQA"
            if len(row.get("说明", "").strip()) < 30:
                row["说明"] = ZOOM_DESC

            updates += 1
            print(f"  [{label}] ZOOM: {row['模式']} {old_status} → 已确认")
            new_rows.append(row)
            continue

        new_rows.append(row)

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)

    return updates, len(new_rows)


def main():
    for fname, label, af_map in [
        ("26111_fl_draft.v1.0.csv", "26111", CAM26111_AF),
        ("26121_fl_draft.v1.0.csv", "26121", CAM26121_AF),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        n, total = process_csv(p, label, af_map)
        print(f"  {n} rows updated, total {total} rows")
        pending = 0
        with open(p, "r", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r.get("状态", "").strip() in ("待确认", "Pending"):
                    pending += 1
        print(f"  {pending}/{total} 待确认 ({(total-pending) * 100 // total}% 已确认)")


if __name__ == "__main__":
    main()
