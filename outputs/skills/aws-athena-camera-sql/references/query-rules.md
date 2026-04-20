# Query Rules

## Base Facts

- Query engine: AWS Athena / Presto syntax
- Main table: `data_mobile_behavior`
- Camera event filter: `event_name = 'NTCamera'`
- Main nested field: `event_params`
- Expand nested params with:

```sql
CROSS JOIN UNNEST(event_params) AS t(param)
```

## Event Types

- `general`: settings / operation events
- `photo_info`: one completed photo capture
- `video_info`: one completed video capture
- `pef_info`: performance metrics
- `OS_Active`: phone DAU denominator
- `App_Launch` with camera package markers: camera DAU helper in some historical queries

## Required Patterns

### Project filter

Use SW code in `project_name`.

```sql
AND project_name = 'Metroid'
```

or

```sql
AND project_name IN ('Frogger', 'FroggerPro')
```

### Time filter

```sql
AND event_date BETWEEN '2026-03-23' AND '2026-03-29'
```

### Packed key filter

```sql
AND param.key = 'photo_info'
AND param.string_value IS NOT NULL
```

## Parsing Rules

### Strings

```sql
LOWER(TRIM(REGEXP_EXTRACT(param.string_value, 'photoMode:([^;]+)', 1))) AS photo_mode
```

### Integers

```sql
TRY_CAST(REGEXP_EXTRACT(param.string_value, 'camera_id:([0-9]+)', 1) AS INTEGER)
```

### Doubles

```sql
TRY_CAST(REGEXP_EXTRACT(param.string_value, 'zoom_ratio:([0-9\\.]+)', 1) AS DOUBLE)
```

### Safe enum cleanup

```sql
CASE
    WHEN raw_mode IN ('3', 'portrait', 'protrait') THEN 'portrait'
    ELSE raw_mode
END
```

## Business Rules

- Default user metric: `COUNT(DISTINCT user_pseudo_id)`
- For adoption / preference / anomaly topics, output:
  - event count or share
  - distinct users or user penetration
- `lux` must be described as an internal AEC brightness index
- For overseas analysis, commonly exclude:

```sql
AND (geo.country IS NULL OR LOWER(geo.country) NOT IN ('china', 'cn', '中国'))
```

If city-level exclusion is needed:

```sql
AND (geo.city IS NULL OR geo.city NOT IN ('Hong Kong', 'Shenzhen', '香港', '深圳'))
```

## Output Style

- Prefer CTEs
- Keep SQL executable
- Add short Chinese comments, especially for:
  - packed-field parsing
  - numerator / denominator
  - regional filters
  - enum normalization
