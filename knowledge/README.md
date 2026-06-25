# Nothing Mobile Camera — Knowledge Base

Camera domain knowledge for AI agents writing PRDs, reviewing feature lists, and validating sensor capabilities.

## Quick Lookup

| 需求 | 读 |
|------|-----|
| 某模式支持什么功能 | `features/rear-camera.json` / `front-camera.json` |
| 某摄像头硬件能力 | `devices/{project}.json` → capability 字段 |
| 某 sensor 详细规格 | `devices/sensors/{model}.yaml` |
| 焦段/变焦配置 | `features/focal-lengths.json` |
| NPS 满意度 | `reference/nps-*.json` |
| 生成功能列表 | `python3 knowledge/generate.py --project {code}` |

## Directory

```
knowledge/
├── README.md
├── features/
│   ├── rear-camera.json    后置: 模式 × 功能 × 超广角/主摄
│   ├── front-camera.json   前置: 模式 × 功能 × 前摄
│   └── focal-lengths.json  各模式焦段/变焦/Preset 配置
├── devices/
│   ├── {project}.json      项目级规格 + capability 基线
│   └── sensors/            每颗 sensor 详细 Datasheet
│       ├── S5KJNSSQ33.yaml
│       ├── GC08A8.yaml
│       ├── IMX896-AJH5-C.yaml
│       └── OS08A10.yaml
├── reference/              外部数据
│   └── nps-*.json
├── _output/                自动生成视图
│   ├── features-{project}.md
│   └── features-{project}.xlsx
└── generate.py             参数化生成器
    Usage: python3 knowledge/generate.py --project 26111 [--format markdown|excel|all]
```

## Sensor Capability Labels

| 值 | 含义 |
|------|------|
| `YES` | 确认支持 |
| `NO` | 确认不支持 |
| `UNSUPPORTED — hardware limit` | 硬件限制 |
| `SENSOR_CAPABLE_BUT_PLATFORM_LIMITED` | Sensor 支持但 ISP/平台限制 |
| `SOFTWARE ONLY` | 无硬件支持，软件模拟 |
| `[inferred]` | 推断值，无数据手册确认 |

## Sensor YAML Fields

All sensor YAMLs expose a `capability_summary` for AI comparison:

```yaml
capability_summary:
  4k_30fps: YES/NO
  4k_60fps: YES/NO
  1080p_60fps: YES/NO
  1080p_120fps: YES/NO
  1080p_240fps: YES/NO
  hdr_photo: YES/NO
  hdr_video: YES/NO
  pdaf: YES/NO
  ois: YES/NO
```

## Agent Behavior When Reviewing Feature List

1. Load `features/rear-camera.json` + `front-camera.json`
2. Load project `devices/{project}.json` → per-camera capability baseline
3. Cross-reference sensor YAML `capability_summary` → detect sensor vs feature list gaps
4. Flag: hardware-impossible ×, missing features, stale/abandoned entries
