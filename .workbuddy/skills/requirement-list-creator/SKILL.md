---
name: requirement-list-creator
description: 制定 Camera 需求列表（Bitable）。从多来源（JIRA/Sheet/群聊）汇聚需求，规范化为统一 Bitable，自动关联 PRD，反向审核完整性。适用场景：新版本需求规划、回落需求整理、跨项目需求合并。
---

# Requirement List Creator — 需求列表制定

## 触发条件

- "制定需求列表"、"整理需求"、"需求规划"
- "回落需求评估"、"跨项目需求合并"
- 给出多个需求来源，要求合并为一张表

若仅需操作已有的单个需求表（如添加字段、更新记录），直接用 `lark-base` skill 操作。

---

## 版本-项目-目录映射（权威来源）

**项目代号 → Camera 版本 → 知识库目录，以此表为准：**

| 项目代号 | Camera 版本 | 目录名 | Node Token |
|---------|------------|--------|------------|
| 26111 | 5.1 | Camera 5.1-26111 | `EIipweDIeiQ0hYkHkCRlrXpvg1d` |
| NOS 5.0 | 5.0 | Camera 5.0-NOS 5.0 | `XfcFwp96giKAPvkPdzllh90hgPe` |
| 25131 | 4.1 | Camera 4.1-25131 | `AaStwP9qVieNBaklnSslJIpSgqe` |
| 25111 | 4.0 | Camera 4.0-25111 | `OAJewVosCiFDqhkBHjWlc0XGg2c` |
| 23112 | 3.5 | Camera 3.5-23112 | `VB5FwkJO5iOXBqkGLBelvCtZgzh` | Abrok / Phone (3a) |
| 23111 | 3.5 | Camera 3.5-23112 | （同上） | Aerodactyl / Phone (2a) / Pacman |
| 23113 | 3.5 | Camera 3.5-23112 | （同上） | Aerodactyl Plus / Phone (2a) Plus / PacmanPro |
| 24111/24121 | 3.0 | Camera 3.0-24111&24121 | `EjtVwCJ5eirnjNk76GMl5Cg6gNg` | |
| Phone 2 | 2.5 | Camera 2.5-phone2 | `NoQewNgIqijKAXkbZnjl8lglgLb` |

**来源标注规范**：

- 当需求来自非当前版本时，标注原始版本：`回落需求评估-第一批 (25111/4.0)`
- **项目代号禁止缩写**：`23111&23113` ✓，`23111&3` ✗。任何涉及项目组合的地方，两个代号都写全

**Bitable 命名规范**：`{项目组合} {升级代号} 需求列表`，如 `23111&23113 17C 需求列表`

**Bitable 必须创建在对应版本的目录下。** 创建后通过 `lark-wiki` skill 移动到目标 parent node。

---

## Bitable 字段规范

### 必备字段（8 个，每条记录均需填写）

| 字段 | 类型 | 说明 |
|------|------|------|
| **需求** | Text | 简洁功能名，不含 JIRA tag、项目前缀。如 "相机新增全局调整调节项" |
| **描述** | Text | 2-5 句话，说清做什么 + 为什么 + 竞品/背景。低于 50 字视为不充分 |
| **优先级** | SingleSelect | P0 / P1 / P2，按版本交付标准判定 |
| **模块** | SingleSelect | 从 `knowledge/feature-tree.md` 映射。选项集与业务树严格同步，格式 `交互区 \| 子模块`。创建/更新 Bitable 时必须检查同步（见下方同步机制） |
| **来源** | SingleSelect | 需求原始来源 + 版本。格式：`来源名 (项目/Camera版本)`。如 "回落需求评估-第一批 (25111/4.0)"、"NOS5.0 相机新需求 (5.0)"。**禁止只写来源不写版本** |
| **JIRA** | URL | JIRA 链接。跨项目需求须创建目标项目的新 JIRA，备注中保留旧 JIRA |
| **PRD** | URL | Wiki PRD 链接。**纯设计类需求可用 Figma 链接代替**。无则留空但须标注 |
| **备注** | Text | 补充信息：原 JIRA tag、风险评估、依赖条件。**禁止含"产品 xxx"前缀**，联系人独立为 `产品负责人` 列 |
| **产品负责人** | User (11) | @ 产品负责人。类型为 User（type=**11**），**不是** Phone（type=13） |
| **JIRA** | URL | JIRA 链接。跨项目需求须创建目标项目的新 JIRA，备注中保留旧 JIRA |
| **支持项目** | MultiSelect (4) | 多选：26111 / 26121。默认都选，仅特定机型的单独勾选 |

### Bitable 字段类型速查

| 类型 | type 值 | 说明 | 注意 |
|------|---------|------|------|
| Text | 1 | 文本 | |
| SingleSelect | 3 | 单选 | |
| MultiSelect | 4 | 多选 | |
| DateTime | 5 | 日期时间 | |
| **User** | **11** | 人员 @ | **不是 13（13=Phone 电话号码）** |
| URL | 15 | 链接 | PRD 字段 `text` 用文档标题，非 "PRD" |

### 附加表：修改记录

创建同名 Bitable 时，同时创建一张 `修改记录` 表，字段：

| 字段 | 类型 | 说明 |
|------|------|------|
| 时间 | DateTime (5) | 修改时间 |
| 修改人 | User (11) | @ 操作人 |
| 需求 | Text | 关联的需求名称 |
| 修改字段 | Text | 改了哪个字段 |
| 原值 | Text | 修改前 |
| 新值 | Text | 修改后 |
| 备注 | Text | 修改原因

### 模块命名规范

模块必须使用 `knowledge/feature-tree.md` 中的交互区名称：

```
预览框 | 预览基础
预览框 | 场景检测
预览框 | 场景检测 | 脏污检测
AE/AF Box | Touch AE/AF
AE/AF Box | Face AE/AF
Zoom | SAT
Zoom | SR 超分
Toolbar | 动态照片
Toolbar | 运动抓拍
Toolbar | Watermark
Mode Switch | 视频
Mode Switch | 视频 | 规格切换
Mode Switch | 视频 | 防抖
Mode Switch | 视频 | 前后双录
Mode Switch | 人像 | 美颜
Mode Switch | 专业模式
Mode Switch | 高像素（50MP）
通用 / Common
通用 / Common | Preset
通用 / Common | Settings | Video
通用 / Common | Settings | Help & Support
```

⚠️ **关键规则**：
- **`快门区域`不可用作模块名** — feature-tree 明确 "Feature List 不展开"
- **`Preset`、`Settings`、`Widget` 必须带 `通用 / Common` 前缀**，不允许单独出现
- **模块字段类型为 SingleSelect（type=3）**，非 Text。选项集 71 个，全部从 tree 提取
- 不允许使用自定义模块名（如 "基础功能改善"、"Shutter"）
- 若功能跨多个模块，用 `|` 分隔

---

## 工作流

### Phase 1: 收集（Gather）

1. **确定版本与项目** → 确定目录位置（见上表）
2. **识别来源**：
   - Lark Sheet/Bitable（如 "回落需求评估-第一批"）
   - JIRA filters（按项目/版本/label）
   - 群聊记录（如澄清群中的共识）
   - Excel 导出文件
3. **读取全部来源**，提取以下原始数据：
   - 需求名称、优先级、JIRA ID、PRD 链接、负责人、备注
4. **去重**：按 JIRA ID 或需求名相似度去重，保留信息最完整的版本

### Phase 2: 规范化（Normalize）

1. **清洗需求名称**：去掉 JIRA tag（`[23112]`）、平台前缀（`[Android 17]`）、模块 tag（`[Tuning]`）
2. **补充描述**：
   - 从 JIRA description 提取
   - 从原始 Sheet 备注栏提取
   - 若两者都无，标记 `[TBD — 需产品补充]`
3. **映射模块**：读 `knowledge/feature-tree.md`，逐条匹配到正确交互位置
4. **统一优先级**：P0 = 必做 / P1 = 应做 / P2 = 可做

### Phase 3: 创建 Bitable（Create）

1. 用 `lark-cli base +base-create` 或 API 创建 Bitable
2. 设计字段（见必备字段）
3. 批量写入记录（`batch_create`，上限 500 条/次）
4. 用 `lark-wiki` skill 将 Bitable 移动到对应版本目录

### Phase 4: 关联 JIRA（Link JIRA）

1. **检查 JIRA 项目 tag**：确认所有 JIRA 的 Device 字段匹配当前项目
2. **跨项目继承**：若需求来自旧项目（如 25131），克隆为新 JIRA（新 project tag + Device），并链接 `Relates to`
3. 新 JIRA 写回 Bitable

### Phase 5: 关联 PRD（Link PRDs）

**背景**：Nothing 手机在每次 Android 大版本升级时，会从更高 Camera 版本回落（backport）需求到老机型。因此需求的实际来源版本 ≠ 目标项目版本。

**核心原则：PRD 在原始版本目录中找，不在目标版本目录中找。**

例如：23112（Camera 3.5）项目包含从 4.0/4.1/5.0 回落的需求，PRD 应去 4.0/4.1/5.0 目录匹配。

**匹配流程**：

1. 递归遍历 **全部** Wiki 版本目录，获取 PRD 列表（标题 + URL + token）
2. 对每条需求，确定其 **原始版本**（从来源字段或 JIRA tag 推断）
3. **优先在原始版本目录中匹配 PRD**
4. 若原始版本无匹配，搜索相邻版本

**匹配规则**：
```
1. 原始版本目录（如需求来自 4.0，去 Camera 4.0-25111 找）     ← 首选
2. 相邻版本目录（±1 版本）                                    ← 次选
3. ❌ 禁止匹配低于原始版本 2 个版本以上的 PRD（如 4.0 需求不能匹配 3.0 PRD）
4. ❌ 禁止匹配高于原始版本 2 个版本以上的 PRD（如 3.5 需求不能匹配 5.1 PRD，除非确认是 forward-port）
```

**反例**：相机基础体验优化（原始版本 4.0/25111）→ 不应匹配 Camera 3.0 的 PRD，应匹配 Camera 4.0 的 `交互&视觉体验优化汇总`

5. 将匹配的 PRD URL 写入 Bitable
6. 无 PRD 匹配项列入审计报告，标注"需新建 PRD"

### Phase 6: 反向审核（Reverse Audit）

逐项检查：

| 检查项 | 通过标准 | 不通过动作 |
|--------|---------|-----------|
| 需求名 | 不含 JIRA tag，< 80 字 | 重新清洗 |
| 描述 | ≥ 50 字，含业务背景 | 补充或标记 [TBD] |
| 优先级 | 全部为 P0/P1/P2 | 修正 |
| 模块 | 全部匹配 feature-tree | 重新映射 |
| JIRA | 每条都有有效链接 | 创建缺失 JIRA |
| JIRA Device | 全部匹配当前项目 | 克隆到正确项目 |
| PRD | 有 PRD 的已链接 ≥ 80% | 解释缺失原因 |
| 去重 | 无相同需求出现两次 | 合并或标注区别 |

输出审计报告：

```
## 审计报告
- 总计: N 条
- 描述完整: X/N
- JIRA 齐全: X/N
- PRD 已关联: X/N
- 无 PRD 项: [列出 + 原因]
- 待补充: [列出 + 负责人]
```

---

## 常用操作速查

### 读取来源 Sheet
```bash
# 普通 Sheet
lark-cli sheets +cells-get --spreadsheet-token <token> --sheet-id <id> --as user

# 嵌入式 Bitable (resource_type: bitable)
lark-cli api GET /open-apis/bitable/v1/apps/<token>/tables/<table_id>/records --as user
```

### 创建 Bitable
```bash
lark-cli api POST /open-apis/bitable/v1/apps --data '{"name":"<项目> 需求列表"}' --as user
```

### 批量写入记录
字段名用中文名。**URL 字段使用 `{link, text}` 对象格式，`text` 用文档标题**：
```json
{"records": [{"fields": {
  "需求":"xxx", "优先级":"P0", "来源":"第一批",
  "JIRA": {"link":"https://...", "text":"NOS-1234"},
  "PRD": {"link":"https://...", "text":"【PRD】Camera 5.1 - 200MP 高像素"}
}}]}
```

### 创建 JIRA（23112 示例）
```bash
curl -u "$JIRA_EMAIL:$JIRA_TOKEN" -H "Content-Type: application/json" \
  -X POST "$JIRA_BASE_URL/rest/api/3/issue" \
  -d '{"fields":{"project":{"key":"NOS"},"summary":"[23112] xxx","issuetype":{"id":"10007"},"components":[{"name":"Camera"}],"customfield_10101":[{"id":"10930"}],"customfield_10682":{"id":"11268"},"customfield_10647":{"id":"11321"}}}'
```

### 递归遍历 Wiki 目录
```bash
lark-cli api GET "/open-apis/wiki/v2/spaces/7623306205619867360/nodes" \
  --params '{"parent_node_token":"<parent>","page_size":50}' --as user
```

---

## 与其他 Skill 的关系

| Skill | 调用时机 |
|-------|---------|
| `lark-base` | Bitable 创建、字段设计、记录读写 |
| `lark-sheets` | 读取来源 Sheet |
| `lark-wiki` | 目录遍历、节点移动、PRD 链接提取 |
| `lark-doc` | 读取 PRD 文档内容（需要匹配时） |
| `lark-im` | 从群聊提取需求共识 |
| `knowledge-base-manage` | 查看设备/传感器约束，验证硬件可行性 |
| `image-feature-prd-writer` | 无 PRD 的需求 → 写新 PRD

---

## 模块同步机制

**模块字段必须使用 SingleSelect（非 Text），选项集与 `knowledge/feature-tree.md` 保持严格同步。**

### 同步检查流程

1. 计算 `knowledge/feature-tree.md` 的 MD5 hash
2. 比较当前 Bitable 字段中存储的 tree hash（通过字段 description 或备注字段记录）
3. 若 hash 不匹配 → 重新提取所有模块路径，调用 API 更新字段选项
4. 排除 `快门区域` 及其子节点（feature-tree 明确"Feature List 不展开"）

### PRD 匹配策略

1. **优先从目标版本 wiki 目录搜索** — 调用 `lark-wiki` 递归遍历
2. 若未匹配，搜索相邻版本目录（±1 版本）或原始需求所属版本目录
3. PRD 字段类型为 URL（类型 15），**`text` 必须用文档实际标题**（如 `【PRD】Camera 5.1 - 200MP 高像素`），非笼统的 "PRD"
4. 无 PRD 匹配项记录到审计报告

---

## 数据来源优先级

**多个来源冲突时，以最新、最权威的来源为准**：

1. **技术评估申请表（如 v1.3）** > 功能需求澄清计划表（如 v1.0）
2. 若申请表标记"需求关闭"，以用户确认是否保留为准
3. 若申请表有新增需求，合并入最终列表
4. 优先级以最新来源为准（v1.3 P1 覆盖 v1.0 P0）

---

## ⚠️ 常见踩坑记录

### 字段类型

- **User 字段是 type=11，不是 13**。type=13 是 Phone，会报 "Failed to convert phone field"
- 修改字段类型需**先删后建**，不能直接更新 type。删除字段会清空所有记录中该字段的值，需提前备份

### API 操作

- `batch_create` 上限 500 条/次，普通批量写入可用
- `batch_update` / `batch_delete` 端点与 `batch_create` 不同，可能不存在或返回 404
- **大量逐条更新时，每次调用前刷新 token**（避免 token 中途过期导致静默失败）
- **新建 Bitable 后应用无权限自动访问**，需用户将 app（`cli_a947663f3ff89eef`）添加为协作者

### 模块映射

- `Shutter` / `快门区域` 不是合法模块名，动态照片应映射到 `Toolbar | 动态照片`
- Preset / Settings / Widget 必须带 `通用 / Common` 前缀
- 模块选项与 feature-tree 严格同步，去掉了 71 个外的任何自定义名称

### PRD 链接

- PRD 字段的 `text` 用文档实际标题，Bitable 才会显示文件名而非 "PRD" 二字
- 优先搜目标版本 wiki 目录，未命中再搜相邻版本
- 继承类需求（继承 25111 Pro / NOS 5.0）无需 PRD

### 多来源合并

- Jack CSV 可能存在重复行号（如 v1.3 的 #40、#51 重复），需人工合并
- 空列（如无设计稿/排期的行）不影响需求提取，只影响备注
- 相册需求在 Camera RL 中不显示（显式排除）
