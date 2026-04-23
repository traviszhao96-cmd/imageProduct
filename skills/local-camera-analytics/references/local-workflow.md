# Local Workflow

## Main Paths

- Local raw export directory:
  - `/Users/travis.zhao/imageProduct/docs/00_inbox/shared/raw_data/`
- Local SQLite DB directory:
  - `/Users/travis.zhao/imageProduct/outputs/local_analytics/`
- Local parsed India DB:
  - `/Users/travis.zhao/imageProduct/outputs/local_analytics/india_4_1_4_7.db`
- Import/query helper:
  - `/Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py`
- DB catalog helper:
  - `/Users/travis.zhao/imageProduct/scripts/list_local_camera_dbs.py`

## Scan Before Query

Before asking the user which local DB to use, inspect the catalog first:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/list_local_camera_dbs.py
```

This is especially important when the request mentions:

- India / 印度
- base 项目
- Frogger / FroggerPro
- date-specific usage analysis

Default preference:

1. local parsed DB on `/Users/travis.zhao/imageProduct/outputs/local_analytics/`

## Import Command

```bash
python3 /Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py import \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db \
  --table photo_events_raw \
  --source /absolute/path/to/export.csv \
  --if-exists replace
```

## List Tables

```bash
python3 /Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py tables \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db
```

## Query

```bash
python3 /Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py query \
  --db /Users/travis.zhao/imageProduct/outputs/local_analytics/db/analytics.db \
  --sql "SELECT COUNT(*) FROM photo_events_raw;"
```

## Recommended Table Names

- `photo_events_raw`
- `video_events_raw`
- `general_events_raw`
- `performance_events_raw`

## When SQLite Is Enough

SQLite is usually fine when:

- the export is only a few days or weeks
- the dataset is a few hundred MB or low millions of rows
- the user mainly wants filtering, grouping, and simple aggregations

## When To Consider Upgrading

Consider DuckDB later if:

- direct `parquet` support becomes important
- the exports become much larger
- the user repeatedly needs heavier analytical workloads
