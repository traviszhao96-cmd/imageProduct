<!-- source: https://nothing-tech.sg.larksuite.com/docx/XOpvdfIjBoVwSPxq6QElp9W8gMg | fetched: 2026-09-15 | revision: 555 -->
# 【PRD】Camera 5.1 - 相机设计改版

## 文档信息

- 产品模块：Camera / 相机
- 适用版本：NOS 5.1
- 首发机型：Phone 5a
- 文档状态：设计对齐稿
- 本次更新范围：

  - Camera Structure：主界面信息层级、预览区、Preset、快门、设置面板与视觉效果改版
  - Effect Discovery：Preset Library 网格视图与 AI Preset 推荐
  - Pro Features：Expert 模式重塑，Tuning 与 Filter 合并为 Style

## 背景

当前相机主界面在视觉层面仍存在以下问题：

- 快门按键采用传统圆形方案，底部视觉重心较强，占用纵向注意力，不利于释放取景区域的视觉空间
- 工具栏呼出方式不够直观，用户在单手持机场景下调用效率不足
- 多个 Slider 中的数字字体风格不统一，辨识度和整体美感存在提升空间

面向 NOS 5.1 在 Phone 5a（项目 26111）首发，相机主界面需要进一步强化品牌化视觉语言，统一主界面结构、效果发现与专业功能的交互，并为后续升级项目建立可复用的设计基线。

## 目标

- 完成相机主界面信息层级重组，提升取景空间利用率、单手可达性与拍摄主流程稳定性
- 通过椭圆快门、模式/预览区重排、Preset 与设置入口调整，建立 NOS 5.1 统一的 Camera Structure
- 通过 Preset Library 网格视图和可逆的 AI Preset 推荐，提升效果发现与应用效率
- 重塑 Expert 模式参数控制，并将 Tuning 与 Filter 统一为 Style 系统，降低专业创作入口的理解成本
- 统一各类数字型 Slider 的字体与数值表现，保证不同模式下的可读性和视觉一致性
- 形成可在后续升级项目复用的相机交互、视觉和兼容性基线

## 目标用户与使用场景

### 4.1 目标用户

- 高频使用系统相机的普通用户
- 偏好单手拍摄、快速切模式、快速调参数的用户
- 对产品视觉质感与交互反馈敏感的核心用户

### 4.2 典型场景

- 用户在照片、视频、人像、夜景、专业等模式间快速切换并拍摄
- 用户单手持机时，需要从右下角快速呼出工具栏完成参数调整
- 用户在缩放、滤镜、曝光、人像光圈等 Slider 上频繁查看和调整数值
- 用户在拍照与录像时，需要通过快门形态和动效快速理解当前状态

## 需求范围

- 照片、视频及前置自拍场景的模式区与预览区域下移，重新分配取景区和底部控制区空间
- Preset 入口上移，交互由滑动选择调整为点击进入/选择；主界面保留当前 Preset 的可感知入口
- 快门按键形状、尺寸与状态动效升级；照片态使用白色椭圆快门，视频态使用红色椭圆快门并适配录制控制
- 设置面板入口下移，设置面板 UI 随底部结构同步下移；面板以底部浮层形式展开与收起
- 取景区域统一圆角；16:9 比例下主界面元素按设计稿完成位置适配
- 半透明控件与浮层增加背景模糊效果，保证复杂取景背景下的可读性
- 模式列表支持拖动选择；设置面板入口保持在右下角易触达区域

## 功能方案

### 6.1 相机设计改版 — 快门形状

#### 6.1.1 设计目标

- 将当前圆形快门升级为横向椭圆形快门
- 降低底部中轴区域的“厚重感”
- 通过更具延展性的造型提升界面现代感与美感
- 在不削弱“可点击性”的前提下，为取景画面留出更多视觉呼吸感

#### 6.1.2 适用范围

- 椭圆形快门需覆盖所有模式，无例外

#### 6.1.4 功能说明

快门键定义主要分为以下几个状态，涉及到静态设计和动态的动效设计

1. 默认态

   - 快门以椭圆形主体展示
   - 保持简洁、稳定、可感知的主操作视觉
2. 拍照触发态

   - 点击后提供短促、干净的触发反馈
   - 动效节奏需体现“果断拍摄”感
3. 录像待机态

   - 在视频模式下，椭圆形快门保持统一主结构
   - 通过内层图形、颜色或局部元素区分“视频可录制”状态
4. 录像进行态

   - 录制开始后，快门需通过显著但克制的形态/颜色变化体现“正在录制”
   - 状态变化应支持快速识别，避免与拍照态混淆
5. 长按或特殊模式态

   - 若模式存在长按录像、连拍、延时等特殊触发逻辑，仍基于椭圆快门统一延展
   - 不允许回退到旧圆形视觉语言
6. 长曝光等待态

   1. 在相机拍摄取帧的过程中的状态，该状态结束之前相机的拍摄并没有结束
7. 处理等待态

   1. 该状态下相机正在处理当中，在处理完成之前， 无法点击快门再次拍摄

![The image shows two smartphone screens with a camera interface. The left screen displays the default态 (default state) of the fast shutter, featuring a red elliptical fast shutter button at the bottom. The right screen shows the recording standby态 (recording standby state) with a red recording indicator at the top right corner and a red elliptical fast shutter button at the bottom. Both screens have a photo/video mode selector at the bottom, with the video mode selected on the right.](https://feishu.cn/file/Zqv9bFLE1oSuKxxMTFIlQuvvgcc)

### 6.2 相机设计改版 — 模式栏下移与快速切换

#### 6.2.1 问题定义

- 照片模式承载的使用比例越来越高，但是模式栏占据了主页面过大的位置
- 当前的模式之前的切换速度慢，比如等待模式加载完成才能切换下一个模式

#### 6.2.2 设计目标

- 将模式栏下移，为工具栏和预览留出更大的可用空间，给用户提供更强的取景沉静感
- 支持模式的快速切换

#### 6.1.4 功能说明

- 模式栏移动到底部，和缩略图，前后翻转移动到同一个层级
- 支持模式之间的快速切换，不需要等待上一个模式完全加载完成即可切换下一个

 

### 6.2 相机设计改版 — 设置面板下移

重整设置面板的信息层级，降低低频功能对主拍摄流程的干扰，并为 Style、Preset、视频开关等能力预留一致的入口位置。具体功能排序和展开/收起逻辑待后续细化。

#### 6.2.1 问题定义

当前工具栏并非新增模块，本期目标是优化其呼出方式，使用户可在右下角热区内更稳定、更直观地调出工具栏。

#### 6.2.2 设计目标

- 在右下角新增工具栏开关入口
- 保证用户在热区范围内可快速触发工具栏呼出
- 优化单手操作可达性与成功率
- 不改变工具栏本身的信息层级与功能集合

#### 6.2.3 交互说明

- 右下角提供明确可感知的工具栏开关入口，四桶形态的入口 icon，位置在快门按键的右侧，右手习惯热区内
- 点击 button，或者从底部快门按键右侧的热区范围内向上滑动，都支持呼出工具栏
- 用户点击后可直接呼出当前工具栏。在底部的大范围热区之内，除快门、缩略图、前后翻转的区域，都支持上滑手势展开；工具栏展开与收起反馈需明确、流畅
- 呼出逻辑需兼容照片、视频、人像、夜景、专业等所有主模式
- 呼出的工具栏遮挡住快门、Preset、模式栏区域，在该状态下同理不支持这些模式的切换
- 工具栏支持高斯模糊的半透明效果——待可行性评估

<grid>
<column width-ratio="0.500000">
![The image shows a smartphone screen displaying a camera interface. The screen has a green grass background with a person lying down. At the bottom, there are three mode options: PORTRAIT, PHOTO (highlighted in red), and VIDEO. Above the modes, there are three circular icons with numbers 0.6, 1x, 2, 3.5, 7. A white rectangular area is in the center, likely the shutter button. This image is related to the context about camera design改版, specifically the setting panel下移 and tool bar interaction, demonstrating the layout of the camera interface.](https://feishu.cn/file/EgBCbh7XPoRo3ZxI0wNl4Bdygkc)
</column>
<column width-ratio="0.500000">
![The image shows a smartphone screen with a camera interface. The screen displays a photo of a person reaching out to grass. Below the photo, there is a tool bar with various icons, including Flash, Timer, HDR, Exposure, Style, Motion photo, 12MP, Quality, Grid, 4:3, Watermark, Glyph mirror, and Settings. This image is related to the context about camera design改版, specifically the setting panel being moved to the bottom, where the tool bar supports gestures like swiping to expand, and its呼出 logic is compatible with all main modes.](https://feishu.cn/file/NHA5bK0UhoB1Qhxq3gHlAoMdgOf)
</column>
</grid>

### 6.5 相机设计改版 — 取景圆角常驻

取景框圆角常驻展示，形成统一视觉风格，并与 NOS 5.0 视觉原则对齐。圆角尺寸及不同画幅下的裁切规则待后续细化。

该需求不同比例设计详见设计稿

### 6.6 相机设计改版 — 半透高斯模糊

优化面板、转场和浮层背景中半透明元素的高斯模糊效果，提高复杂取景背景下的可读性和视觉质感。性能边界与降级方案待后续评估。

#### 6.6.1 设计目标

- 涉及到 变焦条，工具栏 两个控件的高斯模糊效果
- 根据当前评估结果有较大的功耗风险

### 6.7 相机设计改版 — 16:9 布局调整

调整 16:9 比例下快门、模式栏、设置面板与预览区域之间的布局关系，避免控件挤压、重叠或遮挡。

![The image shows a camera app interface on a smartphone with a 16:9 layout. The preview area displays a person lying in a grassy field. At the bottom, there are control elements including a zoom slider with values 0.6, 1x, 2, 3.5, 7, a shutter button, and mode options like PORTRAIT, PHOTO (highlighted in red), and VIDEO. This relates to the "6.7相机设计改版—16:9布局调整" section, which focuses on adjusting layout to avoid control overlap in 16:9 proportions.](https://feishu.cn/file/F2LxbEFu7ohFBGx3Xh2lvd0Ygod)

## 设计依赖

- **设计基线：**[26111 Camera / Gallery design proposal](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/26111-Camera---Gallery-design-proposal?node-id=0-1&p=f&t=Ovpk1jTxojxfvJht-0)；开发实现以设计稿中的正式 Feature list 与定稿页面为准，不将 Exploration 页面直接作为开发结论。
- 本期不涉及第三方字体授权问题
- 开发实现需严格对齐设计输出的快门比例、状态稿、动效节奏和字体规范

## 交互要求

- 快门升级后，用户无需学习成本即可识别其核心拍摄入口属性
- 快门在不同模式下的状态差异应清晰，但基础造型需保持统一
- 工具栏开关需保证在右下角热区内易触达、易触发
- 各类 Slider 数字字体切换后，参数读取效率不得下降
- 整体方案需优先保证拍摄主流程稳定，不因视觉升级引入额外交互负担

## 版本与落地要求

- 本方案应用于 NOS 5.1
- 由 Phone 5a（项目 26111）首发承载
- 后续升级项目需继续支持该套交互与视觉规范
- 后续若新增相机模式或复用主相机底部框架，也需默认继承本期方案

## 非功能要求

### 10.1 性能

- 快门动画、工具栏呼出动画、Slider 数字展示切换需保持流畅
- 不得因视觉升级导致明显掉帧、触控延迟或响应不一致

### 10.2 兼容性

- 需覆盖竖屏主拍摄态
- 需兼容横屏拍摄使用场景
- 需兼容照片、视频、人像、夜景、专业等全部模式

## 验收标准

### 11.1 椭圆快门

- 所有相机模式均已由圆形快门升级为椭圆形快门
- 快门在默认态、按压态、拍照触发态、视频待机态、视频录制态下均有完整视觉定义
- 模式切换过程中快门表现平滑，无明显跳变
- 椭圆快门在视觉上较旧方案释放更多底部空间感，并保持主按钮识别度

### 11.2 工具栏呼出优化

- 用户可通过右下角开关在热区内稳定呼出工具栏
- 工具栏呼出与收起路径清晰，操作成功率高
- 该能力在各主模式下均可正常使用

### 11.3 Slider 字体统一

- Zoom Slider、Filter Slider、Portrait Mode Aperture Slider、Exposure Slider 及其他数字型 Slider 均完成统一字体替换
- 数字在不同场景下保持良好辨识度
- 字体替换后无错位、截断、重叠或排版异常

### 11.4 相机主界面结构

- 照片、视频、前置自拍及 16:9 场景均按设计稿完成预览、模式区和底部控件布局适配，无重叠、越界或不可点击区域
- Preset 可通过左下入口点击进入选择；模式栏支持拖动选择，二者手势不冲突
- 设置入口可稳定展开和收起底部设置面板；浮层打开时快门仍可正常使用
- 圆角、半透明和背景模糊在明暗、复杂取景背景下均保持可读；降级路径无闪烁或黑块

### 11.5 Effect Discovery

- Preset Library 网格卡片信息完整，滚动、选择、关闭与异常恢复路径可用
- AI Preset 推荐不阻塞拍摄主流程，支持一键应用和撤销；撤销后效果状态恢复正确

### 11.6 Expert / Pro Features

- EV、ISO、S、WB、F 的入口、当前值、自动/手动状态与 Slider 调节结果一致
- Expert 参数面板展开时，焦段、快门、直方图、模式切换和图库入口可正常使用
- Style 完成 Tuning 与 Filter 的统一入口，效果选择、色板、强度、返回与重置链路完整
- 旧版本已有 Filter/Tuning 数据或默认配置升级后不丢失；若无法兼容，需按确认后的迁移或重置策略执行

## 正式设计稿（Camera 5.1）

[模式栏下移 / 快速切换模式](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=257-6455&p=f)

[16:9 布局调整](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=257-7011&p=f)

[取景器圆角常驻](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=257-7869&p=f)

[半透明高斯模糊](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=257-8197&p=f)

[快门形状](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=257-9566&p=f)

[工具面板优化](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=257-10327&p=f)