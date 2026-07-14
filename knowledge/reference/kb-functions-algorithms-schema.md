# KB Functions Algorithms Schema

> Purpose: define the canonical KB table used before generating 26111/26121 Feature Lists.

## Table Meaning

`kb-functions-algorithms` is a **canonical function / algorithm manual**, not a project Feature List.

Feature Tree is part of this KB model. It is a generated hierarchical projection of KB nodes, not a separately maintained source. The KB owns both taxonomy and node meaning; `feature-tree.md` may remain as a navigation or audit artifact generated from the same nodes.

Project FL is a downstream acceptance checklist: it defines which Camera functions a project finally supports and is mainly read by Product, SQA, and IQA for development completion and acceptance. Therefore repeated rows in FL are useful output, but they should not become manually maintained knowledge.

In this repository, `KB` means **Knowledge Base**. This table explains what each function/algorithm means, which mode scope it belongs to, how to judge support, what it depends on, and how to verify it.

Rules:

- One row = one unique user-facing function or one unique algorithm capability.
- Do not repeat the same function once per mode.
- Do not create a new KB row just because a PRD updates an existing capability. If the requirement changes copy, interaction detail, judgement basis, dependency, or verification method of an existing feature, update that existing row.
- The `模式` field is a mode scope, such as `通用` (all modes / maximum compatibility), `照片 / 人像 / 视频`, `照片`, or `全部拍摄模式`.
- Use `通用` only when the function applies to all modes. Mode-specific features should use a concrete mode list.
- `Settings`, `Preset`, and `Widget` are common features: use `模式=通用`, with `一级分类=Settings`, `Preset`, or `Widget`; do not expand Settings into specific capture modes in final FL.
- Final FL display values for `模式`, `一级分类`, and `二级分类` should be bilingual in one field, for example `照片 / Photo`, `设置 / Settings`, and `预览框 / Preview`.
- Unsupported states are not represented in the KB. Support / unsupported differences belong to the final project FL.
- Source projects for this KB are baseline references only: `25111 / 25131`.
- Do not write future target projects such as `26111 / 26121` as source projects.
- `验证方法` must be an actual verification method, not `✓`, `✗`, a PRD title, or an ownership note.
- If an item is uncertain, put it in `备注` as `待确认`, with the exact question.

## Fields

| Field | Meaning |
|---|---|
| 模式 | Supported mode scope, not one expanded row per mode |
| 节点 ID | Stable unique identifier for requirements, relations, and FL provenance |
| 父节点 ID | Optional parent node for hierarchy; category-only parents may also be generated from classification fields |
| 一级分类 | `功能`, `算法`, `Preset`, `Settings`, or `Widget` |
| 二级分类 | Interaction/module area, such as `预览框`, `AE/AF`, `Zoom`, `Toolbar`, `Preset`, `General settings`, `Photo settings`, `Video settings`, `Help & Support`, `Widget`, `右侧暂态开关` |
| 名称 | Canonical function/algorithm name |
| 说明 | What the item means in product terms |
| 判断依据 | How to decide support when generating project FL |
| 依赖 | Hardware, algorithm, UI, project policy, or mode dependency |
| 验证方法 | Concrete validation method |
| 来源项目 | Baseline source, usually `25111 / 25131` |
| 备注 | Useful caveats only; do not write meaningless terminology-change notes |

## KB Versus Final FL

| Table | Purpose | Mode handling | Support handling |
|---|---|---|---|
| KB functions algorithms | Function/algorithm manual | One row with a mode scope, such as `照片 / 人像 / 视频` | No `✓` / `✗`; write judgement rules |
| Project Feature List | Project capability matrix | Expand KB mode scope into one row per real mode | Keep rows even when unsupported; write `✗` in camera/project support columns |

Final FL rows are intentionally more repetitive than KB rows because they need to show differences by project, mode, and camera. For example, KB should have one `自动对焦-自动曝光` row with a mode scope; final FL can expand it into rows for Photo, Portrait, Video, Night, etc., with `✓` or `✗` per camera/project.

Do not back-propagate FL duplication into the KB. Use FL as evidence and audit material. Maintain taxonomy and function meaning once in canonical KB nodes, then generate the Feature Tree view from those nodes.

## Generation Flow

1. Maintain canonical KB rows with the schema above.
2. Run the KB builder script to generate `knowledge/_output/kb-functions-algorithms.v6.json`.
3. Audit the generated KB for duplicates, bad source projects, invalid verification methods, and unsupported mode values.
4. Generate project Feature Lists from the canonical KB by expanding mode scopes into real mode rows and applying hardware/config judgement.
5. Use AI review only for the audit and ambiguous support judgement, not for free-form row generation.
