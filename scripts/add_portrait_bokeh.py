#!/usr/bin/env python3
"""Add missing portrait bokeh features to both FL CSVs."""

import csv
from pathlib import Path
from copy import deepcopy

BASE = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")

# New Portrait rows to add (in order: functional, then algorithmic)
NEW_ROWS_26111 = [
    {
        "模式": "人像 / Portrait",
        "一级分类": "功能 / Feature",
        "二级分类": "模式栏 / Mode Switch",
        "名称": "虚化调节",
        "说明": "人像模式虚化强度调节，支持 f/1.4 ~ f/16 光圈模拟虚化效果，通过 slider 实时预览。",
        "Main": "✓", "UW": "✗", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "Product / IQA",
        "验证方法": "人像模式拖动虚化 slider，确认预览虚化强度变化和成片一致。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "功能 / Feature",
        "二级分类": "模式栏 / Mode Switch",
        "名称": "定制化光斑",
        "说明": "人像模式背景光斑形状定制，支持圆形/心形/星形等光斑风格。",
        "Main": "✓", "UW": "✗", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "Product / IQA",
        "验证方法": "人像模式切换光斑风格，在有光源的夜景场景确认背景光斑形状变化。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "基础算法 / Base Algorithm",
        "二级分类": "实时算法 / Realtime Algorithm",
        "名称": "虚化+HDR",
        "说明": "人像虚化链路叠加 HDR：虚化 + RAW HDR + 美颜 + FRT。",
        "Main": "✓", "UW": "✗", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "SE",
        "验证方法": "人像逆光场景拍摄，确认虚化边缘和 HDR 动态范围同时生效。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "基础算法 / Base Algorithm",
        "二级分类": "后处理算法 / Post-processing Algorithm",
        "名称": "虚化+夜景",
        "说明": "人像虚化链路叠加夜景：虚化 + 超级夜景 + 美颜 + 滤镜 + FRT。",
        "Main": "✓", "UW": "✗", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "SE",
        "验证方法": "人像低照场景拍摄，确认虚化边缘和夜景提亮降噪同时生效。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "基础算法 / Base Algorithm",
        "二级分类": "后处理算法 / Post-processing Algorithm",
        "名称": "虚化+MFNR",
        "说明": "人像虚化链路叠加 MFNR 多帧降噪：虚化 + MFNR + 美颜 + 滤镜 + FRT，走轻量化 MFNR。",
        "Main": "✓", "UW": "✗", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "SE",
        "验证方法": "人像普通低照非 HDR/夜景场景拍摄，确认虚化边缘和降噪同时生效。",
    },
]

NEW_ROWS_26121 = [
    # Same as 26111 but add Tele support
    {
        "模式": "人像 / Portrait",
        "一级分类": "功能 / Feature",
        "二级分类": "模式栏 / Mode Switch",
        "名称": "虚化调节",
        "说明": "人像模式虚化强度调节，支持 f/1.4 ~ f/16 光圈模拟虚化效果，通过 slider 实时预览。",
        "Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "Product / IQA",
        "验证方法": "人像模式拖动虚化 slider，确认预览虚化强度变化和成片一致。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "功能 / Feature",
        "二级分类": "模式栏 / Mode Switch",
        "名称": "定制化光斑",
        "说明": "人像模式背景光斑形状定制，支持圆形/心形/星形等光斑风格。",
        "Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "Product / IQA",
        "验证方法": "人像模式切换光斑风格，在有光源的夜景场景确认背景光斑形状变化。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "基础算法 / Base Algorithm",
        "二级分类": "实时算法 / Realtime Algorithm",
        "名称": "虚化+HDR",
        "说明": "人像虚化链路叠加 HDR：虚化 + RAW HDR + 美颜 + FRT。",
        "Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "SE",
        "验证方法": "人像逆光场景拍摄，确认虚化边缘和 HDR 动态范围同时生效。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "基础算法 / Base Algorithm",
        "二级分类": "后处理算法 / Post-processing Algorithm",
        "名称": "虚化+夜景",
        "说明": "人像虚化链路叠加夜景：虚化 + 超级夜景 + 美颜 + 滤镜 + FRT。",
        "Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "SE",
        "验证方法": "人像低照场景拍摄，确认虚化边缘和夜景提亮降噪同时生效。",
    },
    {
        "模式": "人像 / Portrait",
        "一级分类": "基础算法 / Base Algorithm",
        "二级分类": "后处理算法 / Post-processing Algorithm",
        "名称": "虚化+MFNR",
        "说明": "人像虚化链路叠加 MFNR 多帧降噪：虚化 + MFNR + 美颜 + 滤镜 + FRT，走轻量化 MFNR。",
        "Main": "✓", "UW": "✗", "Tele": "✓", "Front": "✓",
        "不支持原因": "UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。",
        "状态": "已确认",
        "确认负责人": "SE",
        "验证方法": "人像普通低照非 HDR/夜景场景拍摄，确认虚化边缘和降噪同时生效。",
    },
]


def add_rows(csv_path, new_rows, label):
    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        all_rows = list(reader)
    
    # Find insertion point: after last existing 人像/Portrait row
    insert_after = -1
    for i, row in enumerate(all_rows):
        if "Portrait" in row.get("模式", ""):
            insert_after = i
    
    # Insert new rows in order
    for nr in new_rows:
        # Create row with all columns
        full_row = {fn: "" for fn in fieldnames}
        full_row.update(nr)
        all_rows.insert(insert_after + 1, full_row)
        insert_after += 1
        print(f"  [{label}] + 人像: {nr['名称']} ({nr['二级分类']})")
    
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
    
    return len(new_rows)


def main():
    for fname, label, rows in [
        ("26111_fl_final.csv", "26111", NEW_ROWS_26111),
        ("26121_fl_final.csv", "26121", NEW_ROWS_26121),
    ]:
        p = BASE / fname
        print(f"\n=== {label} ===")
        n = add_rows(p, rows, label)
        total = 0
        pending = 0
        with open(p, "r", encoding="utf-8-sig") as f:
            for r in csv.DictReader(f):
                total += 1
                if r.get("状态", "").strip() in ("待确认", "Pending"):
                    pending += 1
        print(f"  +{n} rows | {pending}/{total} 待确认 ({(total-pending) * 100 // total}% 已确认)")


if __name__ == "__main__":
    main()
