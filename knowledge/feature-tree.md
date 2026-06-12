# Camera 业务树

> 主干 = 交互层级，对齐 23112 相机体验验收表分组
> `purpose` = 交叉维度标签，用于按功能用途检索
> `[TBD]` = 归属待 PM 确认

## 使用约定

- AI 写 PRD 时，先查主干确认功能在哪个交互位置
- AI 做影响分析时，用 `purpose` 标签找出同类功能
- 新增功能挂载到正确的交互位置，同时打 purpose 标签

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
├── 4. Shutter（快门）
│   ├── 拍照                                  purpose: 拍摄
│   ├── 连拍（长按）                           purpose: 拍摄
│   ├── 快录（长按视频）                       purpose: 拍摄
│   ├── 动态照片（Motion Photo）               purpose: 拍摄
│   │   ├── 封面帧 HDR
│   │   ├── 无效信息截取
│   │   ├── 录制声音
│   │   └── 重选帧
│   └── 快门声（日韩 SKU 特殊逻辑）             purpose: 系统
│
├── 5. Top Toolbar（下拉工具栏）
│   ├── 闪光灯（Flash）                        purpose: 拍摄辅助
│   ├── Glyph 灯 / 补光                        purpose: 拍摄辅助 / 品牌特性
│   ├── 倒计时（3s / 5s / 10s）                purpose: 拍摄辅助
│   ├── HDR（Auto / 关）                       purpose: 图像处理
│   ├── 手动曝光                              purpose: 拍摄
│   ├── 滤镜                                  purpose: 图像处理
│   │   ├── 15 个内置 LUT                     see: filter.md
│   │   ├── 滤镜强度（0-100）                  purpose: 图像处理
│   │   └── 自定义 LUT 导入                    purpose: 个性化
│   ├── Auto Tone                             purpose: 图像处理
│   ├── 照片风格（鲜明 / 自然）                 purpose: 图像处理 / ISP
│   ├── Tuning（调色，7 参数）                  purpose: 图像处理
│   │   see: tuning.md
│   ├── 动态照片开关                          purpose: 拍摄
│   ├── 高像素（50MP）                         purpose: 拍摄 / 硬件
│   ├── 网格线                                purpose: 拍摄辅助
│   ├── 比例（1:1 / 4:3 / 16:9 / FULL）       purpose: 拍摄辅助
│   ├── 色彩模式                              purpose: 图像处理
│   ├── 运动抓拍                              purpose: 拍摄
│   └── 更多（进入次级菜单）
│
├── 6. Mode Switch（模式栏）
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
├── 7. Gallery（相册缩略图）
│   ├── 点击进入相册
│   ├── 相册返回相机
│   └── 拍照后缩略图更新
│
├── 8. Preset（预设）
│   ├── Preset 选择器（底部栏）
│   ├── 快速保存（修改后保存）
│   ├── 卡片信息展示                          purpose: 个性化
│   │   ├── 作者 / 模式 / 焦段
│   │   └── 滤镜缩写 / 曝光
│   ├── 封面编辑                              purpose: 个性化
│   ├── 导入 / 分享                           purpose: 个性化
│   └── 默认 Preset 列表                      see: preset.md
│
├── 9. Settings（设置页）
│   ├── 水印                                  purpose: 个性化
│   │   ├── 文字水印 / 画框水印
│   │   ├── 自定义文字 / 日期 / 位置 / 参数
│   │   └── HDR 照片兼容
│   ├── 水平仪                                purpose: 拍摄辅助
│   ├── 网格线                                purpose: 拍摄辅助
│   ├── 快门声音开关                          purpose: 系统
│   ├── 连拍开关（连拍/快录）                   purpose: 系统
│   ├── 记忆规则                              purpose: 系统
│   ├── 预设记忆（5min）                       purpose: 系统
│   ├── 音量键功能                            purpose: 系统
│   ├── 防闪烁                                purpose: 系统
│   └── 位置信息                              purpose: 系统
│
├── 10. 系统级交互
│   ├── 双击电源键快启                        purpose: 系统
│   ├── 锁屏快捷入口                          purpose: 系统
│   ├── 二维码扫描                            purpose: 拍摄辅助
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
| 照片风格（鲜明/自然）| Top Toolbar |
| HDR / Auto Tone | Top Toolbar |
| 色彩模式 | Top Toolbar |
| 美颜 | Mode Switch → 人像 |
| 虚化 / 光斑 | Mode Switch → 人像 |

### 拍摄
| 功能 | 交互位置 |
|------|------|
| 拍照 / 连拍 / 快录 | Shutter |
| 人像 / 夜景 / 视频 / 慢镜头 / 延时 | Mode Switch |
| 全景 / 专业 / Action / 文档矫正 | Mode Switch |
| 动态照片 | Shutter |

### 拍摄辅助
| 功能 | 交互位置 |
|------|------|
| 场景检测 / 人脸检测 / 运动检测 | 预览框 |
| Touch AE/AF / Face AE/AF | AE/AF Box |
| 变焦 / SAT / 超分 | Zoom |
| 闪光灯 / Glyph / 倒计时 / 网格 / 比例 | Top Toolbar |
| 水平仪 | Settings |
| 二维码扫描 | 系统级 |

### 个性化
| 功能 | 交互位置 |
|------|------|
| Preset（默认+自定义）| Preset |
| 水印 | Settings / Top Toolbar |
| 自定义 LUT 导入 | Top Toolbar → 滤镜 |
| Preset 卡片信息 | Preset |

### 硬件/系统
| 功能 | 交互位置 |
|------|------|
| OIS / EIS / ISZ | Zoom |
| PDAF | AE/AF Box |
| 畸变矫正 | 预览框 |
| 快门声 / 记忆规则 | Settings |
| 息屏 / 快启 / Widget | 系统级 |
