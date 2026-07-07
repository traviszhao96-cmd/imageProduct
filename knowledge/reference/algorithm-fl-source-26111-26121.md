# 26111 / 26121 Algorithm FL Source

> Purpose: clean algorithm source for completing the 26111 and 26121 Camera Feature List.
> Raw OCR inputs:
> - `knowledge/reference/_raw/25111-影像软件设计方案-ocr.md`
> - `knowledge/reference/_raw/25131-算法链路-ocr.md`
> Existing normalized references:
> - `knowledge/reference/algorithms-5a.md`
> - `knowledge/reference/algorithms.md`

## Project Mapping

| Project | Device | Baseline | Camera columns for FL |
|---|---|---|---|
| 26111 | Phone 5a Base | 25131 + 5a P0 deltas | Main / UW / Front |
| 26121 | Phone 5a Pro | 25111 Pro + 5a P0 deltas | Main / UW / Tele / Front |

## Algorithm Rows For FL

Use these rows as `一级分类 = 基础算法`. `✓` means supported by the project FL camera column; `✗` means not supported or not applicable. `[TBD]` means the row should be created but left for SE confirmation before final sign-off.

| 模式 | 二级分类 | 名称 | 说明 | 26111 Main | 26111 UW | 26111 Front | 26121 Main | 26121 UW | 26121 Tele | 26121 Front | 验证方法 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 拍照 | 实时算法 | Raw HDR / TF HDR | RAW 域 HDR，多帧合成；与夜景通过 luxindex 阈值切分。主摄/前置参考 lux < 320，超广角参考 lux < 300。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 暗光 HDR 场景触发；确认不与夜景同时触发 |
| 拍照 | 实时算法 | MFNR | 多帧降噪，普通低照场景走轻量化 MFNR。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 低照非夜景场景出图；检查噪声和帧合成耗时 |
| 夜景 | 实时算法 | TF SN / Super Night | 超级夜景，NZSL/ZSL 多帧链路；与 HDR 互斥。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | luxindex 进入夜景阈值后触发；确认 HDR 关闭 |
| 拍照 | 实时算法 | CFR / 紫边去除 | HDR 内生效；参考触发 lux < 250 且 HDR=True，退出 lux > 280 或 HDR=False。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 高反差边缘场景；验证进出平滑，无跳变 |
| 拍照 | 后处理算法 | SR / Super Resolution | Zoom 超分；YUV 方案参考 zoom >= 4x，RAW 方案参考 zoom >= 2x。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 2x/4x 以上拍照出图；检查细节提升和耗时 |
| 拍照 | 后处理算法 | HDSR | HDR + SR 叠加链路，达到 SR 条件且 HDR 检测成立时触发。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 暗光长焦/高倍 zoom 场景；确认 HDR 与 SR 均生效 |
| 拍照 | 实时算法 | FRT / 人脸清晰度增强 | Face Restoration Technology；有人脸时在拍照/夜景/人像/高像素链路叠加。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 有人脸场景出图；确认脸部细节增强 |
| 拍照 | 实时算法 | EIS / PZS | 拍照高倍 zoom 稳定链路；参考 PZS zoom >= 4x。26111 主摄无 OIS，依赖 EIS/裁切空间。 | ✓ | [TBD] | ✗ | ✓ | [TBD] | ✓ | ✗ | 高倍手持拍摄；检查取景稳定和裁切 |
| 视频 | 实时算法 | Video EIS | 录像默认普通防抖。26121 可与 OIS 叠加；26111 无 OIS。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1080P30 手持录制；确认稳定与视角裁切 |
| 拍照/视频/夜景/延时 | 实时算法 | SAT / 平滑镜头切换 | 多摄平滑切换。26121 主摄/长焦支持；26111 是否支持 Main-UW SAT 当前资料冲突，需 SE 确认。 | [TBD] | [TBD] | ✗ | ✓ | [TBD] | ✓ | ✗ | 变焦跨镜头点；确认亮度/色彩/视角过渡 |
| 人像 | 实时算法 | 人像 HDR | 虚化 + HDR + 美颜 + FRT 链路。 | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | 人像逆光场景；确认虚化和 HDR 同时稳定 |
| 人像/拍照/夜景 | 后处理算法 | 美颜 / 自然质感人像 | 用户触发且 FD 检测到人脸；5a P0 升级自然质感人像。 | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | 人脸场景开关美颜；检查自然质感效果 |
| 拍照/人像/夜景 | 后处理算法 | XDR / Ultra HDR | RAW 算法触发后叠加；人像模式可由用户触发。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 支持 Ultra HDR 的查看器中确认动态范围 |
| 高像素 | 后处理算法 | HW Remosaic | 26111 为 200MP HP5；26121 为 50MP IMX896/JN5 方案。参考高像素 lux < 200；仅叠加滤镜/CFR/FRT。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 高像素模式出图；确认分辨率、耗时、内存 |
| 拍照 | 后处理算法 | AIGC SR / Hyper Zoom | 26121 Tele 高倍 zoom 方案；26111 Base 不支持。 | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | Tele 30x+ 场景；确认 AIGC SR 入口和成片 |
| 拍照 | 实时算法 | ISZ / In Sensor Zoom | 26121 继承 25111 Pro；26111 HP5 裁切空间大但资料仍标注待确认。 | [TBD] | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 2x/3.5x/高倍 zoom；确认是否使用 sensor crop |
| 拍照 | 实时算法 | 运动抓拍 | 5a P0 新增；HDR 运动场景升级、影调升级、智能分区。 | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | 运动场景自动提升快门；检查普通模式引导入口 |
| 视频 | 实时算法 | Video HDR 算法 | 26111 SM7635 不支持；26121 继承 25111 Pro，主摄/长焦支持。 | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | Video HDR 场景录制；检查动态范围和功耗 |
| 视频 | 实时算法 | 视频夜景 | 高通夜景/平台降噪链路。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 暗光录像；确认噪声和帧率稳定 |
| 视频 | 实时算法 | HLG / HDR 规格 | 26111 参考 1080P30；26121 支持 1080P30/60 + 4K30。 | ✓ | ✓ | [TBD] | ✓ | ✓ | ✓ | [TBD] | 开启 HDR 规格录制；确认编码和屏幕提亮 |

## Function Rows With Algorithm Dependency

These are user-visible features (`一级分类 = 功能`) that should stay in the project FL but should link back to the algorithm rows above.

| 模式 | 二级分类 | 名称 | 说明 | 26111 | 26121 | 验证方法 |
|---|---|---|---|---|---|---|
| 视频 | Mode Switch | 双摄同录 v2 | 基线来自 25131 前后双录；5a 支持前后摄通路，具体规格待单独 PRD 定义。 | ✓ | ✓ | 1080P30 前后摄同录；确认布局、单文件、DUAL tag |
| 视频 | Mode Switch | 录制中前后镜头切换 | 5a P0 差异化录像能力；不是普通快门区域的前后摄像头翻转按键，只有录制中不中断切换时才写入 FL。 | ✓ | ✓ | 录制中切换前后镜头；确认不中断录制 |
| 视频 | Settings | 4K 60FPS | Base 不支持；Pro 按当前 `devices/26111.yaml` 标注为 Pro SAT / Ultra 主摄&长焦。 | ✗ | ✓ | 26121 主摄/长焦 4K60 入口和录制 |
| 专业 | Mode Switch | 专业模式 2.0 | 5a P0 新增；算法能力需要和 RAW/HDR/高像素互斥对齐。 | ✓ | ✓ | 专业模式参数、RAW、镜头入口 |
| 拍照 | Top Toolbar | 运动抓拍开关/入口 | 5a P0 新增，普通模式引导入口。 | ✓ | ✓ | Photo 模式入口可见；运动检测后策略生效 |

## Conflicts / SE Confirmation Needed

| Topic | Current evidence | FL action |
|---|---|---|
| 26111 SAT | `knowledge/reference/algorithms-5a.md` says 26111 SAT is not supported; generated `knowledge/_output/features-26111.md` still has SAT inherited on Main/UW in some rows. | Keep SAT rows as `[TBD]` for 26111, do not mark final `✓` until SE confirms Main-UW SAT behavior. |
| 26111 ISZ | HP5 200MP has crop potential, but existing reference marks ISZ as TBD. | Keep ISZ row `[TBD]` for 26111 Main. |
| 26111 slow motion | Existing reference says 25111 Basic does not support and 26111 is TBD. | Do not add final slow-motion algorithm rows until SE confirms. |
| 26111/26121 dual-view exact spec | 25131 PRD defines 1080P30; 5a notes say exact spec needs separate PRD. | Add feature rows, mark detailed spec as pending PRD. |
| Front 4K / HLG | `devices/26111.yaml` lists front 4K upscale as P0, but exact algorithm/spec is not in the PDFs. | Keep as feature/P0 row elsewhere; do not infer algorithm support beyond `[TBD]`. |

## Import Notes

- Split the combined table into two Bitable device tables:
  - 26111 columns: `模式`, `一级分类`, `二级分类`, `名称`, `说明`, `Main`, `UW`, `Front`, `验证方法`.
  - 26121 columns: `模式`, `一级分类`, `二级分类`, `名称`, `说明`, `Main`, `UW`, `Tele`, `Front`, `验证方法`.
- Preserve `[TBD]` in `说明` or `验证方法` if the select field only accepts `✓/✗`.
- Do not create placeholder Tele columns in 26111.
