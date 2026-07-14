---
name: feature-list-writer
description: Create and maintain Camera Feature List Bitables for any project. Covers Bitable creation, table schema design, baseline-to-target population, hardware config management, feature pruning, and algorithm classification. Use when creating a new project FL, migrating an old Sheet FL to Bitable, or updating FL content.
---

# Feature List Writer

## Overview

Creates and maintains Camera Feature Lists as Lark Bitables. Each project gets its own FL Bitable under the `Camera feature list` wiki directory, containing a hardware config table plus per-device feature tables.

FL is a project acceptance checklist artifact. It defines which Camera functions the project finally supports; imaging SE and PM produce it, and PM/QA/test use it to verify that implementation matches design. Its repeated rows and support marks are necessary for acceptance, but they should be generated and audited from Feature Tree, KB, project requirements, and hardware/project config rather than hand-maintained as dead duplicated information.

## When to Use

- "创建 26111 功能列表"
- "生成 XXX 的 Feature List"
- "更新 XXX FL 的硬件配置"
- "把旧 FL 迁移到 Bitable"
- "XX 和 XX 的功能差异是什么"

## FL Bitable Format

### Location

Wiki space → `Camera feature list` (parent token: `AHYRwmHTxiyzSGk7WrJliba2gre`).

### Structure

Each FL Bitable contains:

1. **硬件配置表** — camera hardware specs for all device variants
2. **{项目代号} 表** — one per device variant (e.g., `26111`, `26121`)

### 硬件配置表 Schema

| 列 | 类型 | 说明 |
|---|---|---|
| 项目代号 | text | 25111, 26111... |
| 机型 | text | Base / Pro |
| 相机位置 | select | 主摄 / 超广角 / 长焦 / 前置 |
| Sensor 型号 | text | HP5, IMX896, JN5... |
| 分辨率 | text | 200MP, 50MP, 8MP... |
| Sensor 尺寸 | text | 1/1.4"... |
| 像素大小 | text | 0.64um... |
| OIS | select | YES / NO |
| 光圈 | text | f/1.8... |
| 等效焦距 | text | 24mm... |
| 对焦类型 | text | PDAF / FF |
| Fallback支持 | select | YES / NO |
| 备注 | text | 如 "200MP→50MP HDR upscale" |

### 功能表 Schema

| 列 | 类型 | 说明 |
|---|---|---|
| 模式 | select | 双语枚举，如 通用 / Common、照片 / Photo、人像 / Portrait、视频 / Video、夜景 / Night |
| 一级分类 | select | 功能 / Feature、算法 / Algorithm、预设 / Preset、设置 / Settings、小组件 / Widget |
| 二级分类 | select | 双语枚举：预览框 / Preview、AE/AF、变焦 / Zoom、工具栏 / Toolbar、模式栏 / Mode Switch、预设 / Preset、通用设置 / General Settings、照片设置 / Photo Settings、视频设置 / Video Settings、帮助与反馈 / Help & Support、小组件 / Widget、左侧暂态开关 / Left Transient Switch、右侧暂态开关 / Right Transient Switch、实时算法 / Realtime Algorithm、后处理算法 / Post-processing Algorithm |
| 名称 | text | 功能名或算法方案名 |
| 说明 | text | 功能基本描述 |
| {camera} | select(✓/✗/TBD) | 每个摄像头独立一列，仅列出该设备实际存在的摄像头；TBD 仅用于分发草稿和待确认项 |
| 不支持原因 | text | 当摄像头列为 ✗ 时，说明不支持来自硬件限制、PRD 范围、基线 FL 或项目配置的原因 |
| 状态 | select | 已确认 / 待确认 / Pending |
| 确认负责人 | select | 单一角色：Product / SE / SQA / IQA；旧多选字段也只能保存一个值 |
| 验证方法 | text | 验收标准 |

**Camera columns**: Only include cameras the device actually has. 26111: Main + UW + Front. 26121: Main + UW + Tele + Front. Never create "无长焦" placeholder columns — just omit.

### 功能栏与通用功能规则

- FL 是项目验收 checklist，不是 taxonomy 或功能说明书。Feature Tree 管分类，KB 管功能含义/判断依据/依赖/验证方法，项目配置管硬件和算法开关，FL 负责把这些输入展开成项目可验收的 `✓` / `✗` 矩阵。
- 需求不是全新用户功能、模式入口、交互入口或算法能力时，不要新增 Tree/KB 行；更新已有功能的说明、判断依据、依赖或验证方法。
- Project FL is a capability matrix: expand mode-specific KB scopes into one row per real mode when the table needs per-mode visibility, and keep unsupported rows with `✗` so project/mode/camera differences are visible.
- `Preset`、`Settings`、`Widget` 使用 `模式=通用 / Common`，不要按照片/视频/夜景等模式重复展开。
- Common rows use direct first-level categories: `一级分类=预设 / Preset`、`设置 / Settings`、`小组件 / Widget`.
- Settings 即便只影响照片或视频结果，也保持在 `通用 / Common` 行里，影响范围写进说明、判断依据或验证方法。
- 最终 FL 排序时，先放具体拍摄模式，`模式=通用 / Common` 的行统一放在表格最底部。
- 分发草稿中，每个 `✗` 尽量填写 `不支持原因`；如果一行所有摄像头列都已经是 `✓` 或 `✗`，状态写 `已确认`，有任意 `TBD` 则写 `待确认`。
- `通用` 表示 all modes / 最大适配性，只能用于确实支持所有模式的功能；模式特定功能必须写具体模式范围。
- 快门区域不写入 Feature List：快门按键、相册缩略图、前后摄像头翻转按键是所有相机都有的基础入口，除非某项目新增明确差异化行为，否则不生成行。
- Settings 分组如下：

| Settings group | Feature List rows |
|---|---|
| General | Preset, Save location, Shutter sound, Mirror front camera, Level |
| Photo | Watermark, Auto Tone, Tap to take a photo, QR code scanner, Press and hold shutter, Ultra XDR |
| Video | Video encoding (H.264 / H.265), Power saving recording, Auto FPS (Off / Auto 30 / Auto 30&60), 视频防抖开关, 锁定镜头, 锁定白平衡 |
| Help & Support | Tips and feedback |

### Photo Toolbar 规则

Photo 和 Video 是工具栏最完整的模式，其他模式通常在这两个集合上删减。Photo 模式 Toolbar 使用 `模式=照片 / Photo`、`一级分类=功能 / Feature`、`二级分类=工具栏 / Toolbar`。

| 功能项 | 写法 |
|---|---|
| Flash | Rear: Off / On / Torch；Front: screen fill, can expose Auto；Glyph mode only for projects with required Glyph hardware |
| Timer | Off / 3s / 10s |
| HDR | Current projects use Auto / Off only; no forced On. Off and Auto may map to MFNR / RAW HDR differently by project |
| Exposure | Global exposure, -2EV to +2EV, 0.3EV step |
| Filter | Built-in filters + user-imported filters; reference `knowledge/reference/filter.md`, do not list every filter name |
| Tuning | Manual tuning capability: Tuning Palette / Palette Mode / Parameter Mode / Strength / seven parameters; reference `knowledge/reference/tuning.md` |
| Photo Style | Natural / Vivid ISP style switch; separate from manual Tuning |
| Motion Photo | One row by default; split `Motion Photo cover HDR` or `动态照片 - 无效信息截取` when support differs or QA needs explicit validation |
| Quality | 20MP / 50MP / 200MP depending on camera output and ISZ/crop capability |
| Grid | On / Off |
| Ratio | 1:1 / 4:3 / 16:9 / Full; disabled when current camera is in max-pixel output such as 50MP |
| Watermark | Tap toggles On/Off; long press jumps to Settings > Photo > Watermark |
| More settings | Opens Camera Settings |
| Glyph Mirror | Optional; only projects with large rear Glyph LED hardware, e.g. 25111 Pro supports, 25111 does not |

## Workflow

### 0. Maintain Canonical KB Before Project FL

Before generating 26111/26121 Feature Lists, maintain the canonical KB:

```
python3 scripts/build_kb_functions_algorithms.py
```

Outputs:

- `knowledge/_output/kb-functions-algorithms.v6.json`
- `knowledge/_output/kb-functions-algorithms.v6.audit.md`

KB rules:

- One row = one unique function or algorithm capability.
- `模式` is a supported mode scope, not one row per mode.
- `通用` is allowed in the KB when it means all supported camera modes / maximum compatibility; otherwise use an explicit mode list.
- `来源项目` must be baseline references such as `25111 / 25131`, not target projects `26111 / 26121`.
- `验证方法` must be a real verification method, not `✓`, `✗`, PRD title, owner, or support mark.
- Use the audit output to catch duplicates, bad source projects, and bad verification methods before syncing to Lark.
- Use existing manual FLs as acceptance-output references and drift/audit inputs, not as canonical KB structure.

### 1. Create a New FL

```
1. Identify baseline project (hardware-closest predecessor)
2. Load canonical KB: knowledge/_output/kb-functions-algorithms.v6.json
3. Expand each KB row's mode scope into real project mode rows
4. Apply project/camera hardware judgement and fill each camera column with ✓ / ✗
5. Keep unsupported rows with ✗ when the feature is in that mode scope; this is how FL shows differences
6. Create Bitable in Lark under Camera feature list wiki directory
7. Add 硬件配置 table → populate from devices/{project}.yaml
8. Add per-device tables → populate expanded FL rows
9. Run AI audit for duplicates, missing validation, suspicious source/judgement, and unresolved TBD
```

### 2. Project Inheritance

| 新项目 | 基线 | 说明 |
|---|---|---|
| 26111 Base | 25131 | JN1→HP5, 新增200MP upscale, 无长焦 |
| 26121 Pro | 25111 Pro | IMX896, 同配置直接复用 |
| 25111 Base | 24111 Base | GN9同款, +JN5长焦 |

### 3. Feature Classification Rules

**一级分类 = 预设 / Preset、设置 / Settings、小组件 / Widget**: 不挂在具体拍摄模式下的公共能力
- `模式` 固定使用 `通用 / Common`
- Preset: `二级分类=预设 / Preset`
- Settings: `二级分类=通用设置 / General Settings`、`照片设置 / Photo Settings`、`视频设置 / Video Settings`、`帮助与反馈 / Help & Support`
- Widget: `二级分类=小组件 / Widget`
- Settings 不展开到照片/视频等模式，影响范围写入说明或验证方法

**一级分类 = 功能 / Feature**: 用户可感知的相机功能
- 二级分类 = feature-tree 交互区
- 交互区来源: `knowledge/feature-tree.md`
- 功能名称 = 用户 UI 上看到的名称（如 "自动微距控制"）
- 说明 = 技术实现简述

**一级分类 = 算法 / Algorithm**: 算法和处理链路能力，用户不一定直接感知
- 二级分类 = 实时算法 / 后处理算法
- 实时算法: 预览/拍摄时即时运行的算法（HDR多帧合成、人脸检测、场景检测...）
- 后处理算法: 拍摄后异步处理的算法（AI Upscale、美颜、超分...）
- 名称 = 算法方案名（如 "虹软HDR多帧合成"）
- 说明 = 算法供应商 + 技术要点

### 4. Feature Pruning

When inheriting from baseline:
- Remove: features that depend on hardware the target device doesn't have
- Keep: features that work on existing hardware
- Add: new features listed in device YAML `new_features_p0`
- Mark [TBD]: features that depend on unconfirmed algorithms

### 5. Camera Support Values

- `✓` = supported (tested and confirmed)
- `✗` = not supported (hardware limitation or not applicable)
- `TBD` = draft-only unresolved judgement, requiring PM/SE/QA review before final sign-off
- For final sign-off, resolve `TBD` to `✓` or `✗`.
- For every inferred `✗`, fill `不支持原因` when possible. Put behavior details in `说明` and acceptance steps in `验证方法`.

### 6. Video Specs

Video specifications are independent FL rows under `模式=视频 / Video`, `一级分类=功能 / Feature`, `二级分类=视频规格 / Video Specs`.

Do not keep a broad row such as `前置 4K 视频` in the final checklist. Expand concrete specs such as `1080P 30FPS`, `1080P 60FPS`, `4K 30FPS`, `4K 60FPS`, `1080P 30FPS HLG`, `1080P 60FPS HLG`, `4K 30FPS HLG`, and `4K 60FPS HLG`, then mark every camera column independently.

Video `Filter` and `Style` belong in video Toolbar rows when supported by the project. If a limitation is spec-specific, such as front 4K not supporting Filter/Tuning because only the 1080P pipeline supports it, state that in `说明` / `验证方法`.

`Log 视频` belongs in Video Toolbar, and the row must state the supported resolution, fps, lens and encoding range.

### 7. Slow Motion Specs

Slow motion specifications are independent FL rows under `模式=慢动作 / Slow Motion`, `一级分类=功能 / Feature`, `二级分类=慢动作规格 / Slow Motion Specs`.

Use concrete rows such as `1080P 30FPS`, `1080P 120FPS`, `1080P 240FPS`, `720P 120FPS`, `720P 240FPS`, and `720P 480FPS`. Slow motion mode support can be known while the exact supported spec matrix remains `TBD`.

### 8. High Resolution Specs

High-resolution mode should expose concrete output options rather than one broad `200MP` chain row.

Current 26111 / 26121 draft rules:

| Project | Rows |
|---|---|
| 26111 | `50MP`, `200MP`, `200MP Ultra` |
| 26121 | `50MP`, `50MP Ultra` |

All high-resolution options use remosaic. `Ultra` options apply RAW HDR after remosaic to improve clarity and image quality.

### 9. Canonical Algorithm Names

Normalize old FL, KB, Feature Tree and project requirement names before generating final rows:

| Canonical row | Rule |
|---|---|
| `ASD / AI场景检测` | AI-model semantic scene detection, e.g. green plants, stage and outdoor sky. Do not keep `普通场景检测` as a standalone row when it only means brightness/DRC/motion judgement. |
| `SAT / 平滑镜头切换` | Same as SAT. Rear cameras support the lens-switching capability; front camera does not. `变焦` row should explain SAT smooth switch, hard cut and digital zoom. |
| `Photo EIS` | Photo electronic stabilization, typically enabled for project-defined high-zoom ranges. |
| `PZL` | Post-shutter frame-capture strategy; separate from Photo EIS and different from ZSL pre-buffer capture. |
| `Video EIS` | Video electronic stabilization; the user switch lives in Settings > Video as `视频防抖开关`. |
| `光学畸变矫正` | Merge `镜头畸变矫正` / `光学畸变矫正` / `光学畸变校正`; keep `人脸畸变矫正` separate. |
| `人脸清晰度增强` | Merge FRT wording into this row; keep `人脸检测` separate. |

### 10. Dual View Video

Dual View Video v2 should be split by acceptance surface:

| Row | Placement |
|---|---|
| `前后双录后置镜头选择` | `前后双录 / Dual View Video` → `功能 / Feature` → `预览框 / Preview` |
| `前后双录主副互换 / 小窗大小` | `前后双录 / Dual View Video` → `功能 / Feature` → `预览框 / Preview` |
| `前后双录分开保存` | `通用 / Common` → `设置 / Settings` → `视频设置 / Video Settings` |

### 11. Style / Tuning / Photo Style Dedup

- `Photo Style` = Natural / Vivid ISP style switch. Keep it as an independent FL row when the project exposes this entry.
- `Tuning` = manual tuning capability, including Tuning Palette, Palette Mode, Parameter Mode, Strength, and seven-parameter adjustment.
- `Filter` = LUT / filter selection and imported filters.
- Do not generate `Style / Tuning Palette / Palette-Parameters` as a separate FL row. Treat that wording as a requirement update to `Tuning`, unless PM explicitly confirms a new user-facing `Style` entry that replaces or merges existing Filter and Tuning UI.
- If a PRD says Filter and Tuning may merge in the future but current scope does not merge them, keep current FL rows as `Filter`, `Tuning`, and `Photo Style` only.

## Key Resources

| Resource | Token/Path |
|---|---|
| 26111 & 26121 FL | `YJSObjrqmamennsGWE5lqYdogFh` |
| Feature tree | `knowledge/feature-tree.md` |
| Rear camera baseline | `knowledge/features/rear-camera.json` |
| Front camera baseline | `knowledge/features/front-camera.json` |
| Device configs | `knowledge/devices/{project}.yaml` |
| FL generator | `knowledge/generate.py` |
| Wiki parent dir | `AHYRwmHTxiyzSGk7WrJliba2gre` |

## Quick Lookup

- "创建 26111 FL" → Create Bitable → add 硬件配置 + 26111 table → populate from 25131 baseline
- "更新硬件配置" → Edit 硬件配置 table in the Bitable
- "XX 支持什么功能" → Query the Bitable → filter by mode/camera
- "对比 26111 vs 26121" → Compare two tables in the Bitable
