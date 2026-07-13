#!/usr/bin/env python3
"""Finalize all PM decisions and generate v0.3 final CSVs."""

import csv
from pathlib import Path
from copy import deepcopy

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

def finalize(csv_path: Path, label: str):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)
    
    cameras = [k for k in fieldnames if k not in (
        "模式", "一级分类", "二级分类", "名称", "说明",
        "不支持原因", "状态", "确认负责人", "验证方法")]
    
    new_rows = []
    removed = 0
    updates = 0
    
    for row in rows:
        name = row.get("名称", "").strip()
        mode = row.get("模式", "").strip()
        cat2 = row.get("二级分类", "").strip()
        status = row.get("状态", "").strip()
        
        # --- DELETE rows ---
        if name in ("二维码识别", "工具栏热区呼出"):
            removed += 1
            print(f"  [{label}] DELETE: {name} ({mode})")
            continue
        
        # --- 识别框视觉动效 → move to AE/AF ---
        if name == "识别框视觉动效":
            row["二级分类"] = "AE/AF"
            row["状态"] = "已确认"
            row["确认负责人"] = "Product / SE"
            for c in cameras:
                row[c] = "✓"
            row["不支持原因"] = ""
            updates += 1
            print(f"  [{label}] MOVE: 识别框视觉动效 → AE/AF, 已确认")
        
        # --- 镜头脏污/AI去油污: UW = ✓ ---
        if name == "镜头脏污检测 / AI 去油污 / 提示引导" and status == "待确认":
            if "UW" in cameras:
                row["UW"] = "✓"
            row["状态"] = "已确认"
            row["确认负责人"] = "Product / SE"
            updates += 1
            print(f"  [{label}] 镜头脏污 UW→✓ ({mode})")
        
        # --- 锁定镜头: all ✓ ---
        if name == "锁定镜头" and status == "待确认":
            for c in cameras:
                row[c] = "✓"
            row["不支持原因"] = ""
            row["状态"] = "已确认"
            row["确认负责人"] = "Product / SE"
            updates += 1
            print(f"  [{label}] 锁定镜头 → 已确认")
        
        # --- AI Preset: 照片+人像, all ✓ ---
        if "AI Preset" in name and status == "待确认":
            for c in cameras:
                row[c] = "✓"
            row["不支持原因"] = ""
            row["状态"] = "已确认"
            row["确认负责人"] = "Product / SE"
            row["说明"] = "相机预览页引导入口，位于 Preset 按键附近；覆盖照片和人像模式的所有焦段。点击后分析当前预览帧并推荐滤镜+调色 preset 卡片。"
            updates += 1
            print(f"  [{label}] AI Preset → 已确认（照片+人像，全焦段）")
        
        # --- 26111: 4K30 UW = ✗ ---
        if label == "26111" and name in ("4K 30FPS", "4K 30FPS HLG") and "UW" in cameras and row.get("UW", "") in ("TBD", ""):
            row["UW"] = "✗"
            row["状态"] = "已确认" if all(
                row.get(c, "") in ("✓", "✗") for c in cameras
            ) else row["状态"]
            row["确认负责人"] = "Product / SE / SQA"
            if "UW:" not in (row.get("不支持原因") or ""):
                if row["不支持原因"]:
                    row["不支持原因"] += "；UW: 26111 Base 不支持 4K。"
                else:
                    row["不支持原因"] = "UW: 26111 Base 不支持 4K。"
            updates += 1
            print(f"  [{label}] {name}: UW ✗")
        
        # --- 26121: 慢动作 Tele = ✓ ---
        if label == "26121" and name in ("1080P 120FPS", "1080P 240FPS", "720P 120FPS", "720P 240FPS") and "Tele" in cameras and row.get("Tele", "") == "TBD":
            row["Tele"] = "✓"
            # Check if all cameras are now non-TBD
            all_resolved = all(row.get(c, "") in ("✓", "✗") for c in cameras)
            row["状态"] = "已确认" if all_resolved else row["状态"]
            updates += 1
            print(f"  [{label}] {name}: Tele ✓ → {row['状态']}")
        
        # --- 26121: 1080P60 UW = ✓ ---
        if label == "26121" and name in ("1080P 60FPS", "1080P 60FPS HLG") and "UW" in cameras and row.get("UW", "") in ("TBD", "✗", ""):
            row["UW"] = "✓"
            row["状态"] = "已确认"
            row["确认负责人"] = "Product / SE / SQA"
            updates += 1
            print(f"  [{label}] {name}: UW ✓")
        
        # --- 26121: 4K60 HLG Main/Tele = ✓ ---
        if label == "26121" and name in ("4K 60FPS", "4K 60FPS HLG") and "Main" in cameras:
            if row.get("Main", "") == "TBD":
                row["Main"] = "✓"
            if "Tele" in cameras and row.get("Tele", "") == "TBD":
                row["Tele"] = "✓"
            all_resolved = all(row.get(c, "") in ("✓", "✗") for c in cameras)
            row["状态"] = "已确认" if all_resolved else row["状态"]
            row["确认负责人"] = "Product / SE / SQA"
            updates += 1
            print(f"  [{label}] {name}: Main/Tele ✓")
        
        # --- General: resolve remaining 1080P30 HLG with no TBD cells ---
        if name == "1080P 30FPS HLG" and status == "待确认":
            all_resolved = all(row.get(c, "") in ("✓", "✗") for c in cameras)
            if all_resolved:
                row["状态"] = "已确认"
                row["确认负责人"] = "Product / SE / SQA"
                updates += 1
                print(f"  [{label}] {name}: all resolved → 已确认")
        
        # --- 26121: 4K30/4K30HLG - resolve if all non-TBD ---
        if label == "26121" and name in ("4K 30FPS", "4K 30FPS HLG") and status == "待确认":
            all_resolved = all(row.get(c, "") in ("✓", "✗") for c in cameras)
            if all_resolved:
                row["状态"] = "已确认"
                row["确认负责人"] = "Product / SE / SQA"
                updates += 1
                print(f"  [{label}] {name}: all resolved → 已确认")
        
        new_rows.append(row)
    
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)
    
    return removed, updates, len(new_rows)


def main():
    for fname, label in [
        ("26111_fl_draft.v1.0.csv", "26111"),
        ("26121_fl_draft.v1.0.csv", "26121"),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        rem, upd, total = finalize(p, label)
        pending = 0
        with open(p, "r", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r.get("状态", "").strip() in ("待确认", "Pending"):
                    pending += 1
        print(f"  Delete: {rem} | Updates: {upd} | {pending}/{total} 待确认 ({(total-pending) * 100 // total}% 已确认)")


if __name__ == "__main__":
    main()
