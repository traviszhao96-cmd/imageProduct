---
name: camera-cloud-local-pipeline
description: Use when the user wants to fetch exported camera data from cloud or remote storage and automatically prepare a local analytics database, especially when the source is an HTTP URL, rsync/scp path, or local handoff file that should be downloaded, imported into SQLite, and optionally parsed into `photo_events_parsed`.
---

# Camera Cloud Local Pipeline

## Overview

Use this skill to turn a remote camera export into a ready-to-query local database. It handles three stages in one flow:

1. fetch the raw export into the workspace
2. import it into local SQLite
3. parse `photo_info` into a compact analysis table when the source is an exploded event table

## When To Use

Use this skill when the user:

- has a camera export on a server, URL, or remote path
- wants one command that downloads and prepares local analytics data
- needs a repeatable dependency-style pipeline instead of manual fetch + import + parse
- is working with exports that eventually become `camera_events_raw`, `photo_events_raw`, or `photo_events_parsed`

Do not use this skill for direct Athena querying on AWS. Use `$aws-athena-camera-sql` for that.

## Quick Start

Run:

```bash
python3 /Users/travis.zhao/.codex/skills/camera-cloud-local-pipeline/scripts/cloud_fetch_prepare.py \
  --source "user@host:/path/to/export.csv" \
  --workspace-root /Users/travis.zhao/imageProduct
```

or:

```bash
python3 /Users/travis.zhao/.codex/skills/camera-cloud-local-pipeline/scripts/cloud_fetch_prepare.py \
  --source "https://example.com/export.csv" \
  --workspace-root /Users/travis.zhao/imageProduct
```

## What The Script Does

1. downloads or copies the file into:
   - `/Users/travis.zhao/imageProduct/docs/00_inbox/shared/raw_data/`
2. imports it into:
   - `/Users/travis.zhao/imageProduct/outputs/local_analytics/<name>.db`
3. chooses a default source table from the CSV header:
   - exploded event export -> `camera_events_raw`
   - parsed photo export -> `photo_events_raw`
   - fallback -> `raw_import`
4. if the export is an exploded camera event table, it also builds:
   - `photo_events_parsed`

## Supported Source Types

- `http://...` or `https://...` -> fetched with `curl`
- `user@host:/remote/path.csv` or similar -> fetched with `rsync`
- absolute local file path -> copied locally

## Output Rules

- Prefer keeping raw files in `docs/00_inbox/shared/raw_data/`
- Prefer keeping databases in `outputs/local_analytics/`
- When the pipeline finishes, report:
  - downloaded file path
  - db path
  - source table
  - parsed table if created

## References

- Pipeline behavior: [references/pipeline.md](references/pipeline.md)
- Output locations: [references/paths.md](references/paths.md)
