---
name: gallery-feature-doc
description: Use when the user asks to draft, review, or refine a Gallery feature PRD in Chinese. Handles full drafting, gap collection, refinement, and dev/test review. For event tracking (埋点) design, delegate to gallery-event-tracking.
---

# Gallery Feature Doc

## Overview

Unified entry point for writing Gallery software feature PRDs. Workflow: classify → braindump → check inputs → draft → review.

For event tracking (埋点), delegate to `gallery-event-tracking`.

## Interaction Style

Match the response to how much context the user provides:

| 输入状态 | 策略 |
|---------|------|
| 需求清晰 | 直接出活，标注假设 |
| 部分上下文 | 先出骨架草稿，再定向追问缺失项 |
| 探索性/模糊 | 引导模式，一次一个问题，逐步收窄 |

## Workflow

1. **Classify** the request mode
2. **Braindump first** — 不让用户对空白模板。先问："关于这个功能，你目前想到的、确定的、不确定的、纠结的，全部倒出来。"
3. **Check completeness** — 对照 critical dependencies
4. **Draft** — 用模板，所有未确认值就地写 `[TBD — 需XXX确认]`
5. **Review** — 开发 + 测试 + solution smuggling 检查 + 全文打分

## Anti-Hallucination: [TBD] Rule

**绝对不编造。** 任何用户没说清楚的值，就地标记 `[TBD]`。

```
# 正确
性能目标：[TBD — 需工程侧给出大图场景延迟基线]
支持的最大对象数：[TBD — 需产品确认]

# 错误 — 绝对不要
性能目标：渲染延迟 < 100ms
```

全文中所有 [TBD] 汇总到"待确认/待补充"章节。

## Request Modes

| Mode | Trigger | Action |
|------|---------|--------|
| Full drafting | "写 Gallery PRD" | Braindump → 逐节撰写 |
| Refinement | User provides existing draft | 保留事实 → 重整结构 → 标记缺口 |
| Review only | "评审", "review" | Dev + test + smuggling 检查 + 打分 |
| Gap collection | Scattered notes | 识别缺失 → 分组追问 |
| Coaching | "挑刺", "coach me" | 切换为严厉同行语气，质疑每个交互决策 |

## Input Completeness Check

Before drafting, load [references/required-info-checklist.md](references/required-info-checklist.md).

### Critical Dependencies — Do Not Invent

- **功能定义**: feature name, type, new/enhancement/redesign, applicable module
- **用户价值**: user problem, scenario, expected benefit, benchmark
- **入口与主流程**: entry point, first visible state, toolbar, step-by-step flow, top-level actions (Cancel/Undo/Redo/Save)
- **编辑对象与属性**: what is being edited, which properties, global vs object-level, re-entry behavior
- **状态与持久化**: save/cancel/undo/redo behavior, overwrite vs new image, restoration
- **范围边界**: in/out scope, unsupported types/paths/states, known limits
- **兼容性**: ratios, orientations, dark/light mode, foldable/tablet, performance

### When Critical Info Is Missing

Grouped追问:
- `请补充入口路径、主流程和顶部操作，否则交互链路无法写清楚。`
- `请补充功能支持哪些属性调整，否则功能范围和测试点会过于模糊。`
- `请补充保存策略和撤销恢复规则，否则开发和测试无法确认最终行为。`

## Output Format

Use [assets/gallery-feature-template.md](assets/gallery-feature-template.md). 15 sections:

1. 变更日志
2. 需求背景（问题陈述 + 竞品）
3. 假设（置信度 + 证伪条件）
4. 需求目标
5. 需求范围（In/Out Scope 表格）
6. 需求 — User Story + Gherkin + MoSCoW
7. 产品流程
8. 需求词条（必须含「类型」列，如 菜单项/提示文案/区域标题/按钮）
9. 关键依赖
10. 指标与验收（基线 + 目标 + Owner）
11. 埋点设计 → delegate to `gallery-event-tracking`
12. 干系人（RACI）
13. 待确认/待补充（汇总所有 [TBD]）
14. 初步评审 + 全文打分
15. 附录

### User Story + Gherkin Enforcement

§6 需求章节强制规则：

1. **每条功能需求 = user story** — `As a [具体角色], I want to [动作], so that [价值]`
2. **≥2 条 Gherkin scenario** — 正常路径 + 异常/边界
3. **MoSCoW 优先级** — Must-have / Should-have / Could-have / Won't-have
4. 非功能需求用 NFR 表格

### Writing Standards

- 简洁中文，少填充词
- 声明式语句，非营销语言
- 术语一致
- 已确认 vs 待确认明确区分
- 存在权衡直接陈述

## Review Pass

### Development Review
Check: 入口和状态转换、编辑模型完整性、保存/恢复行为、不支持的场景和限制、埋点需求。

Typical findings:
- `需明确 Text 输入完成后的默认选中态，否则编辑态切换容易产生实现分歧。`
- `需明确保存后是否覆盖原图，否则存储链路和恢复策略无法收敛。`

### Test Review
Check: 验收可测试性、正常+异常路径、重复进入/编辑、多比例/横竖屏、Undo/Redo/Cancel/Save 路径、边界（空输入、最大数量、超出画布）。

### Solution Smuggling 检查
- 问题陈述是否预设了特定方案？
- Scope 中有无"MVP 不应包含"但仍在 In Scope 的内容？

### Scoring（满分 100）

| 维度 | 满分 |
|------|------|
| 问题定义 | 15 |
| 假设明确 | 10 |
| 范围边界 | 15 |
| 需求可测试（User Story + Gherkin） | 20 |
| 交互流程完整 | 15 |
| 指标有基线+目标 | 10 |
| 风险有兜底 | 10 |
| 埋点覆盖 | 5 |

### Completion Status

每次输出结尾标注：

- `DONE` — 所有章节完整，无阻塞性 [TBD]
- `DONE_WITH_CONCERNS` — 内容完整，但有假设待验证或中等风险
- `BLOCKED` — 关键信息缺失，无法继续
- `NEEDS_CONTEXT` — 需要用户补充信息

### Recommend Thinner First Slice
如果 Scope 过大，主动建议最小可行版本。

## Handling Existing Drafts

1. Preserve confirmed facts
2. Normalize structure to template
3. Mark contradictions with `待确认`
4. Add [TBD] for missing values
5. Append review without rewriting confirmed facts

## Feishu Docx Writing

### CRITICAL: Confirm Before Refresh

**每次重新刷飞书文档内容前，必须让用户确认。** `descendant` 写入会全量清除并重建文档，用户可能已经在飞书上做了手动编辑（如删减章节、插入设计稿图片），直接刷新会覆盖这些修改。

刷新前必须告知用户：
```
⚠️ 重新写入会清除飞书文档当前内容并重建。如果你已经手动编辑过飞书文档（删章节、插图等），这些修改会丢失。确认刷新？
```

### Known API Limitations

1. **`descendant` endpoint rejects table blocks (HTTP 400)**
   - 不能通过 `blocks/convert` 把含表格的 markdown 整体转块后用 `descendant` 一次性插入
   - 解决方案：文本段落用 `insert_text_md`，表格用 `children` endpoint 单独创建

2. **表格创建 9 行上限**
   - `POST .../children` 创建 table (block_type=31) 时，`row_size` > 9 返回 HTTP 400 `invalid param`
   - `PATCH` 修改 `row_size` property 虽然返回 code=0，但实际不生效
   - 不能通过 `children` 追加新单元格行
   - 解决方案：超过 9 行的表格拆为多个子表格，每个子表格重复表头

3. **单元格 DELETE 不生效**
   - 表格创建后每个单元格自带一个空文本段落（content=""）
   - `DELETE /batch_delete` 删除单元格子块返回成功但实际删不掉这个默认段落
   - 追加新内容会导致每格出现「空行 + 内容」
   - 解决方案：用 `PATCH update_text_elements` 直接更新已有文本块的内容，而非删旧加新

### Cell Content Best Practice

```python
# ❌ 错误 — DELETE 删不掉默认空行，导致每格多一个空行
api('DELETE', f'.../cells/{cell_id}/children/batch_delete', ...)
api('POST', f'.../cells/{cell_id}/children', ...)

# ✅ 正确 — PATCH 第一个文本子块，无多余空行，速度快
existing = api('GET', f'.../cells/{cell_id}/children?page_size=50')
first_child_id = existing['data']['items'][0]['block_id']
converted = api('POST', '/blocks/convert', {'content_type': 'markdown', 'content': text})
api('PATCH', f'.../blocks/{first_child_id}',
    {'update_text_elements': {'elements': converted['data']['blocks'][0]['text']['elements']}})
```

### Writing Strategy

1. 清除文档：`GET children` → `DELETE batch_delete`
2. 将 markdown 按表格边界拆分为 text/table 交替的 segments
3. 文本段：`insert_text_md` (convert → descendant)
4. 表格段：`create_table_raw`，≤9 行直接建，>9 行拆分子表
5. 使用显式 index（`get_block_count`），不用 `-1`

## Event Tracking Design Rules

设计 Gallery 埋点时遵循：

1. **只报最终保存，不报中间过程** — 不上报拖拽开始、中间落位、取消等中间态
2. **系统相册报名，用户相册报数** — 系统相册（Camera / Videos / Screenshots / Favourite / Maps / Recent）上报名称，用户自建相册只报 `pinned_user_count` / `unpinned_user_count` 数量以保护隐私
3. **用字符串拼接上报最终状态** — 如 `pinned`: `"camera,videos,screenshots,favourite"`
4. **埋点章节必须附 JSON 代码块示例** — 在埋点表格后放 ` ```json ` 代码块，至少 3 个案例（默认布局/部分调整/极端情况），方便开发直接参考上报格式

## Jira 关联

PRD 撰写完成后，在 NOS 项目下创建关联的 Story：

### 创建要点

- **父单**: NOS-10644（Nothing Gallery 3.0 Epic）
- **Issue Type**: Story（不是 Task，Task 会额外要求 Severity）
- **Epic Link**: `customfield_10014`（不是 `parent`）
- **必需字段**:
  - `customfield_10101` (Device): 多选框，通常 `[{"value": "all_phones"}]`
  - `components`: `[{"name": "NTGallery"}]`
  - `assignee`: 必须显式指定 `accountId`，默认经办人不可用
- **建议**: 用 REST API PUT 一次性设置所有字段，避免 CLI update 覆写

### 模板

```bash
# 创建 Story
python3 jira_cli.py create --project NOS --issue-type Story \
  --summary "Album <功能名>" \
  --description "PRD: <飞书链接>" \
  --fields-json '{"customfield_10101": [{"value": "all_phones"}], "components": [{"name": "NTGallery"}], "assignee": {"accountId": "<Travis ID>"}}'

# 然后用 REST API PUT 关联 Epic（CLI update 不可靠）
# PUT /rest/api/3/issue/{key}
# fields: {"customfield_10014": "NOS-10644"}
```

## Reference Files

- [assets/gallery-feature-template.md](assets/gallery-feature-template.md) — 15-section PRD template
- [references/required-info-checklist.md](references/required-info-checklist.md) — completeness checklist
- [references/review-rubric.md](references/review-rubric.md) — dev/test review rubric

## 已知陷阱速查

| # | 陷阱 | 表现 | 解法 |
|---|------|------|------|
| 1 | `descendant` 写表格 | HTTP 400 | 文本用 descendant，表格用 children 单独建 |
| 2 | 表格创建 >9 行 | HTTP 400 `invalid param` | 拆为多个 ≤9 行的子表，各自重复表头 |
| 3 | 单元格 DELETE 不生效 | 每格多一个空行 | PATCH 更新已有文本块，不删旧加新 |
| 4 | 全量刷新覆盖手动编辑 | 用户飞书修改丢失 | **刷新前必须让用户确认** |
| 5 | Epic Link 用 `parent` | 静默失败，parent=null | 用 `customfield_10014` |
| 6 | Device 单选格式 | API 拒绝 | 多选框，格式 `[{"value": "all_phones"}]` |
| 7 | Task 类型缺 Severity | 创建失败 | Gallery 需求统一用 Story |
| 8 | CLI update 返回 `{}` | 无法区分成功/失败 | 关键字段用 REST API PUT，完后 get 验证 |
| 9 | 埋点报中间过程+自建相册 | 隐私风险+噪音大 | 只报最终保存，系统相册报名/用户相册报数 |
| 10 | 词条表缺类型列 | 开发不知道词条用在哪 | 必含「类型」列（菜单项/提示文案/区域标题/按钮） |
| 11 | 埋点章缺代码示例 | 开发不知道上报格式 | 必附 ```json 代码块，至少 3 个案例 |

## Quick Lookup

- "写 Gallery PRD" → full drafting
- "整理成 PRD" → refinement
- "review 一下" → review + scoring
- "还缺什么" → gap collection
- "挑刺" / "coach me" → coaching mode
- "埋点怎么写" → delegate to `gallery-event-tracking`
