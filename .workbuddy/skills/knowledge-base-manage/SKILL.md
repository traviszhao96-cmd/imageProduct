---
name: knowledge-base-manage
description: Use when the user asks to generate camera feature lists, manage device configs, update sensor datasheets, or maintain knowledge base references. Covers feature list generation (parameterized by project), device YAML management, Bitable FL creation, and knowledge base consistency checks.
---

# Knowledge Base Manager

## Overview

Manages the Nothing Camera knowledge base (`knowledge/` directory) and Lark Bitable Feature Lists. Covers: generating feature lists, managing device configs, creating/maintaining Bitable FLs, and cross-referencing consistency.

## Core Capabilities

### 1. Bitable Feature List Creation (primary workflow)

The authoritative Feature List is now a **Lark Bitable** per device, not a local markdown file. Format:

| 列 | 类型 | 说明 |
|---|---|---|
| 模式 | Select | 通用/拍照/录像/人像/夜景/专业/高像素/慢动作/延时摄影/全景/文档矫正 |
| 一级分类 | Select | 功能 / 基础算法 / 预设 / 设置 / 小组件 |
| 二级分类 | Select | 功能→交互区(预览框/AE·AF/Zoom/Toolbar/Mode Switch/暂态开关/系统); 设置→通用设置/照片设置/视频设置/帮助与反馈; 算法→实时算法/后处理算法 |
| 名称 | Text | 功能名或算法方案名 |
| 说明 | Text | 功能基本描述 |
| {camera} | Select(✓/✗) | 每个摄像头独立一列。仅列出该设备实际存在的摄像头。无长焦的设备不设长焦列。 |
| 验证方法 | Text | 验收标准 |

**Two devices = two separate tables.** 26111 has Main/UW/Front. 26121 has Main/UW/Tele/Front.

**Bitable location**: `26111 & 26121 Camera Feature List` under `Camera feature list` wiki directory.
Base token: `YJSObjrqmamennsGWE5lqYdogFh`

### 2. Feature List Generation (legacy — markdown output)

Generate markdown feature list from JSON data:

```bash
python3 knowledge/generate.py --project 26111
python3 knowledge/generate.py --project 25131 --format markdown
```

**How it works:**
1. Reads `knowledge/devices/{project}.yaml` for device config
2. If the project has `inheritance.baseline`, loads baseline features
3. Applies `removed_features` and `new_features_p0`
4. Outputs to `knowledge/_output/features-{project}.md`

The generated markdown is used as **input data** for populating the Bitable FL.

### 3. Hardware Config Table

Each Feature List Bitable includes a **硬件配置** table:

| 列 | 说明 |
|---|---|
| 项目代号 | 25111, 26111... |
| 机型 | Base / Pro |
| 相机位置 | 主摄 / 超广角 / 长焦 / 前置 |
| Sensor 型号 | HP5, IMX896... |
| 分辨率 | 200MP, 50MP... |
| Sensor 尺寸 | 1/1.4"... |
| 像素大小 | 0.64um... |
| OIS | YES/NO |
| 光圈 | f/1.8... |
| 等效焦距 | 24mm... |
| 对焦类型 | PDAF/FF |
| Fallback支持 | YES/NO |
| 备注 | 26111: 200MP→50MP HDR upscale |

### 4. Project Inheritance Convention

| 新项目 | 基线项目 | 说明 |
|---|---|---|
| 26111 Base | 25131 | JN1 → HP5 升级，新增 200MP |
| 26121 Pro | 25111 Pro | IMX896 同配置，直接复用 |

**How to create a new project FL:**
1. Identify the baseline project (hardware-closest predecessor)
2. Create device YAML at `knowledge/devices/{project}.yaml`
3. Generate baseline feature list: `python3 knowledge/generate.py --project {project}`
4. Create Bitable in `Camera feature list` wiki directory
5. Add 硬件配置 table with camera specs
6. Add device table(s) with the standard FL format
7. Populate from baseline, remove inapplicable features, add new ones
8. Mark algorithm-dependent features pending until algorithm doc confirmed

### 5. Device Config Management

Device YAML files at `knowledge/devices/{project}.yaml`:

```yaml
project:           # code, name, market, SoC
cameras:           # base/pro -> main, ultrawide, tele, front
inheritance:       # baseline project, rules, deltas
defaults:          # per-mode default values
new_features_p0:   # new feature names
removed_features:  # removed feature names
```

### 6. Sensor Datasheet Management

Sensor datasheets at `knowledge/devices/sensors/{model}.yaml`. Standard `capability_summary`:
`4k_30fps`, `4k_60fps`, `1080p_60fps`, `1080p_120fps`, `1080p_240fps`, `hdr_photo`, `hdr_video`, `pdaf`, `ois`

### 7. FL Format Design Rules

- ✅ Each device has its own table — don't mix devices in one table
- ✅ Only include cameras that exist on the device (no "无长焦" placeholder columns)
- ✅ ✓/✗ only — don't write resolution values (e.g., "200MP") in support columns; put details in 说明
- ✅ 一级分类 = 功能/基础算法/预设/设置/小组件; 二级分类 maps to feature-tree for 功能, Settings group for 设置, 实时/后处理 for 算法
- ✅ Mode is specific for capture features; use `通用 / Common` only for Preset / Settings / Widget and true all-mode common rows

## Reference Files

- `knowledge/feature-tree.md` — 11 interaction zones + purpose tags + 暂态开关
- `knowledge/devices/{project}.yaml` — device config
- `knowledge/features/rear-camera.json` — rear feature matrix (25131 baseline)
- `knowledge/features/front-camera.json` — front feature matrix (25131 baseline)
- `knowledge/devices/project-mapping.yaml` — all devices mapping
- `knowledge/devices/sensors/` — sensor datasheets
- `knowledge/_output/features-{project}.md` — generated markdown (input for Bitable)

## Quick Lookup

- "生成 26111 功能列表" → `python3 knowledge/generate.py --project 26111` → populate Bitable
- "创建 26111 FL Bitable" → Create table in `YJSObjrqmamennsGWE5lqYdogFh` with standard format
- "26111 硬件能力" → Read 硬件配置 table or `knowledge/devices/26111.yaml`
- "26111 和 25131 差异" → Compare device YAMLs, check `key_deltas_from_25131`
- "更新 FL 硬件配置" → Edit 硬件配置 table in Bitable
