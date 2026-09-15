<!-- source: https://nothing-tech.sg.larksuite.com/docx/Kl8pd7g4FoK52px0LkTlqqn7gdd | fetched: 2026-09-15 | revision: 563 -->
<title>【PRD】Camera 5.1 - 照片专业模式 2.0（Expert Mode 2.0）</title>

# 0. 文档信息

- 文档标题：【PRD】Camera 4.2 - 照片专业模式 2.0（Expert Mode 2.0）
- 项目 / 机型 / 代号：[待补充]
- 所属版本：[待补充]
- 作者：Travis Zhao
- 更新时间：2026-06-08
- 项目阶段：[待补充]
- 上市时间：[待补充]
- 销售地区：[待补充]

---

# 1. 变更日志

| 时间 | 版本号 | 变更人 | 主要变更内容 |
|-|-|-|-|
| 2026-04-24 | v0.1 | Travis Zhao | 初稿创建 |
| 2026-06-08 | v0.2 | Travis Zhao | 砍掉自动/手动混合模式、峰值对焦恢复、新增间隔拍摄、Preset 扩展、测光逻辑完善、视觉更新合并 |

---

# 2. 需求背景

## 2.1 产品 / 数据现状

- 当前现状：专业模式为全手动参数调节，功能相对基础
- 已有方案：现有专业模式支持 ISO、Shutter、EV、WB、Focus 手动调节
- 已知问题：

  - Slide bar 和工具栏视觉风格偏基础，缺乏专业感
  - 缺少测光方式切换、峰值对焦等专业工具
  - 专业模式参数（EV/ISO/S/WB/AF）不支持保存到 Preset
- 数据结论：[待补充：当前专业模式使用率数据]
- 竞品 / 对标情况：

  - iPhone ProRAW / Samsung Expert RAW 支持多种测光模式、峰值对焦等专业工具
  - 竞品普遍支持 Preset 保存完整相机配置

---

# 3. 需求目标

1. 视觉更新：Slide Bar 和工具栏视觉升级，对齐当前相机设计风格
2. 新增测光方式切换（点测光/中央重点/矩阵），扩展专业工具集
3. Preset 支持保存专业模式参数（EV/ISO/S/WB/AF）+ RAW capture
4. 新增间隔拍摄功能
5. 新增峰值对焦功能

---

# 4. 需求范围

## 4.1 范围内

- Slide Bar 视觉优化：样式改版，对齐当前相机设计风格（设计稿已更新，参数刻度规格如下）
- 工具栏视觉优化：图标 + 参数值显示，统一并入视觉更新
- 新增测光方式切换：点测光（跟随对焦点）、中央重点测光、矩阵测光
- Preset 扩展：EV、ISO、S（快门）、WB、AF、RAW capture 可保存到 Preset
- 新增间隔拍摄：工具栏入口，5 张 / 3 秒快捷选项 + 自定义（张数 5-600，间隔 1s-60s）
- 新增峰值对焦：下拉工具栏开关，手动对焦时自动生效，单档位灵敏度

---

# 5. 功能设计

## 5.1 视觉更新（Slide Bar + 工具栏）

### 功能支持范围

- 模式范围：照片专业模式
- 摄像头范围：全部
- 焦段范围：全部
- 地区范围：全球

### Slide Bar

- 样式改版，对齐当前相机设计风格
- 数值：滑块上方悬浮显示当前值
- 支持点击刻度快速跳转
- 设计稿已更新，参数刻度规格如下

**参数与刻度规格：**标尺采用视觉等分布局，支持点击刻度快速跳转。下表同时定义独立规格 bar 与运行时显示规则。独立规格 bar 仅用于范围和刻度交付，所有数字统一使用小字号、非高亮样式，并以文字框中心对齐对应大刻度线中心；实际范围上限按摄像头能力适配。

| 参数 | 范围 / 可选值 | 独立规格 bar 显示数值 | 大刻度 | 小刻度 / 可选步进 | 运行时数值显示 |
|-|-|-|-|-|-|
| F / AF | 0.00–1.00；每 0.02 一档 | 0.00、0.10、0.20、0.30、0.40、0.50、0.60、0.70、0.80、0.90、1.00 | 每 0.10 一根；共 11 根 | 每 0.02 一根；两个大刻度之间 4 根，分别对应 +0.02、+0.04、+0.06、+0.08 | 不常驻显示静态刻度值；仅显示当前选中值 |
| ISO | 50–3200 或 50–6400，按摄像头能力适配 | 50、100、200、400、800、1600、3200、6400；超出机型上限的不显示 | 整档：50、100、200、400、800、1600、3200、6400 | 标准 1/3 EV；两个大刻度之间 2 根。依次为 64/80、125/160、250/320、500/640、1000/1250、2000/2500、4000/5000 | 显示整档数值；当前选中值始终显示 |
| S | 1/8000 s–30 s | 每隔两个大刻度显示一个数值：1/8000、1/1000、1/125、1/15、1/2、4″、30″ | 1/8000、1/4000、1/2000、1/1000、1/500、1/250、1/125、1/60、1/30、1/15、1/8、1/4、1/2、1″、2″、4″、8″、15″、30″ | 标准 1/3 EV；两个大刻度之间 2 根。各区间依次为：（1/6400、1/5000）；（1/3200、1/2500）；（1/1600、1/1250）；（1/800、1/640）；（1/400、1/320）；（1/200、1/160）；（1/100、1/80）；（1/50、1/40）；（1/25、1/20）；（1/13、1/10）；（1/6、1/5）；（0.3″、0.4″）；（0.6″、0.8″）；（1.3″、1.6″）；（2.5″、3.2″）；（5″、6″）；（10″、13″）；（20″、25″） | 每 3 档位 显示一个静态数值；当前选中值始终显示 |
| EV | -2.0–+2.0 EV | -2.0、-1.0、0.0、+1.0、+2.0 | 每 1 EV 一根：-2、-1、0、+1、+2 | 标准 1/3 EV；两个大刻度之间 2 根，对应 ±0.3、±0.7 的显示精度 | 沿用现有显示规则；当前选中值始终显示 |
| WB | 2000–10000K；每 200K 一档 | 2000K、3000K、4000K、5000K、6000K、7000K、8000K、9000K、10000K | 每 1000K 一根；共 9 根 | 每 200K 一根；两个大刻度之间 4 根，例如 2200K、2400K、2600K、2800K，其余区间同规则递增 | 不常驻显示静态刻度值；仅显示当前选中值 |

### 工具栏

- 底部/侧边工具栏，图标 + 参数值双行显示
- 未选中：灰色线性图标
- 选中：品牌色面性图标 + 参数值高亮
- 切换参数时图标有微动效反馈

<grid>
<column width-ratio="0.513080">
![The image shows the camera interface with the Expert Mode 2.0 visual update. At the bottom, there is a tool bar with icons and parameter values displayed in two rows. The icons are gray when not selected, and brand-colored with highlighted parameter values when selected. There is a micro-motion effect feedback when switching parameters. The interface also includes a histogram, EV, ISO, shutter speed, white balance, and focus parameters, with "EXPERT" highlighted in red.](https://feishu.cn/file/Qx65bpfcwoYaJLxUJOllMSftgQr)
</column>
<column width-ratio="0.486920">
![The image shows the camera interface of Camera 5.1 in Expert Mode 2.0. It displays a street scene with a tall building in the background. The interface includes a bottom slider bar with parameters like EV (-3.0 to +3.0), ISO (500), Shutter Speed (1/800), WB (5200K), and AF (0.40). There are icons for Portrait, Expert, and Photo modes at the bottom, with Expert Mode highlighted in red. The interface also shows a histogram and a white circular button in the center.](https://feishu.cn/file/UiANbkuBwoL8I6x4VrFlAUxCgah)
</column>
</grid>

## 5.2 Preset 支持专业模式参数

### 功能说明

Preset 新增支持保存以下专业模式配置项：

| 参数 | 说明 |
|-|-|
| EV | 曝光补偿值 |
| ISO | 感光度 |
| S | 快门速度 |
| WB | 白平衡 |
| AF | 对焦模式 / 对焦位置 |
| RAW capture | RAW 拍摄开关 |

加载 Preset 时，以上参数跟随恢复。

## 5.3 测光方式

### 功能支持范围

- 模式范围：照片专业模式（仅专业模式生效）
- 摄像头范围：全部
- 焦段范围：全部
- 地区范围：全球

### 交互与流程

- 工具栏增加"测光"图标
- 点击测光图标 → 弹出选择面板（点测光 / 中央重点 / 矩阵）
- 选中后实时生效，预览画面曝光实时变化
- 当前测光模式在图标上以小标识显示
- 不显示测光区域框

### 测光方式定义

| 模式 | 说明 |
|-|-|
| 点测光（Spot） | 以对焦点为中心，约 2-5% 范围，跟随对焦点 |
| 中央重点测光（Center-weighted） | 中心 60-80% 区域加权 |
| 矩阵测光（Matrix） | 全画面多区域加权平均 |

### 限制

- 测光模式存 Preset
- ISP 原生支持三种测光模式，需应用层对接

## 5.4 间隔拍摄

### 功能支持范围

- 模式范围：照片专业模式
- 摄像头范围：全部
- 地区范围：全球

### 交互与流程

- 工具栏新增"间隔拍摄"图标
- 点击 → 弹出选项面板：

  - 快捷选项：「5 张 / 3 秒」
  - 「自定义」→ 进入下一级设置

### 自定义设置

| 参数 | 范围 | 默认值 |
|-|-|-|
| 拍摄张数 | 5 \~ 600 张 | 10 张 |
| 间隔时间 | 1s \~ 60s | 3s |

### 行为

- 用户设定参数后点击开始，自动按间隔连续拍摄
- 开始倒计时—>结束倒计时—>开始拍摄—>拍摄完成—>开始倒计时—>
- 开启后，有常驻的顶部工具栏提示，与顶部的 toast 提示 ： “间隔连拍：xx秒 xx 张”
- 拍摄过程中显示已拍张数 / 总张数
- 可随时中断拍摄
- 倒计时兼容：倒计时的执行优先级比间隔连拍更高，在完成了倒计时之后，再执行间隔连拍

<grid>
<column width-ratio="0.250000">
![The image shows the interface of the camera's Expert Mode 2.0 in photo professional mode. At the bottom, there is a tool bar with several icons, including "画面比例" (Aspect Ratio), "柔光" (Soft Light), "运动模式" (Motion Mode), "微距特写" (Macro), "自动HDR" (Auto HDR), "倒计时" (Timer), "间隔连拍" (Interval Shooting), and "设置" (Settings). The "间隔连拍" icon is highlighted in orange, indicating it is the new "Interval Shooting" feature mentioned in the document. The background displays a keyboard and a computer screen.](https://feishu.cn/file/S33Yb8aC2oCJPWxGEuOlTroCgFg)
</column>
<column width-ratio="0.250000">
![The image shows the interface of the Camera 5.1 Expert Mode 2.0 in photo professional mode. At the top, there are icons like EV 0.0 and a menu button. Below, a grid of keyboard keys is visible. At the bottom, a pop-up panel displays icons for scene modes (landscape, portrait, etc.), with "5张·3秒" (5 photos in 3 seconds) and "5张·1秒" (5 photos in 1 second) options highlighted, and "间隔连拍" (interval shooting) at the bottom. This corresponds to the "interval shooting" feature described in the document, where users can set parameters like shooting count and interval time, with the app automatically shooting at the set intervals.](https://feishu.cn/file/BEITbvH5WoutM1xyMSnlhBFSgNd)
</column>
<column width-ratio="0.250000">
![The image shows the "Interval Shooting" settings interface in the Camera 5.1 Expert Mode 2.0. At the bottom, there is a settings panel with "拍摄数量" (Shooting Quantity) set to 5 and "间隔时间" (Interval Time) set to 1 second. Above it, a laptop keyboard and part of a computer screen are visible, with the screen displaying some text and icons. This corresponds to the "自定义" (Custom) setting in the interval shooting function, where users can adjust parameters like shooting quantity and interval time.](https://feishu.cn/file/S2ZNbQzdooLtSLxyjyTlcPjWgLe)
</column>
<column width-ratio="0.250000">
![The image shows a laptop screen with a camera interface. At the bottom center of the screen, there is an orange square button. The laptop is placed on a desk, and a monitor is behind it, displaying some content. The number "2" is prominently displayed in the center of the image, possibly indicating a step or sequence in the context of the camera's interval shooting function.](https://feishu.cn/file/TSZ8byeWcoSjv1xJLPllBP6ngIg)
</column>
</grid>

## 5.5 峰值对焦

### 功能支持范围

- 模式范围：照片专业模式（手动对焦时生效）
- 摄像头范围：全部
- 地区范围：全球

### 交互与流程

- 开关位置：下拉工具栏，点击切换开/关
- 开关开启 + 手动对焦时自动生效，合焦区域红色边缘高亮
- 切回自动对焦时自动关闭

![The image shows the interface of Camera 5.1's Expert Mode 2.0, focusing on the 5.5 Peak Focus feature. It displays the "Interval Shooting: 5 shots, 3 seconds" option at the top. Below, the "5.5 Peak Focus" section lists the function support range: modes in Photo Professional (manual focus effective), all cameras, and global region. The interaction process includes a switch position in the pull-down toolbar, automatic activation with switch on and manual focus, and automatic deactivation when switching back to auto focus. The interface also shows settings like ISO 80, 1/100 shutter speed, EV 0.0, MF 0.04, and WB 6000.](https://feishu.cn/file/BT9Gbi27KoQWCyx7a7wlAMkcgtf)

---

# 6. 关键依赖与约束

## 6.1 技术依赖

| 依赖项 | 说明 | 状态 |
|-|-|-|
| 测光算法 | ISP 原生支持三种测光模式，需应用层对接 | 已确认 |
| 峰值对焦算法 | 边缘检测算法，需确认目标机型支持情况 | [待补充] |
| Preset 存储 | 现有 Preset 存储结构扩展 | [待补充] |
| 间隔拍摄 | Camera HAL 是否支持连续拍摄指令 | [待补充] |

## 6.2 素材 / 文案依赖

- 测光模式引导提示文案
- 峰值对焦设置页面文案
- 间隔拍摄设置项文案

---

# 7. 效果定义与验收标准

## 7.1 预期效果

- 专业模式日活使用率提升 [待补充：目标值]
- 测光模式使用分布数据分析
- 间隔拍摄使用率
- 峰值对焦开启率

## 7.2 验收口径

- 测光准确性：三种测光模式下曝光误差 < [待补充] EV
- 峰值对焦：标准测试场景下，合焦区域识别率 > 90%
- 预览帧率：开启峰值对焦后预览帧率不低于 [待补充] fps
- 间隔拍摄：按设定参数连续完成拍摄，无丢帧

---

# 8. 词条定义

| 应用场景 | 中文词条 | 英文词条 | 备注 |
|-|-|-|-|
| 专业模式 | 专业 | Pro / Expert | 已有 |
| 测光方式 | 测光模式 | Metering mode | 新增 |
| 点测光 | 点测光 | Spot | 新增 |
| 中央重点测光 | 中央重点测光 | Center-weighted | 新增 |
| 矩阵测光 | 矩阵测光 | Matrix | 新增 |
| 间隔拍摄 | 间隔拍摄 | Interval Shooting | 新增 |
| 拍摄数量 |  |  |  |
| 间隔时间 |  |  |  |
| 峰值对焦 | 峰值对焦 | Focus Peaking | 新增 |
| RAW capture | RAW | RAW | 已有 |

---

# 9. 埋点

## 9.1 埋点目标

- 监控各功能使用率，评估功能接受度
- 分析测光模式分布
- 统计间隔拍摄和峰值对焦使用情况

## 9.2 埋点定义

| 参数名 | 参数说明 | 取值 | 触发时机 |
|-|-|-|-|
| pro_mode_metering_mode | 测光模式 | spot / center_weighted / matrix | 切换时上报 |
| pro_mode_interval_shots | 间隔拍摄张数 | 5\~600 | 开始拍摄时上报 |
| pro_mode_interval_seconds | 间隔拍摄秒数 | 1\~60 | 开始拍摄时上报 |
| pro_mode_peaking_toggle | 峰值对焦开关 | on / off | 切换时上报 |

---

# 10. 项目计划与风险

## 10.1 风险与兜底

| 风险 | 影响 | 兜底 |
|-|-|-|
| 峰值对焦算法性能开销大 | 预览卡顿 | 单档位灵敏度降低计算量 |
| 测光模式用户不理解差异 | 负面反馈 | 首次使用时提供引导提示 |
| 间隔拍摄长时间占用相机 | 功耗/发热 | 显示已拍张数，用户可随时中断 |

---

# 11. 待确认事项

1. [待补充] 目标机型：4a / 4a Pro / Phone 3 / 全部？
2. [待补充] 目标版本 / 上线时间
3. [待补充] 峰值对焦算法是否已有？目标机型硬件是否支持？
4. [待补充] 间隔拍摄 Camera HAL 支持情况
5. [待补充] 设计稿（Slide Bar + 工具栏视觉）
6. [待补充] 性能基准数据

## 正式设计稿（Camera 5.1）

[Expert mode — Histogram / visual redesign](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=2659-21016&p=f)

[Expert mode — Focus peaking](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=2659-18505&p=f)

[Expert mode — Metering / interval shooting](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=107-923&p=f)