# Knowledge Base Changelog

> 记录 `knowledge/` 目录文件变更 + 26111&26121 需求列表 (RL) 版本演化。

---

## 2026-07-09

### RL 维护

- **PRD 审计** — 遍历 Camera 5.1-26111 wiki 全部 23 份 PRD，对照 feature-tree 检查交互区归属：
  - 影像基调 (Image Tone) → 纠正为 Settings，非预览框
  - 运动场景引导 → 确认拆分为暂态开关 + Mode Switch | Action
  - Tuning Palette → 纠正为 Toolbar | Tuning（原来误映射到 通用/Common）
- **来源字段更新** — 36 条需求按 CSV 来源分为三类：v1.0+v1.3 双表(22条)、v1.3 新增(13条)、v1.0 保留(1条)
- **模块修正** — Preset 3.0 调色盘从 `通用/Common|Preset` → `Toolbar|Tuning`
- **高像素描述更新** — 根据 PRD 内容重写：200MP HP5 主摄、三档像素、兼容矩阵、交互规格

### Skill

- **`image-feature-prd-writer`** — 新增交互区检查步骤（workflow step 2），checklist 增加 feature-tree 引用，critical dependencies 增加「交互位置」
- **`requirement-list-creator`** — 收录昨天全部踩坑：type=11 vs 13、batch API 差异、token 刷新、PRD text 用标题、数据来源优先级、模块常见错误

### 新增

- **`CHANGELOG.md`** (本文件)

---

## 2026-07-08 — RL v3.0: 26111&26121 需求列表

> 来源：CSV v1.0（澄清计划）+ CSV v1.3（技术评估申请）。v1.3 为更新版本，信息准确性高于 v1.0。

### 需求新增 (+14)

以下来自 v1.3，v1.0 中不存在：

| # | 需求 | 优先级 | 模块 |
|---|------|--------|------|
| 1 | 继承 25111 Pro 系列需求 | P0 | 通用 / Common |
| 2 | 继承 NOS 5.0 软件需求 | P0 | 通用 / Common |
| 3 | 测光策略优化 (0.3→0.1 EV) | P0 | AE/AF Box |
| 4 | 成像预览一致性 (2DOL 方案) | P0 | 预览框 |
| 6 | HDR 运动场景效果升级 | P0 | 预览框 |
| 7 | HDR 影调升级 | P0 | 预览框 |
| 8 | 3A 优化 & 稳定性 | P0 | AE/AF Box |
| 9 | 多摄一致性 (2A Sync) | P0 | 预览框 |
| 10 | AIGC / SR 效果优化 | P0 | Zoom |
| 25 | 视频基础效果和体验优化 | P0 | Mode Switch \| 视频 |
| 26 | 运动场景长焦视频 (仅 26121) | P0 | Mode Switch \| 视频 |
| 36 | 超清 Motion Photo (XDR/4K/播放优化) | P1 | Toolbar \| 动态照片 |
| 16 | AI 场景检测算法升级 | P2 | 预览框 |

### 需求删除

| 需求 | 原因 |
|------|------|
| AI 消除 & AI 去反光 | 相册，本版本不显示 |
| 2亿重新构图 (AI Reframe) | 相册 |
| 搜索体验优化 (OCR + NL) | 相册 |
| 宠物聚类 | 相册 |
| Photo Sync | 相册 |
| 抠图/贴纸/拼图/球星卡 | 相册 |
| RCB 水印关联的相册抠图 | 拆分，仅保留相机侧水印 |
| HDR 分区优化 | 技术评估不通过 (6650/7635 不支持 AI Camera) |
| TF 25MP | 用户明确删除 |
| TF 50MP QuadBayer Raw HDR | v1.3 已关闭 |
| 2亿 raw 专业模式 | v1.3 已关闭 |
| 智能 HDR 分区优化 | v1.3 NG |
| XDR | v1.3 已移除 |
| 聚会模式 | v1.3 已移除 |
| 视频 log 模式 | v1.3 已移除 |
| 录制红框提示 | v1.3 已移除 |
| 裁切比例扩展 | v1.3 已移除 |
| NOS5.0 appfunctions | v1.3 已移除 |
| AI Preset Pose 模板 | v1.0 已取消 + v1.3 无 |
| 宠物对焦识别框 | 用户删除 |
| 2亿超清星空 Preset | 用户删除 |

### 需求修改

| 需求 | 变更 |
|------|------|
| 照片影调 | 3→2 款 (去 Texture，仅 Natural + Vivid) |
| 高像素模式 | v1.3 已关闭，用户保留，规格待定。后根据 PRD 更新为 200MP 三档规格 |
| 专业模式改进 | 优先级 v1.0 P0 → v1.3 P1 (以 v1.3 为准) |
| 帮助与反馈 | 优先级 v1.0 P2 → v1.3 P1 |
| SAT 优化 | 优先级 v1.0 P0 → v1.3 P1 |
| 双摄同录 v2 | 第1点(录制前选摄像头) N/G，仅保留第2/3点 |
| 视频专业参数 + 锁白平衡 | v1.0 为两条独立需求，v1.3 合并为一条 |
| AI Preset | v1.0 拆为滤镜推荐+pose，v1.3 合并为场景推荐 |
| 自然质感人像 | v1.0 的自由变焦人像 + 美颜，v1.3 合并为质感人像 |

### 表结构变更

| 字段 | 变更 |
|------|------|
| 模块 | Text → **SingleSelect** (type=3)，71 选项来自 feature-tree |
| 产品负责人 | **新增** User 字段 (type=**11**，非 13) |
| 支持项目 | **新增** MultiSelect (type=4)，26111/26121 |
| 修改记录 | **新表** (时间/修改人/需求/修改字段/原值/新值/备注) |
| PRD | URL text 改为文档标题，非通用 "PRD" |
| 备注 | 去掉 "产品 xxx" 前缀 |

### 模块映射修正 (v3.0 过程中)

| 修正前 | 修正后 | 原因 |
|--------|--------|------|
| Shutter \| Motion Photo | Toolbar \| 动态照片 | feature-tree 禁止使用快门区域 |
| Preset \| 预设 | 通用 / Common \| Preset | 必须带 Common 前缀 |
| Settings \| 视频设置 | 通用 / Common \| Settings \| Video | 同上 |
| Settings \| 帮助与反馈 | 通用 / Common \| Settings \| Help & Support | 同上 |
| 通用 / Common \| Preset | Toolbar \| Tuning | 调色盘是 Toolbar 风格，非 Preset 系统 |

### PRD 关联

- 从 Camera 5.1-26111 wiki 目录搜索匹配 21/38 条 PRD 链接
- 17 条无 PRD（2 条继承类无需、15 条真正缺失）

### 知识库文件

- **`feature-tree.md`** — 确认 71 个合法模块路径，排除快门区域
- **`devices/26111.yaml`** — 纠正：主摄 OIS YES (HFC66B5003+DW9828N)，UW 是 OV08J10 非 IMX355
- **`devices/project-mapping.yaml`** — 新增 26111/26121 映射
- **`reference/26111-prd-links.md`** — 新增 23 份 PRD 索引
- 其他 8 个 reference 文件新增/更新

### 生成产物 (`_output/`)

- `fl_draft_26111_26121/` — FL 草稿 → 最终版、硬件配置、审计报告
- `lark_26111_requirements/` — 35 个 wiki 节点导出
- `kb-functions-algorithms.v2~v6.json` — KB 映射迭代

---

## 格式约定

- 日期格式：`YYYY-MM-DD`；最新在上
- 分组：`需求新增`、`需求删除`、`需求修改`、`表结构变更`、`模块映射修正`、`PRD 关联`、`知识库文件`、`Skill`、`生成产物`
