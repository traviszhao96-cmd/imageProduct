# Feature List Layout And Common Feature Rules

> Source: Travis verbal clarification, 2026-07-07.
> Purpose: guide canonical KB maintenance and 26111/26121 Feature List expansion.
> Current partner-review release: `v1.0`. Shared Base title and generated artifact filenames must include `v1.0`.

## Functional Bar Layout

From top to bottom, the Camera functional areas are:

1. Toolbar / toolbar drawer
2. Zoom bar
3. Left and right transient switches
4. Mode bar
5. Shutter area
6. Common area: Preset, Settings, Widget

The shutter area includes:

- Shutter button
- Gallery thumbnail
- Front/rear camera flip button

These shutter-area controls should **not** be expanded into Feature List rows because every camera includes them by default and they are not currently differentiated by project/camera. Only create an FL row for a shutter-area item when a project adds a clearly differentiated behavior.

## KB Versus Final FL

FL is a **project acceptance checklist artifact**, not the source of product taxonomy or function meaning.

Primary ownership and readers:

- Producers: SE and Product.
- Core readers: Product, SQA, and IQA.
- Purpose: define which Camera functions the project finally supports, then support project completion and acceptance checks.

`确认负责人` is logically single-select and uses one of four canonical roles only. If a legacy Base still uses a multi-select field container, each record must still contain exactly one value:

- `Product`: product definition, requirement scope, interaction, and project decisions.
- `SE`: hardware, algorithm, pipeline, integration feasibility, and project support boundaries.
- `SQA`: software functionality, interaction, state, compatibility, and specification acceptance.
- `IQA`: image/video quality and algorithm-effect acceptance.

Do not use `PM`, `QA`, `影像 SE`, or `Tuning` as owner values. Use `Product` instead of PM, split QA into SQA or IQA by acceptance type, and use only `SE` for the SE role.

Owner assignment rules:

- Algorithm requirements (`一级分类=算法 / Algorithm`) are confirmed by `SE` only. Do not add Product merely because the algorithm is user-visible.
- Concrete video, slow-motion, and timelapse support boundaries are confirmed by `SE`; SQA executes specification acceptance.
- Pure function and interaction requirements are confirmed by `Product`; SQA executes software acceptance.
- Image/video effect rows retain one accountable confirmation owner; IQA executes effect acceptance and becomes the owner only when the unresolved decision itself belongs to IQA.
- Product must not appear on rows that only describe an algorithm, pipeline, hardware dependency, or implementation capability.

Because FL is used for acceptance, it is intentionally verbose: support differences by project, mode, camera, and algorithm path must be visible. This verbosity should be generated from maintained sources instead of manually duplicated.

Use these layers:

- KB/manual layer: one row per unique function, with `模式` as a mode scope such as `通用` (all modes / maximum compatibility), `全部拍摄模式`, or `照片 / 人像 / 视频`.
- Final FL layer: keep a common row if the table design supports it, or expand the KB mode scope into one row per real project mode, then fill project/camera support columns with `✓` or `✗`.

Use `通用` only when the function applies to all modes. Do not use it for mode-specific features.

Final FL display values for `模式`, `一级分类`, and `二级分类` should be bilingual in one field, for example `照片 / Photo`, `设置 / Settings`, and `预览框 / Preview`.

Final FL sort order should place concrete capture modes first. Rows with `模式=通用 / Common` should be placed at the very bottom of each project table.

Each project FL table must expose one filtered grid view per Mode and must not create views by first-level category. Use this view order: `照片`, `人像`, `运动`, `视频`, `夜景`, `慢动作`, `延时摄影`, `全景`, `专业`, `前后双录`, `高像素`, `通用`. Keep change history in the Base-level `修改记录` table rather than mixing change-log rows into project mode views.

For distribution drafts, include a `不支持原因` field for every `✗` camera support judgement when it can be inferred from hardware, PRD scope, baseline FL, or project configuration. If every camera column in a row has been judged as `✓` or `✗`, mark the row `已确认`; keep `待确认` when any camera column remains `TBD`.

Portrait camera-scope rule: `UW=✗` for every Portrait-mode FL row. The ultrawide stream may be used internally as a depth auxiliary input, but Portrait mode does not expose UW as a selectable/output camera. Use the canonical unsupported reason: `UW: 人像模式不开放超广角摄像头，因此该功能在 UW 不适用。`

Front camera support rule: `Exposure`, `Grid`, `More settings`, `Ratio`, `Watermark`, `风格-滤镜 / Style-Filter`, `风格-调色 / Style-Tuning`, `风格-调色盘 / Style-Tuning Palette`, and `AE / 自动曝光` support Front in modes that expose the front camera. Expert and High Resolution are mode-level exceptions: every row in `专业 / Expert` and `高像素 / High Resolution` must use `Front=✗`, including these otherwise Front-supported functions.

AI maintenance target:

- Treat Feature Tree, KB, project requirements, and hardware/project config as maintained inputs.
- Treat repeated mode/camera rows, unsupported `✗` rows, and camera-specific support marks as generated checklist output.
- Treat PRDs that modify an existing function as updates to existing Tree/KB nodes, not as new rows, unless they introduce a distinct user-facing function, mode, entry, or algorithm capability.
- AI review should focus on drift, conflicts, missing provenance, and disputed support judgement; humans should mainly review disputed or high-risk items.

## Common Category

`模式=通用 / Common` contains features that should not be repeated under each capture mode:

- `预设 / Preset`
- `设置 / Settings`
- `小组件 / Widget`

Use `模式=通用 / Common` for these rows in final FL. Settings rows must not be expanded into `照片 / Photo`, `视频 / Video`, or other capture modes.

## Preset

Preset is a bottom independent functional area under `模式=通用 / Common`.

KB classification:

| Field | Value |
|---|---|
| 模式 | 通用 |
| 一级分类 | Preset |
| 二级分类 | Preset |

Preset applies across modes. In final FL, keep it in `模式=通用 / Common` unless a specific project requirement adds a mode-specific Preset behavior.

## Settings

Settings are common features and stay under `模式=通用 / Common`.

KB classification:

| Field | Value |
|---|---|
| 模式 | 通用 |
| 一级分类 | Settings |
| 二级分类 | General settings / Photo settings / Video settings / Help & Support |

Do not place Settings rows under capture modes in final FL. If a setting affects only photo or video results, keep it in common settings and describe the affected mode scope in `说明` / `判断依据`.

## Widget

Widget is a common feature.

KB classification:

| Field | Value |
|---|---|
| 模式 | 通用 |
| 一级分类 | Widget |
| 二级分类 | Widget |

Known reference:

- Preset Widget 2.0: `knowledge/reference/preset/preset-widget-2.0.md`

### General Settings

General includes:

| Setting | Meaning |
|---|---|
| Preset | Preset-related setting entry |
| Save location | Storage location setting |
| Shutter sound | Camera shutter sound setting |
| Mirror front camera | Front camera mirror setting |
| Level | Level / horizon guide setting |

### Photo Settings

Photo includes settings that can influence still-photo results, including portrait and other still photo modes.

| Setting | Meaning |
|---|---|
| Watermark | Photo watermark settings |
| Auto Tone | Photo tone processing setting |
| Tap to take a photo | Tap preview to trigger capture |
| QR code scanner | QR code scanner setting |
| Press and hold shutter | Long-press shutter behavior, such as burst or quick video |
| Ultra XDR | Ultra HDR / XDR photo display/output setting |

### Video Settings

Video includes:

| Setting | Meaning |
|---|---|
| Video encoding | User can choose H.264 or H.265 |
| Power saving recording | When enabled, Camera saves power by turning off the preview screen while the device is stationary |
| Auto FPS | User can choose Off, Auto 30 FPS, or Auto 30 & 60 FPS |
| 视频防抖开关 | Settings switch for EIS in supported video recording modes |
| 锁定镜头 | Settings switch that keeps recording on the current physical lens and disables SAT during recording |
| 锁定白平衡 | Settings switch that locks initial white balance after recording starts |

### Help & Support

Help & Support includes:

| Setting | Meaning |
|---|---|
| Tips and feedback | Jump to the system Tips and feedback entry; Camera does not host its own form |

Known PRD references:

- Video H.265: `knowledge/reference/26111-prd-links.md` → `视频H265`
- Power saving recording: PRD exists; link needs to be attached when found
- Auto FPS: PRD exists; link needs to be attached when found

## Video Specs

Video recording specifications should be checklist rows under `模式=视频 / Video`, `一级分类=功能 / Feature`, `二级分类=视频规格 / Video Specs`.

Do not keep broad rows such as `前置 4K 视频` when the FL needs acceptance coverage. Instead split the concrete recording specs, for example:

- `1080P 30FPS`
- `1080P 60FPS`
- `4K 30FPS`
- `4K 60FPS`
- `1080P 30FPS HLG`
- `1080P 60FPS HLG`
- `4K 30FPS HLG`
- `4K 60FPS HLG`

Each row should fill every project camera column with `✓`, `✗`, or draft-only `TBD`, so QA can see support differences by camera. Front 4K requirements map to the relevant concrete spec row, usually `4K 30FPS`, with front camera support marked there.

Video `Filter` and `Style` should also appear in video Toolbar rows when the project has video-mode effects/style capabilities. If a capability is only unavailable for a specific spec such as front 4K, describe the spec-level limitation in `说明` / `验证方法` rather than deleting the general video row.

`Log 视频` belongs in Video Toolbar, not Mode Switch. Its row must state the supported resolution, fps, lens and encoding range.

## Slow Motion Specs

Slow motion specifications should be checklist rows under `模式=慢动作 / Slow Motion`, `一级分类=功能 / Feature`, `二级分类=慢动作规格 / Slow Motion Specs`.

Use concrete rows so QA can see the supported spec directly:

- `1080P 30FPS`
- `1080P 120FPS`
- `1080P 240FPS`
- `720P 120FPS`
- `720P 240FPS`
- `720P 480FPS`

Slow motion mode support itself is not the unclear part for 26111/26121 drafts; the unresolved part is which concrete specs and cameras are supported.

## High Resolution Specs

High-resolution mode should expose concrete output options rather than one broad `200MP` chain row.

Current 26111 / 26121 draft rules:

| Project | Rows |
|---|---|
| 26111 | `50MP`, `200MP`, `200MP Ultra` |
| 26121 | `50MP`, `50MP Ultra` |

All high-resolution options use remosaic. `Ultra` options apply RAW HDR after remosaic to improve clarity and image quality.

## Canonical Algorithm Names

Use these canonical names when merging KB, Feature Tree, old FL rows and project requirements:

| Canonical row | Rule |
|---|---|
| `ASD / AI场景检测` | AI-model semantic scene detection, e.g. green plants, stage and outdoor sky. Do not keep `普通场景检测` as a standalone row when it only means brightness/DRC/motion judgement. |
| `SAT / 平滑镜头切换` | Same function as `SAT`. Rear cameras support the lens-switching capability; front camera does not. `变焦` row should explain SAT smooth switch, hard cut and digital zoom. |
| `Photo EIS / PZL` | Photo high-zoom stabilization / post-shutter frame capture. PZL differs from ZSL pre-buffer capture. |
| `Video EIS` | Video electronic stabilization; the user switch lives in Settings > Video as `视频防抖开关`. |
| `光学畸变矫正` | Merge `镜头畸变矫正` / `光学畸变矫正` / `光学畸变校正`; keep `人脸畸变矫正` separate. |
| `FRT / 人像清晰度提升` | 自然质感人像能力族中的独立清晰度增强 feature；合并 `人脸清晰度增强` 等旧称，保留 `人脸检测` 为独立功能。 |
| `美颜升级 / Beauty Upgrade` | 自然质感人像能力族中的独立参数与效果升级 feature；仅在照片、人像模式的 Front 展开，不与 FRT 合并。 |

## Dual View Video

Dual View Video v2 should be split by acceptance surface:

| Row | Placement |
|---|---|
| `前后双录后置镜头选择` | `前后双录 / Dual View Video` → `功能 / Feature` → `预览框 / Preview` |
| `前后双录主副互换 / 小窗大小` | `前后双录 / Dual View Video` → `功能 / Feature` → `预览框 / Preview` |
| `前后双录分开保存` | `通用 / Common` → `设置 / Settings` → `视频设置 / Video Settings` |
