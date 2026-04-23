# Common Templates

## 1. Output 5 sample payload rows

Use this before writing complex parsing SQL or when the previous query failed.

```sql
WITH sample_rows AS (
  SELECT
    event_date,
    param.string_value AS sample_value
  FROM data_mobile_behavior
  CROSS JOIN UNNEST(event_params) AS t(param)
  WHERE event_name = 'NTCamera'
    AND project_name = 'Metroid'
    AND param.key = 'photo_info'
    AND param.string_value IS NOT NULL
    AND event_date BETWEEN '2025-08-01' AND '2025-08-07'
  ORDER BY RAND()
  LIMIT 5
)
SELECT
  event_date,
  sample_value
FROM sample_rows;
```

## 2. Camera DAU vs total DAU

```sql
WITH camera_users AS (
    SELECT
        event_date,
        COUNT(DISTINCT user_pseudo_id) AS camera_dau
    FROM data_mobile_behavior
    WHERE event_name = 'App_Launch'
      AND project_name = 'Galaga'
      AND event_date BETWEEN '2025-07-01' AND '2025-07-10'
      AND any_match(event_params, param -> param.key = 'com.nothing.camera')
    GROUP BY event_date
),
total_dau AS (
    SELECT
        event_date,
        COUNT(DISTINCT user_pseudo_id) AS total_dau
    FROM data_mobile_behavior
    WHERE event_name = 'OS_Active'
      AND project_name = 'Galaga'
      AND event_date BETWEEN '2025-07-01' AND '2025-07-10'
      AND any_match(event_params, param -> param.key = 'active_time')
    GROUP BY event_date
)
SELECT
    c.event_date,
    c.camera_dau,
    t.total_dau,
    ROUND(c.camera_dau * 1.0 / t.total_dau, 4) AS camera_dau_rate
FROM camera_users c
JOIN total_dau t ON c.event_date = t.event_date
ORDER BY c.event_date;
```

## 3. Photo APU

```sql
WITH photo_events AS (
    SELECT
        event_date,
        user_pseudo_id,
        param.string_value AS photo_info_value
    FROM data_mobile_behavior
    CROSS JOIN UNNEST(event_params) AS t(param)
    WHERE event_name = 'NTCamera'
      AND project_name = 'Metroid'
      AND event_date BETWEEN '2025-08-01' AND '2025-08-07'
      AND param.key = 'photo_info'
      AND param.string_value IS NOT NULL
),
user_photo_counts AS (
    SELECT
        event_date,
        user_pseudo_id,
        COUNT(*) AS photo_count
    FROM photo_events
    GROUP BY event_date, user_pseudo_id
)
SELECT
    event_date,
    COUNT(DISTINCT user_pseudo_id) AS camera_dau,
    SUM(photo_count) AS total_photos,
    ROUND(AVG(photo_count), 2) AS avg_photos_per_user
FROM user_photo_counts
GROUP BY event_date
ORDER BY event_date;
```

## 4. Mode penetration

```sql
WITH photo_events AS (
    SELECT
        user_pseudo_id,
        param.string_value AS photo_info_value
    FROM data_mobile_behavior
    CROSS JOIN UNNEST(event_params) AS t(param)
    WHERE event_name = 'NTCamera'
      AND project_name = 'Metroid'
      AND event_date BETWEEN '2026-03-01' AND '2026-03-07'
      AND param.key = 'photo_info'
      AND param.string_value IS NOT NULL
),
photo_mode_extracted AS (
    SELECT
        user_pseudo_id,
        LOWER(TRIM(REGEXP_EXTRACT(photo_info_value, 'photoMode:([^;]+)', 1))) AS raw_mode
    FROM photo_events
    WHERE photo_info_value LIKE '%photoMode:%'
),
mode_standardized AS (
    SELECT
        user_pseudo_id,
        CASE
            WHEN raw_mode IN ('1', 'photo') THEN 'photo'
            WHEN raw_mode IN ('2', 'expert') THEN 'expert'
            WHEN raw_mode IN ('3', 'portrait', 'protrait') THEN 'portrait'
            WHEN raw_mode IN ('4', 'pano') THEN 'pano'
            WHEN raw_mode IN ('5', 'macro') THEN 'macro'
            WHEN raw_mode IN ('6', 'video_shot') THEN 'video_shot'
            WHEN raw_mode = '7' THEN 'tele_macro'
            WHEN raw_mode IN ('8', 'night') THEN 'night'
            ELSE raw_mode
        END AS clean_mode
    FROM photo_mode_extracted
    WHERE raw_mode IS NOT NULL
),
mode_counts AS (
    SELECT
        COALESCE(clean_mode, 'unknown') AS photo_mode,
        COUNT(*) AS events_count,
        COUNT(DISTINCT user_pseudo_id) AS users_count
    FROM mode_standardized
    GROUP BY clean_mode
),
totals AS (
    SELECT
        COUNT(*) AS total_events,
        COUNT(DISTINCT user_pseudo_id) AS camera_dau
    FROM mode_standardized
)
SELECT
    m.photo_mode,
    m.events_count,
    m.users_count,
    ROUND(m.events_count * 1.0 / NULLIF(t.total_events, 0), 4) AS event_ratio,
    ROUND(m.users_count * 1.0 / NULLIF(t.camera_dau, 0), 4) AS user_ratio
FROM mode_counts m
CROSS JOIN totals t
ORDER BY m.events_count DESC;
```

## 5. Preset usage

```sql
WITH photo_events AS (
    SELECT
        user_pseudo_id,
        param.string_value AS photo_info_value
    FROM data_mobile_behavior
    CROSS JOIN UNNEST(event_params) AS t(param)
    WHERE event_name = 'NTCamera'
      AND project_name = 'Metroid'
      AND event_date BETWEEN '2025-08-01' AND '2025-08-07'
      AND param.key = 'photo_info'
      AND param.string_value IS NOT NULL
),
preset_extracted AS (
    SELECT
        user_pseudo_id,
        COALESCE(NULLIF(REGEXP_EXTRACT(photo_info_value, 'preset:([^;]+)'), ''), 'none') AS preset_value
    FROM photo_events
    WHERE photo_info_value LIKE '%preset:%'
),
preset_counts AS (
    SELECT
        preset_value,
        COUNT(*) AS events_count,
        COUNT(DISTINCT user_pseudo_id) AS users_count
    FROM preset_extracted
    GROUP BY preset_value
),
totals AS (
    SELECT
        COUNT(*) AS total_events,
        COUNT(DISTINCT user_pseudo_id) AS camera_dau
    FROM preset_extracted
)
SELECT
    p.preset_value,
    p.events_count,
    p.users_count,
    ROUND(p.events_count * 1.0 / t.total_events, 4) AS event_ratio,
    ROUND(p.users_count * 1.0 / t.camera_dau, 4) AS user_ratio
FROM preset_counts p
CROSS JOIN totals t
ORDER BY p.events_count DESC;
```

## 6. Raw photo export

```sql
SELECT
    event_date,
    CAST(from_unixtime(event_timestamp / 1000000.0) AS VARCHAR) AS exact_time,
    user_pseudo_id,
    project_name AS model_name,
    geo.country,
    param.string_value AS raw_photo_info,
    LOWER(TRIM(REGEXP_EXTRACT(param.string_value, 'photoMode:([^;]+)', 1))) AS photo_mode,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'camera_id:([0-9]+)', 1) AS INTEGER) AS camera_id,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'zoom_ratio:([0-9\\.]+)', 1) AS DOUBLE) AS zoom_ratio,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'lux:([0-9\\.]+)', 1) AS DOUBLE) AS lux,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'adrc:([0-9\\.]+)', 1) AS DOUBLE) AS adrc,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'cct:([0-9\\.]+)', 1) AS DOUBLE) AS cct,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'exp_time:([0-9]+)', 1) AS DOUBLE) AS exp_time_ns,
    COALESCE(NULLIF(TRIM(REGEXP_EXTRACT(param.string_value, 'shot_algo:([^;]+)', 1)), ''), 'None') AS shot_algo,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'face_count:([0-9]+)', 1) AS INTEGER) AS face_count,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'orientation:([0-9]+)', 1) AS INTEGER) AS orientation,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'exposure_adjust:([0-9\\-]+)', 1) AS INTEGER) AS exposure_adjust,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'nightmode:([0-9]+)', 1) AS INTEGER) AS nightmode,
    REGEXP_EXTRACT(param.string_value, 'preset:([^;]+)', 1) AS preset,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'watermark:([0-9]+)', 1) AS INTEGER) AS watermark,
    TRY_CAST(REGEXP_EXTRACT(param.string_value, 'retouching:([0-9]+)', 1) AS INTEGER) AS retouching
FROM data_mobile_behavior
CROSS JOIN UNNEST(event_params) AS t(param)
WHERE event_name = 'NTCamera'
  AND project_name IN ('Frogger', 'FroggerPro')
  AND event_date BETWEEN '2026-04-01' AND '2026-04-14'
  AND param.key = 'photo_info'
  AND param.string_value IS NOT NULL
  AND (geo.country IS NULL OR LOWER(geo.country) NOT IN ('china', 'cn', '中国'));
```
