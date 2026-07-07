---
name: feature-list-writer
description: Create and maintain Camera Feature List Bitables for any project. Covers Bitable creation, table schema design, baseline-to-target population, hardware config management, feature pruning, and algorithm classification. Use when creating a new project FL, migrating an old Sheet FL to Bitable, or updating FL content.
---

# Feature List Writer

## Overview

Creates and maintains Camera Feature Lists as Lark Bitables. Each project gets its own FL Bitable under the `Camera feature list` wiki directory, containing a hardware config table plus per-device feature tables.

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
| 模式 | select | 照片/人像/运动/视频/夜景/慢动作/全景/专业/前后双录/高像素/延时摄影/文档矫正 |
| 一级分类 | select | 功能 / 基础算法 |
| 二级分类 | select | 功能→交互区(预览框/AE·AF/Zoom/左侧暂态开关/右侧暂态开关/Top Toolbar/Mode Switch/Preset/Settings/启动·退出/系统); 算法→实时算法/后处理算法 |
| 名称 | text | 功能名或算法方案名 |
| 说明 | text | 功能基本描述 |
| {camera} | select(✓/✗) | 每个摄像头独立一列，仅列出该设备实际存在的摄像头 |
| 验证方法 | text | 验收标准 |

**Camera columns**: Only include cameras the device actually has. 26111: Main + UW + Front. 26121: Main + UW + Tele + Front. Never create "无长焦" placeholder columns — just omit.

### 功能栏与通用功能规则

- Project FL is a capability matrix: expand KB mode scopes into one row per real mode, and keep unsupported rows with `✗` so project/mode/camera differences are visible.
- `Preset` 是底部独立区域；KB 中用 `模式=全部拍摄模式` 表达，最终 FL 按项目真实模式展开支持状态，除非产品明确要求单独建“通用功能”表。
- `Settings` 是通用功能；KB 中用 `模式=全部拍摄模式` 或具体模式范围表达，最终 FL 按项目真实模式展开支持状态，除非产品明确要求单独建“通用功能”表。
- 不要在 `模式` 字段里写 `通用`，除非 Bitable schema 明确新增这个模式值。
- 快门区域不写入 Feature List：快门按键、相册缩略图、前后摄像头翻转按键是所有相机都有的基础入口，除非某项目新增明确差异化行为，否则不生成行。
- Settings 分组如下：

| Settings group | Feature List rows |
|---|---|
| General | Preset, Save location, Shutter sound, Mirror front camera, Level |
| Photo | Watermark, Auto Tone, Tap to take a photo, QR code scanner, Press and hold shutter, Ultra XDR |
| Video | Video encoding (H.264 / H.265), Power saving recording, Auto FPS (Off / Auto 30 / Auto 30&60) |

### Photo Top Toolbar 规则

Photo 和 Video 是工具栏最完整的模式，其他模式通常在这两个集合上删减。Photo 模式 Top Toolbar 使用 `模式=照片`、`一级分类=功能`、`二级分类=Top Toolbar`。

| 功能项 | 写法 |
|---|---|
| Flash | Rear: Off / On / Torch；Front: screen fill, can expose Auto；Glyph mode only for projects with required Glyph hardware |
| Timer | Off / 3s / 10s |
| HDR | Current projects use Auto / Off only; no forced On. Off and Auto may map to MFNR / RAW HDR differently by project |
| Exposure | Global exposure, -2EV to +2EV, 0.3EV step |
| Filter | Built-in filters + user-imported filters; reference `knowledge/reference/filter.md`, do not list every filter name |
| Tuning | Seven parameters from Preset 2.0 / Tuning Palette; reference `knowledge/reference/tuning.md` |
| Motion Photo | One row by default; only split `Motion Photo cover HDR` when support differs and needs explicit validation |
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
- Do not use `通用` in the KB; use `全部拍摄模式` or an explicit mode list.
- `来源项目` must be baseline references such as `25111 / 25131`, not target projects `26111 / 26121`.
- `验证方法` must be a real verification method, not `✓`, `✗`, PRD title, owner, or support mark.
- Use the audit output to catch duplicates, bad source projects, and bad verification methods before syncing to Lark.

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

**一级分类 = 功能**: 用户可感知的相机功能
- 二级分类 = feature-tree 交互区
- 交互区来源: `knowledge/feature-tree.md`
- 功能名称 = 用户 UI 上看到的名称（如 "自动微距控制"）
- 说明 = 技术实现简述
- `模式` must be a real camera mode in final FL. Do not use `通用` unless the Bitable schema explicitly adds it.

**一级分类 = 基础算法**: 底层算法模块，用户不直接感知
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
- Use only these two values in the select columns. Details go in 说明.

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
