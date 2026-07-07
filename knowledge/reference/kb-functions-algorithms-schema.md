# KB Functions Algorithms Schema

> Purpose: define the canonical KB table used before generating 26111/26121 Feature Lists.

## Table Meaning

`kb-functions-algorithms` is a **canonical function / algorithm manual**, not a project Feature List.

In this repository, `KB` means **Knowledge Base**. This table explains what each function/algorithm means, which mode scope it belongs to, how to judge support, what it depends on, and how to verify it.

Rules:

- One row = one unique user-facing function or one unique algorithm capability.
- Do not repeat the same function once per mode.
- The `模式` field is a mode scope, such as `照片 / 人像 / 视频`, `照片`, or `全部拍摄模式`.
- Do not use `通用` as a mode in this KB. Universal features should use `全部拍摄模式` or a concrete mode list.
- Unsupported states are not represented in the KB. Support / unsupported differences belong to the final project FL.
- Source projects for this KB are baseline references only: `25111 / 25131`.
- Do not write future target projects such as `26111 / 26121` as source projects.
- `验证方法` must be an actual verification method, not `✓`, `✗`, a PRD title, or an ownership note.
- If an item is uncertain, put it in `备注` as `待确认`, with the exact question.

## Fields

| Field | Meaning |
|---|---|
| 模式 | Supported mode scope, not one expanded row per mode |
| 一级分类 | `功能` or `基础算法` |
| 二级分类 | Interaction/module area, such as `预览框`, `AE/AF`, `Zoom`, `Top Toolbar`, `Settings`, `右侧暂态开关` |
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

## Generation Flow

1. Maintain canonical KB rows with the schema above.
2. Run the KB builder script to generate `knowledge/_output/kb-functions-algorithms.v6.json`.
3. Audit the generated KB for duplicates, bad source projects, invalid verification methods, and unsupported mode values.
4. Generate project Feature Lists from the canonical KB by expanding mode scopes into real mode rows and applying hardware/config judgement.
5. Use AI review only for the audit and ambiguous support judgement, not for free-form row generation.
