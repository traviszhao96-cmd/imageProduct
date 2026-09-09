# Athena mapping and query rules

## Confirmed identifier

NPS `deviceId` is the Android ID stored in Athena's `items` array:

```sql
element_at(
  filter(items, x -> lower(x.key) = 'aid'),
  1
).string_value
```

Use the value directly. Do not hash or reformat it.

## Region and source

- India: `ap-south-1`
- Other global data: `eu-north-1`
- Database/table: `dc_database.data_mobile_behavior`
- Camera event: `event_name = 'NTCamera'`
- Workgroup: `ad_hoc` for ordinary queries

Camera telemetry is retained for roughly six months. Always constrain `event_date`; do not run an unbounded device query.

## Batch query

Use `scripts/nps_camera_query.py` with either repeated `--device-id` arguments or a mapping CSV exported from the NPS system.

```bash
python3 scripts/nps_camera_query.py \
  --mapping-csv ./refid-deviceid.csv \
  --start-date 2026-08-14 \
  --end-date 2026-08-21 \
  --region ap-south-1 \
  --project SuperContra \
  --mode summary \
  --output ./nps-camera-summary.csv
```

Use `--dry-run` to inspect SQL without connecting to Athena. The script does not contain credentials; it uses the standard boto3 credential chain or the selected AWS profile.

## Required coverage metrics

After running the query, distinguish:

- deviceIds returned by NPS;
- deviceIds matched anywhere in Athena, if a general-event coverage query is run;
- deviceIds with `NTCamera` events;
- deviceIds with no Camera activity in the selected window.

No Camera event is not evidence of an invalid mapping. It may mean the device had no Camera activity, the date window is wrong, the region is wrong, the build did not upload telemetry, or retention has expired.

## Wrong fields

Do not use:

- `user_pseudo_id`;
- `user_id`;
- `device.device_id`;
- `device.device_id_2`;
- `event_params.aid`;
- `user_properties.aid`.

Those fields caused earlier false negatives because the NPS Android ID is in `items.aid`.
