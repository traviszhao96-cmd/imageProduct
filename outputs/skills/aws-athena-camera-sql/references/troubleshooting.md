# Troubleshooting

## When a query fails

### 1. Verify payload shape first

If parsing SQL fails or returns empty results, output 5 random payload samples first.

Use the sample template in [common-templates.md](common-templates.md).

### 2. Common failure patterns

- Wrong `project_name`: user gave marketing name or internal name instead of SW code
- Wrong key: using `photo_info` for a video question or `video_info` for a photo question
- Missing `param.string_value IS NOT NULL`
- Regex key mismatch:
  - `photoMode` vs `video_mode`
  - `zoom_ratio` vs `first_zoom_ratio` / `last_zoom_ratio`
  - `if_HLG` is embedded inside `video_info`
- Equality on floating zoom values without rounding

### 3. Export before analysis if needed

When the analysis is broad or downstream work will happen locally, first write a parsed export SQL that includes:

- date / time / user / model / country
- raw packed payload
- parsed high-value fields

### 4. Regional filters

Use the correct filter level:

- `geo.country` for country removal
- `geo.city` only when the request explicitly needs city-level cleanup such as Hong Kong / Shenzhen

### 5. Timestamp serialization issues

When Athena output tooling fails on timestamp serialization, cast the timestamp to string:

```sql
CAST(from_unixtime(event_timestamp / 1000000.0) AS VARCHAR) AS exact_time
```

### 6. Reporting habit

After writing SQL for feature adoption, also state which denominator you used:

- total captures
- total distinct shooting users
- total DAU if using `OS_Active`
