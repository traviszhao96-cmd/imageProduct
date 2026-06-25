---
name: camera-data-insight
description: Use when the user wants to query camera telemetry data — either via Athena/Presto SQL on data_mobile_behavior, or via the remote SQLite server for photo_events_parsed. Covers SQL generation, business reports, field mapping, and data-retention rules. For Bitable management and event tracking design, use camera-tracking-manage instead.
---

# Camera Analytics

## Overview

This skill handles all camera telemetry queries — both Athena (data_mobile_behavior) and the shared remote SQLite database. For埋点 table management, event tracking design, and PRD writing, see `camera-tracking-manage`.

## Input Quality Check

开始任何查询前，先判断用户输入是否足够。一句话需求（如"帮我查一下数据"、"看看相机使用率"）必须先追问：

| 缺乏的信息 | 需要确认 |
|-----------|---------|
| 查什么指标？ | 使用率、渗透率、分布、趋势 |
| 什么模式/参数？ | photoMode、camera_id、filter 等 |
| 什么时间范围？ | 日期范围（注意 6 个月保留限制） |
| 哪个数据源？ | Athena / SQLite 远程库 |
| 需要排除什么？ | 海外分析默认排除 China、Hong Kong |

## Data Sources

### 1. Athena (data_mobile_behavior)

Athena/Presto 语法。主表 `data_mobile_behavior`。用于大规模 Camera 埋点分析。

### 2. Remote SQLite (server_sqlite_query_client.py)

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

## Reference Files

- [references/field-mapping.md](references/field-mapping.md) — 产品语言 → 数据库字段映射
