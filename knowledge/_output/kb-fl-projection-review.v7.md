# KB → FL 投影复核 v7

> 代码基线：`CameraApp origin/develop@c97b3137b6`（2026-07-27）

## 结论

KB 的知识粒度和 FL 的验收粒度已经解耦。判断一个节点是否在 FL 展开的唯一问题是：

> 这个差异是否会改变项目支持结论、某颗输出摄像头的结论、某个模式/规格的兼容结论，或独立验收预期？

如果不会，信息保留在 KB；如果会，才生成 FL 行。

## A. 必须展开

这些节点的差异天然会改变项目或摄像头验收，不能只写在一条说明里：

| 节点族 | FL 展开维度 | 原因 |
|---|---|---|
| Video Specs | 项目 × 摄像头 × 分辨率 × FPS × HDR/HLG | 编码、EIS、HDR、功耗限制按组合变化 |
| Slow Motion Specs | 项目 × 摄像头 × 分辨率 × 采集 FPS | Sensor high-speed mode 逐颗不同 |
| Timelapse Specs | 项目 × 摄像头 × 输出规格；倍速按需 | 长录、编码和倍速范围不同 |
| High Resolution Specs | 项目 × 摄像头 × 像素档 × 算法路径 | 50/200MP、Remosaic/HDR 路径不同 |
| Zoom Range | 项目 × 模式 × 摄像头 | 最小/最大倍率和光学点不同 |
| Lens Switching Strategy | 项目 × 模式 × 规格 | SAT、硬切、锁镜和低照策略不同 |
| AE/AF 子能力 | 模式 × 摄像头 | 固定焦、Touch AF、Face AF、CAF、Lock 不同 |
| OIS / EIS | 摄像头 × 规格 | 硬件和规格兼容直接不同 |
| Expert ISO / Shutter / Focus | 摄像头 × 参数范围 | Sensor/HAL 边界不能跨摄像头合并 |
| RAW / DNG | 摄像头 × 输出组合 | RAW capability 和 stream combination 不同 |
| Panorama | 项目 × 摄像头 × 方向/规格 | 输出镜头、方向、拼接和夜景能力不同 |
| Macro / Action 独立模式 | 项目 × 摄像头 | 是否有独立生产入口与只含算法完全不同 |
| Beauty/Bokeh Control | 模式 × 摄像头 | 用户入口和输出镜头范围不同 |
| Motion Photo Audio/Cover HDR | 项目 × 摄像头 × 规格 | 封装、音频、HDR 查看链路可能独立变化 |
| Video Snapshot / Pause / Mute | 项目 × 规格 | HDR/高帧率/并行流可能限制 |
| Launch Entry | 项目 × 入口 | 安全相机权限、默认模式、相册可见范围不同 |

## B. 条件展开

以下节点默认保留一条父能力；只有子能力的支持结论真的不同才拆：

| 父节点 | 默认 FL | 触发子节点展开的条件 |
|---|---|---|
| Style | 一条 Style | Filter 与 Tuning 的模式、摄像头或视频规格范围不同 |
| Preset | 一条 Preset | Import/Share、Widget 或安全策略形成独立项目结论 |
| Motion Photo | 一条 Motion Photo | Audio、Cover HDR、裁剪产生独立支持或验收结论 |
| AE/AF | 一条父行 + 差异子行 | 固定焦、CAF、Lock、EV 范围在摄像头/模式间不同 |
| Expert Mode | 一条模式行 + 参数规格行 | ISO/快门/WB/Focus/RAW 的摄像头范围或边界不同 |
| Mode Switcher | 一条模式集合行 | 快速切换手势、时延或状态继承有独立需求 |

## C. 不应因为 KB 拆细而自动进入 FL

- 目录节点。
- Filter/Tuning 内部的每个参数或每个 LUT 名称。
- Preset 卡片展示字段、内部序列化字段。
- Motion Photo 插帧等纯 pipeline 阶段，除非它形成独立算法/IQ 验收。
- 单摄/双摄虚化的实现分支，若用户输出镜头和验收结论相同。
- Depth 辅助摄像头；它不等于用户可选输出摄像头。
- debug/test/reprocess/厂商验证 Mode；没有生产入口时不投影。

## 本轮补回的代码结构信息

旧 KB 缺少但当前 App 已明确存在：

- 生产/候选 Mode：Photo、Video、Portrait/Bokeh、Night、Slow Motion、Timelapse、Panorama、Manual、Macro、Motion。
- 启动上下文：普通、Secure Camera、Shortcut、Voice、Widget。
- 视频录制交互：Pause/Resume、Mute、Video Snapshot。
- Settings：Default Gallery、Storage Location、Fallback Macro、Reset。
- 用户控制与算法分层：Beauty Control ≠ Beauty Algorithm；Bokeh Control ≠ Portrait Bokeh Algorithm。
- 专业参数子树：ISO、Shutter、WB、Manual Focus、RAW、Histogram。
- Zoom 子树：交互、倍率范围、镜头切换策略、ISZ/SR/OIS。

## 仍需产品或代码负责人确认

1. `锁定白平衡`：KB 有需求描述，但当前代码基线没有找到匹配的生产 SettingKey，已标为 `规划中`。
2. `录制中拍摄 Motion Photo`：现有需求为新增方向，已标为 `规划中`，不能从普通 Video Snapshot 推导支持。
3. `Quick Mode Switch`：需确认是否有独立手势/时延指标，还是普通模式栏切换的文案别名。
4. `Histogram`：Manual Mode 的产品入口与生产门控仍需代码 owner 确认。
5. `Auto Tone / Image Tone / Color Mode`：代码中同时存在 color mode/control keys，需要确认是并存能力、项目变体还是旧版迁移关系。
6. `High Resolution`：当前代码存在高像素/Remosaic 能力和规格，但生产模式数组是否以独立模式展示必须按项目配置确认，不能仅因 debug mode 常量存在而判定。
