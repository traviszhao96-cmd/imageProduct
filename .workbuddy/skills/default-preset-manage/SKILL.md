---
name: default-preset-manage
description: Use when the user asks to read, update, or sync the Camera Default Preset Bitable, add/modify presets, manage cover images, or maintain the change log. Covers the 12 default presets across all Nothing/CMF phone models.
---

# Default Preset Manager

## Overview

This skill manages the **Camera Default Preset** multidimensional table (多维表格) in Lark. It is the single source of truth for all default camera presets shipped on Nothing/CMF phones. The skill handles reading/syncing data between Lark and local git, updating preset parameters, uploading cover images, and maintaining the change log.

## Input Quality Check

开始任何操作前，先判断用户输入是否足够。如果只有一句话需求（如"帮我加一个 preset"、"更新一下封面"），必须先确认以下信息，不要直接操作：

| 缺乏的信息 | 需要确认 |
|-----------|---------|
| 哪个 Preset？ | Preset Name |
| 做什么操作？ | 新增 / 修改 / 删除 |
| 修改了哪些字段？ | 具体字段和值 |
| 有没有设计稿？ | Figma Link（如有） |
| 有没有封面图？ | 图片文件（如有，需 1080×1440 或 16:9） |

**一句话需求示例：**"帮我更新 Sports preset"

→ 应回复："请确认要更新 Sports 的哪些字段？Tuning？Focal Length？Cover？"

## App & Table IDs

| Item | ID |
|------|----|
| Bitable app | `TKuObORHDa0vNgs3gF9lsKdPgUg` |
| Table (presets) | `tblGPOTtAH66KGXN` |
| Table (修改记录) | `tblrxQxcMJ4PN5og` |
| Bitable URL | `https://nothing-tech.sg.larksuite.com/base/TKuObORHDa0vNgs3gF9lsKdPgUg` |
| Old Bitable (read-only ref) | `JeMabM2QWaH4TmsaHxpliCfwgMd` |

## Authentication

```python
import json, urllib.request, ssl
from pathlib import Path

config = json.loads(Path.home().joinpath('.openclaw/openclaw.json').read_text())
account = config['channels']['feishu']['accounts']['main']
app_id, app_secret = account['appId'], account['appSecret']

req = urllib.request.Request(
    'https://open.larksuite.com/open-apis/auth/v3/tenant_access_token/internal',
    data=json.dumps({'app_id': app_id, 'app_secret': app_secret}).encode(),
    headers={'Content-Type': 'application/json'}, method='POST')
token = json.loads(urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()).read())['tenant_access_token']
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
```

## API Endpoints

| 操作 | Method | Path |
|------|--------|------|
| 获取 records | GET | `/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records?page_size=500` |
| 获取 fields | GET | `/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields` |
| 创建 record | POST | `/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records` |
| 更新 record | PUT | `/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}` |
| 删除 record | DELETE | `/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}` |
| 批量创建 | POST | `/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create` |
| 上传附件 | POST | `/open-apis/drive/v1/medias/upload_all` (multipart: file, file_name, parent_type="bitable_file", parent_node=app_token, size) |

### 注意事项

- Python 环境只有标准库，使用 `urllib.request`
- 批量操作后 `time.sleep(0.3)`, 字段操作后 `time.sleep(0.15)`
- 上传附件后 `time.sleep(0.5)`

## Field Structure (24 columns)

| # | Field | Type | Options |
|---|-------|------|---------|
| 1 | Preset Name | Text (1) | Primary field |
| 2 | Sort | Text (1) | |
| 3 | Description | Text (1) | Bilingual EN/CN |
| 4 | 备注 | Text (1) | Device/region notes |
| 5 | Figma Link | Text (1) | URL or "None" |
| 6 | Cover | Attachment (17) | 1080×1440 JPEG（Photo/Portrait/Action/Macro 模式）；16:9 横版（Video 模式） |
| 7 | Mode | SingleSelect (3) | Photo, Video, Action, Portrait, Macro |
| 8 | Lens | SingleSelect (3) | Rear, Front |
| 9 | Focal Length | Text (1) | Device-specific: `25111-160mm \| 25131-28mm` |
| 10 | Exposure | Text (1) | |
| 11 | Filter | Text (1) | Format: `{Name} \| {Strength}` or "Original" |
| 12 | Tuning | Text (1) | Multiline with `\|` separators, or "无" |
| 13 | Author | Text (1) | Name or "无" |
| 14 | Portrait Effect | Text (1) | "不涉及" for non-Portrait modes |
| 15 | Bokeh | Text (1) | "不涉及" for non-Portrait modes |
| 16 | Watermark | SingleSelect (3) | On, Off |
| 17 | Flash | SingleSelect (3) | On, Off, Auto |
| 18 | Timer | SingleSelect (3) | Off, 3s, 10s |
| 19 | HDR | SingleSelect (3) | On, Off, Auto |
| 20 | Auto Tone | SingleSelect (3) | On, Off |
| 21 | Motion Photo | SingleSelect (3) | On, Off |
| 22 | Quality | SingleSelect (3) | 12MP, 50MP, 1080P30, 1080P60, 4K30 |
| 23 | Grid | SingleSelect (3) | On, Off |
| 24 | Ratio | SingleSelect (3) | 4:3, 16:9, 1:1, FULL |

> 共 25 个字段。修改记录表 `tblrxQxcMJ4PN5og` 已从旧 Bitable 同步。

## Fill Rules (填写规则)

When adding or updating preset data, follow these strict conventions:

| 标注 | When to use | Example |
|------|-------------|---------|
| **不涉及** | Field not applicable to this Mode | Bokeh for Photo mode |
| **无** | Field applicable but value is empty/none | No Tuning needed |
| **None** | Explicit empty marker (= 无) | No Figma Link, No Cover |
| **Original** | Filter field: no filter applied | Default filter state |

### Per-field rules

| Field | Has value | No value / Not applicable |
|-------|-----------|---------------------------|
| Author | Actual name (e.g. "Jordan Hemingway") | **无** |
| Figma Link | Full URL | **None** |
| Cover | Attachment uploaded | **None** |
| Filter | `{Name} \| {Strength}` | **Original** |
| Tuning | Parameters with `\|` separators | **无** |
| Portrait Effect | Portrait mode: "Velvet" etc. | **不涉及** (all other modes) |
| Bokeh | Portrait mode: f-stop value | **不涉及** (all other modes) |

## Cricket ↔ Sports Sync Rule

Cricket and Sports are the **same preset with different regional branding**:

- **Cricket**: India/RCB region, Watermark=On (RCB style), 备注="印度地区机型特供，在与 RCB 合作期间有效"
- **Sports**: ROW region, Watermark=Off, 备注="ROW 地区机型支持"

When updating one, **always update the other** with the same core parameters (Focal Length, Exposure, Tuning, Filter, HDR, Quality, Ratio, etc.). Only Watermark and 备注 differ.

## Device-Specific Focal Length Convention

Format: `{project_code}-{focal} | {project_code}-{focal}`

Example:
```
25111-160mm | 25131-28mm
```

When a single focal applies to all devices, just write the value (e.g., `50mm`).

## Source of Truth

**在线多维表格是唯一权威数据源。** 本地快照 `v1.json` 仅作为变更对比的基线。每次操作从在线拉取最新数据开始，绝不允许手动修改本地文件后 push 到在线。

## Workflow: 在线数据变更同步（核心流程）

当用户说"刷新了在线数据"、手动修改了 Bitable、或需要检查变更时执行：

### Step 1: 拉取在线数据

同时拉取 presets 表 `tblGPOTtAH66KGXN` 和修改记录表 `tblrxQxcMJ4PN5og` 的所有 records。

### Step 2: 对比本地基线

加载本地 `references/default-preset-bitable-v1.json`，逐个 preset 按 Preset Name 匹配，逐字段比较。排除 Cover attachment 列表和 `_cover_*` 内部标记字段。

### Step 3: 自动写入修改记录

对每一项变更，自动向在线 `tblrxQxcMJ4PN5og` 追加一条记录：

| 字段 | 值 |
|------|-----|
| 日期 | 当天日期 |
| 变更项 | `{Preset Name}.{Field}` 或 `新增: {Name}` |
| 变更前 | 旧值（截断至 80 字符） |
| 变更后 | 新值（截断至 80 字符） |
| 操作人 | `Sync Bot` |

### Step 4: 更新本地基线

将最新在线数据覆盖保存到 `references/default-preset-bitable-v1.json`。

### Step 5: 报告变更

向用户列出变更摘要：🆕 新增、✏️ 更新、❌ 删除。

## Reference Files

- `references/default-preset-bitable-v1.json` — Full Bitable dump
- `references/default-preset-bitable-v1.md` — Readable markdown table
- `../../knowledge/reference/presets/` — Local preset data + images + changelog

## Quick Lookup

- "拉取 preset 表" / "刷新了在线数据" → Pull from Lark → diff with v1 → auto-add changelog → save snapshot → report
- "更新 xxx preset" → PUT to Lark, update changelog
- "新增 preset" → POST to Lark, update changelog
- "Cricket/Sports 改了什么" → Update both together (same core params, only Watermark/备注 differ)
- "sync preset" → Bi-directional sync Lark ↔ git
