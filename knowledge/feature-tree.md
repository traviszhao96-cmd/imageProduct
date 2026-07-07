# Camera 业务树

> 主干 = 交互层级，对齐 23112 相机体验验收表分组
> `purpose` = 交叉维度标签，用于按功能用途检索
> `[TBD]` = 归属待 PM 确认

## 使用约定

- AI 写 PRD 时，先查主干确认功能在哪个交互位置
- AI 做影响分析时，用 `purpose` 标签找出同类功能
- 新增功能挂载到正确的交互位置，同时打 purpose 标签
- 写 Feature List 时，`快门区域` 不展开为功能行；快门按键、相册缩略图、前后摄像头翻转按键是所有相机都有的基础入口
- 写 Feature List 时，`Preset` 和 `Settings` 归入 `模式=通用`，不要在每个拍摄模式下重复写一遍

---

## 业务树

```
Camera App
│
├── 0. 启动与退出
│   ├── 冷启动（点击图标打开）
│   ├── 热启动（后台恢复）
│   ├── 关闭（上滑/返回/左滑）
│   └── 息屏显示（预览息屏 / 录制息屏）
│
├── 1. 预览框
│   ├── 预览基础
│   │   ├── 预览一致性（与成片对齐）
│   │   ├── 预览动态范围                      purpose: 图像处理
│   │   ├── 自动亮度提升（可禁用）             purpose: 系统
│   │   └── HDR 显示（照片 / 视频）
│   │
│   ├── 场景检测
│   │   ├── 普通场景检测                      purpose: 拍摄辅助
│   │   ├── AI 场景检测                       purpose: 拍摄辅助
│   │   ├── 脏污检测                          purpose: 拍摄辅助
│   │   ├── 人脸检测                          purpose: 拍摄辅助
│   │   ├── 运动检测                          purpose: 拍摄辅助
│   │   └── 脚架检测                          purpose: 拍摄辅助
│   │
│   └── 畸变矫正（光学 / 人脸）               purpose: 硬件
│
├── 2. AE/AF Box（对焦与曝光）
│   ├── Touch AE/AF                          purpose: 拍摄
│   ├── Face AE/AF                           purpose: 拍摄
│   ├── Touch AE/AF Lock                     purpose: 拍摄
│   ├── CAF（连续自动对焦）                   purpose: 拍摄
│   ├── EV+-（曝光补偿）                      purpose: 拍摄
│   ├── 滑动曝光调整                          purpose: 拍摄
│   └── PDAF（2x2 OCoL）                      purpose: 硬件
│
├── 3. Zoom（变焦）
│   ├── 点击光变点                            purpose: 拍摄
│   ├── 滑动变焦条                            purpose: 拍摄
│   ├── 双指缩放                              purpose: 拍摄
│   ├── 长焦预览框（画中画）                   purpose: 拍摄辅助
│   ├── SAT（平滑镜头切换）                   purpose: 拍摄
│   ├── ISZ（In Sensor Zoom）                 purpose: 硬件
│   ├── SR 超分                               purpose: 算法
│   └── EIS / OIS                             purpose: 硬件
│
├── 4. 暂态开关（左右暂态区）
│   ├── 左侧暂态开关
│   │   └── 自动微距控制（Macro Control）       purpose: 拍摄辅助 / 硬件
│   │       └── 前提：仅 Fallback 机型（25111+）。关闭后不切微距镜头。
│   │
│   └── 右侧暂态开关
│       ├── 夜景开关（Night Mode）              purpose: 拍摄辅助
│       └── AI Zoom 开关                       purpose: 算法
│
├── 5. 快门区域（Feature List 不展开）
│   ├── 快门按键
│   ├── 相册缩略图
│   └── 前后摄像头翻转按键
│
├── 6. Top Toolbar（下拉工具栏）
│   ├── Flash（Off / On / Torch / Auto / Glyph） purpose: 拍摄辅助
│   ├── Timer（Off / 3s / 10s）                purpose: 拍摄辅助
│   ├── HDR（Auto / 关）                       purpose: 图像处理
│   ├── Exposure（-2EV ~ +2EV, 0.3EV step）    purpose: 拍摄
│   ├── 滤镜                                  purpose: 图像处理
│   │   ├── 15 个内置 LUT                     see: filter.md
│   │   ├── 滤镜强度（0-100）                  purpose: 图像处理
│   │   └── 自定义 LUT 导入                    purpose: 个性化
│   ├── Tuning（调色，7 参数）                  purpose: 图像处理
│   │   see: tuning.md
│   ├── 动态照片开关                          purpose: 拍摄
│   ├── Quality（20MP / 50MP / 200MP）         purpose: 拍摄 / 硬件
│   ├── 网格线                                purpose: 拍摄辅助
│   ├── 比例（1:1 / 4:3 / 16:9 / FULL）       purpose: 拍摄辅助
│   ├── Watermark                             purpose: 个性化
│   ├── Glyph Mirror                          purpose: 品牌特性 / 硬件
│   ├── 运动抓拍                              purpose: 拍摄
│   └── 更多（进入次级菜单）
│
├── 7. Mode Switch（模式栏）
│   ├── 拍照                                  purpose: 拍摄
│   ├── 人像                                  purpose: 拍摄
│   │   ├── 虚化（bokeh style）
│   │   ├── 光斑
│   │   └── 美颜
│   ├── 夜景                                  purpose: 拍摄
│   ├── 视频                                  purpose: 拍摄
│   │   ├── 规格切换
│   │   ├── HDR 视频
│   │   ├── 防抖
│   │   └── 前后双录
│   ├── 慢镜头                                purpose: 拍摄
│   ├── 延时摄影                              purpose: 拍摄
│   ├── 专业模式                              purpose: 拍摄
│   ├── 全景                                  purpose: 拍摄
│   ├── Action（运动抓拍）                     purpose: 拍摄
│   ├── 文档矫正                              purpose: 拍摄
│   └── 高像素（50MP）                         purpose: 拍摄
│
├── 8. Preset（预设，Feature List 使用 模式=通用）
│   ├── Preset 选择器（底部栏）
│   ├── 快速保存（修改后保存）
│   ├── 卡片信息展示                          purpose: 个性化
│   │   ├── 作者 / 模式 / 焦段
│   │   └── 滤镜缩写 / 曝光
│   ├── 封面编辑                              purpose: 个性化
│   ├── 导入 / 分享                           purpose: 个性化
│   └── 默认 Preset 列表                      see: preset.md
│
├── 9. Settings（设置页，Feature List 使用 模式=通用）
│   ├── General
│   │   ├── Preset
│   │   ├── Save location                      purpose: 系统
│   │   ├── Shutter sound                      purpose: 系统
│   │   ├── Mirror front camera                purpose: 系统
│   │   └── Level                              purpose: 拍摄辅助
│   │
│   ├── Photo
│   │   ├── Watermark                          purpose: 个性化
│   │   ├── Auto Tone                          purpose: 图像处理
│   │   ├── Tap to take a photo                purpose: 拍摄
│   │   ├── QR code scanner                    purpose: 拍摄辅助
│   │   ├── Press and hold shutter             purpose: 系统
│   │   └── Ultra XDR                          purpose: 图像处理
│   │
│   └── Video
│       ├── Video encoding（H.264 / H.265）    purpose: 系统
│       ├── Power saving recording             purpose: 系统
│       └── Auto FPS（Off / Auto 30 / Auto 30&60） purpose: 系统
│
├── 10. 系统级交互
│   ├── 双击电源键快启                        purpose: 系统
│   ├── 锁屏快捷入口                          purpose: 系统
│   ├── 三方应用分享                           purpose: 系统
│   ├── 震动反馈                              purpose: 系统
│   └── Widget（桌面小组件）                   purpose: 系统
│
└── 11. 相册联动
    ├── HDR 照片显示
    ├── 超 HDR（XDR）显示
    ├── 编辑跳转
    └── 视频播放
```

---

## 交叉维度：按功能目的检索

### 图像处理
| 功能 | 交互位置 |
|------|------|
| 滤镜 + 强度 | Top Toolbar |
| Tuning（7参数调色）| Top Toolbar |
| HDR | Top Toolbar |
| Auto Tone | Settings → Photo |
| 美颜 | Mode Switch → 人像 |
| 虚化 / 光斑 | Mode Switch → 人像 |

### 拍摄
| 功能 | 交互位置 |
|------|------|
| 人像 / 夜景 / 视频 / 慢镜头 / 延时 | Mode Switch |
| 全景 / 专业 / Action / 文档矫正 | Mode Switch |
| 动态照片 | Top Toolbar |
| Tap to take a photo | Settings → Photo |

### 拍摄辅助
| 功能 | 交互位置 |
|------|------|
| 场景检测 / 人脸检测 / 运动检测 | 预览框 |
| Touch AE/AF / Face AE/AF | AE/AF Box |
| 变焦 / SAT / 超分 | Zoom |
| Flash / Timer / Grid / Ratio | Top Toolbar |
| Level | Settings → General |
| QR code scanner | Settings → Photo |

### 个性化
| 功能 | 交互位置 |
|------|------|
| Preset（默认+自定义）| Preset（模式=通用） |
| Watermark 快捷开关 | Top Toolbar |
| Watermark 详细设置 | Settings → Photo |
| 自定义 LUT 导入 | Top Toolbar → 滤镜 |
| Preset 卡片信息 | Preset |

### 硬件/系统
| 功能 | 交互位置 |
|------|------|
| OIS / EIS / ISZ | Zoom |
| PDAF | AE/AF Box |
| 畸变矫正 | 预览框 |
| Quality（20MP / 50MP / 200MP） | Top Toolbar |
| Glyph Mirror | Top Toolbar |
| Shutter sound / Save location / Mirror front camera | Settings → General |
| Video encoding / Power saving recording / Auto FPS | Settings → Video |
| 息屏 / 快启 / Widget | 系统级 |
