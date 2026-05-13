---
name: nothing-camera-athena
description: Use when the user wants Athena/Presto SQL, telemetry interpretation, or analysis reports for Nothing/CMF camera data. For Bitable management, event tracking design, or PRD writing, use camera-tracking-manage instead.
---

# Nothing Camera Athena

## Overview

This skill handles Athena/Presto SQL generation and telemetry analysis for Nothing/CMF camera data. For Bitable document management, event tracking design, and PRD writing, see the `camera-tracking-manage` skill.

Key inputs: the `data_mobile_behavior` table schema, the Camera App SW埋点 workbook, and the project-to-model mapping.

## Core Capabilities

### 1. 自然语言查数

Use this mode when the user describes a business question in plain Chinese or English and wants Athena SQL or directly wants the answer backed by SQL.

- Read [references/natural-language-query.md](references/natural-language-query.md).
- Also load the relevant sheet reference plus [references/project-mapping.md](references/project-mapping.md).
- Return production-ready Athena SQL, not pseudo-SQL.

### 2. 一键生成报告

Use this mode when the user wants a concise business report from an Athena link, `queryExecutionId`, SQL text, or SQL results.

- Read [references/report-generation.md](references/report-generation.md).
- Also load [references/sql-playbook.md](references/sql-playbook.md) and the relevant sheet reference when validating SQL semantics.
- If the environment provides an Athena fetch helper, use it. Otherwise analyze the SQL and result payload the user already supplied.

### 3. 埋点文档与 PRD 管理

When the user needs to read/sync the Bitable, design new event tracking specs, or write tracking sections into PRDs, **delegate to the `camera-tracking-manage` skill**. This skill only handles Athena SQL and telemetry analysis — do not mix document management into the query workflow.

Key reference files for Athena queries:
- `camera-event-tracking-bitable-v5.json` / `.md` — field names, allowed key/label values, historical error notes
- The historical spelling compatibility table and Bitable table IDs are maintained in the `camera-tracking-manage` skill

## Quick Start

- For SQL/query-writing rules and report output rules, read [references/sql-playbook.md](references/sql-playbook.md).
- For sheet-level telemetry fields and allowed values, open only the relevant sheet reference:
  - [references/general.md](references/general.md)
  - [references/photo.md](references/photo.md)
  - [references/video.md](references/video.md)
  - [references/performance.md](references/performance.md)
  - [references/workbook-overview.md](references/workbook-overview.md)
- [references/camera-event-tracking-bitable-v5.md](references/camera-event-tracking-bitable-v5.md) — 完整埋点参考（204条，含历史备注）
- [references/camera-event-tracking-bitable-v5.json](references/camera-event-tracking-bitable-v5.json) — JSON 原始数据

## 历史埋点拼写兼容（查询时注意）

以下拼写问题在 `camera-tracking-manage` skill 中维护。Athena 查询时需兼容，**不要用"正确"拼写过滤**（会漏掉历史数据）：

| 原值 | 影响 | Athena 查询建议 |
| --- | --- | --- |
| `pef_info` | key 字段名（9条） | `param.key = 'pef_info'` |
| `protrait` | photoMode string_value | `WHERE string_value = 'protrait'` |
| `tuning_shapen` | label 字段 | `WHERE label = 'tuning_shapen'` |

## Bitable 表参考

- 主表: `tbl3eedJjHPyCEf3` (数据表)
- 完整表结构、视图配置、历史拼写兼容表 → 见 `camera-tracking-manage` skill
- Bitable 数据快照: [references/camera-event-tracking-bitable-v5.json](references/camera-event-tracking-bitable-v5.json)
- For model aliasing and `project_name` / `model_code` mapping, read [references/project-mapping.md](references/project-mapping.md).

## Workflow

1. Identify which telemetry scope the user needs.
   - Settings / app-enter behavior -> `General`
   - Single-photo analysis -> `Photo`
   - Single-video analysis -> `Video`
   - performance / latency analysis -> `性能` (`pef_info`)

2. Normalize the model dimension before you write conclusions.
   - Prefer the analytics-facing `project_name` alias mapping in [references/project-mapping.md](references/project-mapping.md).
   - If a row groups multiple SKUs, disambiguate with `model_code`.
   - Do not confuse internal project names like `Bellsprout` with analytics aliases like `Frogger`.

3. Build Athena SQL with the playbook rules.
   - Use `data_mobile_behavior` as the base table unless the user explicitly says otherwise.
   - Expand `event_params` with `CROSS JOIN UNNEST(event_params) AS t(param)`.
   - Filter with `param.key = '...'` and `param.string_value IS NOT NULL`.
   - Extract numeric values with `TRY_CAST(REGEXP_EXTRACT(...))`.
   - Match floating zoom values with `ROUND(value, 1)`.
   - Treat `lux` as an internal AEC index; derive thresholds from distribution first.

4. Keep business metrics paired.
   - Always report both event share and user penetration when evaluating anomalies, defects, or feature adoption.
   - For overseas analysis, exclude `China` and `Hong Kong` unless the user overrides that requirement.

5. Enforce the data-retention window.
   - Camera telemetry is only retained for about 6 months.
   - Do not write queries that target dates older than roughly 6 months from the current date.
   - If the user asks for an older period, state that the data is likely already cleaned and redirect the query to an in-retention date range.
   - When the user gives relative dates such as “3月21日” or “最近一周”, resolve them against the current date and keep the final SQL inside the retention window.

6. Write outputs in the team's preferred style.
   - SQL should be layered with CTEs.
   - Key extraction and business filters should carry short Chinese comments.
   - Business conclusions should be short, direct, and evidence-based.
   - If evidence is insufficient, say so plainly instead of guessing.

## Mode Selection

- If the user asks "帮我查", "统计", "写 SQL", "想看某功能渗透率", or describes a metric question without giving SQL, go to 自然语言查数 mode.
- If the user asks "生成报告", "解读这条 Athena 查询", "根据这个链接出结论", or already provides SQL / result tables / Athena history links, go to 一键生成报告 mode.
- If the request mixes both, first write or validate the SQL, then produce the report in the same turn.

## Workbook Refresh

When the source xlsx changes, regenerate the sheet references with:

```bash
python3 scripts/export_camera_workbook_refs.py \
  --input "/absolute/path/to/Camera App SW 埋点 2025 v4.0.xlsx" \
  --output-dir references
```

This refreshes:

- `references/workbook-overview.md`
- `references/general.md`
- `references/photo.md`
- `references/video.md`
- `references/performance.md`

Do not hand-edit those generated files unless you are intentionally patching extraction output. The model/project mapping and SQL playbook live in separate hand-maintained references.

## Notes

- The source workbook currently exposes sheets `General`, `Photo`, `Video`, `性能`, and `History`.
- This skill assumes Athena / Presto syntax.
- Prefer loading only the specific reference file needed for the current request to keep context tight.
