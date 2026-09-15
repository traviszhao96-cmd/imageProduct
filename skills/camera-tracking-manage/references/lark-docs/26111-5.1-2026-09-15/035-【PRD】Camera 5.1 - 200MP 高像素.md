<!-- source: https://nothing-tech.sg.larksuite.com/docx/YhNXdLBV6o1kfoxFVGOlXzyCgEf | fetched: 2026-09-15 | revision: 87 -->
# 【PRD】Camera 5.1 - 200MP 高像素

## 一、版本信息

版本号：**2.0** | 上一版：1.1 (Lia, 2025/10/23)

## 二、变更日志

| 时间 | 版本 | 变更人 | 主要变更内容 |
|-|-|-|-|
| 2025/10/23 | 1.0 | Lia | 创建文档 |
| 2026/06/11 | 1.1 | Lia | 补充产品定义、三档像素用户心智模型、待决事项 |
| 2026/07/02 | **2.0** | Travis / Codex | **重大更新**：① 修正技术流水线描述（200MP sensor → HW Remosaic → 50MP RAW HDR，非直出 200MP）；② 补充虹软可行性评估结论（7635 预计 7.4s、1.75GB 内存峰值、NZSL 强制）；③ 新增双套拍摄交互方案（A：预览保持+快门转圈 / B：预览暂停+分模块动画）；④ 标记 26121 (7750) 算法取消；⑤ 补充方案决策标准与待测指标 |

## 三、需求背景

### 产品 / 数据现状

26111 Base (Phone 5a) 首次采用 **200MP 三星 HP5** 主摄（SM7635 平台）。26121 Pro 复用 25111 Pro 相机配置（IMX896），不涉及 200MP。（SM7635 平台）。Sensor 支持通过 HW Remosaic 输出 50MP 标准 Bayer，技术流水线为：

> **200MP 模式：200MP sensor → HW Remosaic → 50MP RAW HDR（多帧融合）→ AI upscale → 200MP | 50MP 模式：200MP sensor → HW Remosaic → 50MP RAW HDR → 不跑 upscale → 50MP。两种模式共享 RAW 域算法流水线（多帧 HDR 合成），差异仅在于是否跑 AI upscale。输出均为 JPEG/HEIC，非 RAW 文件。**

用户选择 200MP 得到 200MP（50MP HDR + upscale），选择 50MP 得到 50MP（50MP HDR，不跑 upscale）。RAW 域算法指多帧融合在 RAW 域处理，非 RAW 文件输出。RAW 为独立功能，与本需求无关。

### 硬件与算法可行性（2026.07 更新）

来自虹软 & 极感技术评估（详见 KSP 文档：`【NT&虹软】TF 50MP方案 可行性评估`）：

| 指标 | 标准要求 | 7635 预估 | 风险 |
|-|-|-|-|
| 处理时长 | <3s | **7.4s** | ❌ 超标 2.5x |
| 算法内存（不含 buffer） | \~500MB | **800-900MB** | ❌ |
| 图像 Buffer（4 帧 50MP） | — | 400MB | — |
| 内存峰值（含后台） | — | **\~1.75GB** | ❌ 连锁杀后台/卡顿 |
| ZSL | 期望 | **不可用**（10 帧 buffer = 1GB） | 强制 NZSL |
| 预览体验 | 无卡顿 | NZSL 下预览定格 | ❌ 显性体验问题 |
| 功耗/温控 | — | 大型 HDR 算法拉高瞬时功耗，触发降频 | ❌ 降频 → 更慢 → 更卡 |

### 商务决策（2026.07.02 群同步）

| 项目 | SoC | 决策 |
|-|-|-|
| 26111 Base (Phone 5a) | SM7635 | **50MP 保留**，算法列表已交商务询价 |
| 26121 Pro (Phone 5a Pro) | SM7750 | **不涉及** — 复用 25111 Pro IMX896，无 200MP sensor |

### 竞品分析

（保持原 v1.1 内容，略）

## 四、需求范围

### 项目范围

- 首上项目：**仅 26111 Base**。26121 Pro 复用 25111 Pro IMX896，不具备 200MP sensor，不涉及本需求。
- 老项目回落：不支持，具体回落计划根据回落排期确认

### In Scope

- 在 50MP 高像素模式下新增 200MP 选项
- 200MP 拍摄中交互的 **A/B 两套方案**（见第五节）
- 拍摄中的操作限制规则
- 拍摄完成后的恢复逻辑
- 200MP 开关状态记忆规则
- 首次使用引导

### Out of Scope

- 26121 (7750)
- 算法选型（虹软 vs 极感，商务决定）
- RAW 文件输出（独立功能，与本需求无关）

## 五、功能详细说明

### 5.1 入口与开关

模式位置：Mode Switch 独立入口「高像素」。顶部工具栏常驻当前分辨率规格，支持切换。照片模式移除 Quality（像素选择），专业模式保留。

feature-tree 挂载：`Top Toolbar | 高像素（200MP）`，purpose: `拍摄 / 硬件`

首次进入相机时，对 200MP 入口做引导说明（弹窗/气泡），管理用户对拍摄时长的预期。

### 5.2 像素规格与算法路径（独立高像素模式）

新增独立「高像素」模式入口（Mode Switch），不在照片模式内作为 Quality 子选项。

**26111 8G 内存：**

| 规格 | 默认 | 算法路径 |
|-|-|-|
| 200MP Ultra | — | lux < 280 → 50MP RAW HDR → AI Upscale → 200MP。lux > 280 → 走常规 12.5MP。预览上帧约 700ms，会定住。后处理约 7s，走 pop 后台。点击快门终止待确认。 |
| 200MP | ✓ 默认 | 高亮环境 → 2亿直出（[TBD] Delevin：TFE clock 725MHz 限制，MIPI 速率超标，建议 50MP upscale）。中间亮度 → 50MP 插值 upscale。暗环境 → 12.5MP 插值 upscale。 |
| 50MP | — | 高亮 → 3 帧 RAW MMF。暗环境 → 12.5MP 插值。支援 1x / 2x ISZ（2x 待评估）。 |

**26111 6G 内存 & 其他项目：**

| 规格 | 说明 |
|-|-|
| 200MP Ultra | ✗ 不支持（待确认正式结果） |
| 200MP | 高亮 → 2亿直出（[TBD] Delevin，同上平台限制）。其他 → 走 12.5MP 插值。 |
| 50MP | 高亮 → 3 帧 RAW MMF（待评估）。暗环境 → 12.5MP 插值。 |

**26121 Pro（SM7750 / IMX896 + JN5 长焦）：**

| 规格 | 算法路径 |
|-|-|
| 50MP | HW Remosaic → 50MP HDR |
| 50MP Ultra | 50MP RAW HDR 全流程直出 |

> ⚠️ 平台限制（Delevin 评估）：SM7635 TFE clock 限 725MHz，200MP 直出 MIPI 速率超标，无法出图。平台不支持 remosaic，需外接三星库处理 200MP RAW，内存/性能/功耗大幅增加。建议策略：50MP 直出 upscale 到 200MP。200MP 直出待进一步评估。

> ⚠️ 200MP 模式下：上帧约 700ms，预览定格。后处理约 7s，走 pop 后台。是否支持点击快门取消拍照 — 待确认。上帧完成后可继续点快门 — 后续视情况考虑限制策略。

新增独立「高像素」模式入口（Mode Switch），不在照片模式内作为 Quality 子选项。

**26111 Base（SM7635 / 200MP HP5，无长焦）**

| 规格 | 流水线 | 说明 |
|-|-|-|
| 50MP | HW Remosaic → 50MP | 标准50MP高像素，不跑 HDR，默认 |
| 200MP | HW Remosaic → 200MP | 标准200MP高像素，不跑 HDR |
| 200MP Ultra | 50MP RAW HDR 全流程 → AI Upscale → 200MP | 最高画质，RAW 域算法全开 |

**26121 Pro（SM7750 / IMX896 主摄 + JN5 长焦，复用 25111 Pro 配置）**

| 规格 | 流水线 | 说明 |
|-|-|-|
| 50MP | HW Remosaic → 50MP | 标准高像素 |
| 50MP Ultra | 50MP RAW HDR 全流程直出 | RAW 域算法全开，大幅提升画质 |

> **Ultra 定义**：50MP 应用 RAW HDR 算法（虹软方案），动态范围显著优于普通 HDR。26111 将 RAW HDR 结果 AI Upscale 至 200MP 输出；26121 直接输出 50MP。

### 5.3 功能兼容情况

| 功能 | 200MP 兼容 | 说明 |
|-|-|-|
| HDR | ✓ | 走 HDR 多帧合成，插帧到高像素 |
| 夜景 | ✓ | 走夜景算法，插帧到高像素 |
| 滤镜 | ✓ | 同 25111 |
| Tuning | ✓ | 同 25111 |
| 变焦 | ✗ | 仅支持光变点（1x），双指缩放提示不可变焦 |
| Motion Photo | ✗ | 互斥，同 25111 |
| 水印 | ✓ | 同 25111 |
| Preset | ✓ | 创建 preset 时支持选择 12/50/200MP |
| RAW | ✗ | [TBD] 需评估文件大小（50MP RAW ≈ 95MB/张）和拍摄时长 |

> ⚠️ **内存风险**：⚠️ 平台限制（Delevin 评估）：SM7635 TFE clock 725MHz，200MP 直出 MIPI 超标。建议 50MP upscale 策略。200MP 直出、RAW支持待评估。6G 内存机型不支持 Ultra。

### 5.4 200MP 开关状态记忆

| 场景 | 行为 |
|-|-|
| 退出相机 <5min 重开 | 保持 200MP |
| 退出相机 >5min 重开 | 恢复默认（12MP） |
| 切到视频/人像等再切回 Photo | 保持 200MP |
| 切前置再切回后置 | 恢复默认（12MP） |
| 杀进程重开 | 恢复默认（12MP） |

### 5.5 拍摄交互 — 方案 A：预览保持 + 快门转圈

![The image shows the 108MP function description pop-up window. It includes a photo of a building and a pop-up window with the text "108MP" and a description: "You can switch to the 108MP mode to capture ultra-high-resolution photos, but there may be a short processing delay when shooting. For best results, please use single lighting conditions." The消失条件 (disappearance condition) is also mentioned: clicking the button or clicking outside the pop-up to close the panel.](https://feishu.cn/file/FNFFbCKDsoG7nfx2zhOlXfyxgZb)

**设计思路**：用户感知"还在相机里操作"，预览不中断。

**触发**：用户在 200MP 模式下点击快门。

**拍摄中状态**：

- **预览画面保持**：继续显示实时取景，不做冻结
- **快门按钮转圈动画**：圆形进度指示覆盖快门按钮
- **处理中文案**："Processing 200MP..."
- **不可操作**：切换摄像头 ✗ | 切换模式 ✗ | Top Toolbar ✗ | Gallery ✗ | 变焦 ✗ | 再次拍照 ✗
- **可操作**：点击快门 → **取消拍摄**（全部丢弃，不保存任何数据，释放 buffer）| Home/退出 → 后台继续处理，完成后通知栏提示

**完成**：转圈消失，快门恢复，缩略图更新，可继续拍摄。

**异常**：App 被杀 → 本次拍摄丢失。

**内存特征**：预览流持续占用 ISP 管线 + preview buffer，无额外节省。

<figure view-type="Preview"><source name="屏幕录制2026-07-07 20.07.38.mov" mime="video/quicktime" origin-height="1506.000000" origin-width="694.000000" size="26266441" token="Vt1obyJYFovuDWxurmDlkFDngGe"/></figure>

### 5.6 拍摄交互 — 方案 B：预览暂停 + 分模块点亮动画

**设计思路**：利用 NZSL 预览自然定格，主动释放预览内存，用动效撑过等待时间。

**触发**：同方案 A。

**拍摄中状态**：

- **预览冻结 + 截图**：按下快门瞬间截取当前预览帧作为静态占位图
- **预览流释放**：sensor 停预览管线或切回 12.5M 低功耗，释放 preview buffer
- **分模块依次点亮动效**：

  - 阶段 1（0s）：屏幕整体变暗 20%，中心显示"Processing 200MP..."
  - 阶段 2（\~1s）：Top Toolbar → Mode Switch → Zoom → 缩略图依次消隐（每个 150ms）
  - 阶段 3（\~2s+）：屏幕分 4 块区域（左上→右上→左下→右下），逐一亮起再变暗，循环播放，暗色背景，传达"系统在做大规模运算"
- **不可操作**：全部禁止（同方案 A + 预览区域不可交互）
- **取消方式**：无快门取消；Home/退出 → 后台处理

**完成**：动效结束，预览恢复，快门恢复，缩略图更新。

**异常**：同方案 A。

**内存特征**：释放 preview buffer + ISP 管线，减少预览流内存占用。具体节省量 [TBD — 评估中]。更适合内存紧张场景。



### 5.7 两方案对比

| 维度 | 方案 A | 方案 B |
|-|-|-|
| 预览画面 | 实时取景保持 | 冻结截图 |
| 动画 | 快门转圈 | 分模块依次点亮 |
| 用户取消 | ✅ 点快门取消 | ❌ 无法手动取消 |
| 内存开销 | 高（预览流保持） | 低（预览流释放） |
| 感知等待 | 长（预览可能有卡顿闪烁） | 中（动效转移注意力） |
| 恢复体验 | 快门恢复即继续拍 | 需等动效播完 |
| 适用场景 | 处理 <5s | 处理 >5s，内存紧张 |

### 5.8 方案决策标准

最终方案选择基于 **26111 7635 算法性能实测数据**：

| 指标 | 方案 A 更适用 | 方案 B 更适用 |
|-|-|-|
| 处理耗时 | <5s | ≥5s |
| 内存峰值（不含 preview） | <1.2GB | ≥1.2GB |
| 6G 内存机型是否支持 | 否 | 是 |

建议算法验证完成后，两套交互各做一版 Demo，PM + 开发共同决定。

## 六、待决事项

| # | 事项 | 状态 |
|-|-|-|
| 1 | 算法选型（虹软 vs 极感）最终确定 | [TBD — 商务询价中] |
| 2 | 200MP vs 50MP 实际清晰度差异 | [TBD — 实机验证] |
| 3 | 7635 平台实测处理时长与内存数据 | [TBD — 算法移植后测试] |
| 4 | RAW 文件大小和拍摄时长 | [TBD — 待评估] |
| 5 | 6G 内存机型是否支持 200MP | [TBD — 依赖实测内存] |
| 6 | Preview buffer 具体可释放量（方案 B） | [TBD — 开发确认] |

## 七、非功能需求

（保持原 v1.1 内容）

## 八、埋点

| 参数 | 说明 | 值 |
|-|-|-|
| pixel_mode | 高像素模式使用情况 | 50MP / 200MP |
| shot_algo | 高像素拍摄时走的算法 | HDR / MMF / Night |
| processing_duration | 处理耗时（ms） | 数值 |
| pixel_mode | 高像素模式 | 50MP / 200MP |

## 九、项目规划

- 26111 (7635)：50MP 保留，等算法商务结果
- 26121 Pro (7750)：不涉及（复用 25111 Pro 相机配置，主摄 IMX896）

⚠️ 7/14 更新：专业模式不再提供高像素入口，仅独立高像素模式支持高像素。拍照模式 + 专业模式均移除 Quality/高像素入口。

---

## ⚠️ 原版不清晰之处（v2.0 已修正）

| # | 问题 | 修正 |
|-|-|-|
| 1 | 文档标题和全文中"200MP"暗示 200MP 直出，实测是 50MP RAW HDR | 补充技术流水线说明 |
| 2 | 26121 (7750) 仍标记为支持项目 | 明确 26121 算法取消 |
| 3 | 处理时长写"3-5s"，实际评估 7.4s | 更新为 7.4s（实测数据待补充） |
| 4 | 只有一套交互方案（快门转圈+预览卡顿[待定]） | 拆为 A/B 两套明确方案 + 决策标准 |
| 5 | 内存约束没写，NZSL/ZSL 没提 | 补全性能约束 |
| 6 | HDR/夜景标 ✓ 兼容，但未说明这是主要内存压力源 | 增加内存风险提示 |
| 7 | "RAW 支持待评估"一直没结论 | 标注 [TBD]，补充文件大小估算 |
| 8 | 无方案决策标准，开发不知道按哪个做 | 增加实测数据驱动决策表 |