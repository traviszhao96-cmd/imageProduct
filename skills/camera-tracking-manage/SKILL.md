---
name: camera-tracking-manage
description: Use when the user asks to read, sync, or manage Camera event tracking (埋点) Bitable, design new tracking specs, annotate historical errors, or output standard 9-column tracking tables. For Athena SQL queries, use nothing-camera-athena instead.
---

# Camera Event Tracking Manager

## Overview

This skill is the single source of truth for Camera App SW 埋点 (event tracking) document management. It covers reading/saving Lark documents, maintaining the Bitable with historical error annotations, designing new event tracking specs, and writing tracking sections into PRDs.

## Core Capabilities

### 1. 读飞书文档 — 自动本地保存

每次通过 API 读取飞书文档（Bitable、Wiki、Docx）时，**必须同时保存到本地**：

- Bitable 数据 → `references/camera-event-tracking-bitable-v5.json` (JSON) + `.md` (表格)
- Wiki/PRD/飞书文档 → `references/lark-docs/<文档标题>.md`
- 保存时注明 **source URL** 和 **拉取日期**

### 2. Bitable 同步与维护

当用户要求同步、更新或加备注到 Bitable 时，按以下 6 步流程：

1. **拉取最新数据** — 从主表 `tbl3eedJjHPyCEf3` 全量拉取所有 records
2. **标注历史错误** — 检查 4 类历史拼写问题，在 `备注` 列添加说明，**绝不修正原值**
3. **更新本地 JSON** — 写入备注后保存 `camera-event-tracking-bitable-v5.json`
4. **创建含备注表** — 通过 API 创建新表（字段结构从 `tbl3eedJjHPyCEf3` 复制），批量上传含备注 records，`event_name` 作为首列/主列
5. **复制视图** — 从原表拉取视图配置（筛选条件基于 `key` 字段），用 PATCH API 写入新表
6. **更新 SKILL.md** 中的含备注表 ID

### 3. 埋点设计输出

当用户需要为新功能设计埋点时，按以下规范输出。

#### 标准 9 列格式

所有 Camera 埋点输出统一使用：

```
| event_name | key | key_note | label | Label_note | string_value | value_note | 默认值 | 上报方式 |
```

#### 开关类功能

开关类功能（如 `shutter_sound`、`lock_lens`、`auto_fps`）使用**独立 key**，不挂在 `video_info`/`photo_info` 下：

- `key_note` 格式: `"功能名——功能开关"`
- `label` 和 `Label_note` 留空
- `event_name` 固定为 `NTCamera`
- `value_note` 描述值的含义
- `上报方式` 描述触发时机（如"点击开关时记录"、"选择选项时记录"）

#### 参考已有埋点

设计新埋点前，先查 `references/camera-event-tracking-bitable-v5.json` 中相似功能的 key 和 pattern，保持一致性。

### 4. PRD 埋点写入

PRD 中使用简化的 5 列格式（与 Bitable 列名映射见下），一行一个 parameter：

| event_name | parameter | parameter_description | parameter_value | 说明 |
|------------|-----------|----------------------|-----------------|------|

Bitable → PRD 映射：`event_name` → `event_name`，`key` → `parameter`，`key_note` → `parameter_description`，`string_value` → `parameter_value`。

飞书 Docx API 对嵌套表格 block 的 `descendant` 插入有限制。

- **优先** — 提供可复制粘贴的 9 列表格给用户，让用户手动粘贴到 PRD 对应位置
- **API 写入** — 仅当用户明确要求时尝试；先用 `insert_text_md` 写标题和描述文字，再用 `create_table` + 逐 cell 填充

## 历史埋点拼写兼容

以下为历史遗留拼写问题，查询和写入时需兼容，**不可修正原值**，详见各记录的 `备注` 字段：

| 原值 | 正确拼写 | 影响范围 | 备注 |
| --- | --- | --- | --- |
| `protrait` | `portrait` | label=photoMode, string_value | 1 条记录 |
| `tuning_shapen` | `tuning_sharpen` | label 字段名 | 1 条记录 |
| `glyph_mirro` | `glyph_mirror` | label_note 中描述 | 2 条记录 |
| `pef_info` | `perf_info` | key 字段名 | 9 条记录 |
| `Rec_light` | — | label（大写R） | 按原表保留 |
| `if_HLG` | — | label（大写HLG） | 按原表保留 |

## Bitable 表

| 表 | ID | 说明 |
| --- | --- | --- |
| 主表 | `tbl3eedJjHPyCEf3` | 原始数据表，不可改 |
| 含备注表 | `tblh05JLoheZIXfr` | Camera埋点v5.0(含备注)，204 条记录，13 条含历史备注 |

Base token: `N2azb9muvaqqmwsIB7IlPmFGgpg`

### 视图配置

两个表均维护 5 个视图，通过 `key` 字段（SingleSelect）筛选：

| 视图 | 筛选条件 |
|------|---------|
| ALL | 无筛选 |
| photo | `key` IS `photo_info` |
| video | `key` IS `video_info` |
| general | `key` NOT IN (`photo_info`, `video_info`, `pef_info`) |
| performance | `key` IS `pef_info` |

## API Reference

### 认证

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

### 常用端点

| 操作 | Method | Path |
|------|--------|------|
| 获取 records | GET | `/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/records?page_size=500` |
| 批量创建 records | POST | `/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/records/batch_create` |
| 获取 fields | GET | `/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/fields` |
| 创建表 | POST | `/open-apis/bitable/v1/apps/{base_token}/tables` |
| 获取视图 | GET | `/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/views` |
| 创建视图 | POST | `/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/views` |
| 更新视图 | PATCH | `/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/views/{view_id}` |
| 删除视图 | DELETE | `/open-apis/bitable/v1/apps/{base_token}/tables/{table_id}/views/{view_id}` |
| 读取 Docx | GET | `/open-apis/docx/v1/documents/{doc_id}/raw_content` |
| 获取 Wiki 节点 | GET | `/open-apis/wiki/v2/spaces/get_node?token={wiki_token}` |

### 字段类型

- `1` = Text（多行文本）
- `3` = SingleSelect（单选）

### Block 类型

- `3` = heading1, `4` = heading2, `5` = heading3, `9` = heading4
- `31` = table

### 注意事项

- Python 环境只有标准库，使用 `urllib.request`（不要用 `requests`）
- API 限频：batch_create 后 `time.sleep(0.3)`，创建 fields 后 `time.sleep(0.15)`
- 创建表时必须在 payload 中指定 `event_name` 为首个字段，否则会自动生成空的"多行文本"主列

## Reference Files

- `camera-event-tracking-bitable-v5.json` — 完整 204 条埋点记录（JSON）
- `camera-event-tracking-bitable-v5.md` — 完整埋点参考表格（含备注列）
- `lark-docs/` — 已保存的飞书文档本地副本

## Quick Lookup

- "帮我读一下埋点表" → 拉取 Bitable → 保存本地
- "这个功能的埋点怎么设计" → 查已有 pattern → 输出 9 列表格
- "更新埋点表，加备注" → 6 步同步流程
- "把这个埋点写入 PRD" → 输出复制粘贴版本
- "新建含备注表" → 从主表拉取 + 标注 + 创建 + 复制视图
