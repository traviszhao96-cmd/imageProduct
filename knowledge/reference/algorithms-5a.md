# 算法链路 - Phone (5a) 项目

> 项目: 26111 + 26121
> 最后更新: 2026-07-13
> 当前工程基线: [26111 / 26121 HAL 软件设计摘要](hal-26111-26121.md)
> FL 行级来源: [algorithm-fl-source-26111-26121.md](algorithm-fl-source-26111-26121.md)

## 证据优先级

1. 项目最新 PRD决定用户功能、入口、选项和产品裁剪。
2. 2026-07-13 HAL 设计决定项目通路、算法链路、规格上限和性能依赖。
3. 25111 / 25131 只作为未定义项的参考基线，不能覆盖项目 HAL 的明确结论。

## 1. 平台与硬件

| 维度 | 26111 | 26121 |
|---|---|---|
| SoC | SM7635 | SM7750 |
| 主摄 | 200MP HP5, OIS | 50MP IMX896, OIS |
| 超广角 | 8MP OV08J10 | 8MP IMX355 |
| 长焦 | 无 | 50MP JN5, OIS, 3.5x |
| 前置 | 32MP OV32D, FF | 32MP KD1, FF |
| 后置照片焦段 | 0.6x-40x, 2SAT | 0.6x-120x, SAT |
| 平台视频能力 | 4K30 | 4K60 |

旧版中“26111 HP5 无 OIS”“26111 不支持 4K/1080P60”“26121 不支持 4K60”“26111 不支持 SAT”的结论已被项目 HAL 推翻，不再使用。

## 2. 核心算法矩阵

| 算法/能力 | 26111 | 26121 | 当前边界 |
|---|---|---|---|
| TF HDR | 支持 | 支持 | 后置、前置与人像链路均有 HDR usecase；逐摄像头阈值由调试配置决定 |
| MFNR | 支持 | 支持 | 普通照片、前置、高像素和动态照片链路使用 |
| TF Super Night | 支持 | 支持 | 通常 NZSL 8 帧；26111 6GB 策略降为 7 帧 |
| SR | Main | Main + Tele | 26111 2x QBC RAW；4x 依赖 hex/4x4 RAW + 外部软件 remosaic |
| HDSR | 支持 | 支持 | HDR 与 SR 组合条件触发 |
| Motion Capture | 支持 | 支持 | HAL 后置照片独立 usecase；产品入口以 Action/运动抓拍 PRD 为准 |
| CFR / LDC / FRT | 链路包含 | 链路包含 | 是否在具体模式生效由算法条件和产品配置决定 |
| Photo EIS | 链路包含 | 链路包含 | 与 OIS/SAT/运动检测/畸变矫正的叠加顺序按 HAL 链路验收 |
| OIS | Main | Main + Tele | 26111 HP5 OIS 已由 HAL 物料表确认 |
| SAT | 2SAT | SAT | HAL 标注无 Fallback；模式范围和切换体验仍需逐项确认 |
| ISZ | Main 2x 通路 | Main + Tele | 26111 非 seamless；UW 不使用 ISZ |
| AIGC 高倍变焦 | 评估中 | 评估中 | 不得直接写成 FL 已确认；26111 重点是 6GB 内存/性能，26121 方案也未锁定 |
| 美颜/自然质感人像 | 链路包含 | 链路包含 | 前置照片/人像链路明确；后置产品范围以 PRD 为准 |
| 人像 Bokeh/Depth | 支持 | 支持 | 计算 depth 使用主副摄单帧图，暗光噪声影响虚化边缘 |
| 动态照片 | 支持 | 支持 | MFNR/SR 通路明确；4K Live 仍是专项评估 |
| 双景录像 | 1080P30 双路 | 1080P30 双路 | HAL 只确认前后双路通路，布局、保存和交互以 PRD 为准 |

## 3. 照片链路

后置照片 HAL usecase：

| Usecase | 算法 | 取帧基线 |
|---|---|---|
| c0 | TF Super Night | NZSL 8 帧 |
| c1 | TF HDR | ZSL + NZSL/PSL 7 帧 |
| c2 | TF SR | ZSL 5 帧 |
| c3 | MFNR | ZSL 5 帧 |
| c4 | Motion Capture | 项目策略 |
| c5 / 部分模式 c4 | HDSR | HDR + SR |

常见后处理模块包括 CFR、LDC、FRT、美颜、滤镜和水印。模块存在于通路不等于每个模式都需要在 FL 建独立功能行；算法行应按模式和摄像头的真实启用范围展开。

### 变焦与 ISZ

- 26111 / 26121 的视频模式均不支持 ISZ，原因是切换 ISZ setting 会造成录像效果跳变并增加功耗；本节其余 ISZ 点位和算法链路仅描述照片类模式。
- 26111 主摄满足亮度条件时，2x 预览切换到 in-sensor zoom setting；SM7635 不支持 seamless 切换。
- 26111 4x SR 依赖外部软件 remosaic，需完成 6GB 内存与性能评估。
- 26121 主摄和长焦满足亮度条件时使用 ISZ，超广角不需要 ISZ。
- 26121 项目最大倍率按 HAL 总表为 120x；算法示意图出现 140x，需由产品/SE 统一。

## 4. 人像链路

- 多帧人像使用 ZSL 5 帧，HDR 人像使用约 7 帧，夜景人像使用约 8 帧。
- Depth 只能使用主副摄对应的单帧图计算，不能使用多帧融合结果。
- 1x/2x 人像：Wide 为主图，UW 为副图。
- 26121 3.5x 人像：Tele 为主图，Wide 的 1/2 binning + crop 为副图。
- 进入 ISZ 后改走 ISZ MFNR / ISZ HDR。
- UW 在 1x/2x 人像中仅作为算法内部 depth 辅助流，不代表人像模式向用户开放 UW；FL 所有人像行统一为 `UW=✗`。

## 5. 视频与视频类模式

| 规格 | 26111 | 26121 | 限制 |
|---|---|---|---|
| 1080P30 | HAL 支持 | HAL 支持 | 逐镜头范围待确认 |
| 1080P60 | HAL 支持 | HAL 支持 | 26111 HLG ON 时不支持 |
| 4K30 | HAL 支持 | HAL 支持 | 逐镜头范围待确认 |
| 4K60 | 不支持 | HAL 支持 | 26121 逐镜头范围、功耗、温升待确认 |
| 录像滤镜 | 1080P30 only | 1080P30 only | APP 录屏特效链路 |
| 慢动作 | Main 1080P120 | Main 1080P120 | 不从旧项目推导 Tele/UW/Front |
| 延时摄影 | Main 1080P30 / 4K30 | Main 1080P30 / 4K30 | 焦段 1x-8x |
| 前置视频 | Front 1080P30/60 | Front 1080P30/60 | 前置 4K 未被 HAL 证明 |

HLG：

- 26111 的 1080P30/4K30 有 HLG 通路；1080P60 不支持 HLG。
- 26121 的 1080P30/60 与 4K30/60 都画出了 HLG 通路，但产品开放和摄像头范围仍需 SE 确认。
- 前置 HLG 写为“根据产品需求实现”，因此状态为 TBD。

## 6. 高像素链路

### 26111

- HAL 明确 Main、1x、4:3、NZSL 高像素通路。
- 50MP / 200MP / 200MP Ultra 的产品选项与算法定义继续以最新版高像素 PRD 为准。

### 26121

Main 和 Tele 均有高像素通路，按场景选择：

| 场景 | 输入与算法 | 输出 |
|---|---|---|
| 高亮、低动态 | Sensor 直出 50MP + HAL MMF | 50MP |
| 中亮、低动态 | 12.5MP binning + TF MMF | upscale 50MP |
| 高动态 | 12.5MP binning + TF HDR | upscale 50MP |
| 低照 | 12.5MP binning + TF Super Night | upscale 50MP |

这不是“所有场景统一 remosaic”的链路。FL 的说明应描述场景自适应直出或 binning + upscale，产品选项名称仍以高像素 PRD 为准。

## 7. 当前争议项

1. 后置视频各规格的 Main/UW/Tele/Front 支持矩阵。
2. 26111 2SAT 的模式范围，以及无 Fallback 对 Macro Control 的影响。
3. 26111 4x 外部软件 remosaic 和 AIGC 在 6GB 上是否量产。
4. 26121 4K60 HLG 的镜头范围与热功耗结论。
5. 26121 高像素 Main/Tele 的产品入口以及 50MP Ultra 定义。
6. 前置 HLG、前置 4K、录像中拍照、4K Live 是否量产。
7. 26121 Video Log 是否保留；HAL 有项目链接，但旧配置曾列为移除。
8. 26121 最大倍率是 120x 还是 140x。
