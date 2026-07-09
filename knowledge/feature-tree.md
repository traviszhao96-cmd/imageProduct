# Camera 业务树

> 主干 = 交互层级，对齐 23112 相机体验验收表分组  
> `purpose` = 交叉维度标签，用于按功能用途检索  
> `[TBD]` = 归属待 PM 确认

## 使用约定

- AI 写 PRD 时，先查主干确认功能在哪个交互位置
- AI 做影响分析时，用 `purpose` 标签找出同类功能
- 新增功能挂载到正确的交互位置，同时打 purpose 标签
- 写 Feature List 时，`快门区域` 不展开为功能行；快门按键、相册缩略图、前后摄像头翻转按键是所有相机都有的基础入口
- 写 Feature List 时，`Preset`、`Settings`、`Widget` 使用 `模式=通用 / Common`，并分别作为 `一级分类=预设 / Preset`、`设置 / Settings`、`小组件 / Widget`；不要在每个拍摄模式下重复写一遍
- 写 Feature List 时，模式、一级分类、二级分类都使用双语枚举，例如 `照片 / Photo`、`设置 / Settings`、`预览框 / Preview`

---

## 业务树

```
Camera App
│
├── 0. 启动与退出 / Launch & Exit
│   ├── 冷启动 / Cold Launch（点击图标打开）
│   ├── 热启动 / Hot Launch（后台恢复）
│   ├── 关闭 / Close（上滑/返回/左滑）
│   └── 息屏显示 / AOD（预览息屏 / 录制息屏）
│
├── 1. 预览框 / Preview Box
│   ├── 预览基础 / Preview Basics
│   │   ├── 预览一致性 / Preview Consistency（与成片对齐）
│   │   ├── 预览动态范围 / Preview Dynamic Range   purpose: 图像处理
│   │   ├── 自动亮度提升 / Auto Brightness（可禁用） purpose: 系统
│   │   └── HDR 显示 / HDR Display（照片 / 视频）
│   │
│   ├── 场景检测 / Scene Detection
│   │   ├── ASD / AI 场景检测 / AI Scene Detection purpose: 拍摄辅助
│   │   ├── 脏污检测 / Dirt Detection             purpose: 拍摄辅助
│   │   ├── 人脸检测 / Face Detection             purpose: 拍摄辅助
│   │   └── 脚架检测 / Tripod Detection           purpose: 拍摄辅助
│   │
│   └── 畸变矫正 / Distortion Correction（光学 / 人脸） purpose: 硬件
│
├── 2. AE/AF Box / AE/AF Box（对焦与曝光）
│   ├── Touch AE/AF                          purpose: 拍摄
│   ├── Face AE/AF                           purpose: 拍摄
│   ├── Touch AE/AF Lock                     purpose: 拍摄
│   ├── CAF / CAF（连续自动对焦）              purpose: 拍摄
│   ├── EV+- / EV+-（曝光补偿）                purpose: 拍摄
│   ├── 滑动曝光调整 / Sliding Exposure        purpose: 拍摄
│   └── PDAF / PDAF（2x2 OCoL）               purpose: 硬件
│
├── 3. Zoom / Zoom（变焦）
│   ├── 点击光变点 / Tap Optical Zoom          purpose: 拍摄
│   ├── 滑动变焦条 / Slider Zoom               purpose: 拍摄
│   ├── 双指缩放 / Pinch Zoom                  purpose: 拍摄
│   ├── 长焦预览框 / Tele PIP（画中画）         purpose: 拍摄辅助
│   ├── SAT / SAT（平滑镜头切换）              purpose: 拍摄
│   ├── ISZ / ISZ（In Sensor Zoom）            purpose: 硬件
│   ├── SR 超分 / SR Super Resolution          purpose: 算法
│   └── EIS / OIS                             purpose: 硬件
│
├── 4. 暂态开关 / Transient Switches（左右暂态区）
│   ├── 左侧暂态开关 / Left Transient
│   │   └── 自动微距控制 / Macro Control       purpose: 拍摄辅助 / 硬件
│   │       └── 前提：仅 Fallback 机型（25111+）。关闭后不切微距镜头。
│   │
│   └── 右侧暂态开关 / Right Transient
│       ├── 夜景开关 / Night Mode              purpose: 拍摄辅助
│       ├── AI Zoom 开关 / AI Zoom Switch      purpose: 算法
│       └── 文本模式 / Text Mode               purpose: 算法
│
├── 5. 快门区域 / Shutter Area（Feature List 不展开）
│   ├── 快门按键 / Shutter Button
│   ├── 相册缩略图 / Gallery Thumbnail
│   └── 前后摄像头翻转按键 / Flip Camera
│
├── 6. Toolbar / Toolbar（下拉工具栏）
│   ├── 照片工具栏 / Photo Toolbar
│   │   ├── Flash / 闪光灯（Off / On / Torch / Auto / Glyph） purpose: 拍摄辅助
│   │   ├── Timer / Timer（Off / 3s / 10s）          purpose: 拍摄辅助
│   │   ├── HDR / HDR（Auto / 关）                    purpose: 图像处理
│   │   ├── Exposure / Exposure（-2EV ~ +2EV, 0.3EV step） purpose: 拍摄
│   │   ├── Style / Style（滤镜 + 调色 + 调色盘合并）
│   │   │   ├── 滤镜 / Filters（15 个内置 LUT + 强度 + 自定义导入）see: filter.md
│   │   │   ├── 调色 / Tuning（7 参数）               see: tuning.md
│   │   │   └── 调色盘 / Tuning Palette             purpose: 图像处理 / 个性化
│   │   ├── 动态照片开关 / Motion Photo             purpose: 拍摄
│   │   ├── Quality / Quality（20MP / 50MP / 200MP） purpose: 拍摄 / 硬件
│   │   ├── 网格线 / Grid Lines                     purpose: 拍摄辅助
│   │   ├── 比例 / Aspect Ratio（1:1/4:3/16:9/FULL）purpose: 拍摄辅助
│   │   ├── Watermark / Watermark                   purpose: 个性化
│   │   ├── Glyph Mirror / Glyph Mirror             purpose: 品牌特性 / 硬件
│   │   └── 更多 / More（进入次级菜单）
│   └── 视频工具栏 / Video Toolbar
│       ├── Flash / Flash
│       ├── 滤镜 / Filters
│       ├── 白平衡 / White Balance
│       ├── 曝光调节 / Exposure Adjustment
│       ├── 规格切换 / Resolution Switch
│       ├── HDR 视频 / HDR Video
│       └── 防抖 / Stabilization
│
├── 7. Mode Switch / Mode Switch（模式栏）
│   ├── 拍照 / Photo                           purpose: 拍摄
│   ├── 人像 / Portrait                        purpose: 拍摄
│   │   ├── 虚化 / Bokeh（bokeh style）
│   │   ├── 光斑 / Lens Flare
│   │   └── 美颜 / Beauty
│   ├── 夜景 / Night                           purpose: 拍摄
│   ├── 视频 / Video                           purpose: 拍摄
│   │   └── 前后双录 / Dual Recording
│   ├── 慢镜头 / Slow Motion                   purpose: 拍摄
│   ├── 延时摄影 / Timelapse                   purpose: 拍摄
│   ├── 专业模式 / Expert Mode                 purpose: 拍摄
│   ├── 全景 / Panorama                        purpose: 拍摄
│   ├── Action / Action（运动抓拍）             purpose: 拍摄
│   ├── 文档矫正 / Document Scan               purpose: 拍摄
│   └── 高像素 / High Resolution               purpose: 拍摄
│
├── 8. 通用 / Common（Feature List 使用 模式=通用 / Common）
│   ├── Preset / 预设
│   │   FL: 一级分类=预设 / Preset；二级分类=预设 / Preset
│   │   ├── Preset 选择器 / Preset Selector（底部栏）
│   │   ├── 快速保存 / Quick Save（修改后保存）
│   │   ├── 卡片信息展示 / Card Info            purpose: 个性化
│   │   │   ├── 作者/模式/焦段 / Author/Mode/Focal
│   │   │   └── 滤镜缩写/曝光 / Filter/Exposure
│   │   ├── 封面编辑 / Cover Edit               purpose: 个性化
│   │   ├── 导入/分享 / Import/Share            purpose: 个性化
│   │   └── 默认 Preset 列表 / Default Preset List see: preset.md
│   │
│   ├── Settings / Settings（设置页）
│   │   FL: 一级分类=设置 / Settings；二级分类按设置分组展开
│   │   ├── General / 通用设置
│   │   │   FL: 二级分类=通用设置 / General Settings
│   │   │   ├── Preset / 预设
│   │   │   ├── Save location                  purpose: 系统
│   │   │   ├── Shutter sound                  purpose: 系统
│   │   │   ├── Mirror front camera            purpose: 系统
│   │   │   └── Level                          purpose: 拍摄辅助
│   │   │
│   │   ├── Photo / 照片
│   │   │   FL: 二级分类=照片设置 / Photo Settings
│   │   │   ├── Watermark                      purpose: 个性化
│   │   │   ├── Auto Tone                      purpose: 图像处理
│   │   │   ├── Tap to take a photo            purpose: 拍摄
│   │   │   ├── QR code scanner                purpose: 拍摄辅助
│   │   │   ├── Press and hold shutter         purpose: 系统
│   │   │   └── Ultra XDR                      purpose: 图像处理
│   │   │
│   │   ├── Video / 视频
│   │   │   FL: 二级分类=视频设置 / Video Settings
│   │   │   ├── Video encoding / 视频编码（H.264/H.265） purpose: 系统
│   │   │   ├── Power saving recording          purpose: 系统
│   │   │   └── Auto FPS / Auto FPS（Off/Auto 30/Auto 30&60） purpose: 系统
│   │   │
│   │   └── Help & Support / Help & Support
│   │       FL: 二级分类=帮助与反馈 / Help & Support
│   │       └── Tips and feedback               purpose: 系统
│   │
│   └── Widget / 桌面小组件
│       FL: 一级分类=小组件 / Widget；二级分类=小组件 / Widget
│       └── Preset Widget                      purpose: 系统 / 个性化
│
├── 9. 系统级交互 / System Interactions
│   ├── 双击电源键快启 / Double-Press Power     purpose: 系统
│   ├── 锁屏快捷入口 / Lock Screen Shortcut     purpose: 系统
│   ├── 三方应用分享 / Share to Apps            purpose: 系统
│   └── 震动反馈 / Haptic Feedback              purpose: 系统
│
└── 10. 相册联动 / Gallery Integration
    ├── Ultra HDR 显示 / Ultra HDR（XDR）Display
    ├── 编辑跳转 / Jump to Edit
    └── 视频播放 / Video Playback
```

---

## 交叉维度：按功能目的检索

### 图像处理

| 功能            | 交互位置             |
| ------------- | ---------------- |
| 滤镜 + 强度       | Toolbar          |
| Tuning（7参数调色） | Toolbar          |
| HDR           | Toolbar          |
| Auto Tone     | Settings → Photo |
| 美颜            | Mode Switch → 人像 |
| 虚化 / 光斑       | Mode Switch → 人像 |

### 拍摄

| 功能                      | 交互位置             |
| ----------------------- | ---------------- |
| 人像 / 夜景 / 视频 / 慢镜头 / 延时 | Mode Switch      |
| 全景 / 专业 / Action / 文档矫正 | Mode Switch      |
| 动态照片                    | Toolbar          |
| Tap to take a photo     | Settings → Photo |

### 拍摄辅助

| 功能                           | 交互位置               |
| ---------------------------- | ------------------ |
| ASD / AI 场景检测 / 人脸检测         | 预览框                |
| Touch AE/AF / Face AE/AF     | AE/AF Box          |
| 变焦 / SAT / 超分                | Zoom               |
| Flash / Timer / Grid / Ratio | Toolbar            |
| Level                        | Settings → General |
| QR code scanner              | Settings → Photo   |

### 个性化

| 功能             | 交互位置             |
| -------------- | ---------------- |
| Preset（默认+自定义） | Preset（模式=通用）    |
| Watermark 快捷开关 | Toolbar          |
| Watermark 详细设置 | Settings → Photo |
| 自定义 LUT 导入     | Toolbar → 滤镜     |
| Preset 卡片信息    | Preset           |

### 硬件/系统

| 功能                                                  | 交互位置               |
| --------------------------------------------------- | ------------------ |
| OIS / EIS / ISZ                                     | Zoom               |
| PDAF                                                | AE/AF Box          |
| 畸变矫正                                                | 预览框                |
| Quality（20MP / 50MP / 200MP）                        | Toolbar            |
| Glyph Mirror                                        | Toolbar            |
| Shutter sound / Save location / Mirror front camera | Settings → General |
| Video encoding / Power saving recording / Auto FPS  | Settings → Video   |
| 息屏 / 快启 / Widget                                    | 系统级                |
