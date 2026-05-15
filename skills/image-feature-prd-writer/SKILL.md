---
name: image-feature-prd-writer
description: Use when the user asks to draft, review, or publish a Camera or Gallery feature PRD/规划文档 in Chinese. Handles full drafting, gap collection, refinement, and dev/test review. For event tracking (埋点) design, delegate to camera-tracking-manage or gallery-event-tracking.
---

# Image Feature PRD Writer

## Overview

Unified entry point for writing Camera and Gallery feature PRDs. Workflow: classify → braindump → check inputs → draft → review → publish.

For event tracking (埋点), delegate to the domain-specific skill:
- Camera features → `camera-tracking-manage`
- Gallery features → `gallery-event-tracking`

## Interaction Style

Match the response to how much context the user provides:

| 输入状态 | 策略 |
|---------|------|
| 需求清晰 | 直接出活，标注假设 |
| 部分上下文 | 先出骨架草稿，再定向追问缺失项 |
| 探索性/模糊 | 引导模式，一次一个问题，逐步收窄 |

## Workflow

1. **Classify** the request mode and domain (Camera / Gallery)
2. **Braindump first** — 不让用户对空白模板。先问："关于这个功能，你目前想到的、确定的、不确定的、纠结的，全部倒出来。" 混乱的原始想法先被外化，再结构化。
3. **Check completeness** — 对照对应领域的 critical dependencies 检查
4. **Draft** — 用对应领域模板，所有未确认值就地写 `[TBD — 需XXX确认]`
5. **Review** — agent 开发 + agent 测试 + agent solution smuggling 检查 + agent 全文打分
6. **Publish** — 如果要求

## Anti-Hallucination: [TBD] Rule

**绝对不编造。** 任何用户没说清楚的值，就地标记 `[TBD]`，不写看起来合理的假数字。

```
# 正确
性能目标：[TBD — 需算法侧给出预览延迟基线]
上市时间：[TBD — 需产品经理确认版本窗口]

# 错误 — 绝对不要
性能目标：预览延迟 < 200ms
```

[TBD] 变体：
- `[TBD — 需XXX确认]` — 等待特定角色输入
- `[TBD — 待数据验证]` — 需要埋点/实验数据
- `[TBD — 待法务确认]` — 合规相关

全文中所有 [TBD] 汇总到"待确认/待补充"章节。

## Request Modes

| Mode | Trigger | Action |
|------|---------|--------|
| Full drafting | "写 PRD", "出规划文档" | Braindump → 逐节访谈式撰写 |
| Refinement | User provides existing draft | 保留事实 → 重整结构 → 标记缺口 |
| Review only | "评审", "review" | agent dev + test + smuggling 检查 + 打分 |
| Gap collection | Scattered notes | 识别缺失 → 分组追问 |
| Coaching | "挑刺", "coach me" | 切换为严厉 PM 同行语气，质疑每一个假设 |

## Input Completeness Check

Before drafting, check domain-specific requirements:

- Camera: [references/camera-required-info-checklist.md](references/camera-required-info-checklist.md)
- Gallery: [references/gallery-required-info-checklist.md](references/gallery-required-info-checklist.md)

### Shared Critical Dependencies — Do Not Invent

- **产品背景**: product line, target market, release window, project stage
- **用户价值**: target users, scenario, pain point, expected improvement
- **功能范围**: feature boundaries, in-scope, out-of-scope, entry path
- **技术依赖**: algorithm, hardware/sensor, ISP/SoC, platform version, cross-team
- **交付依赖**: milestone, owner, external dependency, fallback plan

### When Critical Info Is Missing

```
以下信息缺失，当前无法可靠定稿，请先补充：

1. 产品与版本
- 机型/项目代号：[TBD]
- 上市时间或版本窗口：[TBD]

2. 功能边界
- 明确不做的内容：[TBD]

3. 技术依赖
- 依赖的硬件/算法/平台：[TBD]
- 跨团队依赖：[TBD]

4. 验收与风险
- 成功指标：[TBD]
- 兜底方案：[TBD]
```

## Output Format

Choose template by domain:

- **Camera**: [assets/camera-prd-template.md](assets/camera-prd-template.md) — 12 sections + 附录
- **Gallery**: [assets/gallery-feature-template.md](assets/gallery-feature-template.md) — 13 sections + 附录

Both share the same core structure; domain differences are in domain-specific sections (词条表 for Gallery, 方案说明 for Camera, etc.).

### PRD Writing Standards

- 用简洁中文，少用填充词
- 声明式语句，不用营销语言
- 术语全文档一致
- 已确认 vs 待确认明确区分
- 存在权衡时直接陈述
- 不重复相同观点

### §4 需求章节写作规范

需求描述用 **叙事格式**，不用代码块和僵硬的属性表。每条需求包含：
- 功能名 + 一句话定义
- 优先级
- 行为描述（自然语言）
- 正常路径 + 边界情况（自然语言，不用 Gherkin 代码块）

格式示例：
```
### R1 · 功能名

优先级：Must-have

功能的一句话定义和行为描述。

*正常路径：* ...
*边界：* ...
```

### 埋点设计原则

- **只报最终状态，不报中间过程** — 不上报拖拽中间态、取消等
- **隐私保护** — Gallery: 系统相册报名，用户相册报数不报名
- **精简** — 能用一个事件说清的不用两个，参数从值对即可推断方向的不额外加 direction 参数
- **必须附 JSON 代码块示例** — 方便开发直接参考上报格式

### 护栏指标处理

不放入 PRD。手机厂商出厂质量门控（崩溃率、性能）是 release gate，不是 product metric。如有特殊质量担忧，写在风险与兜底章节。

### 考虑过但放弃的方案

放在附录，不在方案说明章节中展开。

## Review Pass

所有评审子章节统一加 `agent` 前缀，表明为 AI 辅助评审，非人工评审结论。

### agent Development Review
Check: 方案可行性、scope 边界、依赖就绪度、接口影响、进度风险、回退策略。

### agent Test Review
Check: 验收可测试性、场景/设备覆盖、兼容性矩阵、异常路径、回归范围、客观 pass/fail 信号。

### agent Solution Smuggling 检查
- 问题陈述是否预设了特定方案？是 → 重新表述问题
- Scope 中有无"MVP 不应包含"但仍在 In Scope 的内容？有 → 标出

### agent Scoring（满分 100）

| 维度 | 满分 |
|------|------|
| 问题定义清晰 | 15 |
| 假设明确可验证 | 10 |
| 范围边界明确 | 15 |
| 需求可测试 | 20 |
| 依赖完整 | 10 |
| 指标有基线+目标 | 15 |
| 风险有兜底 | 10 |
| 埋点覆盖 | 5 |

### agent Completion Status

每次输出结尾标注：

- `DONE` — 所有章节完整，无阻塞性 [TBD]
- `DONE_WITH_CONCERNS` — 内容完整，但有假设待验证或中等风险项
- `BLOCKED` — 关键信息缺失，无法继续
- `NEEDS_CONTEXT` — 需要用户补充信息后再继续

### agent Recommend Thinner First Slice
如果 Scope 过大，主动建议最小可行版本：去掉哪些可以后续做，保留哪些必须在第一版。

## Feishu Docx Writing

### CRITICAL: Confirm Before Refresh

**每次重新刷飞书文档内容前，必须让用户确认。** 写入会清除并重建整个文档，用户可能已手动编辑（删章节、插图等）。刷新前必须告知：
```
⚠️ 重新写入会清除飞书文档当前内容并重建。确认刷新？
```

### Known API Limitations

1. **`descendant` endpoint rejects table blocks (HTTP 400)**
   - 不能通过 `blocks/convert` 把含表格的 markdown 整体转块后用 `descendant` 一次性插入
   - 解决方案：文本段落用 descendant，表格用 `children` endpoint 单独创建

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

## Jira 关联

PRD 撰写完成后创建 Jira Story 关联父 Epic：

| 字段 | ID/格式 | 示例值 |
|------|---------|-------|
| Epic Link | `customfield_10014`（不是 `parent`） | `"NOS-10644"` |
| Device | `customfield_10101` 多选数组 | `[{"value": "all_phones"}]` |
| Components | 对象数组 | `[{"name": "NTGallery"}` 或对应组件] |
| Assignee | accountId 对象 | `{"accountId": "<Travis ID>"}` |

- Issue Type 统一用 Story（Task 会额外要求 Severity）
- `jira_cli.py update` 返回 `{}` 时无法区分成功/失败，关键字段用 REST API PUT
- 创建后必须 `get` 验证关键字段

## Handling Existing Drafts

1. Preserve confirmed facts
2. Normalize structure to template
3. Mark contradictions with `待确认`
4. Add [TBD] for missing values
5. Append review without rewriting confirmed facts

## 已知陷阱速查

| # | 陷阱 | 表现 | 解法 |
|---|------|------|------|
| 1 | `descendant` 写表格 | HTTP 400 | 文本用 descendant，表格用 children |
| 2 | 表格 >9 行 | HTTP 400 `invalid param` | 拆为多个 ≤9 行子表 |
| 3 | 单元格 DELETE 不生效 | 每格多空行 | PATCH 更新已有文本块 |
| 4 | 全量刷新覆盖手动编辑 | 用户修改丢失 | **刷新前必须用户确认** |
| 5 | Epic Link 用 `parent` | 静默失败 | 用 `customfield_10014` |
| 6 | Device 单选格式 | API 拒绝 | 多选框需数组 `[{...}]` |
| 7 | Task 类型缺 Severity | 创建失败 | 统一用 Story |
| 8 | CLI update 返回 `{}` | 无法区分成败 | 关键字段用 REST API PUT |
| 9 | 埋点章缺代码示例 | 开发不知道格式 | 必附 ```json 代码块 |
| 10 | 埋点设计过于复杂 | 参数过多/事件过多 | 精简为一个事件，参数自解释 |
| 11 | 护栏指标放在 PRD | 手机厂商无意义 | 出厂质量门控不放 PRD 指标 |
| 12 | 代码块降低可读性 | 需求难以扫读 | 叙事格式，正常/边界用自然语言 |

## Reference Files

- [assets/camera-prd-template.md](assets/camera-prd-template.md) — Camera PRD template (11 sections)
- [assets/gallery-feature-template.md](assets/gallery-feature-template.md) — Gallery PRD template (12 sections + 附录)
- [references/camera-required-info-checklist.md](references/camera-required-info-checklist.md) — Camera completeness checklist
- [references/gallery-required-info-checklist.md](references/gallery-required-info-checklist.md) — Gallery completeness checklist
- [references/review-rubric.md](references/review-rubric.md) — Dev/test review rubric

## Quick Lookup

- "写 PRD" / "写 Gallery PRD" → full drafting
- "整理成 PRD" → refinement
- "review 一下" → review + scoring
- "还缺什么" → gap collection
- "挑刺" / "coach me" → coaching mode
- "发布到飞书" → publish
- "埋点怎么写" → delegate to camera-tracking-manage or gallery-event-tracking
