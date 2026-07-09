#!/usr/bin/env python3
"""Fix portrait bokeh: classification + update KB."""

import csv, json
from pathlib import Path

BASE = Path("/Users/travis.zhao/imageProduct")
CSV_DIR = BASE / "knowledge/_output/fl_draft_26111_26121"
KB_PATH = BASE / "knowledge/_output/kb-functions-algorithms.v6.json"

# Classification fixes
FIXES = {
    "虚化+HDR": {"二级分类": "后处理算法 / Post-processing Algorithm"},
    "虚化+夜景": {"二级分类": "后处理算法 / Post-processing Algorithm"},  # already correct
    "虚化+MFNR": {"二级分类": "后处理算法 / Post-processing Algorithm"},  # already correct
    "虚化调节": {
        "二级分类": "变焦 / Zoom",
        "说明": "人像模式 zoom bar 右侧虚化开关。虚化强度调节 slider，支持 f/1.4 ~ f/16 光圈模拟，实时预览。",
    },
    "定制化光斑": {
        "二级分类": "变焦 / Zoom",
        "说明": "人像模式 zoom bar 右侧虚化开关子选项。背景光斑形状定制，支持圆形/心形/星形等。",
    },
}

# New KB entries
NEW_KB = [
    {
        "模式": "人像",
        "一级分类": "功能",
        "二级分类": "Zoom",
        "名称": "虚化调节",
        "说明": "人像模式 zoom bar 右侧虚化开关，虚化强度 slider（f/1.4~f/16），实时预览虚化效果。",
        "判断依据": "人像模式存在虚化调节 slider 且能实时影响预览虚化强度时填写。",
        "依赖": "依赖虚化算法、预览流、slider UI、光圈映射曲线。",
        "验证方法": "人像模式拖动虚化 slider，确认预览虚化和成片虚化强度一致，f-stop 映射正确。",
        "来源项目": "25111 / 25131",
        "备注": "位于人像 zoom bar 右侧，与美颜开关（zoom bar 左侧）对称。"
    },
    {
        "模式": "人像",
        "一级分类": "功能",
        "二级分类": "Zoom",
        "名称": "定制化光斑",
        "说明": "人像模式 zoom bar 右侧虚化开关子选项，背景光斑形状定制，支持圆形/心形/星形等风格。",
        "判断依据": "人像模式存在光斑风格切换入口时填写。",
        "依赖": "依赖虚化算法、光斑渲染、预览流、UI 入口。",
        "验证方法": "切换不同光斑风格，在有光源的夜景/灯光场景确认背景光斑形状变化。",
        "来源项目": "25111 / 25131",
        "备注": "虚化调节的子功能，与虚化 slider 联动。"
    },
    {
        "模式": "人像",
        "一级分类": "基础算法",
        "二级分类": "后处理算法",
        "名称": "虚化+HDR",
        "说明": "人像虚化链路叠加 HDR：虚化 + RAW HDR + 美颜 + FRT，后处理合成。",
        "判断依据": "人像模式同时开启虚化和 HDR 时，虚化和 HDR 可叠加处理时填写。",
        "依赖": "依赖虚化算法、RAW HDR、美颜、FRT、后处理合成链路。",
        "验证方法": "人像逆光场景开启虚化+HDR 拍摄，确认虚化边缘和 HDR 动态范围同时生效，无合成伪影。",
        "来源项目": "25111 / 25131",
        "备注": "虚化+HDR 走同一后处理管线，非实时叠加。"
    },
    {
        "模式": "人像",
        "一级分类": "基础算法",
        "二级分类": "后处理算法",
        "名称": "虚化+夜景",
        "说明": "人像虚化链路叠加夜景：虚化 + 超级夜景 + 美颜 + 滤镜 + FRT，全部在后处理完成。",
        "判断依据": "人像模式低照触发夜景时，虚化和 Super Night 可叠加处理时填写。",
        "依赖": "依赖虚化算法、Super Night、美颜、滤镜、FRT、后处理合成链路。",
        "验证方法": "人像低照场景开启虚化拍摄，确认虚化边缘和夜景提亮降噪同时生效，合成延时在可接受范围。",
        "来源项目": "25111 / 25131",
        "备注": "低照场景虚化+夜景叠加，处理耗时可能高于普通虚化。"
    },
    {
        "模式": "人像",
        "一级分类": "基础算法",
        "二级分类": "后处理算法",
        "名称": "虚化+MFNR",
        "说明": "人像虚化链路叠加 MFNR：虚化 + MFNR 多帧降噪 + 美颜 + 滤镜 + FRT，走轻量化 MFNR，后处理完成。",
        "判断依据": "人像模式非 HDR/非夜景普通低照，虚化和 MFNR 可叠加处理时填写。",
        "依赖": "依赖虚化算法、MFNR、美颜、滤镜、FRT、后处理合成链路。",
        "验证方法": "人像普通低照场景开启虚化拍摄，确认虚化边缘和多帧降噪同时生效。",
        "来源项目": "25111 / 25131",
        "备注": "轻量化 MFNR 叠加，处理时长接近普通虚化。"
    },
]


def fix_csv(csv_path, label):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    fixed = 0
    for row in rows:
        name = row.get("名称", "").strip()
        if name in FIXES:
            for k, v in FIXES[name].items():
                row[k] = v
            fixed += 1
            print(f"  [{label}] {name}: updated {list(FIXES[name].keys())}")

    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return fixed


def update_kb():
    with open(KB_PATH, "r", encoding="utf-8") as f:
        kb = json.load(f)

    added = 0
    for entry in NEW_KB:
        exists = any(
            e.get("名称") == entry["名称"] and e.get("模式") == entry["模式"]
            for e in kb
        )
        if not exists:
            kb.append(entry)
            added += 1
            print(f"  KB + {entry['模式']}: {entry['名称']}")

    with open(KB_PATH, "w", encoding="utf-8") as f:
        json.dump(kb, f, ensure_ascii=False, indent=2)

    return added, len(kb)


def main():
    # Fix CSVs
    for fname, label in [
        ("26111_fl_final.csv", "26111"),
        ("26121_fl_final.csv", "26121"),
    ]:
        p = CSV_DIR / fname
        print(f"\n=== Fix {label} ===")
        fix_csv(p, label)

    # Update KB
    print("\n=== Update KB ===")
    added, total = update_kb()
    print(f"  +{added} entries, KB now {total} rows")


if __name__ == "__main__":
    main()
