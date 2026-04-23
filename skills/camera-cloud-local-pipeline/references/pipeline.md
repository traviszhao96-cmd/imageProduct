# Pipeline

## Default Flow

1. Fetch source file into raw data directory
2. Inspect CSV header
3. Import into SQLite with `/Users/travis.zhao/imageProduct/scripts/local_sql_analytics.py`
4. If the file is an exploded event export with:
   - `event_key`
   - `string_value`
   then parse `photo_info` into `photo_events_parsed` with `/Users/travis.zhao/imageProduct/scripts/parse_camera_event_table.py`

## Default Table Selection

- Header contains `event_key` and `string_value` -> `camera_events_raw`
- Header contains `raw_photo_info` or already parsed photo columns -> `photo_events_raw`
- Otherwise -> `raw_import`

## Good Uses

- new weekly or daily remote export
- large India / region package that should land locally once and be reused
- repeated server handoff workflow

## Notes

- The importer already supports streaming CSV import for large files.
- Parsing `photo_info` after import is optional but usually worth doing for local dashboard work.
