# Local Database Catalog

Use this file when the user asks a local imaging data question and you need to decide which SQLite database to query first.

## Always Scan First

Before asking broad clarification questions about data source, run:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/list_local_camera_dbs.py
```

This tells you:

- which local `.db` files exist
- which tables they contain
- whether `photo_events_parsed` exists
- date range
- model coverage
- country coverage

## Current Important Databases

### `/Users/travis.zhao/imageProduct/outputs/local_analytics/india_4_1_4_7.db`

- Preferred local analytics source
- Current local tables:
  - `photo_events_parsed`
  - `video_events_parsed`
  - `photo_events_time_buckets`
  - `camera_events_raw`
- Date range:
  - `2026-04-01` to `2026-04-07`
- Main projects/models:
  - `Frogger`
  - `FroggerPro`
- Main country:
  - `India`

Use this DB first when the request mentions:

- local analytics
- `/Users/travis.zhao/imageProduct/outputs/local_analytics`
- India / 印度
- Frogger / FroggerPro
- 2026-04-01 to 2026-04-07
- local feature usage analysis
- local video analysis

### `/Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db`

- Local generic import / staging DB
- Current checked table:
  - `photo_events_raw`

Do not treat this as the default answer source for date-specific business questions when a parsed DB is available.

## Routing Rules

### Rule 1: Default to local parsed DBs

When the user says “查一下数据”, default order is:

1. local parsed DB with `photo_events_parsed` / `video_events_parsed`
2. local raw DB if parsed DB is unavailable
3. shared server DB
4. Athena / Presto

Do not jump to Athena first unless the user explicitly asks for Athena or the local DB clearly cannot answer.

### Rule 2: Scan before asking

Before asking “数据源是什么”, first inspect:

- date coverage
- country coverage
- model coverage
- parsed vs raw table availability

### Rule 3: Normalize business language

- `base项目` usually means a base model project, not a database name
- `印度数据` should bias toward India-tagged local DBs
- `global数据` should never be guessed; verify whether a global DB actually exists locally
- `人像模式` may appear as `protrait`
- `美颜` often maps to `retouching`, but the answer should still state the exact metric definition

### Rule 4: Never answer the wrong date as if it matched

If the local DB does not cover the requested date:

- state what DB was checked
- state its actual date range
- say the requested date is missing
- recommend the next best source

Do not silently substitute another week or month.

## Query Tips

When the result for a mode is empty, inspect actual mode values first:

```sql
SELECT photo_mode, COUNT(*)
FROM photo_events_parsed
WHERE event_date='2026-04-02'
  AND model_name='Frogger'
  AND camera_id=1
GROUP BY 1
ORDER BY 2 DESC;
```

When answering a usage-rate question, include:

- 总事件数
- 命中事件数
- 使用率
- 口径说明
