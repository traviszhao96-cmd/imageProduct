#!/usr/bin/env python3
"""Apply PM review notes from 26121 Bitable to both CSVs."""

import csv
from pathlib import Path
from copy import deepcopy

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

def apply_fixes(csv_path, label):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        all_rows = list(reader)
    
    cameras = [k for k in fieldnames if k not in (
        "模式", "一级分类", "二级分类", "名称", "说明",
        "不支持原因", "状态", "确认负责人", "验证方法")]
    
    new_rows = []
    fixes = 0
    
    for row in all_rows:
        name = row.get("名称", "").strip()
        mode = row.get("模式", "").strip()
        cat2 = row.get("二级分类", "").strip()
        
        # --- 1. 长时间无交互息屏 → move 到 Common, delete from Photo ---
        if "无交互息屏" in name and "Photo" in mode:
            # Change to Common
            row["模式"] = "通用 / Common"
            row["一级分类"] = "功能 / Feature"
            row["二级分类"] = "系统 / System"
            row["说明"] = "长时间无交互时息屏以节约电量，适用于所有模式。"
            fixes += 1
            print(f"  [{label}] MOVE: 长时间无交互息屏 → Common")
        
        # --- 2. OIS → add description for all rows ---
        if name == "OIS" and len(row.get("说明", "").strip()) < 10:
            row["说明"] = "光学防抖，由摄像头 OIS 硬件提供。拍摄和录像时补偿手持抖动，提升成片清晰度。26121 Pro 主摄(IMX896)和长焦(JN5)均配备 OIS。"
            fixes += 1
            print(f"  [{label}] OIS: updated 说明 ({mode})")
        
        # --- 3. 录影灯 → add description ---
        if name == "录影灯" and len(row.get("说明", "").strip()) < 10:
            row["说明"] = "录制指示灯。录像时闪烁红灯提示被摄对象正在录制中。"
            fixes += 1
            print(f"  [{label}] 录影灯: updated 说明 ({mode})")
        
        # --- 4. Flash (Expert) → add description ---
        if name == "Flash" and "Expert" in mode and len(row.get("说明", "").strip()) < 10:
            row["说明"] = "专业模式闪光灯入口。后置支持 Off / On / Torch，前置使用屏幕补光。"
            fixes += 1
            print(f"  [{label}] Flash: updated 说明 ({mode})")
        
        # --- 5. 1080P 240FPS → add default spec note ---
        if name == "1080P 240FPS":
            if "默认规格" not in (row.get("说明", "") or ""):
                row["说明"] = "慢动作模式高帧率录制规格：1080P 240FPS。慢动作默认规格之一。"
                fixes += 1
                print(f"  [{label}] 1080P 240FPS: updated 说明")
        
        # --- 6. 50MP/200MP/Ultra → move from 模式栏 to 工具栏 ---
        if name in ("50MP", "200MP", "200MP Ultra", "50MP Ultra"):
            if "模式栏" in cat2 or "Mode Switch" in cat2:
                row["二级分类"] = "工具栏 / Toolbar"
                row["说明"] = "高像素模式工具栏输出像素选项。" + name + "。使用 remosaic 高像素链路。" + ("Ultra 选项在 remosaic 后叠加 RAW HDR。" if "Ultra" in name else "")
                fixes += 1
                print(f"  [{label}] {name}: 模式栏 → 工具栏 ({mode})")
        
        new_rows.append(row)
    
    # --- 7. 延时摄影: split 4K row into 1080P30 + 4K30 spec rows ---
    new_rows_after = []
    for row in new_rows:
        name = row.get("名称", "").strip()
        if name == "4K" and "Timelapse" in row.get("模式", ""):
            fixes += 1
            print(f"  [{label}] SPLIT: 延时4K → 1080P30 + 4K30 spec rows")
            
            # Create 1080P30 row
            r1080 = deepcopy(row)
            r1080["名称"] = "1080P 30FPS"
            r1080["二级分类"] = "延时规格 / Timelapse Specs"
            r1080["说明"] = "延时摄影录制规格：1080P 30FPS。基础延时规格，所有支持延时摄影的摄像头默认支持。"
            r1080["验证方法"] = "切到延时摄影模式，选择 1080P 30FPS，逐个摄像头录制并检查入口、文件分辨率/帧率、稳定性和发热。"
            new_rows_after.append(r1080)
            
            # Create 4K30 row
            r4k = deepcopy(row)
            r4k["名称"] = "4K 30FPS"
            r4k["二级分类"] = "延时规格 / Timelapse Specs"
            r4k["说明"] = "延时摄影录制规格：4K 30FPS。高分辨率延时规格，需摄像头硬件支持4K输出。"
            r4k["验证方法"] = "切到延时摄影模式，选择 4K 30FPS，逐个支持摄像头录制并检查入口、文件分辨率/帧率、稳定性和发热。"
            new_rows_after.append(r4k)
        else:
            new_rows_after.append(row)
    
    new_rows = new_rows_after
    
    # --- 8. Panorama toolbar expansion ---
    pano_toolbar = ["Exposure", "Flash", "Grid", "More settings"]
    pano_existing = {r["名称"] for r in new_rows if "Panorama" in r.get("模式", "") and "Toolbar" in r.get("二级分类", "")}
    
    # Get Photo templates
    photo_toolbar_templates = {}
    for r in new_rows:
        if "Photo" in r.get("模式", "") and "Toolbar" in r.get("二级分类", ""):
            photo_toolbar_templates[r["名称"]] = r
    
    for tname in pano_toolbar:
        if tname not in pano_existing and tname in photo_toolbar_templates:
            nr = deepcopy(photo_toolbar_templates[tname])
            nr["模式"] = "全景 / Panorama"
            if tname == "Flash":
                for c in cameras: nr[c] = "✓"
                nr["不支持原因"] = ""
            new_rows.append(nr)
            fixes += 1
            print(f"  [{label}] + Panorama Toolbar: {tname}")
    
    # --- 9. Dual View Video toolbar expansion ---
    dv_existing = {r["名称"] for r in new_rows if "Dual View" in r.get("模式", "") and ("Toolbar" in r.get("二级分类", "") or "风格" in r.get("二级分类", ""))}
    dv_toolbar = ["Grid", "More settings", "Ratio"]
    
    for tname in dv_toolbar:
        if tname not in dv_existing and tname in photo_toolbar_templates:
            nr = deepcopy(photo_toolbar_templates[tname])
            nr["模式"] = "前后双录 / Dual View Video"
            nr["二级分类"] = "工具栏 / Toolbar"
            new_rows.append(nr)
            fixes += 1
            print(f"  [{label}] + DualView Toolbar: {tname}")
    
    # Sort: capture modes first, Common at bottom
    mode_order = [
        "照片 / Photo", "人像 / Portrait", "运动 / Action",
        "视频 / Video", "夜景 / Night", "慢动作 / Slow Motion",
        "全景 / Panorama", "专业 / Expert", "前后双录 / Dual View Video",
        "高像素 / High Resolution", "延时摄影 / Timelapse",
        "通用 / Common",
    ]
    def sort_key(row):
        try: return mode_order.index(row["模式"])
        except ValueError: return len(mode_order)
    new_rows.sort(key=sort_key)
    
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)
    
    return fixes, len(new_rows)


def main():
    for fname, label in [
        ("26111_fl_final.csv", "26111"),
        ("26121_fl_final.csv", "26121"),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        n, total = apply_fixes(p, label)
        pending = 0
        with open(p, "r", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                if r.get("状态", "").strip() in ("待确认", "Pending"):
                    pending += 1
        print(f"  {n} fixes | {pending}/{total} 待确认 ({(total-pending) * 100 // total}% 已确认)")


if __name__ == "__main__":
    main()
