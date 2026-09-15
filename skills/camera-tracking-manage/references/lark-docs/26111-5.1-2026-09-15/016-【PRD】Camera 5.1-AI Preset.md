<!-- source: https://nothing-tech.sg.larksuite.com/docx/R6bPdX8BOoAQWfxaSGpllX6ngGg | fetched: 2026-09-15 | revision: 408 -->
# 【PRD】Camera 5.1 - AI Preset

> 文档状态: Draft | 版本: v1.13 | 更新: 2026-08-28 | 作者: Travis | 审核: [TBD]

---

## 变更日志

| 日期 | 版本 | 变更人 | 变更内容 |
|-|-|-|-|
| 2026/8/28 | 1.13 | Travis | 收敛 R6 保存规则：明确英文命名与同名编号、允许独立副本，并新增基于固定特征色准备专属封面的方案。 |
| 2026/8/28 | 1.12 | Travis | 新增 R6 长按保存 Preset 需求；同步更新范围、验收条件、成功指标与待确认项 |
| 2026/8/28 | 1.11 | Travis | 词条独立成章：新增「需求词条」章节，收录设置页与 Preset 保存弹窗本地化词条，R4/R5 改为引用该章；后续章节重新编号 |
| 2026/1/13 | 1.0 | Travis | 梳理大致 AI Preset 方案 |
| 2026/3/9 | 1.1 | Travis | 输出初版交互方案 |
| 2026/3/17 | 1.2 | Travis | 补充竞品分析内容 |
| 2026/7/31 | 1.4 | Travis | 补充顶部环境信息、ADRC 文案分级及滤镜固定映射逻辑 |
| 2026/8/3 | 1.5 | Travis | 明确本期 Preset 等同滤镜、Photo 模式范围，校正滤镜数量并清理空章节 |
| 2026/8/5 | 1.6 | Travis | 新增 Preset suggestions 设置开关与中英文文案；统一用户可见术语；明确 31 个实体滤镜、27 个推荐池及 4 个排除项；补充设置页视觉参考 |
| 2026/8/6 | 1.7 | Travis | 修复 v7 交付包：补齐 27 条 filters[]、27 个运行时 PNG、稳定随机与图片评分过滤接口，并附 v7.1 App-ready 正式包 |
| 2026/8/6 | 1.8 | Travis | 统一中文界面使用“预设”；补齐设置开关、顶部色温与光线状态、右侧风格描述的中英文文案及双语元数据规则 |
| 2026/8/6 | 1.9 | Travis | 根据设计评审调整语言策略：设置页继续本地化；顶部环境信息、右侧风格说明与底部推荐名称改为所有语言固定英文，并移除推荐区中文风格映射 |
| 2026/8/6 | 1.10 | Travis | 统一当前开发口径为 27 个推荐滤镜（网络 11、原生相机 9、AI 场景 7）；主映射表删除 Cold、709通用轻创意、Noir、33portra400-2，并与 App-ready 规则包及 Manifest 对齐 |

---

## 1. 背景与目标

### 问题陈述

本期 AI Preset 面向普通拍照用户解决滤镜选择成本高的问题。用户面对数十个滤镜时缺乏明确依据，不知道哪一种更适合当前画面；系统通过场景分析前置推荐 4 个滤镜，用户点击后应用。

### 证据与数据

- 竞品参考：DOKA 相机已上线场景识别 + 滤镜推荐功能，根据画面内容分析后推荐合适的滤镜并给出理由
- [TBD — 需补充用户反馈/埋点数据]

### 目标用户与场景

- 用户角色：普通拍照用户，不希望手动调试参数
- 核心场景：打开相机 → 对准拍摄目标 → 一键获得适合当前场景的调色方案
- 使用频率：[TBD — 需数据验证]

### 预期收益

1. 让用户轻松应用合适的效果风格，提升照片和视频拍摄的满意度
2. 降低 preset 功能的使用门槛，让用户可以一键快速应用合适的 preset

---

## 2. 假设

| 假设 | 置信度 | 证伪条件 | 验证方式 |
|-|-|-|-|
| 我们相信 **AI 场景分析 + 滤镜推荐** 对 **普通拍照用户** 会带来 **Preset 使用率提升**，因为 **降低了选择成本** | Medium | Preset 应用率无显著变化 | 埋点对比 AI Preset 与手动滤镜使用率 |

---

## 3. 功能定义

### 功能描述

- 功能名称：AI Preset
- 一句话描述：根据当前拍摄场景，在 Preset 面板顶部前置展示 4 个推荐滤镜，用户点击后应用。本期 Preset 等同于单一滤镜，不包含 Tuning、EV 或其他相机参数。

### 范围

**In Scope:**

- 相机端场景分析 → Preset 面板 4 个推荐滤镜
- 具备场景识别与推荐能力；具体算法策略由算法方案维护，本 PRD 不固化实现细节
- 用户点击推荐卡片后才应用对应滤镜；系统不自动套用效果
- Preset 长按保存至预设库（开发新增），弹窗与提示词条见「5. 需求词条」

**Out of Scope:**

| 不做什么 | 说明 | 未来是否考虑 |
|-|-|-|
| 独立 AI Preset 入口 | AI Preset 承载在 Preset 面板内，不新增单独按钮，避免入口分散 | 否 |
| 仅首次打开推荐 | 每次打开 Preset 面板都展示 4 个推荐，推荐区作为高权重内容常驻面板前段 | 否 |
| 并入 Style | Style 是 Filter 与 Tuning 二合一的新功能；本期 AI Preset 仅推荐现有滤镜，不包含 Tuning | 否 |
| 姿势/构图引导 | 构图助手归属工具栏小功能，不纳入 AI Preset | 是 |
| 复合 Preset（滤镜 + Tuning + EV） | 本期只推荐现有滤镜，不组合或动态调整 Tuning、EV 等参数；复合 Preset 留待后续版本评估 | 后续评估 |

### 适用模式/入口

- 相机预览页 → 快门左侧 Preset 入口 → Preset 面板顶部 4 个推荐区
- 本期仅覆盖 Photo 模式；其他拍摄模式不展示 AI 预设推荐，不进入本期验收范围

---

## 4. 需求

### R1 · AI Preset 场景推荐

优先级：Must-have

<cite doc-id="Xg10wzdujigZa5kugaYlrC88gsg" file-type="wiki" title="相机 AI 推荐功能立项申请书" type="doc"></cite>

AI Preset 不新增独立入口。用户从快门左侧 Preset 入口打开 Preset 面板后，系统在面板前段展示基于当前场景推荐的 4 个 Preset。推荐只负责排序和露出，用户点击某个推荐卡片后才应用效果。

*正常路径：*

1. 用户在相机预览页点击快门左侧 Preset 入口，打开 Preset 面板
2. 系统根据当前拍摄场景生成推荐结果，并准备 Preset 面板顶部推荐内容
3. Preset 面板顶部展示 4 个推荐卡片；用户点击卡片后，对应 Preset 立即应用到预览

*边界：*

- 推荐 Preset 默认来自官方/内置 Preset 池；是否纳入用户自建 Preset 后续评估
- Preset 面板固定展示 4 个推荐；如推荐结果不足或不可用，使用兜底 Preset 补齐
- 识别超时、无命中或算法不可用时，展示安全通用 Preset fallback，不展示错误态或空态
- 弱光、极暗、纯色/低信息画面等边界场景需要算法侧给出覆盖范围；产品默认要求 fallback 可用

![The image shows two smartphone screens with a mountain and sky scene. The left screen has a 4:3 aspect ratio, a green icon at the top, and a Preset panel at the bottom with "Change icon when AI preset generated" and "没有使用中AI preset, 权限AI preset" text. The right screen has "AI preset" at the top, a Preset panel with "Show detected info" and "Tap to see all presets" text, and a "Tap to see all presets" button. This relates to the AI Preset scene recommendation in the document, demonstrating the Preset panel interface.](https://feishu.cn/file/F5xNb4XzwogmqbxnUtNl6bj5gbh)

![The image shows three mobile phone screens presenting the AI Preset scene recommendation interface. Each screen displays a mountain landscape photo with a Preset panel at the bottom. The Preset panel has 4 recommendation cards, and the top of each screen shows the current Preset name and description. The left screen has a red line indicating the Preset list 4:3, and the middle and right screens have text about Preset fallback and兜底Preset. This corresponds to the context describing the normal path of AI Preset scene recommendation, where the system generates recommendations and displays them in the Preset panel.](https://feishu.cn/file/DAIybC5rToevJRxIObLlOGPAg1c)

### R2 · 4 个推荐的展示策略

优先级：Must-have（随 R1）

每次打开 Preset 面板时，系统将 4 个最适合当前场景的 Preset 前置展示。推荐结果需要兼顾场景相关性、效果安全性、可感知差异与面板展示稳定性。

*正常路径：*

- **推荐原则**：4 个推荐需要匹配当前拍摄场景，并保证效果安全可用；具体打分、排序和兜底策略由算法方案维护
- **展示稳定性**：同一次面板打开期间推荐不频繁跳变；关闭后再次打开可按当前场景刷新 4 个

*边界：*

- 4 个推荐应有可感知差异，避免全部呈现为同一滤镜或同一视觉倾向
- **设置开关：**在 Camera Settings > Photo 中提供 Preset suggestions 开关，默认开启。关闭后停止生成和展示基于场景的预设推荐，但不影响用户从滤镜列表手动选择和应用滤镜。



### R3 · 推荐内容与场景边界

本期 AI 预设推荐的是可直接应用的滤镜，不包含 Tuning、EV 或其他相机参数。具体场景识别、打分和排序策略不在本 PRD 展开，由算法方案和技术评审维护；复合 Preset 作为后续版本能力评估。

- 推荐数量：面板前段展示 4 个推荐 Preset。
- 推荐内容：每个推荐 Preset 对应一个现有滤镜，用户点击后直接应用该滤镜。
- 推荐池：本期默认从官方/内置滤镜中推荐；是否纳入用户自建滤镜后续评估。
- 兜底：无法识别或推荐不可用时，用安全通用 Preset 补齐，不展示错误态或空态。
- 构图：构图助手是工具栏中的独立功能，不纳入 AI Preset。



### R4 · 环境与 Preset 信息展示

<grid>
<column width-ratio="0.504845">
![The image shows a smartphone screen displaying the Camera 5.1 app interface. The background features a snowy mountain with a cloudy sky. At the top, there are settings like "WB 3200K" and "LIGHT LOW - EVEN". Below, there are zoom options (0.6, 1x, 2, 3.5, 7) and a slider. At the bottom, there are five preset icons labeled "STD" with a red cross mark, and a circular icon with a globe and a refresh symbol. This relates to the "R4·环境与Preset信息展示" (Environment and Preset Information Display) section, showing preset information and settings.](https://feishu.cn/file/DL0UbKWbxoOCzixXqhulNihfgac)
</column>
<column width-ratio="0.495155">
![The image shows a mobile app interface for Camera 5.1-AI Preset, displaying environmental and preset information. The background features a snowy mountain and a cloudy sky. On the left, it shows "COLOUR TEMP 3200K" and "LIGHTING BRIGHT EVEN". On the right, "WARM SKIN TONES" with "WARM - SOFT" is displayed. Below, there are five preset options labeled "STD 1" with a "X" mark, and a "1x" button is highlighted. The interface also includes a "STD" button, a circular icon, and a refresh icon at the bottom.](https://feishu.cn/file/QO5kbI8xBoMNc0xcyJ5lJUcHg8e)
</column>
</grid>

#### 1. 文案结构

顶部信息分为左右两组。左侧始终用于描述当前拍摄环境，右侧只用于描述当前选中的 Preset 风格；未选择 Preset 时右侧隐藏。底部候选卡片根据选择状态切换：未选中时显示固定缩略编号，选中时显示完整英文名称。**顶部环境信息、右侧风格描述、缩略编号和选中名称在所有系统语言下均只显示英文。**

| 位置 / 状态 | 显示内容 | 职责 |
|-|-|-|
| 左侧第一行 | **COLOR TEMP**　3200K | 描述环境色温 |
| 左侧第二行 | **LIGHTING**　LOW · EVEN | 描述环境明暗和明暗关系 |
| 右侧第一行 | TEAL & AMBER | 选中 Preset 后描述主要色彩变化；未选中时隐藏 |
| 右侧第二行 | DEEP · PUNCHY | 选中 Preset 后描述影调与质感；未选中时隐藏 |
| 底部候选 · 未选中 | **C**（左下）　**1**（右下） | 显示固定缩略编号，保持候选列表整齐 |
| 底部候选 · 已选中 | **CINEMA** | 缩略编号隐藏，改为显示完整英文名称 |



| 界面状态 | 左侧光线描述 | 右侧风格描述 |
|-|-|-|
| 尚未选择 Preset | 显示 | 隐藏，不显示占位文案 |
| 已选择 Preset | 继续显示 | 显示该 Preset 固定绑定的两行描述 |
| 切换 Preset | 不受影响 | 立即切换为新 Preset 的固定描述 |

```text
COLOR TEMP  3200K        TEAL & AMBER
LIGHTING    LOW · EVEN   DEEP · PUNCHY

Unselected card: C                              1
Selected card:   CINEMA
```

#### 2. 左侧：光线描述逻辑

左侧只显示相机能够相对可靠测得的 COLOR TEMP 与 LIGHTING，不显示产品场景标签。COLOR TEMP 来自 AWB 稳定后的 CCT；LIGHTING 由 Lux Metric 明暗等级和 ADRC 明暗关系等级组合。

**COLOR TEMP。**CCT 显示到最接近的 100K；变化不足 200K 时不刷新，新数值连续稳定约 500ms 后更新。AWB 未收敛或数据缺失时显示 —K 或暂时隐藏。只显示 Kelvin 数值，不额外翻译成 WARM / COOL。

**明暗等级。**当前工程读取的是相机内部 Lux Metric，并非物理照度 Lux；数值越大代表环境越暗。该指标只描述明暗，不用于推断室外、室内或夜景。

| Lux Metric | 显示文案（全语言） | 说明 |
|-|-|-|
| < 180 | BRIGHT | 环境明亮 |
| 180–319 | BALANCED | 光线适中 |
| 320–449 | LOW | 低照环境 |
| ≥ 450 | DIM | 暗光环境 |

**明暗关系。**ADRC 用于判断画面明暗关系的强弱，不用于判断逆光、侧光、顶光或混合光。UI 不直接显示 MEDIUM / HIGH / EXTREME CONTRAST，而使用更短的感知语言。

| ADRC | 显示文案（全语言） | 说明 |
|-|-|-|
| < 1.3 | EVEN | 明暗均匀，光比低 |
| 1.3–1.99 | DEFINED | 明暗层次清晰，但不过分强烈 |
| 2.0–2.99 | BOLD | 明暗分离明显，视觉力度较强 |
| ≥ 3.0 | DRAMATIC | 明暗关系强烈，具有戏剧性 |

**组合格式。**所有语言环境固定使用 `{LUX_STATE} · {ADRC_STATE}` 英文组合。前词描述环境明暗，后词描述明暗关系，例如 BRIGHT · EVEN、BALANCED · DEFINED、LOW · BOLD、DIM · DRAMATIC。不为组合结果创造 NIGHT、BACKLIT 等场景名称。

**稳定和缺失处理。**Lux 与 ADRC 使用最近约 0.5–1 秒数据的中位数或平滑值，新等级至少持续 500ms 后切换；Lux 阈值加入约 ±15 滞回，ADRC 阈值加入约 ±0.1 滞回。ADRC 缺失时只显示 Lux 等级，不显示分隔点；Lux 缺失时暂不显示 LIGHTING 结果或显示 ANALYSING。该状态在所有系统语言下保持英文。

#### 3. 右侧：风格描述逻辑

右侧风格描述不是根据取景环境实时生成，而是与滤镜一一绑定的固定英文元数据。推荐算法只输出 `filter_id`；界面根据该 ID 读取两行英文风格描述，不随系统语言变化。没有选择滤镜时右侧完全隐藏，选择或切换后立即显示对应内容。

| 字段 / 状态 | 英文格式 | 文案规则 |
|-|-|-|
| 右侧第一行 | COLOR EFFECT | 只显示英文；描述最明显的色彩变化，建议 2–3 个简短英文单词，例如 TEAL & AMBER |
| 右侧第二行 | TONALITY · TEXTURE | 只显示英文；固定两个短词并以中点连接，例如 DEEP · PUNCHY |
| 底部候选 · 未选中 | CODE LETTER + CODE INDEX | 左下显示一个大写英文字母，右下显示固定序号；例如 C 与 1 |
| 底部候选 · 已选中 | DISPLAY NAME | 缩略编号隐藏，显示一个 2–8 个大写英文字母组成的完整名称；不使用空格、连字符或中文 |

底部卡片回答“它是哪一个 Preset”：未选中时使用固定缩略编号，选中后显示完整英文名称；顶部右侧回答“它会怎样改变画面”。三类文案由同一个 Preset ID 固定映射，但顶部不复述名称。环境检测词 BRIGHT、BALANCED、LOW、DIM、EVEN、DEFINED、BOLD、DRAMATIC 不用于 Preset 名称或右侧描述，避免左右信息混淆。

#### 4. 底部候选卡片命名与状态

底部候选卡片采用“固定缩略编号 + 选中完整名称”的两态结构。未选中时优先保证列表秩序与视觉一致性；选中后再提供可读的风格名称。顶部右侧继续显示此前定义的两行固定英文风格描述，不将缩略编号或完整名称重复到顶部。

| 界面状态 | 卡片底部 | 顶部右侧 |
|-|-|-|
| 尚未选择 Preset | 左下显示 **codeLetter**，右下显示 **codeIndex** | 隐藏，不显示占位文案 |
| 已选择 Preset | 隐藏缩略编号，显示 **displayName** | 显示该 Preset 固定绑定的 **colorEffect** 与 **finish** |
| 切换 Preset | 上一项恢复缩略编号，新选中项显示完整名称 | 立即切换为新 Preset 对应的两行描述 |
| 退出推荐状态 | 结束当前选中状态；下次推荐重新生成候选列表 | 隐藏 |

**完整名称规则。**`displayName` 使用单个英文词条，仅包含 A–Z 大写英文字母，长度为 2–8 个字符。名称应表达影像风格或材质联想，不直接使用 FOOD、PET、FOREST、BEACH 等拍摄对象作为用户可见名称。字体大小保持统一，不通过动态缩小字号容纳超长名称。

**缩略编号规则。**`codeLetter` 取发布时完整名称的首字母；同首字母名称按主表顺序递增 `codeIndex`。最终编号作为固定产品元数据写入配置，不在运行时根据数组顺序生成。正式发布后，新增或删除滤镜不得导致已有编号重排；完整名称后续调整时也默认保留已发布编号。

**显示语言与信息分工。**缩略编号、完整名称及顶部两行描述在所有系统语言下均显示英文。卡片回答“当前选择的是哪种风格”，顶部右侧回答“它会怎样改变画面”；两处信息互补，不互相复述。

```text
UNSELECTED CARD     C                                 1
SELECTED CARD       CINEMA
TOP RIGHT LINE 1    TEAL & AMBER
TOP RIGHT LINE 2    DEEP · PUNCHY
```

| 配置字段 | 示例 | 用途 |
|-|-|-|
| `thumbnailCode` | `C1` | 调试与埋点使用的组合标识；视觉层按字母与数字分开展示，无障碍不朗读该字段 |
| `codeLetter` | `C` | 未选中卡片左下角 |
| `codeIndex` | `1` | 未选中卡片右下角 |
| `displayName` | `CINEMA` | 选中卡片完整名称；无障碍朗读也使用该字段 |
| `colorEffect` | `TEAL & AMBER` | 顶部右侧第一行 |
| `finish` | `DEEP · PUNCHY` | 顶部右侧第二行 |

#### 5. 全局用户可见文案

设置页按系统语言提供中英文文案：英文使用 **Preset**，中文统一翻译为“预设”。相机预览区属于影像风格信息层，顶部环境信息、右侧风格描述、底部缩略编号和选中完整名称在所有系统语言下均固定显示英文。用户界面不露出 AI；内部模块名和工程字段可继续保留 AI Preset。

| 位置 / 状态 | 英文界面 | 中文界面 | 使用说明 |
|-|-|-|-|
| 顶部色温标签 | COLOR TEMP | COLOR TEMP | 推荐预览区固定英文；数值使用 K |
| 顶部光线标签 | LIGHTING | LIGHTING | 推荐预览区固定英文 |
| 亮度等级 | BRIGHT / BALANCED / LOW / DIM | BRIGHT / BALANCED / LOW / DIM | 所有语言固定英文 |
| 明暗关系 | EVEN / DEFINED / BOLD / DRAMATIC | EVEN / DEFINED / BOLD / DRAMATIC | 所有语言固定英文 |
| 右侧第一行示例 | WARM SKIN TONES | WARM SKIN TONES | 选中 Preset 后读取固定英文元数据 |
| 右侧第二行示例 | SOFT · SMOOTH | SOFT · SMOOTH | 选中 Preset 后读取固定英文元数据 |
| 底部推荐名称示例 | C1 / CINEMA | C1 / CINEMA | 未选中显示固定缩略编号；选中显示完整英文名称 |

**文案规则：**设置页英文使用 Preset，中文使用“预设”；Filters / 滤镜只表示滤镜库和管理入口。相机预览区顶部环境信息、右侧风格描述、底部缩略编号与选中名称一律只显示英文，不随系统语言切换。不使用 AI、Auto、Automatically applies 或“自动应用”等用户可见措辞；开关只控制推荐展示，不会自动套用 Preset。需要翻译的设置页词条（中英文对照）收录于「5. 需求词条」。

#### 6. 工程滤镜一一映射表

当前版本推荐滤镜库共 **27 个**（网络 11 个、原生相机 9 个、AI 场景 7 个），与 **v7-pruned-filter-pool**、App-ready rules.json、运行时 PNG 和交付 Manifest 保持一致。下表是开发接入使用的完整主表；推荐结果、固定缩略编号、选中完整名称、顶部两行风格描述和特征色必须使用同一行配置。中文短名仅作为资料保留，不在推荐预览区显示。

| 当前工程名称 | 来源 | 中文短名（资料） | 缩略编号 | 选中完整名称 | 特征色 HEX | 顶部右侧第一行 | 顶部右侧第二行 |
|-|-|-|-|-|-|-|-|
| 709电影感（青橙+增强对比） | 网络 | 青橙 | **C1** | **CINEMA** | `#843A21` | TEAL & AMBER | DEEP · PUNCHY |
| 709电影感（青橙+增强对比）2 | 网络 | 苔青 | **M1** | **MOSS** | `#5D5543` | OLIVE FILM TONES | MUTED · FADED |
| 709复古年代3 | 网络 | 年代 | **A1** | **ARCHIVE** | `#4D322B` | AGED NEUTRAL TONES | TEXTURED · FILMIC |
| 709婚礼自然暖肤 | 网络 | 珠光 | **P1** | **PEARL** | `#8B6E66` | CREAMY SKIN TONES | AIRY · SOFT |
| 709霓虹赛博高冲击 | 网络 | 赛博 | **V1** | **VOLT** | `#104650` | NEON CYAN TONES | DEEP · GLOWING |
| 709日系奶油低饱和 | 网络 | 奶油 | **I1** | **IVORY** | `#D4B879` | CREAMY COOL TONES | SOFT · AIRY |
| 709日系清新（低对比低饱和） | 网络 | 轻盈 | **D1** | **DAYLIGHT** | `#8799B1` | CLEAN NEUTRAL TONES | MUTED · SOFT |
| 709日系清新柔雾褪色低饱和 | 网络 | 柔雾 | **B1** | **BLOOM** | `#674A4C` | PASTEL MAGENTA TONES | AIRY · FADED |
| 709柔和的中性色调01 | 网络 | 温润 | **M2** | **MELLOW** | `#B5AB76` | WARM NEUTRAL TONES | SOFT · SMOOTH |
| 709商业鲜明高对比 | 网络 | 灰绿 | **S1** | **SAGE** | `#9C9841` | WARM OLIVE TONES | CRISP · PUNCHY |
| 709通用轻创意3 | 网络 | 淡彩 | **M3** | **MUTED** | `#3E412C` | MUTED NEUTRAL TONES | CLEAN · NATURAL |
| 菲林黑白11.5 | 原生相机 | 柔灰 | **S2** | **SILVER** | `#666664` | TEXTURED GRAYS | HARD · GRAINY |
| 负片11.5 | 原生相机 | 冷负片 | **N1** | **NEGATIVE** | `#795F6A` | COOL MAGENTA TONES | RICH · FILMIC |
| 暖调11.5 | 原生相机 | 暖金 | **A2** | **AMBER** | `#AF8D43` | GOLDEN WARM TONES | FRESH · SMOOTH |
| 正片11.5 | 原生相机 | 青蓝 | **S3** | **SLIDE** | `#2E607F` | CLEAR CYAN TONES | CRISP · FILMIC |
| 质感11.5 | 原生相机 | 明锐 | **C2** | **CRISP** | `#59615A` | NEUTRAL TRUE COLORS | CRISP · CLEAN |
| 自然11.5 | 原生相机 | 自然 | **N2** | **NATURAL** | `#8C8375` | LIFELIKE COLORS | NATURAL · CLEAN |
| Analog | 原生相机 | 暖棕 | **A3** | **ANALOG** | `#826142` | WARM VINTAGE TONES | MUTED · FADED |
| Chrome | 原生相机 | 哑金 | **M4** | **MATTE** | `#856D42` | WARM OLIVE TONES | MATTE · FADED |
| fuji-cc-v1.1-33_3.2-1 | 原生相机 | 褪色 | **M5** | **MEMORY** | `#6E746B` | MUTED NEUTRAL TONES | SOFT · MATTE |
| AI Portrait Soft | AI 场景 | 柔和 | **S4** | **SATIN** | `#C49B8F` | HEALTHY SKIN TONES | SOFT · SMOOTH |
| AI Food Warm | AI 场景 | 浓郁 | **R1** | **RICH** | `#B36A32` | RICH WARM TONES | RICH · CRISP |
| AI Sunset Gold | AI 场景 | 金辉 | **G1** | **GLOW** | `#B8933F` | AMBER HIGHLIGHTS | RICH · GLOWING |
| AI Night Neon | AI 场景 | 霓虹 | **N3** | **NOCTURNE** | `#042325` | NEON BLUE TONES | DEEP · GLOWING |
| AI Forest Fresh | AI 场景 | 鲜活 | **B2** | **BOTANIC** | `#466443` | FRESH GREENS | CLEAN · CRISP |
| AI Beach Clear | AI 场景 | 清透 | **L1** | **LAGOON** | `#668FA8` | CLEAR AQUA TONES | AIRY · CRISP |
| AI Pet Soft | AI 场景 | 柔亮 | **V2** | **VELVET** | `#A79A83` | WARM NATURAL TONES | SOFT · CLEAN |

#### 7. 工程映射与范围

客户端维护 `styleMetaByFilterId` 映射；推荐结果返回完整 `filter_id` 后，直接读取 `thumbnailCode`、`codeLetter`、`codeIndex`、`displayName`、`featureColor`、`colorEffect` 和 `finish`。这些字段均为固定元数据，不随系统语言变化，也不在运行时根据候选顺序重新生成。CCT、Lux、ADRC 与场景标签不参与名称、编号或右侧文案生成。

```json
{\n  "filterId": "lut_filter-lut_cinema_example",\n  "thumbnailCode": "C1",\n  "codeLetter": "C",\n  "codeIndex": 1,\n  "displayName": "CINEMA",\n  "featureColor": "#843A21",\n  "colorEffect": "TEAL & AMBER",\n  "finish": "DEEP · PUNCHY",\n  "recommendationEnabled": true\n}
```

**异常与约束：**仅上表 27 个滤镜允许进入推荐结果。缺少 thumbnailCode、displayName、colorEffect 或 finish 任一映射时，该滤镜必须从候选中排除，不能回退显示工程名称、中文短名或运行时临时编号；特征色必须读取上表固定 HEX，不在运行时生成。

---

### R5 · 预设推荐设置开关

**优先级：**Must-have

在 **Camera Settings > Photo** 中新增推荐功能开关，位于 Filters 入口上方。开关仅控制基于场景的预设推荐，不控制滤镜库，也不会自动应用任何滤镜。开关标题与副标题词条见「5. 需求词条」。

| 状态 / 场景 | 产品行为 |
|-|-|
| **默认状态** | 默认开启，并持久保存用户选择；Camera App 重启后沿用上次状态。 |
| **开启** | 进入 Photo 模式后允许执行场景分析；识别成功时展示成功动效、4 个推荐 Preset，以及顶部环境信息。选中推荐项后，右侧展示该 Preset 固定绑定的风格描述。 |
| **关闭** | 不触发场景推荐，不展示识别成功动效、推荐卡片和推荐相关的环境/风格信息。用户仍可进入 Filters 管理 LUT 与滤镜，并手动选择和应用滤镜。 |
| **使用中关闭** | 立即移除推荐结果并回到普通滤镜选择状态；已经由用户手动选中的滤镜效果保持不变，直到用户更换或取消。 |
| **使用中开启** | 从下一次可用的场景分析周期开始生成推荐，不自动选中或套用推荐结果。 |

**埋点建议：**记录开关曝光、开/关操作、推荐生成成功、推荐项点击与应用，用于验证功能使用率和关闭原因。

**视觉参考：**Photo 设置页中的 Preset suggestions 开关及英文文案如下。

![Preset suggestions 设置开关（English UI）](https://feishu.cn/file/NUjxbnEoAogOJjxE4czlgVVBg8f)

### R6 · 长按保存 Preset

**优先级：**Must-have（开发新增能力）

长按任一推荐滤镜卡片，将该滤镜保存至预设库；保存动作不改变当前预览，也不影响推荐结果。

| 项目 | 规则 |
|-|-|
| **保存内容** | 本期仅保存 Photo 模式下的目标滤镜，不保存当前场景、色温、光线、镜头、变焦、EV 或 Tuning。 |
| **名称** | 使用滤镜映射表中的完整英文名，如 CINEMA。出现同名时自动命名为 CINEMA 2、CINEMA 3，以此类推。 |
| **重复保存** | 允许重复保存；每次生成独立 Preset，不覆盖已有内容。一次长按只触发一次保存。 |
| **特征色** | 继承滤镜映射表中的固定 featureColor HEX；不从当前画面动态取色，同一滤镜的副本使用相同特征色。 |
| **封面** | 每个滤镜根据其特征色准备一张专属封面图，保存时将对应封面一并写入 Preset。当前可先使用统一的 3:4 同色系渐变模板，不包含文字、图标或当前场景画面；最终封面视觉及 27 张资源由设计补充。 |
| **保存结果** | 成功后可在预设库中找到，重启后仍保留；失败不影响当前预览与已应用滤镜。保存后的 Preset 不进入推荐池。 |

**弹窗与提示：**使用「5. 需求词条」中的保存弹窗、成功提示和失败提示，不新增其他用户可见文案。

**埋点建议：**长按保存触发、保存成功、保存失败。

## 5. 需求词条

本章收录随系统语言本地化（需翻译）的用户可见词条。相机预览区的顶部环境信息、右侧风格描述、底部缩略编号与选中名称在所有系统语言下固定显示英文，不随系统语言翻译，对应规格见 **R4**。

| 应用场景 | 中文词条 | 英文词条 | 备注 |
|-|-|-|-|
| 保存弹窗标题 | **保存预设** | **Save preset** | 长按保存 Preset 后弹出的保存弹窗 |
| 保存弹窗说明 | 你可以在预设库中找到此预设 | You can find this preset in your preset library | 长按保存 Preset 后弹出的保存弹窗 |
| 保存成功提示 | 预设已保存至预设库 | Preset saved to library | 长按保存 Preset 后弹出 |
| 保存失败提示 | 无法保存预设 | Unable to save preset | 长按保存 Preset 后弹出 |
| Camera Settings > Photo — 设置项标题 | **预设推荐** | **Preset suggestions** | 设置页随系统语言本地化 |
| Camera Settings > Photo — 设置项说明 | 根据场景推荐预设 | Suggests presets based on the scene | 设置页随系统语言本地化，不暗示自动应用 |
| Camera Settings > Photo — 滤镜管理副标题 | 管理 LUT 与滤镜 | Manage your LUTs and Filters | 沿用当前设置页管理入口 |

## 6. 关键依赖

| 依赖项 | 负责方 | 状态 | 风险 |
|-|-|-|-|
| 场景分析算法（光线/色系/主体识别） | app | 使用 ML-Kit 方案 | 准确率决定推荐质量 |
| 预设推荐策略方案 | app | 使用自研方案，数据待标注 | 多样性与合理性平衡 |
| 预览帧实时分析延迟 | App  | ML-Kit 暂无性能问题 | 需控制在可接受范围 |
| 老项目回落兼容 | 工程 | [TBD] | 需验证回退路径 |

---

## 7. 指标与验收

### 成功指标

| 指标 | 基线 | 目标 | 测量方式 | Owner |
|-|-|-|-|-|
| AI Preset 点击率 | [TBD] | [TBD] | 埋点 | [TBD] |
| 推荐卡片选择率（点击后选中应用） | [TBD] | [TBD] | 埋点 | [TBD] |
| Preset 保存成功率 | [TBD] | [TBD] | 埋点 | [TBD] |

### 验收条件

- [ ] 打开 Preset 面板后，面板前段展示 4 个推荐卡片；推荐结果不可用时由兜底 Preset 补齐

- [ ] 4 个推荐卡片不可全为同一滤镜

- [ ] 4 个推荐卡片之间有可感知差异，避免全部为同一滤镜或同一视觉倾向

- [ ] 构图助手入口在工具栏独立呈现，不作为 AI 预设推荐卡片或 Preset 面板内容

- [ ] 所有场景下推荐效果不出现色阶断层、噪点激增

- [ ] 仅在 Photo 模式展示 AI 预设推荐；其他模式不展示且现有功能不受影响

- [ ] 老项目回落正常

- [ ] 长按保存后弹出保存弹窗，文案与「5. 需求词条」一致

- [ ] 保存成功后出现成功提示，Preset 可在预设库中找到

- [ ] 保存失败时出现失败提示，不影响当前预览与已应用滤镜状态

---

## 8. 干系人

| 角色 | 姓名 | RACI | 沟通频率 |
|-|-|-|-|
| PM | Travis | A |  |
| 算法 | [TBD] | R | 周会 |
| 工程 | [TBD] | R | 周会 |
| 测试 | [TBD] | C | 评审节点 |
| 设计 | [TBD] | C | 评审节点 |

---

## 9. 待确认/待补充

|  | 待确认项 | 章节 | 阻塞级别 |
|-|-|-|-|
| 1 | 场景分析算法成熟度与延迟基线 | 6 | 阻塞 |
| 2 | 推荐策略方案与可用边界 | 6 | 阻塞 |
| 3 | 分析超时兜底策略 | 4 (R2) | 不阻塞 |
| 4 | 弱光/极暗场景覆盖边界 | 4 (R2) | 不阻塞 |
| 5 | 成功指标基线与目标值 | 7 | 不阻塞 |
| 6 | 用户反馈/埋点数据补充分析背景 | 1 | 不阻塞 |
| 7 | 老项目版本列表与回落验证计划 | 6 | 阻塞 |
| 8 | 27 张特征色封面的最终视觉与资源交付 | 4 (R6) | 不阻塞 |

---

## 10. 初步评审

> `agent` 前缀表示 AI 辅助评审，非人工结论。

### agent 开发评审

- 方案可行性：AI 场景分析 + 推荐架构清晰，无硬件依赖，纯软件可控
- 依赖就绪度：推荐策略与可用边界是关键路径，需尽早确认体验可用性
- 实现风险：老项目回落兼容性需验证
- 回退策略：AI preset 不可用时回退为手动 preset

### agent 测试评审

- 验收标准可测试性：大部分可测试，但"风格可感知差异"偏主观，建议细化
- 场景覆盖：需建立测试场景库（室外/室内/晴天/阴天/夜景/人像/风光/弱光）
- 异常路径：分析超时、网络异常（如模型在云端）、极端场景（纯黑/过曝）
- 回归范围：现有 preset 创建/编辑/应用全路径

### agent Solution Smuggling 检查

- [x] 问题陈述中是否预设了特定方案？— 无，"AI 推荐"是方案，"用户不知道选哪个滤镜"是问题，表述合理

- [x] Scope 中是否有"MVP 不应该包含"但仍在 In Scope 的内容？— 无，已明确排除仿色和姿势推荐

### agent 全文评分

| 维度 | 满分 | 得分 | 说明 |
|-|-|-|-|
| 问题定义清晰 | 15 | 13 | 问题描述清晰，缺用户数据支撑 |
| 假设明确可验证 | 10 | 5 | 仅 1 条假设，缺更多验证维度 |
| 范围边界明确 | 15 | 14 | In/Out scope 明确 |
| 需求可测试 | 20 | 14 | 核心路径可测试，主观项需细化 |
| 依赖完整 | 10 | 6 | 算法依赖已标记，待确认 |

| 维度 | 满分 | 得分 | 说明 |
|-|-|-|-|
| 指标有基线+目标 | 15 | 5 | 指标框架完备，但基线/目标均为 TBD |
| 风险有兜底 | 10 | 6 | 老项目回落已提及，算法兜底待补 |
| 埋点覆盖 | 5 | 1 | 待完整设计 |
| **总分** | **100** | **64** | — |

**结论:** `DONE_WITH_CONCERNS` — 主链路和本期范围已明确，当前有 7 项待确认（其中 3 项阻塞）；指标与埋点方案仍待补充。

### agent 高风险项

- 推荐策略与可用边界是核心依赖，如推荐延迟、稳定性或效果安全性不达标，功能体验会明显受损
- 老项目回落兼容需尽早验证，避免功能上线后老版本崩溃

### agent 推荐第一版最小切片

建议第一版聚焦 AI 预设推荐主链路：用户打开 Preset 面板后看到 4 个推荐 Preset，推荐内容包含滤镜效果，点击后直接应用；构图助手作为工具栏独立功能另行承接。算法打分、场景覆盖与兜底策略在算法方案中维护，PRD 只约束产品体验与验收边界。

---

## 11. 附录

### 竞品分析摘要

**DOKA 相机 — 智能调色（滤镜推荐）：**

- 根据图片内容给出滤镜推荐，结合场景给出推荐理由
- 参考价值：场景分析→推荐→理由的交互模式可借鉴

<grid><column width-ratio="0.200000"><img name="image.png" alt="The image shows a camera interface with an AI analysis process. At the top, there&#39;s a red circular icon with a white play button, and a message &#34;AI 正在分析画面...&#34; (AI is analyzing the scene). The main area displays a photo of a building with a clock tower, surrounded by trees and traffic lights. Below the photo, there are zoom options (0.5x, 1x, 2x, 3x) and a &#34;退出构图&#34; (Exit Composition) button. The bottom has icons for camera modes, including &#34;相机&#34; (Camera) and &#34;我的&#34; (My). This relates to the context discussing AI Preset features in the Camera app." mime="image/png" scale="0.811111" src="SNAXbqzVBoNWkexQKHnlBjnJgab"/></column><column width-ratio="0.200000"><img name="image.png" alt="The image shows a camera interface with a building as the main subject. At the top, there is a prompt &#34;请对准彩色圆环&#34; (Please aim at the colored circle). Below the main image, there are zoom options: 0.5x, 1x, 2x, 3x. At the bottom, there are icons for camera modes, including &#34;相机&#34; (Camera), &#34;我的&#34; (My), and a circular shutter button. This interface is related to the context discussing camera AI preset features, possibly demonstrating a filter or preset application scenario." mime="image/png" scale="0.811111" src="L2MxbUix8oPDXsxhQOglT9mPgnf"/></column><column width-ratio="0.200000"><img name="image.png" alt="The image shows a camera interface with a blue square frame highlighting a building as the main subject. Below the frame, there are zoom options (0.5x, 1x, 2x, 3x) and aspect ratio settings (3:4). At the bottom, there are icons for camera modes (camera, portrait, my) and a shutter button. This relates to the &#34;姿势/构图引导&#34; (Pose/Composition Guidance) section in the document, which discusses considering this feature but ultimately放弃了 (abandoning) it as it is unrelated to the color recommendation scenario." mime="image/png" scale="0.811111" src="JQ94bdq2BoTqIdxKhtHlPkzfgGg"/></column><column width-ratio="0.200000"><img name="image.png" alt="The image shows a camera interface with a building as the main subject. At the top, there is a notification that reads &#34;暖色建筑场景，推荐滤镜Gold 200 (Pro专属滤镜，限定次数免费)&#34;. Below the notification, there are zoom options: 0.5x, 1x, 2.0x, 3x. In the bottom left corner, there is a filter icon with &#34;200&#34; on it. The bottom of the interface has buttons labeled &#34;相机&#34;, &#34;我的&#34;, and &#34;退出构图&#34;. This image is related to the &#34;DOKA相机—智能调色（滤镜推荐）&#34; section, showing a filter recommendation scenario." mime="image/png" scale="0.811111" src="X6W6bXOd1o3i5Zx9IhAlt8LSgWf"/></column><column width-ratio="0.200000"><figure view-type="Preview"><source name="ScreenRecording_03-17-2026 15-53-59_1.mov" mime="video/quicktime" origin-height="2532.000000" origin-width="1170.000000" size="119275073" token="Mtzmb5Q2aoR1dmxauKIlxwHQgQe"/></figure></column></grid>

### 考虑过但放弃的方案

- 仿色/追色功能（相册端提取风格图片→生成 preset）：放弃原因 — 非本期优先级，且竞品效果参差不齐，评估成本高
- 姿势/构图引导：放弃原因 — 与调色推荐无关，聚焦滤镜推荐场景



### 开发交付包 · v7.1 App-ready

<callout emoji="❗">
\n
**旧包停用：**2026-08-05 的 v7 压缩包只在 filters[] 中注册了 7 个 AI 场景滤镜，另外 20 个 CUBE 仅作为资源存在，不能作为完整运行包接入。
\n
</callout>

2026-08-06 重建为 **v7.1-app-ready**。推荐策略版本仍为 `v7-pruned-filter-pool`，推荐池不变；本次只补齐运行时资源、注册信息与算法接口。

| 交付项 | 定义 |
|-|-|
| 完整滤镜注册 | 27 条 filters[]：11 个网络滤镜、9 个原生相机滤镜、7 个 AI 场景滤镜。 |
| 运行时 LUT | 27 个统一 512×512 PNG；20 个 CUBE 已转换为 PNG，所有条目均有唯一 effectName 和 lutFile。 |
| 状态与强度 | 默认强度 100；status=active；iqaStatus=approved；recommendationEnabled=true。 |
| 稳定随机 | FNV-1a 32-bit UTF-8；种子为 recommendationVersion\|userId\|imageId\|sessionId。相同用户、图片和会话结果稳定。 |
| 图片评分过滤 | 输入 filterScores[filterId] 存在且 score ≤ 0 时过滤；未提供分数时保持可推荐。 |
| 推荐组成 | 输出 4 个；候选充足时包含 1–2 个 ordinary，并至少包含 1 个 strong。 |
| 接口与验证 | 包内包含输入 JSON Schema、Rules Schema、可执行参考实现及 4 项自动化测试。 |

**开发应使用以下两个附件：**独立 rules.json 便于评审；ZIP 是包含 27 个 PNG、完整规则、源 LUT、Schema 和参考实现的正式接入包。

<figure view-type="Card"><source name="rules.json" mime="application/json" size="57162" token="QZBVbdhTJopjwIxlkY3l65ZSgBg"/></figure>

<figure view-type="Card"><source name="AI_Preset_v7_1_AppReady_Filter_Library_27_20260806.zip" mime="application/zip" size="12560635" token="OLocbQ83zocGiyxgpLJlbt1Egmh"/></figure>

## 正式设计稿（Camera 5.1）

[AI preset](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=181-8423&p=f)