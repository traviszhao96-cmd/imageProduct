---
name: server-camera-analytics
description: Use when the user wants to query the shared remote camera analytics SQLite database over HTTP, especially for tables like `photo_events_parsed`, `camera_events_raw`, and `photo_events_time_buckets`.
---

# Server Camera Analytics

## Overview

Use this skill when camera analytics data has been moved onto a shared server and you need to query it interactively from a local Codex session.

The default client entrypoint is:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/server_sqlite_query_client.py
```

This skill assumes the local environment already has:

- `ANALYTICS_QUERY_BASE_URL`
- `ANALYTICS_QUERY_TOKEN`

For feature-to-field mapping, read:

- [references/field-mapping.md](references/field-mapping.md)

## Workflow

1. Start by listing tables:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/server_sqlite_query_client.py tables
```

2. If the user asks a new question, translate it into read-only SQL.

3. Query with:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/server_sqlite_query_client.py query \
  --sql "SELECT * FROM photo_events_parsed LIMIT 5;"
```

4. Return both:

- the SQL when useful
- the key result in Chinese

## Table Hints

Current SQLite database commonly includes:

- `photo_events_parsed`
- `camera_events_raw`
- `photo_events_time_buckets`

Important fields in `photo_events_parsed`:

- `event_date`
- `exact_time`
- `user_pseudo_id`
- `model_name`
- `country`
- `photo_mode`
- `camera_id`
- `zoom_ratio`
- `lux`
- `adrc`
- `cct`
- `face_count`
- `orientation`
- `nightmode`
- `preset`
- `watermark`
- `retouching`

Additional feature fields to look for in newer exports / rebuilt databases:

- `filter`
- `exposure_adjust`
- `tuning_apply`
- `tuning_contrast`
- `tuning_saturation`
- `tuning_warmth`
- `tuning_tint`
- `tuning_shapen`
- `tuning_grain`
- `tuning_vignette`

Filter classification reminder:

- Do not use `preset` to answer filter questions.
- For `filter`, use the official list from `Nothing Filter 3.1 for Camera_Gallery.xlsx`.
- Treat raw aliases like `cc` -> `CC Film` and `b&w` -> `B&W Film`.
- Treat numeric values like `101`, `102` as DIY / custom unless product provides an official mapping table.

## Query Rules

- Only use read-only SQL.
- Prefer `SELECT` and `WITH`.
- Keep results narrow and useful.
- Add `LIMIT` when exploring.
- For business analysis, pair event counts with user counts when relevant.
- If the metric could be ambiguous, explain the assumed definition briefly.
- If a requested feature field is not present in the current shared database, say so clearly and recommend rebuilding the database or checking `raw_photo_info` / the raw export first.
