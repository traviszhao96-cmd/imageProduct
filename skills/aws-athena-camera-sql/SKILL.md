---
name: aws-athena-camera-sql
description: Use when the user wants Athena/Presto SQL for camera telemetry on AWS, especially for queries against `data_mobile_behavior`, `event_params`, `NTCamera`, `photo_info`, `video_info`, `pef_info`, DAU/APU, mode penetration, preset usage, camera lens distribution, night mode, or raw export SQL.
---

# AWS Athena Camera SQL

## Overview

Use this skill for AWS Athena camera telemetry work. It turns natural-language camera analysis questions into Athena / Presto SQL using the team's house rules for `data_mobile_behavior`, SW code `project_name`, packed `event_params`, and common camera metrics.

## Quick Start

1. Identify the scope:
   - settings / entry behavior -> `general`
   - single-photo analysis -> `photo_info`
   - single-video analysis -> `video_info`
   - performance / latency -> `pef_info`
   - DAU / APU / exports -> broader event logic
2. Read [references/query-rules.md](references/query-rules.md).
3. If model mapping matters, read [references/model-mapping.md](references/model-mapping.md).
4. If the request matches a common analysis, reuse [references/common-templates.md](references/common-templates.md).
5. If the user mentions query failures, missing fields, or wants sample payloads first, read [references/troubleshooting.md](references/troubleshooting.md).

## Workflow

### 1. Normalize the project filter

- Use SW code in `project_name`, not internal or marketing names.
- Example: use `project_name = 'Galaga'`, not the human project name.
- If the user says a device family, map it through [references/model-mapping.md](references/model-mapping.md).

### 2. Pick the correct event grain

- `event_name = 'NTCamera'` is the base filter for camera telemetry.
- `general` events are user operations and settings toggles.
- `photo_info` is one record per completed photo capture.
- `video_info` is one record per completed video capture.
- `pef_info` is performance telemetry.

### 3. Parse packed payloads correctly

- Camera payloads live in `event_params`.
- Expand with:

```sql
CROSS JOIN UNNEST(event_params) AS t(param)
```

- Filter the target key and nulls explicitly.
- Use `REGEXP_EXTRACT` plus `TRY_CAST` to parse packed values from `param.string_value`.
- Avoid direct equality on floating zoom values; prefer `ROUND(value, 1)`.

### 4. Keep business output paired

For feature adoption, anomaly analysis, or behavior analysis, output both:

- event share
- user penetration

Default user metric:

```sql
COUNT(DISTINCT user_pseudo_id)
```

### 5. Follow team output style

- Return executable Athena / Presto SQL, not pseudo-SQL.
- Prefer layered CTEs.
- Add short Chinese comments around key extraction and business filters.
- If evidence is insufficient, say so plainly and provide the closest valid SQL.

## Built-in Defaults

- Main table: `data_mobile_behavior`
- Main camera event: `event_name = 'NTCamera'`
- Default time format: `YYYY-MM-DD`
- Default overseas exclusion when requested: exclude China / Hong Kong / Shenzhen style regions as needed
- When exporting raw photo data, include:
  - `event_date`
  - `exact_time`
  - `user_pseudo_id`
  - `project_name AS model_name`
  - `geo.country`
  - parsed camera fields such as `photo_mode`, `camera_id`, `zoom_ratio`, `lux`, `adrc`, `cct`, `exp_time_ns`, `shot_algo`, `face_count`, `orientation`, `exposure_adjust`, `nightmode`, `preset`, `watermark`, `retouching`

## Special Rules

- `lux` is an AEC / ISP-side brightness index, not physical lux.
- `protrait` may appear in payloads and should usually be standardized to `portrait`.
- `preset = 0` means no preset applied.
- If the query fails because parsing assumptions are weak, first output 5 sample payload rows and repair the regex from evidence.
- If the user asks for full exports, prefer a clean parsed export over dumping raw nested records.

## References

- Query rules: [references/query-rules.md](references/query-rules.md)
- Common templates: [references/common-templates.md](references/common-templates.md)
- Model mapping: [references/model-mapping.md](references/model-mapping.md)
- Troubleshooting: [references/troubleshooting.md](references/troubleshooting.md)
