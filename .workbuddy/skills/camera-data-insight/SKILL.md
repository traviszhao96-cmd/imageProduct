---
name: camera-data-insight
description: Use when the user wants to query camera telemetry data — either via Athena/Presto SQL on data_mobile_behavior, or via the remote SQLite server for photo_events_parsed. Covers SQL generation, business reports, field mapping, and data-retention rules. For Bitable management and event tracking design, use camera-tracking-manage instead.
---

# Camera Analytics

## Overview

This skill handles all camera telemetry queries — both Athena (data_mobile_behavior) and the shared remote SQLite database. For埋点 table management, event tracking design, and PRD writing, see `camera-tracking-manage`.

## ⚡ Query Execution Protocol（必走流程）

⚠️ **真正的资产是文档知识库（Skill + 模板 + 字段映射 + 踩坑记录），不是数据副本。**
本地库是过渡期的 sample 验证工具，最终只保留最小样本，甚至完全去掉。

核心理念：**信任文档。模板覆盖 ≥90% 常见查询，不需要验证。直接写 SQL。**

### Step 0: Trust The Docs（信任文档，<10s）

先查已有知识。模板存在 → 直接写 SQL。不许探头。

- [ ] 查 `references/field-mapping.md` — 产品用语 → 字段名
- [ ] 查 `camera_athena_queries.sql` — 匹配最近模板（9 个已验证）
- [ ] 查 `memory/data-report-index.md` — 是否有现成报告可复用

**→ 模板命中：基于模板直接写 SQL，跳过验证，直接进入 Step 1。**
**→ 模板未命中（新字段/新结构）：进入 Step 0a。**

### Step 0a: Sample Validation（仅在模板不存在时，<30s）

⚠️ 只有遇到文档里没记录的新字段/新格式时才触发。仅用最小 sample 验证 regex 和值域，不是跑全量。

```bash
# 最小 sample 验证：只跑 20 行，确认格式
python3 ~/imageProduct/scripts/local_sql_analytics.py query \
  --db ~/imageProduct/outputs/local_analytics/db/{sample}.db \
  --sql "SELECT ... FROM photo_events_parsed WHERE ... LIMIT 20"
```

验证通过后，**必须回写知识库**：
1. 新字段格式 → 补充到 `references/field-mapping.md`
2. 新查询模式 → 追加到 `camera_athena_queries.sql`
3. 新踩坑点 → 补充到本文 `## ⚠️ 实战踩坑` 章节
4. 然后进入 Step 1

### Step 1: One-Shot Athena（一次扫描出所有结果）

⚠️ 所有需要的维度在一个 CTE 中完成。**禁止分次扫描。**

```sql
-- ✅ 正确：CTE 一次扫描，多维度输出
WITH base AS (
  SELECT ... FROM data_mobile_behavior CROSS JOIN UNNEST(event_params) ...
  WHERE 条件
)
SELECT '聚合' AS label, model, COUNT(*) ... FROM base GROUP BY model
UNION ALL
SELECT '分滤镜', model, filter_val, COUNT(*) ... FROM base GROUP BY model, filter_val
```

| 需求场景 | 合并方法 |
|---------|---------|
| 总渗透率 + 分设备 | CTE 带 model，GROUP BY model |
| 总渗透率 + 分滤镜排名 | CTE 带 filter，窗口函数 `SUM() OVER (PARTITION BY model)` 算占比 |
| 总渗透率 + 分时间段趋势 | CTE 带 event_date，GROUP BY event_date, model |
| 多个独立指标 | 一个 CTE + UNION ALL 输出多个结果集 |

### Step 2: Cache & Update Knowledge（归档 + 反哺知识库）

1. 结果保存到 `~/imageProduct/outputs/athena_results/{主题}/{YYYY-MM-DD}.csv`
2. 更新 `memory/data-report-index.md` 追加新条目
3. 如果查询中发现文档未记录的模式 → 反哺到知识库（Step 0a 的规则同样适用）

---

## Input Quality Check

开始任何查询前，先判断用户输入是否足够。一句话需求（如"帮我查一下数据"、"看看相机使用率"）必须先追问：

| 缺乏的信息 | 需要确认 |
|-----------|---------|
| 查什么指标？ | 使用率、渗透率、分布、趋势 |
| 什么模式/参数？ | photoMode、camera_id、filter 等 |
| 什么时间范围？ | 日期范围（注意 6 个月保留限制） |
| 哪个数据源？ | Athena（生产） / 本地 sample（仅新字段验证） |
| 需要排除什么？ | 海外分析默认排除 China、Hong Kong |

## Data Sources

优先级：文档知识库 > 最小 sample 验证 > Athena。

### 1. 文档知识库（第一优先级）

真正的资产。所有可复用知识在这里，不依赖数据副本：
- [`camera_athena_queries.sql`](../scripts/camera_athena_queries.sql) — 11 个已验证 SQL 模板
- [`references/field-mapping.md`](references/field-mapping.md) — 产品用语 → 字段映射
- 本文 `## ⚠️ 实战踩坑` — schema 陷阱和历史兼容

### 2. 本地 Sample 库（仅用于新字段验证，过渡工具）

⚠️ **不是数据源。** 仅在遇到文档未记录的新字段/新格式时，用于验证 regex 和值域（LIMIT 20）。

最终目标：文档知识库足够完善后，可删除或压缩为最小样本。

```bash
python3 ~/imageProduct/scripts/local_sql_analytics.py query \
  --db ~/imageProduct/outputs/local_analytics/db/{sample}.db \
  --sql "SELECT ... LIMIT 20"
```

### 3. Athena (data_mobile_behavior)

唯一的生产数据源。所有正式查询在这里执行。规则：
- 基于模板直接写 SQL，不许探头
- 一次 CTE 扫描输出所有维度
- 结果必须归档

### 4. Remote SQLite (server_sqlite_query_client.py)

HTTP 远程 SQLite 数据库。常用表：`photo_events_parsed`、`camera_events_raw`、`photo_events_time_buckets`。

```bash
# 列出表
python3 /Users/travis.zhao/imageProduct/scripts/server_sqlite_query_client.py tables

# 查询
python3 /Users/travis.zhao/imageProduct/scripts/server_sqlite_query_client.py query \
  --sql "SELECT * FROM photo_events_parsed LIMIT 5;"
```

环境变量：`ANALYTICS_QUERY_BASE_URL`、`ANALYTICS_QUERY_TOKEN`。

## SQL Rules

### Athena 模式

- 使用 `CROSS JOIN UNNEST(event_params) AS t(param)` 展开参数
- 过滤参数：`param.key = '...'` 和 `param.string_value IS NOT NULL`
- 浮点字段用 `ROUND(value, 1)` 匹配
- 数值用 `TRY_CAST(REGEXP_EXTRACT(...))` 提取
- 使用 CTE 分层，中文注释

### SQLite 模式

- 只允许只读 SQL（SELECT、WITH）
- 禁止 DELETE/INSERT/UPDATE/DROP
- 探索时加 `LIMIT`
- 字段缺失时告知用户，建议重建数据库

## 历史拼写兼容

查询时需兼容历史拼写错误，**不要用"正确"拼写过滤**（会漏掉历史数据）：

| 原值 | 正确值 | 影响 |
|------|-------|------|
| `protrait` | `portrait` | photoMode |
| `tuning_shapen` | `tuning_sharpen` | label |
| `pef_info` | `perf_info` | key |

**Athena**: `WHERE string_value IN ('portrait', 'protrait')`
**SQLite**: `WHERE photo_mode IN ('portrait', 'protrait')`

## 数据保留窗口

Camera 埋点数据仅保留约 6 个月。不要写超出保留期的查询。如果用户要求的时间超出窗口，告知并建议重定向。

## 海外分析

默认排除 `China` 和 `Hong Kong`，除非用户明确覆盖。

## 常用字段

### photo_events_parsed (SQLite)

`event_date`, `exact_time`, `user_pseudo_id`, `model_name`, `country`, `photo_mode`, `camera_id`, `zoom_ratio`, `lux`, `adrc`, `cct`, `face_count`, `orientation`, `nightmode`, `preset`, `watermark`, `retouching`, `filter`, `exposure_adjust`, `tuning_apply`, `tuning_contrast`, `tuning_saturation`, `tuning_warmth`, `tuning_tint`, `tuning_shapen`, `tuning_grain`, `tuning_vignette`

### 字段映射

filter vs preset 是两个不同概念。查滤镜用 `filter` 字段，不要用 `preset` 字段。滤镜别名：`cc` → `CC Film`, `b&w` → `B&W Film`。数字值如 `101`/`102` 为自定义滤镜。

详细字段映射见 [references/field-mapping.md](references/field-mapping.md)。

## Mode Selection

- "帮我查"、"统计"、"写 SQL"、"渗透率" → 写 SQL
- "生成报告"、"解读"、"根据链接出结论" → 生成报告
- 两者混合 → 先写 SQL，再出报告

## Report Output

- SQL 用 CTE 分层，中文注释
- 业务结论简洁、直接、基于证据
- 同时报事件量和用户渗透率
- 证据不足时明确说明，不猜测
- 返回中文结论

## ⚠️ 实战踩坑（2026-06-26 更新）

以下是在实际查询 25111base 人像模式多条件组合时发现的坑，**写 SQL 前务必回顾**。

### 1. 表没有 `dt` 列

`data_mobile_behavior` **没有** `dt` 分区列。日期过滤用 `event_timestamp`（bigint, epoch 毫秒）：

```sql
-- ❌ 错
dt >= '2026-06-19'

-- ✅ 对
AND from_unixtime(event_timestamp / 1000) >= TIMESTAMP '2026-06-19 00:00:00'
AND from_unixtime(event_timestamp / 1000) < TIMESTAMP '2026-06-26 00:00:00'
```

### 2. photo_info 打包字符串的分隔符是 `;`（分号），不是 `,`（逗号）

原始字符串示例：
```
photoMode:protrait;filter:0;watermark:0;effects:0;hdr:2;retouching:0;...
```

如果用 `[^,]+` 做正则，由于字符串中没有逗号，会捕获整个剩余字符串，导致字段解析永远错误。某些字段值本身含有 `,`（如 `shot_algo:BokehHDR,CFR`），所以分隔符一定是 `;`。

```sql
-- ❌ 错（捕获整个剩余字符串）
REGEXP_EXTRACT(photo_info_raw, 'photoMode:([^,]+)', 1)

-- ✅ 对
REGEXP_EXTRACT(photo_info_raw, 'photoMode:([^;]+)', 1)
REGEXP_EXTRACT(photo_info_raw, 'retouching:([^;]+)', 1)
REGEXP_EXTRACT(photo_info_raw, 'filter:([^;]+)', 1)
```

### 3. photo_info 字段顺序不固定

某些字段（如 `ai_zoom`、`face_ratio`）在有数据时才出现，不会在所有行中一致。总是按名提取，不要按位置。

### 4. 写查询前先抽样验证

写包含多个字段解析的 SQL 前，**必须先 LIMIT 看原始字符串**，确认字段名/分隔符/值格式：

```sql
SELECT param.string_value AS photo_info_raw
FROM data_mobile_behavior
CROSS JOIN UNNEST(event_params) AS t(param)
WHERE event_name = 'NTCamera'
  AND param.key = 'photo_info'
  AND param.string_value IS NOT NULL
  AND project_name = 'Frogger'
LIMIT 5;
```

不这么做可能会白扫 700GB+ 后发现解析错误。

### 5. 多条件组合查询的逐步验证技巧

当多个功能叠加命中数为 0 时，不要直接改 SQL 扫全表重试。应当**逐步查询**各功能的交叉命中数，定位瓶颈：

```sql
-- 示例：逐步检查人像+美颜强+滤镜+水印+光斑+HDR 的衰减链
SELECT
  COUNT(*) AS total,
  COUNT_IF(retouching = '2') AS retouch2,
  COUNT_IF(retouching = '2' AND filter != '0') AS plus_filter,
  COUNT_IF(retouching = '2' AND filter != '0' AND watermark != '0') AS plus_wm,
  COUNT_IF(...) AS plus_effect,
  COUNT_IF(...) AS all
FROM ...
WHERE photo_mode = 'protrait';
```

## Reference Files

- [references/field-mapping.md](references/field-mapping.md) — 产品语言 → 数据库字段映射
