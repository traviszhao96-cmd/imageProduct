---
name: gallery-event-tracking
description: Design and review Gallery analytics event tracking for product documents and feature specs. Use when Codex needs to add埋点内容 for Gallery features, align event names and parameter structures with the existing NTGallery event tracking workbook, avoid inventing inconsistent naming, and propose save-time settlement events for edit features such as Text, Draw, Crop, Erase, or other Gallery modules.
---

# Gallery Event Tracking

## Purpose

Use this skill when the user wants埋点内容 for Gallery features.
This skill aligns new tracking proposals with the existing `NTGallery App Event Tracking Spec 2026` workbook rather than inventing a new style from scratch.

## Default Source

Gallery 埋点的权威数据源是飞书多维表格：

| 项目 | 值 |
|------|-----|
| Bitable URL | `https://nothing-tech.sg.larksuite.com/base/WB4QbWtr2ajCGXsZucglh0DAgsh` |
| Base Token | `WB4QbWtr2ajCGXsZucglh0DAgsh` |
| Table | `Gallery` (tbl4YaZDJ2Psv9ok) |
| 记录数 | 73 条（截至 2026-06） |

### Bitable 字段结构

| 字段 | 类型 | 说明 |
|------|------|------|
| `event_name` | 文本 | 事件名（gallery_view / media_manage / edit_action / album_reorder ...） |
| `event_description` | 文本 | 事件描述，说明什么时候上报 |
| `parameter_name` | 多选 | 参数名列表 |
| `parameter_value` | 文本 | 参数值（枚举用换行分隔，自由值写说明） |
| `value_note` | 文本 | 参数值的含义解释 |
| `操作场景说明` | 文本 | 触发时机和场景 |
| `备注` | 文本 | 版本、状态、注意事项 |

## Existing Pattern

Gallery 使用多 `event_name`（`gallery_view`、`media_manage`、`album_manage`、`edit_action` 等），不同于 Camera 的单 `NTCamera`。PRD 中一行一个 parameter，与 Bitable 对齐：

| event_name | key | key_description | parameter_value | 说明 |
|------------|-----|-----------------|-----------------|------|

与埋点总表（Bitable）列名映射：

| 总表列 | PRD 列 | 含义 |
|--------|--------|------|
| `event` | `event_name` | 事件名 |
| `label` | `key` | 参数名 |
| `label_note` | `key_description` | 参数的中文说明 |
| `value` | `parameter_value` | 参数可选值 |
| `value_note` / `操作场景说明` | `说明` | 触发场景/备注 |

同一次上报涉及多个参数时，拆为多行，`event_name` + `说明` 保持一致。

常见 `event_name` 分组：
- `gallery_view` — 浏览/导航行为
- `media_manage` — 媒体管理操作
- `album_reorder` — 相册排序

For Edit features, the pattern is usually:

1. `edit_action`
   For entering the一级模块 or clicking specific sub-tools.
2. `edit_<feature>`
   For save-time settlement of final effective parameters.
3. `UUID`
   For session correlation.

## Workflow

1. Identify the feature and whether it belongs to `Manage`, `Edit`, or `Settings`.
2. Check whether the new feature should reuse an existing event family.
3. For editing features, default to:
   - one `edit_action` row for module entry
   - one `edit_<feature>` event family for save-time settlement
4. Only add process events if the business need is explicit.
5. Output in the workbook-style table format.
6. Mark unsupported or undecided enums as `待确认`.

## Re-edit Detection

编辑可能是全新创作，也可能是在历史图片上二次修改。用 `is_reedit` 区分：

| is_reedit | 含义 | 触发条件 |
|-----------|------|---------|
| 0 | 首次编辑 | 进入编辑模块时画布上没有该类型的已有内容 |
| 1 | 二次编辑 | 画布上已有历史内容（如之前加的 text），本次编辑在此基础上修改 |

**上报方式：** 前端传最终画面全貌（如 `text_details: T1*1, T2*1, T3*1`），`is_reedit` 标记是否为二次修改。数据端通过 `is_reedit=1` 知道 D 是在 C 的基础上改的，不会误判为"一次新增 3 个 text"。

**示例 — 场景 1（叠加）：**
```
B = A + T1 → text_details: T1*1, is_reedit: 0
C = B + T2 → text_details: T1*1, T2*1, is_reedit: 1
D = C + T3 → text_details: T1*1, T2*1, T3*1, is_reedit: 1
```

**示例 — 场景 2（删除）：**
```
B 有 T1 → 用户删除 T1 并保存 → text_details: none, is_reedit: 1
```

## Privacy-First Rule

**只改文字内容、不改任何样式 → 不上报 edit_text。**

理由：
- 文字内容属于用户隐私，不应通过埋点泄露
- 初始字串 = 最终字串 → 判定为无有效样式变更
- 用户"碰过" Text 工具的动作，已由 `edit_action` 记录

这是一个有意识的 tradeoff：PM 无法通过埋点知道"多少人改了文字内容"，但隐私保护优先级更高。如果产品确实需要这个数据，加一个轻量的 `text_edited: 0/1` flag（不报内容、不报样式），不当做 edit_text 上报。

## Rules

- Keep event names short and consistent with the workbook.
- Prefer enum-style parameter values over free text.
- Reuse `UUID` when the feature belongs to an edit session.
- Do not mix entry events and final settlement events into the same semantic bucket.
- Do not create overly granular events for every gesture unless explicitly required.
- If the exact enum set is unknown, keep the event row and mark the values as `待确认`.

## Output Format

### PRD 中使用（给开发看）

| event_name | key | key_description | parameter_value | 说明 |
| --- | --- | --- | --- | --- |

### 写入 Bitable 时（给 AI 或同步用）

对齐 Gallery Bitable 的 7 列：

```
event_name | event_description | parameter_name | parameter_value | value_note | 操作场景说明 | 备注
```

**映射关系：**
- PRD 的 `key` → Bitable 的 `parameter_name`（多选字段）
- PRD 的 `key_description` → Bitable 的 `value_note`
- PRD 的 `说明` → Bitable 的 `操作场景说明`
- Bitable 额外需要 `event_description`（一句话描述什么时候上报）

### 示例

PRD 格式：
```
edit_action | enter_module | 进入的编辑模块 | draw | 进入 Draw 编辑时上报
```

Bitable 格式：
```
edit_action | 进入某个编辑子模块时上报 | enter_module | draw | 进入 Draw 编辑 | 点击编辑入口时
```

## Writing to Bitable

设计新埋点时，先查 Bitable 是否有可复用的 event_name，再决定是追加 parameter 还是新增 event。

1. 查询已有记录 → 确认 event_name 和 parameter 是否可复用
2. 新增记录 → 按 Bitable 7 列格式写入 `tbl4YaZDJ2Psv9ok`
3. 不确定的枚举值 → `value_note` 写「待确认」，`备注` 标注原因
4. PRD 交付 → 用 5 列简化格式给开发，同步用 7 列格式更新 Bitable

## Event Patterns Reference

以下为已确立的 Gallery 埋点命名和结构模式，设计新埋点时必须对齐。

### 常用 event_name 分组

| event_name | 用途 | 示例参数 |
|------------|------|---------|
| `gallery_view` | 浏览/导航行为 | album_type, entry_source, duration, has_location_media |
| `media_manage` | 媒体管理操作 | action (favorite/share/delete/edit/hide), select_count, media_type |
| `album_reorder` | 相册排序保存 | pinned (系统相册名单), pinned_user_count, source (drag/edit) |
| `edit_action` | 编辑模块进入/子工具点击 | enter_module, adjust_click, erase_click, crop_click, UUID |
| `edit_adjust` | 编辑参数保存结算 | 变更的参数名: 最终数值, UUID |
| `edit_crop` | 裁剪保存结算 | ratio, rotate_slider, rotate_90, flip, UUID |

### 编辑类埋点模式

所有编辑功能遵循统一模式：进入事件 + 保存结算事件 + UUID 关联。

```
edit_action (进入模块/点击子工具)
  - enter_module: adjust / crop / erase / filter / watermark / trim / audio / slow_mo
  - <module>_click: 具体子工具名
  - UUID: 会话标识

edit_<feature> (保存时结算最终参数)
  - 只上报最终生效的参数值
  - UUID: 与 edit_action 的 UUID 相同，用于关联
```

**示例 — 新增 Text 功能：**
```
edit_action: enter_module=text, UUID=xxx
edit_text: font=Roboto, size=18, color=#FFFFFF, UUID=xxx
```

## Review Focus

When reviewing埋点内容, check:

- whether names follow existing Gallery conventions
- whether parameters are enum-friendly
- whether save-time and process-time events are separated
- whether there are too many low-value events
- whether key funnel stages are missing

## References

- [references/ntgallery-event-patterns.md](references/ntgallery-event-patterns.md): extracted structure and naming patterns from the existing workbook
