# Nothing Camera Athena SQL Playbook

## Scope

Use this playbook when writing Athena / Presto SQL or analysis reports for Nothing camera telemetry.

## Core Query Rules

1. Main table defaults to `data_mobile_behavior`.
2. Camera parameters live inside `event_params`; expand them with:

```sql
CROSS JOIN UNNEST(event_params) AS t(param)
```

3. Filter the target key and discard null payloads:

```sql
WHERE param.key = 'photo_info'
  AND param.string_value IS NOT NULL
```

4. Extract numerics from packed strings with safe casting:

```sql
TRY_CAST(REGEXP_EXTRACT(param.string_value, 'zoomRatio:([0-9\\.]+)', 1) AS DOUBLE)
```

5. Never compare floating zoom ratios with `=`.

```sql
ROUND(zoom_ratio, 1) = 3.5
```

6. Do not treat `lux` as physical lux. It is an ISP-side AEC index. When a brightness threshold is needed, first compute distribution stats such as `approx_percentile(lux, 0.5)` and `approx_percentile(lux, 0.75)`.

## Business Output Rules

For anomaly analysis, feature penetration, or defect-trigger analysis, always output both:

- Event share: `target event count / total capture count`
- User penetration: `target distinct user_pseudo_id / total distinct user_pseudo_id`

For overseas dashboards or investigations, exclude:

```sql
geo.country NOT IN ('China', 'Hong Kong')
```

Map model names with `project_name` first, using [project-mapping.md](project-mapping.md). If one `project_name` can represent multiple SKUs, refine with `model_code`.

## Output Style

- Use CTEs to layer logic cleanly.
- Add short Chinese comments around:
  - key extraction
  - packed-string parsing
  - business filters
  - numerator / denominator definitions
- Keep business conclusions concise and evidence-based.
- If current SQL cannot support the requested conclusion, say so and provide a corrected SQL draft.

## Skeleton

```sql
WITH exploded AS (
  SELECT
    dt,
    user_pseudo_id,
    project_name,
    geo.country AS country,
    param.string_value AS photo_info_raw
  FROM data_mobile_behavior
  CROSS JOIN UNNEST(event_params) AS t(param)
  WHERE event_name = 'NTCamera'
    AND param.key = 'photo_info'
    AND param.string_value IS NOT NULL
),
parsed AS (
  SELECT
    dt,
    user_pseudo_id,
    project_name,
    country,
    -- 解析打包字符串中的拍摄模式
    REGEXP_EXTRACT(photo_info_raw, 'photoMode:([^,]+)', 1) AS photo_mode,
    -- 安全提取变焦倍数
    TRY_CAST(REGEXP_EXTRACT(photo_info_raw, 'zoomRatio:([0-9\\.]+)', 1) AS DOUBLE) AS zoom_ratio
  FROM exploded
),
agg AS (
  SELECT
    project_name,
    COUNT(*) AS total_capture_cnt,
    COUNT(DISTINCT user_pseudo_id) AS total_user_cnt,
    COUNT_IF(ROUND(zoom_ratio, 1) = 3.5) AS target_capture_cnt,
    COUNT(DISTINCT CASE WHEN ROUND(zoom_ratio, 1) = 3.5 THEN user_pseudo_id END) AS target_user_cnt
  FROM parsed
  WHERE country NOT IN ('China', 'Hong Kong')
  GROUP BY 1
)
SELECT
  project_name,
  total_capture_cnt,
  total_user_cnt,
  target_capture_cnt,
  target_user_cnt,
  target_capture_cnt * 1.0 / NULLIF(total_capture_cnt, 0) AS event_share,
  target_user_cnt * 1.0 / NULLIF(total_user_cnt, 0) AS user_penetration
FROM agg
ORDER BY event_share DESC;
```
