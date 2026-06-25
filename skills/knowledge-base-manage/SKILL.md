---
name: knowledge-base-manage
description: Use when the user asks to generate camera feature lists, manage device configs, update sensor datasheets, or maintain knowledge base references. Covers feature list generation (parameterized by project), device YAML management, and knowledge base consistency checks.
---

# Knowledge Base Manager

## Overview

This skill manages the Nothing Camera knowledge base (`knowledge/` directory). It covers generating feature lists for any project, managing device configuration files, and maintaining reference documents.

## Core Capabilities

### 1. Feature List Generation

Generate a camera feature list for any project:

```bash
# Generate markdown for 26111
python3 knowledge/generate.py --project 26111

# Generate markdown only
python3 knowledge/generate.py --project 25131 --format markdown

# Generate excel
python3 knowledge/generate.py --project 26111 --format excel
```

**How it works:**
1. Reads `knowledge/devices/{project}.yaml` (or `.json`) for device config
2. If the project has `inheritance.baseline`, loads baseline features
3. Applies `removed_features` (name-match filtering) and `new_features_p0` (appends)
4. Reads camera specs from YAML `cameras` section for device specs table
5. Outputs to `knowledge/_output/features-{project}.md` (and `.xlsx`)

**Supported projects:** 25111, 25131, 26111 (as of 2026-06)

### 2. Device Config Management

Device YAML files live at `knowledge/devices/{project}.yaml`. Standard sections:

```yaml
project:           # code, name, market, SoC, software baseline
cameras:           # base/pro -> main, ultrawide, tele, front sensors
inheritance:       # baseline project, rules, deltas
defaults:          # per-mode default values (photo/portrait/video/front/pro/settings etc.)
                   #   other configs can reference "使用默认值" to inherit from here
new_features_p0:   # list of new feature names (human-readable)
removed_features:  # list of removed feature names
stakeholders:      # PM, SE, ISP, Camera App, design, test
status:            # feature_list, algorithms, sensors, feature_json
```

### 3. Sensor Datasheet Management

Sensor datasheets live at `knowledge/devices/sensors/{model}.yaml`. Standard schema includes `capability_summary` with fields: `4k_30fps`, `4k_60fps`, `1080p_60fps`, `1080p_120fps`, `1080p_240fps`, `hdr_photo`, `hdr_video`, `pdaf`, `ois`.

### 4. Knowledge Base Consistency Check

When reviewing a feature list against hardware:
1. Load `knowledge/features/rear-camera.json` + `front-camera.json`
2. Load project `knowledge/devices/{project}.yaml`
3. Cross-reference sensor `capability_summary` against feature list
4. Flag: hardware-impossible features (❌), missing features, unconfirmed (`[inferred]`)

## Project Inheritance Convention

Projects follow a baseline + delta model:

| Project | Baseline | Feature Source |
|---------|----------|---------------|
| 25131 | — (reference) | `features/rear-camera.json` |
| 26111 | 25131 | 25131 features + deltas in `devices/26111.yaml` |

**How to add a new project:**
1. Create `knowledge/devices/{project}.yaml` with device config
2. Set `inheritance.baseline` to the closest existing project
3. List `new_features_p0` and `removed_features`
4. Run `python3 knowledge/generate.py --project {project}` to generate feature list
5. Mark `status.feature_list` as "待 SE 确认算法后定稿" until SE confirms

## Reference Files

- `knowledge/devices/{project}.yaml` — device config per project
- `knowledge/features/rear-camera.json` — canonical rear camera feature matrix (25131)
- `knowledge/features/front-camera.json` — canonical front camera feature matrix (25131)
- `knowledge/features/focal-lengths.json` — focal length configuration
- `knowledge/feature-tree.md` — feature taxonomy (11 interaction zones)
- `knowledge/devices/sensors/` — sensor datasheets
- `knowledge/_output/features-{project}.md` — generated feature lists
- `knowledge/README.md` — knowledge base overview

## Quick Lookup

- "生成 26111 功能列表" → `python3 knowledge/generate.py --project 26111`
- "更新 26111 设备配置" → Edit `knowledge/devices/26111.yaml`
- "26111 硬件能力" → Read `knowledge/devices/26111.yaml` + sensor YAMLs
- "26111 和 25131 有什么差异" → Compare device YAMLs, check `key_deltas_from_25131`
