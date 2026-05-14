---
name: camera-prd-writer
description: Use when the user asks to draft, review, or publish a Camera feature PRD/规划文档 in Chinese. Handles full drafting, gap collection, refinement, and dev/test review. For event tracking (埋点) design, delegate to camera-tracking-manage.
---

# Camera PRD Writer

## Overview

Unified entry point for writing Camera PRDs. Workflow: classify → check inputs → braindump → draft → review → publish.

For event tracking (埋点), delegate to `camera-tracking-manage`.

## Interaction Style

Match the response to how much context the user provides:

| 输入状态 | 策略 |
|---------|------|
| 需求清晰 | 直接出活，标注假设 |
| 部分上下文 | 先出骨架草稿，再定向追问缺失项 |
| 探索性/模糊 | 引导模式，一次一个问题，逐步收窄 |

## Workflow

1. **Classify** the request mode
2. **Braindump first** — 不让用户对空白模板。先问："关于这个功能，你目前想到的、确定的、不确定的、纠结的，全部倒出来。" 混乱的原始想法先被外化，再结构化。
3. **Check completeness** — 对照 critical dependencies 检查
4. **Draft** — 用模板，所有未确认值就地写 `[TBD — 需XXX确认]`
5. **Review** — 开发 + 测试 + solution smuggling 检查 + 全文打分
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
| Review only | "评审", "review" | Dev + test + smuggling 检查 + 打分 |
| Gap collection | Scattered notes | 识别缺失 → 分组追问 |
| Coaching | "挑刺", "coach me" | 切换为严厉 PM 同行语气，质疑每一个假设 |

## Input Completeness Check

Before drafting, load [references/required-info-checklist.md](references/required-info-checklist.md).

### Critical Dependencies — Do Not Invent

- **产品背景**: product line, target market, release window, project stage
- **用户价值**: target users, scenario, pain point, expected improvement
- **功能范围**: feature boundaries, in-scope, out-of-scope, entry path
- **技术依赖**: algorithm, hardware/sensor, ISP/SoC, platform version, cross-team
- **质量目标**: IQ target, performance, power/thermal, compatibility
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

Use [assets/camera-prd-template.md](assets/camera-prd-template.md). 12 sections:

1. 背景与目标（问题陈述 + 证据 + 合规）
2. 假设（强制格式：置信度 + 证伪条件）
3. 功能定义（In/Out Scope 表格）
4. 需求（User Story + Gherkin + MoSCoW）
5. 方案说明（含"考虑过但放弃的方案"）
6. 关键依赖
7. 指标与验收（基线 + 目标 + Owner + 护栏指标）
8. 埋点设计 → delegate to `camera-tracking-manage`
9. 项目计划
10. 干系人（RACI 矩阵）
11. 待确认/待补充（汇总所有 [TBD]）
12. 初步评审 + 全文打分

### User Story + Gherkin Enforcement

§4 需求章节强制规则：

1. **每条功能需求 = user story 格式** — `As a [具体角色], I want to [动作], so that [价值]`
2. **≥2 条 Gherkin scenario** — 正常路径 + 异常/边界，用 `GIVEN / WHEN / THEN`
3. **MoSCoW 优先级** — Must-have / Should-have / Could-have / Won't-have
4. 非功能需求用 NFR 表格，单独列出

### Writing Standards

- 用简洁中文，少用填充词
- 声明式语句，不用营销语言
- 术语全文档一致
- 已确认 vs 待确认 明确区分
- 存在权衡时直接陈述
- 不重复相同观点

## Review Pass

### Development Review
Check: 方案可行性、scope 边界、依赖就绪度、接口影响、资源成本、进度风险、回退策略、可观测性。

### Test Review
Check: 验收可测试性、场景/设备覆盖、环境依赖、兼容性矩阵、异常路径、回归范围、客观 pass/fail 信号。

### Solution Smuggling 检查
- 问题陈述是否预设了特定方案？是 → 重新表述问题
- Scope 中有无"MVP 不应包含"但仍在 In Scope 的内容？有 → 标出

### Scoring（满分 100）

| 维度 | 满分 |
|------|------|
| 问题定义清晰 | 15 |
| 假设明确可验证 | 10 |
| 范围边界明确 | 15 |
| 需求可测试（User Story + Gherkin） | 20 |
| 依赖完整 | 10 |
| 指标有基线+目标 | 15 |
| 风险有兜底 | 10 |
| 埋点覆盖 | 5 |

### Completion Status

每次输出结尾标注：

- `DONE` — 所有章节完整，无阻塞性 [TBD]
- `DONE_WITH_CONCERNS` — 内容完整，但有假设待验证或中等风险项
- `BLOCKED` — 关键信息缺失，无法继续
- `NEEDS_CONTEXT` — 需要用户补充信息后再继续

### Recommend Thinner First Slice
如果 Scope 过大，主动建议最小可行版本：去掉哪些可以后续做，保留哪些必须在第一版。

## Feishu Docx Writing

### CRITICAL: Confirm Before Refresh

**每次重新刷飞书文档内容前，必须让用户确认。** 写入会清除并重建整个文档，用户可能已手动编辑（删章节、插图等）。刷新前必须告知：
```
⚠️ 重新写入会清除飞书文档当前内容并重建。确认刷新？
```

### Known API Limitations

1. **`descendant` endpoint rejects table blocks (HTTP 400)**
2. **表格创建 9 行上限** — `row_size` > 9 → 超限拆子表，各自重复表头
3. **单元格 DELETE 不生效** — 用 `PATCH update_text_elements` 直接更新已有文本块

详见 [gallery-feature-doc SKILL.md](../gallery-feature-doc/SKILL.md) Feishu Docx Writing 章节。

## Jira 关联

PRD 撰写完成后创建 Jira Story 关联父 Epic：

| 字段 | ID/格式 | 示例值 |
|------|---------|-------|
| Epic Link | `customfield_10014`（不是 `parent`） | `"NOS-10644"` |
| Device | `customfield_10101` 多选数组 | `[{"value": "all_phones"}]` |
| Components | 对象数组 | `[{"name": "NTGallery"}` 或对应 Camera 组件] |
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
| 2 | 表格 >9 行 | HTTP 400 | 拆为多个 ≤9 行子表 |
| 3 | 单元格 DELETE 不生效 | 每格多空行 | PATCH 更新已有文本块 |
| 4 | 全量刷新覆盖手动编辑 | 用户修改丢失 | **刷新前必须用户确认** |
| 5 | Epic Link 用 `parent` | 静默失败 | 用 `customfield_10014` |
| 6 | Device 单选格式 | API 拒绝 | 多选框需数组 `[{...}]` |
| 7 | Task 类型缺 Severity | 创建失败 | 统一用 Story |
| 8 | CLI update 返回 `{}` | 无法区分成败 | 关键字段用 REST API PUT |
| 9 | 埋点章缺代码示例 | 开发不知道格式 | 必附 ```json 代码块 |

## Reference Files

- [assets/camera-prd-template.md](assets/camera-prd-template.md) — 12-section PRD template
- [references/required-info-checklist.md](references/required-info-checklist.md) — completeness checklist
- [references/review-rubric.md](references/review-rubric.md) — dev/test review rubric

## Quick Lookup

- "写 PRD" → full drafting
- "整理成 PRD" → refinement
- "review 一下" → review only + scoring
- "还缺什么" → gap collection
- "挑刺" / "coach me" → coaching mode
- "发布到飞书" → publish
- "埋点怎么写" → delegate to `camera-tracking-manage`
