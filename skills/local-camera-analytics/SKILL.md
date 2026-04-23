---
name: local-camera-analytics
description: Use when the user wants to analyze exported camera telemetry locally, especially when data has been downloaded as CSV/JSON/JSONL and needs to be imported into SQLite, queried with SQL, turned into charts, or summarized into dashboard-style reports from fields such as `photo_info`, `video_info`, `lux`, `cct`, `adrc`, `camera_id`, `photo_mode`, and `preset`.
---

# Local Camera Analytics

## Overview

Use this skill for local-first camera data analysis. It covers the full loop: place exported files in the workspace, import them into a local SQLite database, write SQL against the resulting tables, interpret the results against the camera telemetry schema, and produce plots or short business reports.

This skill supports both photo and video analysis. For video questions, treat `video_info` as one completed video record and remember that some environment fields are reported separately for the first and last frame.

## When To Use

Use this skill when the user:

- has downloaded camera data from a server and wants to query it locally
- wants to build a local SQLite workflow instead of relying on remote agents or restricted APIs
- needs SQL on exported `photo_info` / `video_info` style data
- wants a dashboard-style analysis report from local data
- wants plots from fields such as `lux`, `cct`, `adrc`, `camera_id`, or `photo_mode`
- wants local video analysis for mode, duration, quality, HLG, filter, tuning, preset, or face metrics

Do not use this skill for direct Athena / Presto SQL on AWS. For that, use `$aws-athena-camera-sql`.

## Quick Start

1. Inspect available local DBs first with `/Users/travis.zhao/imageProduct/scripts/list_local_camera_dbs.py`.
2. Put raw exports under `/Users/travis.zhao/imageProduct/docs/00_inbox/shared/raw_data/`.
3. Import files into SQLite with `/Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py`.
4. Read the local workflow guide in [references/local-workflow.md](references/local-workflow.md).
5. Read the DB routing notes in [references/local-database-catalog.md](references/local-database-catalog.md).
6. Read [references/project-mapping.md](references/project-mapping.md) when the user asks by whole-device project, marketing name, SW code, or model code.
7. For camera field meaning and dashboard logic, read [references/analysis-playbook.md](references/analysis-playbook.md).
8. For a full executive-style analysis template that covers Portrait / Video / Feature / Compare, read [references/full-analysis-template.md](references/full-analysis-template.md).
9. For local video structure, report logic, and first-frame / last-frame rules, read [references/video-analysis-playbook.md](references/video-analysis-playbook.md).
10. For a reusable local video report layout, read [references/video-report-template.md](references/video-report-template.md).
11. For charting, read [references/charting.md](references/charting.md).

## Workflow

### 1. Confirm the local data location

- Inspect the local DB catalog first:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/list_local_camera_dbs.py
```

- Raw downloaded exports usually live in:
  - `/Users/travis.zhao/imageProduct/docs/00_inbox/shared/raw_data/`
- Local DBs commonly include:
  - `/Users/travis.zhao/imageProduct/outputs/local_analytics/india_4_1_4_7.db`
  - `/Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db`

Routing rule:

- Default to the best matching local parsed DB first
- Only ask the user to clarify the data source after checking which local DBs already exist
- Only jump to Athena when the local DB cannot satisfy the request

### 2. Import the files

Use:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py import \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db \
  --table photo_events_raw \
  --source /absolute/path/to/file.csv \
  --if-exists replace
```

The importer supports `CSV / JSON / JSONL`, sanitizes field names, infers simple types, and appends or replaces tables.

### 3. Query locally with SQL

Use:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py query \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db \
  --sql "SELECT photo_mode, COUNT(*) FROM photo_events_raw GROUP BY 1;"
```

For country / project / date specific questions, prefer a parsed DB when available:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py query \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/india_4_1_4_7.db \
  --sql "SELECT event_date, model_name, country, COUNT(*) FROM photo_events_parsed GROUP BY 1,2,3 LIMIT 20;"
```

For raw exploded event exports, route by `event_key`:

- `photo_info` -> photo capture analysis
- `video_info` -> video behavior analysis
- `pef_info` -> performance analysis
- `general` -> settings and behavior events

### 4. Interpret fields with camera context

Common locally available columns in parsed photo exports include:

- `event_date`
- `exact_time`
- `user_pseudo_id`
- `model_name`
- `country`
- `raw_photo_info`
- `photo_mode`
- `camera_id`
- `zoom_ratio`
- `lux`
- `adrc`
- `cct`
- `exp_time_ns`
- `shot_algo`
- `face_count`
- `orientation`
- `exposure_adjust`
- `nightmode`
- `preset`
- `watermark`
- `retouching`

Camera name mapping:

- `camera_id = 0` -> `主摄` / `后置广角` / `Wide`
- `camera_id = 1` -> `前置` / `Front`
- `camera_id = 2` -> `超广` / `后置超广` / `UW`
- `camera_id = 3` -> `长焦` / `后置长焦` / `Tele`
- `camera_id = 4` -> current local data may contain this value, but mapping is still incomplete and should be called out explicitly instead of guessed

Special notes:

- `lux` is an AEC / ISP-side brightness index, not physical lux.
- `protrait` may need to be normalized to `portrait`.
- `preset = 0` means no preset applied.
- `camera_id=4` and `nightmode=3` may appear in data even if the workbook mapping is incomplete.
- `retouching` is often the first local proxy for “美颜”, but answers should still include one short line defining the metric.

When the user writes camera names in natural language, normalize them before writing SQL:

- `主摄`, `后置广角`, `wide`, `main camera` -> `camera_id = 0`
- `前置`, `front`, `selfie camera` -> `camera_id = 1`
- `超广`, `后置超广`, `uw`, `ultra wide` -> `camera_id = 2`
- `长焦`, `后置长焦`, `tele`, `telephoto` -> `camera_id = 3`

If the user says “不同摄像头” without naming one, prefer returning both `camera_id` and the mapped camera name in SQL output.

### 4.1 Normalize device / project names before SQL

If the user asks by:

- marketing name
- whole-device project
- project code
- project name
- SW code name
- model code

read [references/project-mapping.md](references/project-mapping.md) and normalize the request before writing SQL.

Examples:

- `Nothing Phone (4a)` -> local `model_name = 'Frogger'`
- `Nothing Phone (4a) Pro` -> local `model_name = 'FroggerPro'`
- `Bellsprout` -> likely the 4a family; confirm whether base / pro / both are needed
- `A069` -> filter the base 4a SKU
- `AIN065` -> India Nothing Phone (2)

### 4.2 Handle video fields explicitly

For `video_info`:

- treat one row as one completed video
- use `video_mode` for mode analysis
- use `video_length` for duration distribution
- use `quality` for resolution + fps analysis
- use `if_HLG` for HLG usage
- use `filter`, `filter_strength`, and `tuning_*` for creative-control analysis
- use `preset` for preset analysis
- treat `first_*` and `last_*` fields as start-frame and end-frame metrics, not interchangeable duplicates

For video reports, do not silently collapse first-frame and last-frame fields into one value. If the question is about recording environment, state whether you used:

- first frame only
- last frame only
- both first and last side by side
- delta between first and last

If the user asks for front vs rear face analysis, only claim that split when the local video dataset has an explicit camera-facing field, `camera_id`, or another stable front/rear marker. Do not guess front/rear from zoom ratio alone.

### 5. Generate reports and charts

- For dashboard or business summaries, follow [references/analysis-playbook.md](references/analysis-playbook.md).
- For full camera analysis reports that mix Portrait, Video, Feature, and Compare sections, follow [references/full-analysis-template.md](references/full-analysis-template.md).
- For video dashboard summaries, also follow [references/video-analysis-playbook.md](references/video-analysis-playbook.md) and [references/video-report-template.md](references/video-report-template.md).
- For `cct / lux / adrc` scatter plots, use:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/plot_lux_cct_adrc_scatter.py \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db \
  --output /Users/travis.zhao/imageProduct/outputs/lux_cct_adrc_scatter.svg
```

- The plotter also supports subgroup plots via `--where` and custom titles via `--title`.

## Output Rules

- Default to local-first. If the user just says “查一下数据”, do not begin by asking which data source to use.
- Before answering, inspect which local DBs exist and pick the one that best matches date / country / model / table coverage.
- If multiple local DBs exist, state which DB you used.
- If a local DB does not contain the requested date or parsed table, say that clearly before recommending Athena or another source.
- Do not substitute a different date range as if it answered the original question.
- When analyzing feature usage or behavior, prefer both:
  - event share
  - user penetration
- Be explicit about what the current local table can and cannot support.
- If the user asks for DAU / APU / performance and the current local export does not contain the required source events, say that clearly.
- When writing reports, keep them business-first and evidence-based.
- For video reports, always distinguish:
  - current local video coverage
  - whether first / last frame are both available
  - whether front / rear split is actually supported by the data

## References

- Local workflow: [references/local-workflow.md](references/local-workflow.md)
- Local DB catalog: [references/local-database-catalog.md](references/local-database-catalog.md)
- Project mapping: [references/project-mapping.md](references/project-mapping.md)
- Analysis playbook: [references/analysis-playbook.md](references/analysis-playbook.md)
- Full analysis template: [references/full-analysis-template.md](references/full-analysis-template.md)
- Video analysis playbook: [references/video-analysis-playbook.md](references/video-analysis-playbook.md)
- Video report template: [references/video-report-template.md](references/video-report-template.md)
- Charting: [references/charting.md](references/charting.md)
