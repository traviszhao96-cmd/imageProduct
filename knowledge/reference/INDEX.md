# Camera Feature Reference — PRD 索引

自动从 _raw/prd/ 整理。按功能组分类。

## 功能定义
| 文档 | 说明 |
|------|------|
| [memory-mutex.json](memory-mutex.json) | 记忆规则（5min记忆逻辑，45项功能）× 互斥逻辑（20条规则），v2.0，25111 MP1.5 基线 |
| [kb-functions-algorithms-schema.md](kb-functions-algorithms-schema.md) | KB Functions Algorithms 总表 schema、去重原则、生成流程 |
| [feature-list-layout-common-rules.md](feature-list-layout-common-rules.md) | FL 功能栏布局、通用功能、Preset/Settings 展开规则 |
| [mode-zoom-transient-rules.md](mode-zoom-transient-rules.md) | 模式栏、变焦栏、左右暂态开关规则 |
| [photo-top-toolbar-rules.md](photo-top-toolbar-rules.md) | Photo 模式 Top Toolbar 功能项与判断规则 |

## 算法说明书
| 文档 | 适用项目 |
|------|---------|
| [algorithms-5a.md](algorithms-5a.md) | Phone (5a) — 26111 + 26121 |
| [algorithm-fl-source-26111-26121.md](algorithm-fl-source-26111-26121.md) | 26111 / 26121 FL 算法行导入源 |
| [_raw/25111-影像软件设计方案-ocr.md](_raw/25111-影像软件设计方案-ocr.md) | 25111 PDF OCR 原始转写 + 页面图 |
| [_raw/25131-算法链路-ocr.md](_raw/25131-算法链路-ocr.md) | 25131 PDF OCR 原始转写 + 页面图 |

## Default Preset
| 文档 | 说明 |
|------|------|
| [presets/README.md](presets/README.md) | 全部 preset 对比表（v3.3） |
| [presets/v3.3-sports.md](presets/v3.3-sports.md) | v3.3 +Sports 完整详情（12 个 preset + 封面图） |
| 原始 xlsx | `~/Downloads/Default preset v3.2.xlsx` (65MB, 含 v3.2/v3.1/v3.0/v2.1/v1.0) |

## 4.1 版本
| PRD | 功能组 | 文件 |
|-----|--------|------|
| 视频前后双录 | video | `video/dual-recording.md` |
| Preset x Widget 2.0 | preset | `preset/preset-widget-2.0.md` |
| Preset 导入上限提升 | preset | `preset/import-limit.md` |
| 水印样式更新 | watermark | `watermark/style-update-4.1.md` |
| Disco / DV 特效滤镜 | filter | `filter/disco-dv.md` |

## 5.0 版本
| PRD | 功能组 | 文件 |
|-----|--------|------|
| 工具栏 & slider 优化 | ui | `ui/toolbar-slider-5.0.md` |
| 对焦框视觉优化 | ui | `ui/focus-frame-5.0.md` |
| 相机按键视觉与动效 | ui | `ui/button-animation-5.0.md` |
| 二维码识别交互优化 | qrcode | `qrcode/interaction-5.0.md` |
| 日韩SKU快门声逻辑 | region | `region/jp-kr-shutter-5.0.md` |
