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
| 拍照 | 后处理算法 | 多帧降噪 / MFNR | 通过多张短曝光帧对齐与融合降低随机噪声；主要用于 HDR 关闭或未进入 HDR / Super Night 的普通拍照链路，尤其是中低照静态场景，运动场景可能切换策略。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 覆盖正常光、中低照、HDR/夜景阈值和运动场景，结合算法 tag 确认 MFNR 生效区间、帧数、互斥关系、噪声、鬼影和耗时 |
| 夜景 | 实时算法 | TF SN / Super Night | 超级夜景，NZSL/ZSL 多帧链路；与 HDR 互斥。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | luxindex 进入夜景阈值后触发；确认 HDR 关闭 |
| 拍照 | 实时算法 | CFR / 紫边去除 | HDR 内生效；参考触发 lux < 250 且 HDR=True，退出 lux > 280 或 HDR=False。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 高反差边缘场景；验证进出平滑，无跳变 |
| 拍照 | 后处理算法 | 超分 / Super Resolution（SR） | 高倍率变焦或裁切拍照链路的超分辨率能力；YUV 4x、RAW 2x 仅作旧方案参考，当前项目核心待确认项是每个物理摄像头的实际生效焦段。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 在生效边界前一档、边界点和后一档拍摄并检查算法 tag，确认逐摄像头实际生效焦段、细节、伪影、耗时和功耗 |
| 拍照 | 后处理算法 | HDSR | HDR + SR 叠加链路，达到 SR 条件且 HDR 检测成立时触发。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 暗光长焦/高倍 zoom 场景；确认 HDR 与 SR 均生效 |
| 拍照/夜景/人像/高像素 | 后处理算法 | FRT / 人像清晰度提升 | Face Restoration Technology；独立的人脸细节恢复与清晰度增强能力，不等同于美颜。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 逐模式、摄像头和规格确认算法 tag；检查人脸细节、身份特征保持、伪影和过度锐化 |
| 拍照 | 实时算法 | Photo EIS | 拍照高倍 zoom 电子防抖能力，通过陀螺仪运动信息和画面裁切补偿手持抖动。26111 Main 与 26121 Main/Tele 均有 OIS，仍需验收 OIS/EIS 叠加、裁切和稳定性。 | ✓ | [TBD] | ✗ | ✓ | [TBD] | ✓ | ✗ | 高倍手持拍摄；检查 OIS/EIS 叠加、取景稳定、裁切和成片清晰度 |
| 视频 | 实时算法 | Video EIS | 录像默认普通防抖。26111 Main 与 26121 Main/Tele 可与 OIS 叠加。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1080P30 手持录制；确认稳定、视角裁切和 OIS/EIS 叠加 |
| 拍照/视频/夜景/延时 | 实时算法 | SAT / 平滑镜头切换 | 26111 HAL 为 2SAT，26121 为 SAT；两者均标注无 Fallback。具体模式、规格和镜头组合需要分别确认。 | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | 变焦跨镜头点；确认 SAT/硬切、亮度/色彩/视角过渡，并验证无 Fallback 时的近焦行为 |
| 人像 | 实时算法 | 人像 HDR | 虚化 + HDR + 美颜 + FRT 链路。 | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | 人像逆光场景；确认虚化和 HDR 同时稳定 |
| 拍照/人像 | 后处理算法 | 美颜算法 / Beauty Algorithm | 独立的美颜后处理算法；本期仅 Front 支持，包含现有参数优化以及匀肤、肤色/性别/年龄分层和脸型流畅。 | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✓ | Front 人脸场景验证 Natural/Strong、参数与效果升级、多肤色/性别/年龄适配及中性回退 |
| 拍照/人像/夜景 | 后处理算法 | Ultra HDR | 支持 Google 通用 Ultra HDR 照片格式编码，输出兼容 SDR 的基础图像和 HDR gain map / 元数据。 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 检查文件编码和 gain map / 元数据，并在支持 Ultra HDR 与仅支持 SDR 的查看器中验证显示兼容性 |
| 高像素 | 后处理算法 | 高像素场景自适应链路 | 26111 Main 高像素通路已确认，产品选项以高像素 PRD 为准。26121 Main/Tele 按场景选择 50MP 直出+MMF，或 12.5MP binning 后叠加 TF MMF/HDR/SN 再 upscale 到 50MP。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 分亮度和动态范围拍摄，确认实际链路、输出分辨率、耗时、内存和产品选项映射 |
| 拍照 | 后处理算法 | AI Zoom / AIGC SR | 两项目 HAL 都保留评估项，尚未形成最终量产结论。26111 重点评估 6GB 内存/性能和外部算法数据；26121 替代方案也待定。 | [TBD] | ✗ | ✗ | ✗ | ✗ | [TBD] | ✗ | 高倍场景确认最终算法、入口、触发倍率、内存、性能与伪影；未确认前不得标为已支持 |
| 拍照 | 实时算法 | ISZ / In Sensor Zoom | 26111 Main 亮度满足时在 2x 切换 in-sensor zoom setting，SM7635 非 seamless；26121 Main/Tele 支持，UW 不使用 ISZ。 | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 2x/3.5x/高倍 zoom；确认 sensor setting 切换、非 seamless 过渡和成片输入 |
| 拍照 | 实时算法 | 运动抓拍 | 5a P0 新增；HDR 运动场景升级、影调升级、智能分区。 | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | 运动场景自动提升快门；检查普通模式引导入口 |
| 视频 | 实时算法 | Video HDR 算法 | 视频录制时通过 Sensor HDR 曝光/读出模式与 ISP/算法处理扩展动态范围，保留高光和暗部细节，并按支持的 HDR 格式编码输出。当前项目范围：26111 不支持；26121 支持 Main/Tele，不支持 UW/Front。需逐摄像头确认分辨率/帧率、Sensor mode、输出格式，以及与 EIS、变焦、风格/LUT、Log 的兼容关系和功耗温升。 | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | 对支持摄像头逐项验证 1080P30/60、4K30/60，确认 Sensor mode、HDR 编码/元数据、动态范围、EIS/变焦/风格/Log 互斥以及功耗温升；不支持摄像头确认入口不可用 |
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
| Video ISZ | 2026-07-14 项目口径确认 26111 / 26121 视频模式均不支持 In-Sensor Zoom，原因是切换 ISZ setting 会造成录像效果跳变并增加功耗。 | 两项目视频模式的 `ISZ / In Sensor Zoom` 行所有摄像头均标 `✗`；不支持原因填写效果跳变与功耗问题；照片 ISZ 行保持独立判断。 |
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
