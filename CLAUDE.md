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

### 2. When Creating a Requirement List

Use the **`requirement-list-creator` skill** — it covers the full workflow:

1. **Gather** from all sources (JIRA, Sheets, Bitables, chat)
2. **Normalize** names, descriptions, priorities, modules (from `feature-tree.md`)
3. **Create Bitable** in the correct wiki directory (e.g., Camera 5.0-NOS 5.0 for NOS 5.0)
4. **Link JIRA** — clone cross-project tickets, verify Device field
5. **Link PRDs** — cross-reference with wiki PRD directory
6. **Reverse Audit** — check all 8 required fields, output audit report

Required fields: 需求, 描述 (≥50 chars), 优先级, 模块 (from feature-tree), 来源, JIRA, PRD, 备注

### 3. When Reviewing a Feature List

1. Load `features/rear-camera.json` + `features/front-camera.json`
2. Load project `devices/{project}.yaml` → per-camera capability baseline
3. Cross-reference sensor YAML `capability_summary` → detect sensor vs feature list gaps
4. **Flag these issues:**
   - ❌ Hardware-impossible features (sensor doesn't support it)
   - ⚠️ Missing features (sensor supports but feature list doesn't include)
   - ⚠️ Stale/abandoned entries
   - ℹ️ `[inferred]` values — no datasheet confirmation

### 4. When Creating Gallery JIRA Tickets

1. **Create an Epic** for the version (e.g., "Nothing Gallery - 3.2") — `issuetype: 10000`, `component: NTGallery`, device `all_phones`
2. **Create Stories** under the Epic — `issuetype: 10007`, set `parent: {"key": "NOS-XXXXX"}`
3. **Write descriptions** in ADF format with Background + Feature Summary + PRD link
4. **Check for existing tickets** — search NOS before creating duplicates (e.g., Backup to Google Photos = NOS-6692 from 2025)
5. **Update Gallery weekly Bitable** — add/update records after JIRA changes

### 5. When Maintaining Gallery Weekly Bitable

The Gallery weekly Bitable (`ObiAby1DGaA7eEsVjU4lArSSgRf`, table `tblgO6TzGtoKTao8`) is the single source of truth for Gallery requirements.

Key fields: Title, PRD, Description, 发布版本, 需求状态, 需求优先级, JIRA.

- Add new records when new PRDs or JIRA tickets are created
- Update status when features move through the pipeline
- Sync JIRA links when tickets are created
- Remove or mark as cancelled features that are dropped

### 6. When Checking Sensor Capability

Use the standardized labels from `knowledge/README.md`:
- `YES` / `NO` — confirmed
- `UNSUPPORTED — hardware limit` — physically impossible
- `SENSOR_CAPABLE_BUT_PLATFORM_LIMITED` — sensor OK but ISP/platform blocks it
- `SOFTWARE ONLY` — no hardware support, software simulation
- `[inferred]` — guessed, no datasheet proof

Every sensor YAML has a `capability_summary` with standardized fields:
`4k_30fps`, `4k_60fps`, `1080p_60fps`, `1080p_120fps`, `1080p_240fps`, `hdr_photo`, `hdr_video`, `pdaf`, `ois`

## Version ↔ Project Mapping

| Project Code | Codename | Market Name | Camera Version | Wiki Directory |
|---|---|---|---|---|
| 26111 | Caterpie (Bellsprout) | Phone (5a) | 5.1 | Camera 5.1-26111 |
| 26121 | Caterpie Pro | Phone (5a) Pro | 5.1 | (same, reuses 25111 Pro camera) |
| 25131 | Blastoise Pro | Phone (4b) | 4.1 | Camera 4.1-25131 |
| 25111 | Bellsprout | Phone (4a) | 4.0 | Camera 4.0-25111 |
| 23112 | Arbok | Phone (3) | 3.5 | Camera 3.5-23112 |
| 24111 | Arcanine | Phone (3a) | 3.0 | Camera 3.0-24111&24121 |
| 24121 | Bulbasaur | CMF Phone 2 Pro | 3.0 | Camera 3.0-24111&24121 |
| 23111 | Aerodactyl | Phone (2a) | 3.5 | Camera 3.5-23112 |
| 23113 | Aerodactyl Plus | Phone (2a) Plus | 3.5 | Camera 3.5-23112 |

**JIRA device IDs** (for `customfield_10101`):
- 25111 → 11420, 25111 Pro → 11421
- 23112 → 10930 (verify)
- all_phones → 10957

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
| `requirement-list-creator` | Create standardized requirement Bitables: gather → normalize → link JIRA/PRD → reverse audit |
| `default-preset-manage` | Read/update/sync Camera Default Preset Bitable, manage covers & changelog |
| `image-feature-prd-writer` | Write camera/gallery PRDs using templates and required-info checklists |
| `camera-data-insight` | 相机数据洞察 — Athena SQL + remote SQLite 查询、业务报告、字段映射、数据保留规则 |
| `camera-tracking-manage` | Camera event tracking bitable management (Lark docs) |
| `gallery-event-tracking` | Gallery event tracking patterns |
| `jira-automation` | Jira ticket automation via CLI |
| `google-play-whats-new` | Google Play "What's New" release note generation |
| `feature-list-writer` | Create/maintain Camera Feature List Bitables — table schema, baseline population, hardware config, feature pruning, algorithm classification |
| `knowledge-base-manage` | Manage device configs, sensor datasheets, knowledge base consistency checks |

## Feature Tree Convention

The camera feature tree (`knowledge/feature-tree.md`) organizes all features by **interaction zone** (12 zones: 启动退出, 预览框, AE/AF, Zoom, 暂态开关, 快门区域, Top Toolbar, Mode Switch, Preset, Settings, 系统级交互, 相册联动).

Feature List generation rules:
- `快门区域` is documented for UI completeness but should not be expanded into FL rows. Shutter button, gallery thumbnail, and front/rear camera flip are default camera controls.
- KB is the function manual; final FL is the project capability matrix. In KB, `模式` is a mode scope such as `全部拍摄模式` or `照片 / 人像 / 视频`. In final FL, expand that scope into real mode rows and use `✓` / `✗` to show support differences.
- Do not use `通用` as a mode value by default. Preset and Settings can use `全部拍摄模式` in KB, then expand to actual modes in final FL unless a separate common-feature table is explicitly designed.
- Settings groups are General (Preset, Save location, Shutter sound, Mirror front camera, Level), Photo (Watermark, Auto Tone, Tap to take a photo, QR code scanner, Press and hold shutter, Ultra XDR), and Video (Video encoding H.264/H.265, Power saving recording, Auto FPS).
- Detailed rules: `knowledge/reference/feature-list-layout-common-rules.md`.
- Photo Top Toolbar rows follow `knowledge/reference/photo-top-toolbar-rules.md`: Flash, Timer, HDR, Exposure, Filter, Tuning, Motion Photo, Quality, Grid, Ratio, Watermark, More settings, Glyph Mirror, with `Motion Photo cover HDR` as the only default split-out sub-row.

Each feature has a **`purpose` tag** for cross-dimensional retrieval:
- `拍摄` (capture), `拍摄辅助` (capture assist), `图像处理` (image processing)
- `硬件` (hardware), `算法` (algorithm), `ISP` (ISP)
- `个性化` (personalization), `品牌特性` (brand), `系统` (system)

When writing PRDs, always tag with the correct purpose from the tree.

## JIRA Conventions

All Camera & Gallery tickets live in the **NOS** project (`https://nothingtech.atlassian.net`). Individual device projects (BELL, ARBOK, BLASTP, etc.) contain only bugs/defects.

| Field | Camera | Gallery |
|---|---|---|
| Project | NOS | NOS |
| Story (需求) | `issuetype: 10007` | `issuetype: 10007` |
| Epic (长篇故事) | `issuetype: 10000` | `issuetype: 10000` |
| Component | `Camera` | `NTGallery` |
| Device (`customfield_10101`) | Project-specific IDs | `all_phones` (10957) |
| SW Version (`customfield_10682`) | Version-specific | `不涉及` (11268) |
| Sprint (`customfield_10647`) | Sprint-specific | `不涉及` (11321) |

**JIRA API**: Use `POST /rest/api/3/search/jql` (the old `GET /rest/api/3/search` is deprecated). Descriptions require ADF format. `PUT /rest/api/3/issue/{key}` returns 204 on success.

**Gallery Epic parenting**: Stories use `"parent": {"key": "NOS-XXXXX"}` to nest under an Epic.

## Lark Wiki Space Structure

**Camera PRD Space** (`space_id: 7623306205619867360`):

```
Camera PRD/
├── Camera 5.1-26111          ← current
├── Camera 5.0-NOS 5.0
├── Camera 4.1-25131
├── Camera 4.0-25111
├── Camera 3.5-23112
├── Camera 3.0-24111&24121
├── Camera 2.5-phone2
└── WIP
```

**Gallery PRD Directory** (under same space, parent `WsWrwKB43iuujZkJgeMlBXFPgah`):

```
Gallery PRD/
├── Gallery v3.2               ← current (26111 target)
├── Gallery v3.1               ← Map Album only
├── Gallery v3.0
├── Gallery v2.9
├── Gallery IV / III
└── 其他                       ← older docs (e.g., Gallery V Backup)
```

## Key Lark Resources

| Resource | Token | Purpose |
|---|---|---|
| Gallery weekly Bitable | `ObiAby1DGaA7eEsVjU4lArSSgRf` | Gallery 需求看板 — single source of truth for all Gallery features |
| Camera tracking Bitable | `N2azb9muvaqqmwsIB7IlPmFGgpg` / table `tbl3eedJjHPyCEf3` | Camera 埋点 219 records |
| Gallery tracking Bitable | `WB4QbWtr2ajCGXsZucglh0DAgsh` / table `tbl4YaZDJ2Psv9ok` | Gallery 埋点 73 records |
| Default Preset Bitable | `TKuObORHDa0vNgs3gF9lsKdPgUg` / table `tblGPOTtAH66KGXN` | 12 default presets |
| 25111 Feature List | Sheet `Nh8Us6qyLhsC6Nt7QDPlEiQigTd` | 验收 checklist (verification, not requirement management) |
| 23112 Feature List | Sheet `ETm3s4VNrhRuYItPyG8utTPMsjg` | 验收 checklist |
| 25131 Feature List | Sheet `GDqusuZ32hH7T7tmqT5lwdergYb` | Embedded Bitable — limited API access |

## Device Compatibility Rules

### Fallback & Macro Control
- **Fallback** (AF automatically switches to ultrawide for close-ups) is only supported on **25111 (Phone 4a) and later**.
- **Macro Control switch** (NOS-9804) requires fallback support. Pre-25111 devices (23112, 24111, 24121, etc.) and 25131 do NOT support fallback and must NOT show the macro control toggle.
- **UI position**: Macro Control is a **左侧暂态开关** near the zoom bar. Night mode and AI Zoom are **右侧暂态开关**. Transient switches are independent interaction zones, not children of Zoom. See `knowledge/feature-tree.md` → 暂态开关.

### 26111 Camera Hardware
- **26111 Base (Phone 5a)**: SM7635 + 200MP HP5 main + 8MP IMX355 UW + 50MP JN5 tele (OIS)
- **26121 Pro (Phone 5a Pro)**: SM7750 + **IMX896** (reuses 25111 Pro camera config). No 200MP sensor.
- 200MP pipeline: 200MP sensor → HW Remosaic → 50MP RAW HDR → upscale. NOT direct 200MP output.
- 200MP only on 26111 Base (7635). 50MP on 7635 ≈ 7.4s processing time, ~1.75GB memory peak, ZSL impossible.

### 17C Upgrade Projects (Android 17 backport)
- Devices receiving 17C: 23112 (ARBOK17C), 23111 (AERO17C), 23113 (AEROP17C), 24111 (ARCA17C), 24121 (GALAGA17C)
- Fallback-dependent features (e.g., Macro Control) should NOT be backported to these projects.

## Important Conventions

- PRDs are in Chinese (markdown), stored in `knowledge/reference/_raw/prd/`
- Structured reference docs are in `knowledge/reference/{feature-group}/`
- Device configs use YAML for human readability, JSON for feature matrices
- Sensor datasheets follow a standard YAML schema with `capability_summary` for AI consumption
- Gallery feedback CSVs are gitignored (large files); analysis summaries are in JSON
- The `_output/` directory is auto-generated — don't edit manually
- **Gallery weekly Bitable** is the single source of truth for Gallery feature status. Keep it updated whenever JIRA tickets or PRDs change.
