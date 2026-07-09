# 26111 / 26121 Tree + KB Integration Review v1

Source scope:

- Wiki space: Camera PRD (`7623306205619867360`)
- Directory: `Camera 5.1-26111` (`EIipweDIeiQ0hYkHkCRlrXpvg1d`)
- Local cache: `knowledge/_output/lark_26111_requirements/`
- Docx fetched with Travis user identity: 32 / 32
- Embedded Base resources read: 4 / 4
- Embedded Sheet workbooks read: 3 workbooks, 17 sub-sheets

This file is an integration candidate review, not a canonical merge. It should be reviewed before updating `knowledge/feature-tree.md` or the canonical KB builder.

## Pipeline Decision

Use these layers:

1. Project requirement sources: Lark PRDs, embedded Base/Sheet, product planning slides if needed later.
2. Requirement business tree: why this requirement exists and which business goal it serves.
3. Feature tree: unique owner of product/function taxonomy.
4. Function KB: explains functions and algorithms, referencing tree nodes instead of inventing categories.
5. Project FL: expands KB mode scopes with project hardware/config and fills `✓` / `✗`.

## Access Result

Accessible with `--as user` as Travis Zhao:

- Camera PRD root and `Camera 5.1-26111`.
- Current Feature List Base node: `26111 & 26121 Camera Feature List`.
- Embedded PRD Base and Sheet resources inside fetched docs.

Not fully consumed yet:

- Slides: `26111 Camera 产品规划(WIP)`, `camera-selection-strategy-english`.
- Sheet: `26111 Camera Feature List_v1.0`.
- Supplier PDF under `供应商能力汇总`.

These should be treated as secondary sources after the docx PRD integration pass.

## Candidate Counts

- Total candidates: 25
- Low dispute: 8
- Medium dispute: 14
- High dispute: 3

Pending / not advancing per PM correction on 2026-07-07:

- `25MP 超清模式`
- `200MP 自动裁切`
- `构图助手`
- `宠物识别框`

Classification rule added on 2026-07-07: if a requirement is not a fully new function, do not create a new tree/KB row. Update the existing function description, judgement basis, dependency, or verification method instead.

Recommended merge order:

1. Low-dispute KB/tree updates.
2. Medium-dispute items after PM/algorithm wording check.
3. High-dispute items only after manual decision.

## Low-Dispute Candidates

These are structurally clear and can likely be merged after a quick human skim:

| ID | Requirement | Tree Action | KB Action | Notes |
|---|---|---|---|---|
| REQ26111-KB-006 | 前置自动小广角 | Add Zoom / 前置自动小广角 | Add front auto-wide | PRD found; depends on gyroscope/orientation and front 0.8x/1x support. |
| REQ26111-KB-010 | 照片专业模式 2.0 | Update Mode Switch / 专业模式 | Update multiple Pro rows | 5.1 scope confirmed; includes metering, interval shooting, focus peaking, Preset extension. |
| REQ26111-KB-012 | Photo Style | Add Top Toolbar / Photo Style | Add Photo Style | Needs Filter/Tuning/Preset stacking order. |
| REQ26111-KB-016 | Video EIS switch | Update Settings / Video | Add Video Stabilization | Confirm slow-motion wording mismatch. |
| REQ26111-KB-018 | Lock White Balance | Add Settings / Video | Add Lock WB | Align priority with manual WB controls. |
| REQ26111-KB-020 | Default H.265 | Update Settings / Video encoding | Update Video encoding | Engineering risks remain, but KB meaning is clear. |
| REQ26111-KB-023 | SAT optimization | Update Zoom / SAT | Update SAT verification | Probably verification-method update, not a new FL row. |
| REQ26111-KB-028 | Tips and feedback | Update Settings / Help & Support | Add Tips and feedback | Clear Settings entry; confirm new Help & Support group. |

## High-Dispute Candidates

These need human decision before canonical merge:

| ID | Requirement | Main Dispute |
|---|---|
| REQ26111-KB-005 | 相机设计改版 | Mostly visual spec; avoid polluting FL with shutter/default UI controls. |
| REQ26111-KB-009 | 200MP 高像素 | Latest v2/revision 36 confirms 26121 does not involve 200MP sensor and exposes major 7635 risk; final 26111 FL decision needed. |
| REQ26111-KB-029 | Video Log | Evaluation doc, not final PRD; 26121-only candidate. |

## PM Corrections Applied

| ID | Requirement | Updated classification |
|---|---|---|
| REQ26111-KB-002 | 识别框视觉动效 | Update existing `预览框 / 识别框视觉动效`; pet box is Pending and no independent row is created. |
| REQ26111-KB-004 | 二维码识别框优化 | Update existing recognition-frame / QR scanner behavior; do not create a new QR function row unless PM adds a new entry. |
| REQ26111-KB-006 | 前置自动小广角 | Add `Zoom / 前置自动小广角`; PRD scope is front Photo, dependency is gyroscope/orientation + front 0.8x/1x. |
| REQ26111-KB-007 | Tuning Palette | Update existing Tuning/Style area. PM says it contains the Style direction that merges Filter + Tuning; cached PRD still says current phase does not merge Filter, so this remains a medium dispute. |
| REQ26111-KB-010 | 照片专业模式 2.0 | 5.1 scope confirmed. Update Pro mode and add/update metering, interval shooting, focus peaking, and Preset professional-parameter save. |
| REQ26111-KB-013 | AI Preset | Move primary tree node from `Preset / AI Preset` to `预览框 / AI Preset 引导入口`; Preset remains the applied result area. |
| REQ26111-KB-026 | 镜头脏污专项 / AI 去油污 | Add new Camera function under `预览框 / 镜头脏污检测与 AI 去油污引导`; support modes are Photo and Portrait. Hardware coating/accessory items stay out of Camera FL. |

## Mode Scope Rule

PM correction on 2026-07-07: `通用` means the function supports all modes. It is a valid simplification and represents maximum compatibility, especially for common Settings/Preset-style capabilities.

Recommended rule before canonical merge:

- KB may use `通用` when the intended meaning is all modes / maximum compatibility.
- Project FL may keep a common row or expand to concrete mode rows depending on the final table design.
- Do not treat `通用` as a category error; audit it only when a function is actually mode-specific.

## Proposed Review Gate

For each candidate, a human reviewer should mark one of:

- `approve_tree_kb`: merge into feature tree and KB.
- `approve_kb_only`: tree already has the node; only update KB.
- `fl_only`: do not update canonical tree/KB; apply only to project FL generation.
- `reference_only`: keep as source material, no canonical merge.
- `blocked`: missing decision or source conflict.

AI audit should then check:

- no duplicate tree nodes;
- KB rows reference existing tree nodes;
- source project is classified as baseline/reference/project requirement correctly;
- `通用` is used only for all-mode/common capabilities, not for mode-specific functions;
- no `✓` / `✗` in KB;
- all high-dispute items have a manual decision before merge.
