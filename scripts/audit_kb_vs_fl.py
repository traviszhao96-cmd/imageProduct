#!/usr/bin/env python3
"""Audit: KB features per mode vs FL rows per mode."""

import json, csv
from pathlib import Path
from collections import defaultdict

BASE = Path("/Users/travis.zhao/imageProduct")
KB_PATH = BASE / "knowledge/_output/kb-functions-algorithms.v6.json"
FL_PATH = BASE / "knowledge/_output/fl_draft_26111_26121/26111_fl_draft.v0.2.csv"

# Mode name mapping from KB to FL
MODE_MAP = {
    "通用": "通用 / Common",
    "照片": "照片 / Photo",
    "人像": "人像 / Portrait",
    "运动": "运动 / Action",
    "视频": "视频 / Video",
    "夜景": "夜景 / Night",
    "慢动作": "慢动作 / Slow Motion",
    "全景": "全景 / Panorama",
    "专业": "专业 / Expert",
    "前后双录": "前后双录 / Dual View Video",
    "高像素": "高像素 / High Resolution",
    "延时摄影": "延时摄影 / Timelapse",
}

# Load KB
with open(KB_PATH, "r", encoding="utf-8") as f:
    kb = json.load(f)

# Parse KB mode scopes
kb_coverage = defaultdict(list)
for item in kb:
    raw_modes = item.get("模式", "")
    name = item.get("名称", "")
    cat1 = item.get("一级分类", "")
    cat2 = item.get("二级分类", "")
    modes = [m.strip() for m in raw_modes.replace("/", " / ").split(" / ")]
    modes = [m.strip() for m in modes if m.strip()]
    # Combine into single modes
    # e.g. "照片 / 人像" → ["照片", "人像"]
    simple_modes = []
    for m in modes:
        m = m.strip()
        if m in MODE_MAP:
            simple_modes.append(m)
    
    for m in simple_modes:
        kb_coverage[m].append(f"{cat1} > {cat2} > {name}")

# Load FL
with open(FL_PATH, "r", encoding="utf-8-sig") as f:
    fl = list(csv.DictReader(f))

fl_coverage = defaultdict(list)
for row in fl:
    mode = row.get("模式", "").strip()
    name = row.get("名称", "").strip()
    cat1 = row.get("一级分类", "").strip()
    cat2 = row.get("二级分类", "").strip()
    # Reverse map FL mode to KB mode
    for kb_m, fl_m in MODE_MAP.items():
        if mode == fl_m:
            fl_coverage[kb_m].append(f"{cat1} > {cat2} > {name}")
            break

# Compare
print("## KB vs FL: 功能覆盖差异\n")
print("KB function names → 'KB expects' means KB says this function belongs in this mode.\n")

for kb_mode in sorted(kb_coverage.keys()):
    kb_set = set(kb_coverage[kb_mode])
    fl_set = set(fl_coverage.get(kb_mode, []))
    
    # Extract just function names for comparison
    kb_names = set()
    for item in kb_set:
        parts = item.split(" > ")
        if len(parts) >= 3:
            kb_names.add(parts[2])
    
    fl_names = set()
    for item in fl_set:
        parts = item.split(" > ")
        if len(parts) >= 3:
            fl_names.add(parts[2])
    
    missing = kb_names - fl_names
    extra = fl_names - kb_names
    
    fl_m = MODE_MAP.get(kb_mode, kb_mode)
    print(f"### {fl_m} ({kb_mode})")
    print(f"KB expects: {len(kb_names)} funcs, FL has: {len(fl_names)} funcs")
    
    if missing:
        print("\n**Missing in FL:**")
        for n in sorted(missing):
            # Find KB item
            for item in kb_set:
                if n in item:
                    print(f"  - `{item}`")
    if extra:
        print(f"\n**Extra in FL (not in KB):**")
        for n in sorted(extra)[:10]:
            print(f"  - {n}")
    print()

# Also: show which KB items are NOT mapped to any FL mode
print("\n## KB items with NO FL coverage\n")
all_kb_names = set()
for items in kb_coverage.values():
    for item in items:
        parts = item.split(" > ")
        if len(parts) >= 3:
            all_kb_names.add(parts[2])

all_fl_names = set()
for items in fl_coverage.values():
    for item in items:
        parts = item.split(" > ")
        if len(parts) >= 3:
            all_fl_names.add(parts[2])

unmapped = all_kb_names - all_fl_names
if unmapped:
    print(f"{len(unmapped)} KB functions not in FL at all:")
    for n in sorted(unmapped):
        print(f"  - {n}")
