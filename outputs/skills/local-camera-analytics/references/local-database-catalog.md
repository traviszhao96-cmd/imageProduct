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

### `4a_4aPro_ROW_20260323-0329.db`

- **Path**: `/Users/travis.zhao/imageProduct/outputs/local_analytics/db/4a_4aPro_ROW_20260323-0329.db`
- **Region**: ROW (Rest of World, excludes India)
- **Models**: 4a (Frogger), 4a Pro (FroggerPro)
- **Date range**: 2026-03-23 ~ 2026-03-29
- **Data scale**: ~29.7 万张照片, 7,820 用户, 95 个国家
- **Tables**:
  - `photo_events_raw` — 照片事件（原始导入，HDR/flash/nightmode 等字段在 raw_photo_info 中）

Use this DB first when the request mentions:
- ROW / 全球（非 India）数据
- 2026-03-23 ~ 2026-03-29
- 4a / 4a Pro 早期数据
- 功能使用率分析（HDR、闪光灯、夜景等）

### `4a_4aPro_India_20260415-0421.db`

- **Path**: `/Users/travis.zhao/imageProduct/outputs/local_analytics/db/4a_4aPro_India_20260415-0421.db`
- **Region**: India
- **Models**: 4a (Frogger), 4a Pro (FroggerPro)
- **Date range**: 2026-04-15 ~ 2026-04-21
- **Data scale**: ~559 万张照片, 8.5 万用户
- **Tables**:
  - `camera_events_raw` — 原始相机事件
  - `photo_events_parsed` — 照片事件（已解析）
  - `video_events_parsed` — 视频事件（已解析）

Use this DB first when the request mentions:
- India / 印度数据
- 2026-04-15 ~ 2026-04-21
- 4a / 4a Pro
- 视频分析（video mode、HLG、duration 等）
- 照片+视频综合分析

## Routing Rules

### Rule 1: Default to local parsed DBs

When the user says "查一下数据", default order is:

1. latest local parsed DB with `photo_events_parsed` / `video_events_parsed`
2. local raw DB if parsed DB is unavailable
3. shared server DB
4. Athena / Presto

Do not jump to Athena first unless the user explicitly asks for Athena or the local DB clearly cannot answer.

### Rule 2: Scan before asking — ALWAYS present choices when user doesn't specify

When the user asks a data query without specifying which dataset to use:

1. **Always** run `list_local_camera_dbs.py` first (or use `ls -lh` on the db directory) to see current DB list
2. **Always** present the available databases to the user with key metadata (date range, region, models, scale)
3. Let the user choose before running the query

Format for presenting choices:
```
本地有以下数据库可用：
1. 4a_4aPro_ROW_20260323-0329 — ROW, 3/23-3/29, ~30万张
2. 4a_4aPro_India_20260415-0421 — India, 4/15-4/21, ~559万张
你要查哪个？
```

Before responding, inspect:
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

### Rule 6: Use new DB naming convention

Database files follow the naming convention:
`{models}_{region}_{YYYYMMDD-MMDD}.db`

Examples:
- `4a_4aPro_ROW_20260323-0329.db` — 4a + 4a Pro, Rest of World, Mar 23-29
- `4a_4aPro_India_20260415-0421.db` — 4a + 4a Pro, India, Apr 15-21

### Rule 5: Ignore invalid DB artifacts

- If a `.db` file is `0B`, ignore it.
- Never use `.db` files stored inside the skill directory itself.
- Only trust DBs surfaced by `list_local_camera_dbs.py` from the configured local roots.

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
