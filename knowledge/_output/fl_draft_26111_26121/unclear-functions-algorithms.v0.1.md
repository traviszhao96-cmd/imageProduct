# 26111 / 26121 当前不清楚的功能与算法清单 v0.1

> Source snapshot: local FL draft v0.2, KB audit v6, Tree+KB integration candidates v1.
> Purpose: collect the items that still need PM / imaging SE / platform / QA judgement before the 26111 and 26121 FL can become a final acceptance checklist.

## Summary

| Area | Current signal |
|---|---|
| FL rows still marked `待确认` | 26111: 118 rows; 26121: 123 rows |
| Unique unclear names after mode aggregation | 26111: 51; 26121: 52 |
| Tree+KB integration candidates needing decision | Medium dispute: 14; High dispute: 3 |
| KB definition issues | 2 explicit issues: `普通场景检测` vs `AI场景检测` boundary |

This list is intentionally aggregated by function / algorithm name. It does not repeat every mode row from the FL.

## P0 - Blocks Final Support Matrix

| Item | Type | Projects / scope | What is unclear | Suggested owner | Suggested decision |
|---|---|---|---|---|---|
| 高像素 / 200MP / HW Remosaic / RAW HDR / AI Upscale | Feature + algorithm chain | 26111 mainly; 26121 not involved by current sensor plan | Whether 26111 should mark 200MP as supported, risk-only, or reference-only. Latest doc describes 200MP sensor -> HW Remosaic -> 50MP RAW HDR -> AI Upscale -> 200MP, with 7635 time / memory / NZSL risk and algorithm supplier still TBD. | PM + imaging SE + platform | Decide FL state for 26111 200MP: `✓`, `TBD`, `Pending`, or remove from delivery FL. |
| SAT / 平滑镜头切换 | Algorithm + Zoom feature | 26111 Main/UW; 26121 UW mostly | Local sources conflict: one source says 26111 SAT not supported, inherited FL rows still imply Main/UW support. 26121 Main/Tele clearer, UW still uncertain. | Imaging SE | Confirm per project/camera/mode SAT support and whether UI `SAT` feature row should mirror algorithm row. |
| ISZ / In Sensor Zoom | Algorithm + Zoom feature | 26111 Main, video ISZ; 26121 video scope | 26111 HP5 has crop potential, but references still mark ISZ as TBD. Video ISZ also needs EIS stack order and spec/mode coverage confirmation. | Imaging SE + platform | Confirm ISZ points by camera and mode; define interaction with EIS and high zoom enhancement. |
| 前置 4K / Front 4K | Video spec + algorithm dependencies | 26111 / 26121 Front | FL now maps this to `4K 30FPS`, but HLG, Beauty, Base encoding capability, EIS quality impact, long-recording throttling and user prompts remain unclear. | Platform + imaging SE + PM | Confirm front 4K capability matrix and mutual exclusions; keep broad `前置 4K 视频` out of FL. |
| 视频规格 UW rows | Video spec | 26111 UW 4K30; 26121 UW 1080P60 / 4K30 | Current generated rows keep these as `TBD`; sources do not clearly say whether ultra-wide supports these specs. | Platform + imaging SE | Fill UW support for each concrete spec row. |
| HLG / HDR 规格 | Video algorithm / spec | Video; especially Front | HLG/HDR support for front 4K remains pending; front column is still TBD in algorithm source. | Imaging SE + platform | Confirm supported resolution/fps/camera combinations and encoding path. |
| EIS / PZS / video stabilization | Realtime algorithm | Photo/video/night/slow motion/timelapse; high zoom | Current rows still use broad `TBD`. Support depends on mode, lens, zoom ratio and video spec; 4x rule is not reliable across hardware. | Imaging SE | Replace broad rule with per project/camera/mode/spec support table. |
| OIS | Hardware-derived realtime capability | All cameras | Current FL draft leaves OIS as TBD in places, but this should mostly be derived from hardware config. 26111 has no OIS cameras; 26121 Main/Tele have OIS. | Imaging SE / generator owner | Auto-fill from hardware config and remove unnecessary TBD rows. |
| Slow motion | Mode / algorithm support | 26111 especially | Existing algorithm source says 25111 Basic does not support and 26111 is TBD; current FL still has slow-motion mode rows. | PM + imaging SE | Decide whether slow motion is in 26111 scope, and which cameras/specs support it. |
| 前后双录 v2 | Video mode feature | 26111 / 26121 | 4K dual-view was crossed out in one place but still appears as evaluation in embedded tables; split-save, rear lens choice, Pro tele support, filter/Tuning mutual exclusions and performance risk need final decision. | PM + platform + QA | Confirm exact dual-view spec and whether 4K is `TBD`, `✗`, or not in FL. |
| Log 视频 | Video feature / algorithm | 26121 candidate | Current source is an evaluation document, not final PRD. Needs Nothing Log curve, restore LUT, 10-bit recording capability and entry definition. | PM + imaging SE + platform | Decide whether it enters canonical KB/FL now, stays candidate, or is Pending. |

## P1 - Function Definition Or Tree / KB Ownership Is Unclear

| Item | Type | Projects / modes | What is unclear | Suggested owner | Suggested decision |
|---|---|---|---|---|---|
| 普通场景检测 vs AI场景检测 | KB definition | All projects / many modes | KB audit explicitly says their boundary is undefined. Current FL expands both across many modes, creating duplicated unclear rows. | PM + imaging SE | Define difference: normal scene tag / ISP trigger vs AI semantic scene recognition, or merge one into the other. |
| AI场景检测 support scope | Preview feature / algorithm | Many modes and cameras | Support is still TBD across modes. Need to know whether it is a real user-facing preview function in each mode or only an algorithm trigger. | Imaging SE + PM | Confirm mode scope and whether FL should expose it as feature, algorithm, or both. |
| 人脸检测 / 人脸清晰度增强 / 人脸畸变矫正 | Preview + post algorithm | Photo/Portrait/Night/Video etc. | Face detection is broad and likely supported, but exact mode/camera scope and linkage to enhancement/distortion correction are not clearly separated. | Imaging SE | Split detection, enhancement and distortion correction support by mode/camera. |
| 脏污检测 vs 镜头脏污检测 / AI 去油污 / 提示引导 | Preview feature + AI repair | Photo and Portrait by PM correction | Need final scope: detection only, AI repair, prompt interaction, and whether UW/Tele support should be `✗` or `TBD`. Hardware coating/accessory items should stay out of Camera FL. | PM + imaging SE | Confirm FL rows and per-camera support; keep this as a new Camera feature only for in-app detection/repair/prompt. |
| Tuning / Tuning Palette | Toolbar feature | Photo/Portrait/Video baseline; Night/Expert/High-res scope needs confirmation | Tuning Palette is not a new FL row. It updates the existing `Tuning` row with Palette Mode, Parameter Mode, Strength and seven-parameter adjustment. Current PRD says Filter and Tuning do not merge in this phase. | PM + Tuning/ISP | Keep one `Tuning` row; confirm exact supported modes and stacking order with Filter, Photo Style and Preset. |
| Photo Style | Toolbar feature + ISP tuning | Still-photo modes | Low-dispute to add as a separate Natural / Vivid ISP style row, but actual ISP parameters, HDR/night interaction and EXIF/metadata are still TBD in PRD. | PM + ISP | Confirm exact mode scope and keep it separate from manual `Tuning`. |
| AI Preset 预览引导入口 / 场景推荐 | Preview feature / Preset relation | Common row currently, likely preview entry | Entry near Preset is confirmed, but coverage of all modes/focal lengths vs first-version scene range remains unclear. | PM | Decide scope and whether FL row belongs under Preview only, with Preset as applied result. |
| 视频曝光调节 / 视频白平衡调节 | Video toolbar feature | Video mode | Relationship with Lock White Balance is unclear; tree may need a Video Toolbar sub-area or reuse generic Toolbar. | PM + camera app + platform | Define entry, persistence, reset behavior and relation to settings. |
| 锁定白平衡 / 锁定镜头 / 视频防抖开关 | Settings features | Common / Video settings | Some rows are clear individually, but inheritance into 26111/26121 and relation to video toolbar controls still need source cleanup. | PM + QA | Decide whether these are 5.1 new needs, inherited baseline, or settings updates. |
| 录像中拍照（VSS）效果提升 | Video feature / shutter exception | Video mode | Should enter FL as an exception to "shutter area not listed", but MFNR, frame capture bias and filter retention are P1 / to-be-tested. | PM + imaging SE + QA | Keep as FL row, but decide exact acceptance criteria and support by spec/camera. |
| 人像模式 Consistent Zoom | Zoom feature + portrait algorithm | Portrait mode | Intermediate focal portrait pipeline, continuous bokeh curve and default focal memory need engineering/algorithm confirmation. | PM + imaging SE | Confirm camera/focal range support and whether unsupported focal segments should be visible in FL. |
| 普通照片模式运动场景引导 | Preview feature / motion detection | Photo only | Capsule display area, trigger threshold and focal range remain unclear. It should not appear in Front/Video/Portrait/Night/Action by current note. | PM + imaging SE | Confirm UI zone, trigger rules and supported cameras. |
| 二维码识别 / 识别框视觉动效 | Preview feature update | Photo | Current decision is "update existing behavior", not a new row. Need confirm if QR jump button on zoom bar creates a distinct acceptance row. | PM + QA | Decide update-only vs separate FL row for QR jump interaction. |
| 工具栏热区呼出 | Toolbar interaction | Common / design update | Mostly visual design; only the right-bottom hot zone may be a verifiable interaction. Need avoid adding shutter/default visual rows to FL. | PM + UX + QA | Decide FL inclusion: `reference_only`, `fl_only`, or canonical KB row. |

## P2 - Probably Clear Function, But Generator Still Needs Better Rules

| Item | Why it appears unclear now | Suggested action |
|---|---|---|
| Grid / More settings / Watermark / Ratio | Basic toolbar items show `TBD` because current generator lacks baseline support rules, not because the function meaning is unknown. | Auto-fill from baseline/manual FL; keep only real project exceptions as TBD. |
| Motion Photo / Motion Photo cover HDR | Motion Photo support differs by project/camera; cover HDR needs explicit confirmation. | Add project/camera rules from current manual FL or PRD, then keep cover HDR split only where needed. |
| Glyph Mirror | Should be hardware-dependent on large Glyph rear LED, but generator currently does not derive this cleanly. | Auto-fill `✗` for projects without required Glyph hardware; support only for known Glyph-capable devices. |
| 自动对焦-自动曝光 | Meaning is clear, but support is broad and every mode/camera remains TBD. | Use a baseline rule and only leave exceptions for modes where AF/AE behavior is genuinely different. |
| 变焦 | Meaning is clear, but exact default zoom points and lens switching support depend on hardware, ISZ and mode. | Generate from device camera config + mode rules instead of leaving all rows TBD. |
| Text Mode / 自动夜景 / 自动微距控制 | Functional meaning is mostly clear, but camera/mode trigger conditions and hardware dependencies need rules. | Link to transient switch rules and hardware fallback/macro/night scene conditions, then auto-fill obvious unsupported cameras. |

## High-Dispute Requirement Candidates

| ID | Requirement | Current recommendation |
|---|---|---|
| REQ26111-KB-005 | 相机设计改版 | Do not merge wholesale. Only consider right-bottom toolbar hot zone if it is a verifiable interaction. |
| REQ26111-KB-009 | 200MP 高像素 | Manual decision required before final FL. Major algorithm, time, memory and supplier risk. |
| REQ26111-KB-029 | Video Log | Keep candidate / Pending until final PRD and platform capability are confirmed. |

## Explicit KB Definition TODO

| KB item | Open question |
|---|---|
| 普通场景检测 | What is the boundary versus AI scene detection? Is it an internal algorithm trigger, a visible UI behavior, or both? |
| AI场景检测 | What exactly makes it AI scene detection in Camera FL? Which modes and cameras expose or depend on it? |

## Next Suggested Review Order

1. PM decides high-dispute features: 200MP, Video Log, design hot-zone inclusion.
2. Imaging SE confirms algorithm support matrix: SAT, ISZ, EIS/PZS, HLG/HDR, front 4K, slow motion.
3. PM + SE define ambiguous feature meaning: scene detection boundary, dirty lens / AI de-oil, Tuning / Filter / Photo Style stacking order, AI Preset.
4. Generator rules auto-fill obvious baseline items: OIS from hardware, Glyph Mirror from Glyph hardware, basic Toolbar support, AF/AE support.
