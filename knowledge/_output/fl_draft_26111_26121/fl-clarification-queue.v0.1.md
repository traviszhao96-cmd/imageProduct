# 26111 / 26121 FL 澄清清单 v0.1

> Source: local FL draft v0.2, KB v6 audit, Travis clarification on 2026-07-08.
> Purpose: separate resolved taxonomy decisions from remaining PM / SE / QA fill-in items before final FL sync.

## Snapshot

| Area | 26111 | 26121 | Meaning |
|---|---:|---:|---|
| FL rows | 218 | 235 | Current generated distribution draft rows |
| `状态=待确认` | 95 | 102 | Need PM/SE/QA decision or generator rule |
| Rows containing TBD/review signal | 95 | 103 | Includes unresolved support marks |
| Weak or missing `说明` rows | 31 | 47 | Mostly inherited manual FL rows; not always real product uncertainty |
| KB rows | 55 | 55 | Canonical function / algorithm manual |
| KB definition TODO | 1 | 1 | `锁定镜头` inheritance |

## Resolved In This Pass

| Topic | Decision |
|---|---|
| 普通场景检测 | Removed as a standalone canonical row. It is basic brightness/DRC/motion judgement and overlaps with many algorithms. |
| AI 场景检测 | Canonical name is `ASD / AI场景检测`; it means AI-model semantic scene detection such as green plants, stage and outdoor sky. |
| 运动检测 | Removed as a standalone canonical row when it only means basic scene judgement; keep explicit user-facing rows such as `运动场景引导`. |
| 200MP / 高像素 | Split into concrete mode options. 26111: `50MP`, `200MP`, `200MP Ultra`; 26121: `50MP`, `50MP Ultra`. Ultra means RAW HDR after remosaic. |
| SAT / 平滑镜头切换 | `SAT` and `SAT / 平滑镜头切换` are the same function. Support matrix is rear cameras ✓, front ✗. `变焦` description must state SAT smooth switch vs hard cut vs digital zoom. |
| EIS / PZL / Video EIS | Split into `Photo EIS / PZL` and `Video EIS`. PZL is post-shutter frame capture; ZSL is zero-shutter-lag pre-buffer capture. |
| 视频防抖开关 | Settings item under `通用 / Common` → `设置 / Settings` → `视频设置 / Video Settings`; it controls Video EIS availability. |
| Video specs | Expanded into 8 rows: 1080P/4K x 30/60FPS plus HLG variants. Front 4K is represented by front camera support on concrete rows. |
| Slow motion specs | Expanded into 6 rows: `1080P 30FPS`, `1080P 120FPS`, `1080P 240FPS`, `720P 120FPS`, `720P 240FPS`, `720P 480FPS`. |
| Dual View Video v2 | Split into preview rows for rear lens choice and main/sub window interaction, plus common Settings row `前后双录分开保存`. Removed vague `4K evaluation` wording. |
| Log 视频 | Moved to `视频 / Video` → `功能 / Feature` → `工具栏 / Toolbar`; support spec range still needs SE/PM confirmation. |
| Similar names | `镜头畸变矫正` / `光学畸变矫正` normalized to `光学畸变矫正`; `人脸畸变矫正` remains separate. `FRT` normalized into `人脸清晰度增强`. |

## P0 - Still Blocking Final Sign-Off

| Item | Current issue | Owner | Decision needed |
|---|---|---|---|
| Video spec matrix | 8 concrete rows exist, but some UW / Front / HLG cells remain TBD. | platform + imaging SE | Confirm each camera/spec/HLG support cell. |
| Slow motion spec matrix | 6 concrete rows exist, but support cells are intentionally TBD until the exact project spec is confirmed. | PM + imaging SE + QA | Fill supported slow-motion specs by camera. |
| Log 视频 | Row is in Video Toolbar, but supported resolution/fps/lens/encoding range is still unknown. | PM + imaging SE + platform | Decide final support and spec restrictions. |
| ISZ / In Sensor Zoom | Meaning is clear, but exact points by project/mode/camera still need confirmation. | imaging SE + platform | Confirm ISZ points and interaction with EIS/SR/video zoom. |
| 锁定镜头 | KB audit still flags whether 26111/26121 inherit this baseline setting. | PM + SE | Confirm inherit / not inherit, and affected video modes. |

## P1 - Meaning Clear, Support Or Copy Still Needs Cleanup

| Group | Current reading | Needed cleanup |
|---|---|---|
| Dirty lens / AI de-oil | `脏污检测` is baseline detection; `镜头脏污专项 / AI 去油污` is a new interaction/repair capability for Photo and Portrait. | Decide whether final FL needs one row or split detection / prompt / AI repair rows. |
| Face stack | `人脸检测`, `人脸清晰度增强`, `人脸畸变矫正`, `美颜 / 自然质感人像` are separate layers. | Fill mode/camera scope and remove inherited duplicates with empty copy. |
| HDR / XDR | Toolbar HDR, Ultra XDR setting, HLG video specs, Motion Photo cover HDR and RAW HDR are different layers. | Keep rows separated by layer and fill missing support reasons. |
| Night stack | 自动夜景 transient switch, 超级夜景 algorithm, 极夜 branch and 夜景+美颜 chain are different layers. | Normalize inherited Night rows and remove all-✗ legacy noise if not acceptance-relevant. |
| Style / tuning / filter | `Tuning` includes Tuning Palette / Palette Mode / Parameter Mode; `Photo Style` is Natural/Vivid ISP style; `Filter` remains LUT/filter. | Do not generate `Style / Tuning Palette / Palette-Parameters` as a separate row unless PM confirms a new Style entry. |
| Motion Photo | `Motion Photo`, `Motion Photo cover HDR`, `动态照片 - 无效信息截取` may need independent QA rows. | Confirm whether audio recording and invalid clip trimming require separate acceptance. |
| Common Settings copy | Structure is fixed under Common, but several inherited rows have thin descriptions. | Polish descriptions and validation method before Lark sync. |

## P2 - Generator Cleanup, Not Product Unknown

| Item | Why |
|---|---|
| OIS | Can be derived from hardware: 26111 none; 26121 Main/Tele. |
| Glyph Mirror | Hardware-dependent on large Glyph hardware; likely auto-fill `✗` for 26111/26121 if no required hardware. |
| Basic toolbar rows | Grid / More settings / Watermark / Ratio are known concepts; missing support is baseline mapping. |
| AF/AE | Meaning is clear; should use broad baseline rule with fixed-focus exceptions. |
| Unsupported reasons | Many `✗` cells now have draft reasons; audit should keep improving reasons that are still generic. |

## Suggested Next Step

1. PM + SE fill the P0 matrices: video specs, slow-motion specs, Log video, ISZ, lock-lens inheritance.
2. Run generator again and review only rows still marked `TBD`.
3. Sync 26111 and 26121 to Bitable after disputed rows are either resolved or intentionally kept as distribution-draft `TBD`.
