#!/usr/bin/env python3
"""Generate views from the knowledge base JSON files.

Usage:
  python3 knowledge/generate.py markdown  → knowledge/_output/features.md
  python3 knowledge/generate.py excel     → knowledge/_output/features.xlsx
  python3 knowledge/generate.py all       → both
"""

import json, os, sys
from pathlib import Path
from collections import defaultdict

KB = Path(__file__).parent
OUT = KB / '_output'

# ===== Load data =====

def load(name):
    with open(KB / name) as f:
        return json.load(f)

# ===== Markdown generator =====

def md_support_table(features, title, cameras):
    """Generate a markdown table grouped by mode→category→group."""
    lines = [f'# {title}', '', f'> 项目 25131 | 自动生成 | {len(features)} 项功能', '']

    # Group by mode
    by_mode = defaultdict(list)
    for f in features:
        by_mode[f['mode']].append(f)

    for mode in sorted(by_mode):
        items = by_mode[mode]
        cam_keys = list(items[0].get('support', {}).keys())
        cam_header = ' | '.join(cam_keys)
        header = f'| 分类 | 功能 | {cam_header} | 验证方式 |'
        sep = f'|------|------|{"|".join("------" for _ in cam_keys)}|------|'

        lines.append(f'## {mode}')
        lines.append('')
        lines.append(header)
        lines.append(sep)

        for f in items:
            def ss(v):
                if v == 'supported': return '✅'
                if v == 'unsupported': return '❌'
                return v
            support_str = ' | '.join(ss(f['support'].get(c, '')) for c in cam_keys)
            verify = f.get('verify', '')[:80]
            lines.append(f'| {f["category"]} | {f["group"]} > {f["name"]} | {support_str} | {verify} |')

        lines.append('')

    return '\n'.join(lines)


def md_focal_lengths(configs):
    """Generate focal length configuration table."""
    lines = ['# 焦段配置', '', f'> 项目 25131 | {len(configs)} 个模式/模式组', '']

    for c in configs:
        lines.append(f'## {c["mode"]}')
        lines.append('')
        lines.append(f'- 焦段按钮: {", ".join(c["buttons"])}')
        lines.append(f'- 滑动变焦: {"✅" if c["slide_zoom"] else "❌"}')
        lines.append(f'- 最大变焦: {c["max_zoom"]}')
        lines.append(f'- Preset 可选: {", ".join(c["preset_focal_lengths"])}')
        lines.append('')

    return '\n'.join(lines)


def md_devices(specs):
    """Generate device specs markdown."""
    lines = ['# 设备规格', '', f'> 项目 {specs["project"]}', '']

    for cam_key, cam in specs['cameras'].items():
        lines.append(f'## {cam["name"]} ({cam_key})')
        lines.append('')
        lines.append('| 属性 | 值 |')
        lines.append('|------|-----|')
        for key, val in cam['specs'].items():
            lines.append(f'| {key} | {val} |')
        lines.append('')

    return '\n'.join(lines)


# ===== Excel generator =====

def generate_excel():
    try:
        import openpyxl
        from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    except ImportError:
        print("Need openpyxl: pip install openpyxl")
        return

    rear = load('features/rear-camera.json')
    front = load('features/front-camera.json')
    fl = load('features/focal-lengths.json')
    specs = load('devices/25131.json')

    wb = openpyxl.Workbook()

    # --- Rear Camera sheet ---
    ws = wb.active
    ws.title = '后置摄像头'

    header_font = Font(bold=True, size=11)
    header_fill = PatternFill(start_color='1C1A16', end_color='1C1A16', fill_type='solid')
    header_font_white = Font(bold=True, size=11, color='FFFFFF')
    thin_border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )

    # Header
    cam_keys = ['ultrawide', 'main', 'macro']
    headers = ['模式', '分类', '功能组', '子功能', '超广角', '主摄', '微距', '验证方式']
    for ci, h in enumerate(headers, 1):
        cell = ws.cell(row=1, column=ci, value=h)
        cell.font = header_font_white
        cell.fill = header_fill
        cell.border = thin_border

    for ri, f in enumerate(rear['features'], 2):
        ws.cell(row=ri, column=1, value=f['mode']).border = thin_border
        ws.cell(row=ri, column=2, value=f['category']).border = thin_border
        ws.cell(row=ri, column=3, value=f['group']).border = thin_border
        ws.cell(row=ri, column=4, value=f['name']).border = thin_border
        for ci, ck in enumerate(cam_keys, 5):
            v = f['support'].get(ck, '')
            ws.cell(row=ri, column=ci, value='√' if v == 'supported' else ('×' if v == 'unsupported' else v)).border = thin_border
        ws.cell(row=ri, column=8, value=f.get('verify', '')).border = thin_border

    ws.auto_filter.ref = ws.dimensions
    ws.freeze_panes = 'A2'

    # --- Front Camera sheet ---
    ws2 = wb.create_sheet('前置摄像头')
    headers2 = ['模式', '分类', '功能组', '子功能', '前置', '验证方式']
    for ci, h in enumerate(headers2, 1):
        cell = ws2.cell(row=1, column=ci, value=h)
        cell.font = header_font_white
        cell.fill = header_fill
        cell.border = thin_border

    for ri, f in enumerate(front['features'], 2):
        ws2.cell(row=ri, column=1, value=f['mode']).border = thin_border
        ws2.cell(row=ri, column=2, value=f['category']).border = thin_border
        ws2.cell(row=ri, column=3, value=f['group']).border = thin_border
        ws2.cell(row=ri, column=4, value=f['name']).border = thin_border
        v = f['support'].get('front', '')
        ws2.cell(row=ri, column=5, value='√' if v == 'supported' else ('×' if v == 'unsupported' else v)).border = thin_border
        ws2.cell(row=ri, column=6, value=f.get('verify', '')).border = thin_border

    ws2.auto_filter.ref = ws2.dimensions
    ws2.freeze_panes = 'A2'

    # --- Focal Lengths sheet ---
    ws3 = wb.create_sheet('焦段配置')
    for ci, h in enumerate(['模式', '焦段按钮', '滑动变焦', '最大变焦', 'Preset焦距'], 1):
        cell = ws3.cell(row=1, column=ci, value=h)
        cell.font = header_font_white
        cell.fill = header_fill
        cell.border = thin_border

    for ri, c in enumerate(fl['configs'], 2):
        ws3.cell(row=ri, column=1, value=c['mode']).border = thin_border
        ws3.cell(row=ri, column=2, value='\n'.join(c['buttons'])).border = thin_border
        ws3.cell(row=ri, column=3, value='✓' if c['slide_zoom'] else '×').border = thin_border
        ws3.cell(row=ri, column=4, value=c['max_zoom']).border = thin_border
        ws3.cell(row=ri, column=5, value='\n'.join(c['preset_focal_lengths'])).border = thin_border

    ws3.freeze_panes = 'A2'

    # --- Hardware Specs sheet ---
    ws4 = wb.create_sheet('硬件规格')
    for ci, h in enumerate(['属性', '50M 主摄', '8M 广角', '16M 前摄'], 1):
        cell = ws4.cell(row=1, column=ci, value=h)
        cell.font = header_font_white
        cell.fill = header_fill
        cell.border = thin_border

    cam_names = ['main', 'ultrawide', 'front']
    all_spec_keys = []
    for ck in cam_names:
        if ck in specs['cameras']:
            all_spec_keys.extend(specs['cameras'][ck]['specs'].keys())
    all_spec_keys = list(dict.fromkeys(all_spec_keys))

    for ri, key in enumerate(all_spec_keys, 2):
        ws4.cell(row=ri, column=1, value=key).border = thin_border
        for ci, ck in enumerate(cam_names, 2):
            val = specs['cameras'].get(ck, {}).get('specs', {}).get(key, '')
            ws4.cell(row=ri, column=ci, value=val).border = thin_border

    ws4.freeze_panes = 'B2'

    out_path = OUT / 'features.xlsx'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(str(out_path))
    return out_path


# ===== Main =====

def main():
    fmt = sys.argv[1] if len(sys.argv) > 1 else 'all'
    OUT.mkdir(parents=True, exist_ok=True)

    if fmt in ('markdown', 'all'):
        rear = load('features/rear-camera.json')
        front = load('features/front-camera.json')
        fl = load('features/focal-lengths.json')
        specs = load('devices/25131.json')

        md = []
        md.append(md_support_table(rear['features'], '后置摄像头功能列表', rear['meta']))
        md.append('\n---\n')
        md.append(md_support_table(front['features'], '前置摄像头功能列表', front['meta']))
        md.append('\n---\n')
        md.append(md_focal_lengths(fl['configs']))
        md.append('\n---\n')
        md.append(md_devices(specs))

        out = '\n'.join(md)
        path = OUT / 'features.md'
        path.write_text(out)
        print(f'Markdown: {path} ({len(out):,} chars)')

    if fmt in ('excel', 'all'):
        path = generate_excel()
        print(f'Excel: {path}')

if __name__ == '__main__':
    main()
