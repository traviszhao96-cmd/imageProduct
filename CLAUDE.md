# Nothing Camera — AI Agent Knowledge Base

Camera domain knowledge for AI agents working on Nothing/CMF phone camera features: writing PRDs, reviewing feature lists, validating sensor capabilities, analyzing feedback, and generating reports.

## Quick Start

Before doing ANY camera-related work, load the relevant knowledge files first:

| Task | Read These Files |
|------|-----------------|
| Write a camera PRD | `knowledge/feature-tree.md` → `knowledge/features/{rear,front}-camera.json` → `knowledge/devices/{project}.yaml` |
| Review a feature list | `knowledge/features/{rear,front}-camera.json` → `knowledge/devices/{project}.yaml` → sensor YAMLs |
| Check hardware capability | `knowledge/devices/{project}.yaml` → `knowledge/devices/sensors/{model}.yaml` |
| Analyze NPS/feedback | `knowledge/reference/nps-*.json` → `knowledge/reference/gallery-feedback-*.json` |
| Understand device lineup | `knowledge/devices/project-mapping.yaml` |
| Check zoom/focal config | `knowledge/features/focal-lengths.json` |
| Look up a specific feature PRD | `knowledge/reference/INDEX.md` → navigate to feature group |

## Knowledge Base Structure

```
knowledge/
├── README.md                          # Agent behavior & sensor capability labels
├── feature-tree.md                    # Complete camera feature taxonomy (11 interaction zones × purpose tags)
├── generate.py                        # JSON → markdown/excel converter
│
├── features/                          # WHAT each camera mode supports
│   ├── rear-camera.json               # Rear camera: mode × feature × lens (UW/Main/Tele)
│   ├── front-camera.json              # Front camera: mode × feature
│   └── focal-lengths.json             # Zoom/Preset/focal config per mode
│
├── devices/                           # Hardware capability per project
│   ├── project-mapping.yaml           # ALL devices: project_code → codename → market → SoC → camera
│   ├── {project}.yaml/json            # Per-project spec + capability baseline
│   └── sensors/                       # Individual sensor datasheets
│       ├── S5KJNSSQ33.yaml            # JN1 (50MP)
│       ├── GC08A8.yaml                # GC08A (8MP)
│       ├── IMX896-AJH5-C.yaml         # IMX896 (50MP)
│       └── OS08A10.yaml               # OS08A10
│
├── reference/                         # External data & feature specs
│   ├── INDEX.md                       # PRD index by version (4.1, 5.0) and feature group
│   ├── memory-mutex.json              # Memory rules (45 features × 9 scenarios) + mutual exclusion (20 rules)
│   ├── algorithms.md                  # Algorithm/capability descriptions
│   ├── filter.md / tuning.md          # Filter & tuning parameter docs
│   ├── photo.md / action.md           # Photo & action mode specs
│   ├── preset.md                      # Preset feature spec
│   ├── nps-*.json                     # NPS satisfaction data (base, pro, camera-detail, dimensions)
│   ├── gallery-feedback-*.json        # Gallery user feedback analysis
│   ├── {feature-group}/               # Structured feature PRDs (filter/, video/, ui/, preset/, etc.)
│   └── _raw/                          # Raw source PRDs (markdown, Chinese)
│
└── _output/                           # Auto-generated views (features.md, features.xlsx)
```

## Agent Standard Operating Procedure

### 1. When Writing a Camera PRD

1. **Load `feature-tree.md`** — determine which interaction zone the feature belongs to
2. **Load `features/rear-camera.json` and `front-camera.json`** — check what modes already support similar functions
3. **Load the target device file** (`knowledge/devices/{project}.yaml`) — understand hardware constraints
4. **Check `knowledge/reference/INDEX.md`** — find related PRDs for reference
5. **Use the `image-feature-prd-writer` skill** — it has the PRD template and required-info checklist
6. **Tag the feature with `purpose` from feature-tree.md** — enables cross-dimensional retrieval
7. **Define memory rules** — for any feature with user-modifiable state, fill all 9 standard scenarios (switch mode, switch camera, gallery, settings, kill 5min in/out, Home 5min in/out, secure camera). Reference: `knowledge/reference/memory-mutex.json`
8. **Define mutual exclusion** — list all conflicting features with resolution behavior, including basic/pro differences. Reference: `knowledge/reference/memory-mutex.json`

### 2. When Reviewing a Feature List

1. Load `features/rear-camera.json` + `features/front-camera.json`
2. Load project `devices/{project}.yaml` → per-camera capability baseline
3. Cross-reference sensor YAML `capability_summary` → detect sensor vs feature list gaps
4. **Flag these issues:**
   - ❌ Hardware-impossible features (sensor doesn't support it)
   - ⚠️ Missing features (sensor supports but feature list doesn't include)
   - ⚠️ Stale/abandoned entries
   - ℹ️ `[inferred]` values — no datasheet confirmation

### 3. When Checking Sensor Capability

Use the standardized labels from `knowledge/README.md`:
- `YES` / `NO` — confirmed
- `UNSUPPORTED — hardware limit` — physically impossible
- `SENSOR_CAPABLE_BUT_PLATFORM_LIMITED` — sensor OK but ISP/platform blocks it
- `SOFTWARE ONLY` — no hardware support, software simulation
- `[inferred]` — guessed, no datasheet proof

Every sensor YAML has a `capability_summary` with standardized fields:
`4k_30fps`, `4k_60fps`, `1080p_60fps`, `1080p_120fps`, `1080p_240fps`, `hdr_photo`, `hdr_video`, `pdaf`, `ois`

## Device Naming Conventions

- **Project code**: 5-digit number (20111, 22111, 23111, 24121, 25131...)
- **Pokémon codename**: Internal codename (Abra, Alakazam, Arcanine, Beedrill, Bellsprout...)
- **Market name**: Nothing Phone (x) / CMF Phone (x)
- **SoC**: Qualcomm SMxxxx or MediaTek Dxxxx
- **Full mapping**: See `knowledge/devices/project-mapping.yaml`

## Available Skills

Skills in `skills/` directory provide specialized workflows:

| Skill | Purpose |
|-------|---------|
| `default-preset-manage` | Read/update/sync Camera Default Preset Bitable, manage covers & changelog |
| `image-feature-prd-writer` | Write camera/gallery PRDs using templates and required-info checklists |
| `camera-data-insight` | 相机数据洞察 — Athena SQL + remote SQLite 查询、业务报告、字段映射、数据保留规则 |
| `camera-tracking-manage` | Camera event tracking bitable management (Lark docs) |
| `gallery-event-tracking` | Gallery event tracking patterns |
| `jira-automation` | Jira ticket automation via CLI |
| `google-play-whats-new` | Google Play "What's New" release note generation |
| `knowledge-base-manage` | Generate camera feature lists (parameterized by project), manage device configs, maintain sensor datasheets |

## Feature Tree Convention

The camera feature tree (`knowledge/feature-tree.md`) organizes all features by **interaction zone** (11 zones: 启动退出, 预览框, AE/AF, Zoom, Shutter, Top Toolbar, Mode Switch, Gallery, Preset, Settings, 系统级交互, 相册联动).

Each feature has a **`purpose` tag** for cross-dimensional retrieval:
- `拍摄` (capture), `拍摄辅助` (capture assist), `图像处理` (image processing)
- `硬件` (hardware), `算法` (algorithm), `ISP` (ISP)
- `个性化` (personalization), `品牌特性` (brand), `系统` (system)

When writing PRDs, always tag with the correct purpose from the tree.

## Important Conventions

- PRDs are in Chinese (markdown), stored in `knowledge/reference/_raw/prd/`
- Structured reference docs are in `knowledge/reference/{feature-group}/`
- Device configs use YAML for human readability, JSON for feature matrices
- Sensor datasheets follow a standard YAML schema with `capability_summary` for AI consumption
- Gallery feedback CSVs are gitignored (large files); analysis summaries are in JSON
- The `_output/` directory is auto-generated — don't edit manually
