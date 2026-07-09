#!/usr/bin/env python3
"""Generate a fresh clarification queue from current FL draft CSVs."""

import csv
from pathlib import Path
from collections import defaultdict

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

def analyze_csv(path: Path, label: str):
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    pending = []  # 状态=待确认
    has_tbd = []  # 状态=已确认 but cells contain TBD
    weak_desc = []  # empty or very short 说明
    total = len(rows)

    for row in rows:
        status = row.get("状态", "").strip()
        name = row.get("名称", "").strip()
        mode = row.get("模式", "").strip()
        cat1 = row.get("一级分类", "").strip()
        cat2 = row.get("二级分类", "").strip()
        desc = row.get("说明", "").strip()
        
        # Get camera columns
        cameras = [k for k in row if k not in 
                   ("模式","一级分类","二级分类","名称","说明","不支持原因","状态","确认负责人","验证方法")]
        
        tbd_cells = [c for c in cameras if "TBD" in (row.get(c, "") or "")]
        has_empty_desc = len(desc) < 10

        key = f"{mode} | {cat1} | {cat2} | {name}"

        if status in ("待确认", "Pending"):
            pending.append({
                "key": key,
                "mode": mode,
                "name": name,
                "cat1": cat1,
                "cat2": cat2,
                "desc": desc[:80],
                "tbd_cams": tbd_cells,
                "cam_status": {c: row.get(c, "").strip() for c in cameras},
                "owner": row.get("确认负责人", "").strip(),
            })
        elif tbd_cells:
            has_tbd.append({
                "key": key,
                "mode": mode,
                "name": name,
                "tbd_cams": tbd_cells,
                "cam_status": {c: row.get(c, "").strip() for c in cameras},
            })
        
        if has_empty_desc and status != "待确认":
            weak_desc.append(key)

    return total, pending, has_tbd, weak_desc


def group_pending(pending_26111, pending_26121):
    """Group pending items by theme."""
    themes = defaultdict(list)
    
    all_keys_26111 = {p["key"] for p in pending_26111}
    all_keys_26121 = {p["key"] for p in pending_26121}
    
    for p in pending_26111:
        key = p["key"]
        name = p["name"]
        mode = p["mode"]
        
        if "视频规格" in p.get("cat2", "") or "Video Specs" in p.get("cat2", ""):
            themes["视频规格矩阵"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "慢动作规格" in p.get("cat2", "") or "Slow Motion" in p.get("cat2", ""):
            themes["慢动作规格矩阵"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "锁定镜头" in name:
            themes["锁定镜头继承"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "ISZ" in name or "In Sensor" in name:
            themes["ISZ点位"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "Log" in name:
            themes["Log视频规格"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "AE/AF" in name or "自动对焦" in name:
            themes["AE/AF基础能力"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "变焦" == name:
            themes["变焦配置"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "ASD" in name or "AI场景检测" in name:
            themes["ASD/AI场景检测"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "人脸检测" == name:
            themes["人脸检测"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "脏污检测" == name or "去油污" in name:
            themes["脏污/去油污"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "Glyph" in name:
            themes["Glyph Mirror"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "Grid" in name or "More settings" in name or "Watermark" in name or "Ratio" in name:
            themes["基础Toolbar行"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "Text Mode" in name:
            themes["Text Mode"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "自动夜景" in name:
            themes["自动夜景暂态开关"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "自动微距" in name:
            themes["自动微距控制"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "运动场景引导" in name:
            themes["运动场景引导"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "识别框" in name or "二维码识别" in name:
            themes["识别框/二维码"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "工具栏热区" in name:
            themes["工具栏热区"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "AI Preset" in name or "场景推荐" in name:
            themes["AI Preset引导"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "VSS" in name or "录像中拍照" in name:
            themes["录像中拍照(VSS)"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "视频曝光" in name or "白平衡调节" in name:
            themes["视频曝光/WB调节"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "OIS" in name:
            themes["OIS"].append((key, mode, name, p["tbd_cams"], "26111"))
        elif "HLG" in name or "HDR 规格" in name:
            themes["HLG/HDR视频"].append((key, mode, name, p["tbd_cams"], "26111"))
        else:
            themes[name].append((key, mode, name, p["tbd_cams"], "26111"))
    
    # Add 26121-only pending items
    for p in pending_26121:
        key = p["key"]
        if key not in all_keys_26111:
            themes["26121-only"].append((key, p["mode"], p["name"], p["tbd_cams"], "26121"))
    
    return themes


def main():
    print("# 26111 / 26121 FL 澄清清单 v0.2\n")
    print("> 生成时间: 2026-07-08, 基于 v0.2 restyled drafts\n")
    
    t1, p1, tbd1, weak1 = analyze_csv(BASE / "26111_fl_draft.v0.2.csv", "26111")
    t2, p2, tbd2, weak2 = analyze_csv(BASE / "26121_fl_draft.v0.2.csv", "26121")
    
    print("## Snapshot\n")
    print(f"| | 26111 | 26121 |")
    print(f"|---|---:|---:|")
    print(f"| 总行数 | {t1} | {t2} |")
    print(f"| 状态=待确认 | {len(p1)} | {len(p2)} |")
    print(f"| 已确认但含TBD cells | {len(tbd1)} | {len(tbd2)} |")
    print(f"| 说明过短(<10字) | {len(weak1)} | {len(weak2)} |")
    
    themes = group_pending(p1, p2)
    
    # P0 items
    p0_themes = ["视频规格矩阵", "慢动作规格矩阵", "HLG/HDR视频", "Log视频规格", "ISZ点位", "锁定镜头继承"]
    print("\n## P0 — 阻塞最终签核\n")
    for theme in p0_themes:
        if theme in themes:
            items = themes[theme]
            print(f"### {theme} ({len(items)} 行)\n")
            print(f"| 项目 | 模式 | 名称 | TBD摄像头 |")
            print(f"|------|------|------|------|")
            for key, mode, name, tbd, proj in items:
                tbd_str = ", ".join(tbd) if tbd else "—"
                print(f"| {proj} | {mode} | {name} | {tbd_str} |")
            print()
    
    # P1 items
    p1_themes = ["AE/AF基础能力", "变焦配置", "ASD/AI场景检测", "人脸检测", 
                  "脏污/去油污", "自动夜景暂态开关", "自动微距控制", "Glyph Mirror",
                  "基础Toolbar行", "Text Mode", "运动场景引导", "识别框/二维码",
                  "OIS", "录像中拍照(VSS)", "视频曝光/WB调节", "AI Preset引导",
                  "工具栏热区"]
    
    print("## P1 — 含义清楚，待填支持矩阵\n")
    for theme in p1_themes:
        if theme in themes:
            items = themes[theme]
            print(f"### {theme} ({len(items)} 行)\n")
            modes_covered = set()
            for key, mode, name, tbd, proj in items:
                modes_covered.add(mode)
                tbd_str = ", ".join(tbd) if tbd else "全部TBD"
                print(f"| {proj} | {mode} | {name} | {tbd_str} |")
            print()
    
    # P2 items (已确认但有TBD cells)
    if tbd1 or tbd2:
        print("## P2 — 已确认但有TBD cells（需数据填充）\n")
        all_tbd = list(set(
            (r["mode"], r["name"], ", ".join(r["tbd_cams"])) for r in tbd1
        )) + list(set(
            (r["mode"], r["name"], ", ".join(r["tbd_cams"])) for r in tbd2
        ))
        all_tbd_dedup = list(dict.fromkeys(all_tbd))
        for mode, name, cams in all_tbd_dedup[:20]:
            print(f"| {mode} | {name} | {cams} |")
        print(f"\n(仅显示前 20 项，共 {len(all_tbd_dedup)} 项)")

    # Other items
    other_themes = set(themes.keys()) - set(p0_themes) - set(p1_themes)
    if other_themes:
        print("\n## 其他\n")
        for theme in sorted(other_themes):
            items = themes[theme]
            for key, mode, name, tbd, proj in items:
                print(f"| {proj} | {mode} | {name} | {', '.join(tbd) if tbd else '—'} |")


if __name__ == "__main__":
    main()
