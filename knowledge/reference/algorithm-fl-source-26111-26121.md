# 26111 / 26121 Algorithm FL Source

> Purpose: clean algorithm source for completing the 26111 and 26121 Camera Feature List.
> Raw OCR inputs:
> - `knowledge/reference/_raw/25111-影像软件设计方案-ocr.md`
> - `knowledge/reference/_raw/25131-算法链路-ocr.md`
> Current project HAL source:
> - `knowledge/reference/hal-26111-26121.md` (2026-07-13; overrides conflicting baseline inference)
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
| 拍照 | 实时算法 | 人脸清晰度增强 | Face Restoration Technology；有人脸时在拍照/夜景/人像/高像素链路叠加。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 有人脸场景出图；确认脸部细节增强 |
| 拍照 | 实时算法 | Photo EIS / PZL | 拍照高倍 zoom 稳定链路；PZL 是按下快门后再取帧的后取帧策略，区别于 ZSL。26111 Main 与 26121 Main/Tele 均有 OIS，Photo EIS 仍需验收裁切、稳定和时序。 | ✓ | [TBD] | ✗ | ✓ | [TBD] | ✓ | ✗ | 高倍手持拍摄；检查 OIS/EIS 叠加、取景稳定、裁切和后取帧时序 |
| 视频 | 实时算法 | Video EIS | 录像默认普通防抖。26111 Main 与 26121 Main/Tele 可与 OIS 叠加。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1080P30 手持录制；确认稳定、视角裁切和 OIS/EIS 叠加 |
| 拍照/视频/夜景/延时 | 实时算法 | SAT / 平滑镜头切换 | 26111 HAL 为 2SAT，26121 为 SAT；两者均标注无 Fallback。具体模式、规格和镜头组合需要分别确认。 | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | 变焦跨镜头点；确认 SAT/硬切、亮度/色彩/视角过渡，并验证无 Fallback 时的近焦行为 |
| 人像 | 实时算法 | 人像 HDR | 虚化 + HDR + 美颜 + FRT 链路。 | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | 人像逆光场景；确认虚化和 HDR 同时稳定 |
| 人像/拍照/夜景 | 后处理算法 | 美颜 / 自然质感人像 | 用户触发且 FD 检测到人脸；5a P0 升级自然质感人像。 | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | 人脸场景开关美颜；检查自然质感效果 |
| 拍照/人像/夜景 | 后处理算法 | XDR / Ultra HDR | RAW 算法触发后叠加；人像模式可由用户触发。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 支持 Ultra HDR 的查看器中确认动态范围 |
| 高像素 | 后处理算法 | 高像素场景自适应链路 | 26111 Main 高像素通路已确认，产品选项以高像素 PRD 为准。26121 Main/Tele 按场景选择 50MP 直出+MMF，或 12.5MP binning 后叠加 TF MMF/HDR/SN 再 upscale 到 50MP。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 分亮度和动态范围拍摄，确认实际链路、输出分辨率、耗时、内存和产品选项映射 |
| 拍照 | 后处理算法 | AI Zoom / AIGC SR | 两项目 HAL 都保留评估项，尚未形成最终量产结论。26111 重点评估 6GB 内存/性能和外部算法数据；26121 替代方案也待定。 | [TBD] | ✗ | ✗ | ✗ | ✗ | [TBD] | ✗ | 高倍场景确认最终算法、入口、触发倍率、内存、性能与伪影；未确认前不得标为已支持 |
| 拍照 | 实时算法 | ISZ / In Sensor Zoom | 26111 Main 亮度满足时在 2x 切换 in-sensor zoom setting，SM7635 非 seamless；26121 Main/Tele 支持，UW 不使用 ISZ。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 2x/3.5x/高倍 zoom；确认 sensor setting 切换、非 seamless 过渡和成片输入 |
| 拍照 | 实时算法 | 运动抓拍 | 5a P0 新增；HDR 运动场景升级、影调升级、智能分区。 | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | 运动场景自动提升快门；检查普通模式引导入口 |
| 视频 | 实时算法 | Video HDR 算法 | HAL 证明两项目存在 HLG、normal/stagger sensor mode 与 HDR10+ 输出通路，但没有给出逐镜头 Video HDR 算法启用矩阵。 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | 按规格和摄像头确认 sensor mode、HDR 编码、动态范围、功耗和产品入口 |
| 视频 | 实时算法 | 视频夜景 | 高通夜景/平台降噪链路。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 暗光录像；确认噪声和帧率稳定 |
| 视频 | 实时算法 | HLG / HDR 规格 | 26111 HAL 覆盖 1080P30/4K30，1080P60 不支持 HLG；26121 HAL 覆盖 1080P30/60 与 4K30/60。当前证据未按摄像头拆分。 | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | 按摄像头和规格确认 HLG 入口、sensor mode、编码、屏幕提亮、温升和稳定性 |

## Function Rows With Algorithm Dependency

These are user-visible features (`一级分类 = 功能`) that should stay in the project FL but should link back to the algorithm rows above.

| 模式 | 二级分类 | 名称 | 说明 | 26111 | 26121 | 验证方法 |
|---|---|---|---|---|---|---|
| 视频 | Mode Switch | 双摄同录 v2 | 基线来自 25131 前后双录；5a 支持前后摄通路，具体规格待单独 PRD 定义。 | ✓ | ✓ | 1080P30 前后摄同录；确认布局、单文件、DUAL tag |
| 视频 | Mode Switch | 录制中前后镜头切换 | 5a P0 差异化录像能力；不是普通快门区域的前后摄像头翻转按键，只有录制中不中断切换时才写入 FL。 | ✓ | ✓ | 录制中切换前后镜头；确认不中断录制 |
| 视频 | 视频规格 | 4K 60FPS | 26111 不支持；26121 HAL 确认项目级 4K60 通路，但没有给出逐镜头产品范围。 | ✗ | ✓ | 26121 按 Main/UW/Tele/Front 逐列确认入口、录制、功耗、温升和稳定性 |
| 视频 | 视频规格 | 1080P 60FPS | 两项目 HAL 均支持项目级通路；26111 在 HLG ON 时不支持 1080P60。 | ✓ | ✓ | 按 Main/UW/Tele/Front 逐列确认，不能从项目级能力直接全选 |
| 视频 | 视频规格 | 4K 30FPS | 两项目 HAL 均支持项目级通路。 | ✓ | ✓ | 按 Main/UW/Tele/Front 逐列确认 |
| 慢动作 | 慢动作规格 | 1080P 120FPS | HAL 明确 Wide/Main 单摄 1x-2x。 | ✓ | ✓ | Main 可确认；UW/Tele/Front 不从旧项目推断 |
| 延时摄影 | 视频规格 | 4K 30FPS | HAL 明确 Wide/Main 单摄 1x-8x。 | ✓ | ✓ | Main 可确认；UW/Tele/Front 不从旧项目推断 |
| 视频 | 视频规格 | 前置 1080P 60FPS | HAL 前置视频模式明确 1080P30/60。 | ✓ | ✓ | Front 可确认；前置 4K 仍为 TBD |
| 专业 | Mode Switch | 专业模式 2.0 | 5a P0 新增；算法能力需要和 RAW/HDR/高像素互斥对齐。 | ✓ | ✓ | 专业模式参数、RAW、镜头入口 |
| 拍照 | Toolbar | 运动抓拍开关/入口 | 5a P0 新增，普通模式引导入口。 | ✓ | ✓ | Photo 模式入口可见；运动场景识别后策略生效 |

## Conflicts / SE Confirmation Needed

| Topic | Current evidence | FL action |
|---|---|---|
| SAT naming | `SAT` and `SAT / 平滑镜头切换` are the same capability. | Use one canonical row `SAT / 平滑镜头切换`; describe whether project zoom uses SAT smooth transition or hard cut in the `变焦` row. |
| 26111 ISZ | 2026-07-13 HAL 明确 Main 2x in-sensor zoom setting，且 SM7635 非 seamless。 | 26111 Main 标 `✓`；说明非 seamless，并把 4x remosaic/6GB 风险留作 TBD。 |
| 26111 slow motion | HAL 明确 Wide/Main 1080P120、1x-2x。 | 26111 Main 标 `✓`；其他摄像头不推断。 |
| 26111/26121 dual-view exact spec | 25131 PRD defines 1080P30; 5a notes say exact spec needs separate PRD. | Add feature rows, mark detailed spec as pending PRD. |
| Front 4K / HLG | HAL 只明确前置 1080P30/60；前置 HLG 写为按产品需求实现，没有前置 4K 通路。 | 前置 1080P60 可确认；前置 HLG/4K 保留 `[TBD]`。 |
| 26111 OIS | HAL 物料表明确 HP5 OIS，与旧算法说明冲突。 | Main OIS 标 `✓`，废弃“26111 无 OIS”说明。 |
| 26121 high resolution | HAL 为 Main/Tele 场景自适应 50MP 直出或 12.5MP+upscale，不是统一 remosaic。 | 更新高像素算法说明；产品选项名称继续以最新版 PRD 为准。 |
| AIGC high zoom | 两项目 HAL 均保留评估问号。 | 不把 AI Zoom/AIGC 算法写成已确认支持。 |

## Import Notes

- Split the combined table into two Bitable device tables:
  - 26111 columns: `模式`, `一级分类`, `二级分类`, `名称`, `说明`, `Main`, `UW`, `Front`, `验证方法`.
  - 26121 columns: `模式`, `一级分类`, `二级分类`, `名称`, `说明`, `Main`, `UW`, `Tele`, `Front`, `验证方法`.
- Preserve `[TBD]` in `说明` or `验证方法` if the select field only accepts `✓/✗`.
- Do not create placeholder Tele columns in 26111.
