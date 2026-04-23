# Video Analysis Playbook

## Scope

Use this reference when the local dataset contains `video_info`, usually as:

- `camera_events_raw` with `event_key = 'video_info'`
- a future parsed table such as `video_events_parsed`

Treat one `video_info` row as one completed video record.

## Field Coverage

Common video fields available in local raw exports:

- `video_mode`
- `video_length`
- `quality`
- `if_HLG`
- `filter`
- `filter_strength`
- `tuning_apply`
- `tuning_contrast`
- `tuning_saturation`
- `tuning_warmth`
- `tuning_tint`
- `tuning_shapen`
- `tuning_grain`
- `tuning_vignette`
- `preset`
- `first_zoom_ratio`
- `last_zoom_ratio`
- `first_orientation`
- `last_orientation`
- `first_lux`
- `last_lux`
- `first_adrc`
- `last_adrc`
- `first_cct`
- `last_cct`
- `first_face_count`
- `last_face_count`

Interpretation rules:

- `video_mode = 1` -> `video`
- `video_mode = 2` -> `slo_mo`
- `video_mode = 3` -> `time_lapse`
- `quality` is the combined resolution + fps field, such as `1080p-30`, `1080p-60`, `4k-30`, `4k-60`
- `if_HLG = 1` means HDR video recorded in HLG format
- `preset = 0` means no preset
- `filter = 0` means no filter
- `tuning_apply = 1` means the tuning feature was applied

## First Frame / Last Frame Rules

Video environment and subject fields are not single values. They may be reported for both recording start and recording end.

Use these rules:

- for start-of-recording environment, use `first_lux`, `first_adrc`, `first_cct`
- for end-of-recording environment, use `last_lux`, `last_adrc`, `last_cct`
- for subject presence at recording start, use `first_face_count`
- for subject presence at recording end, use `last_face_count`
- if the question is about the whole recording, show first and last side by side instead of silently picking one
- if the question is about change during recording, compute delta as `last - first`

Do not merge first and last fields into one average unless the user explicitly asks for that simplification.

## Required Report Blocks

When the user asks for a local video dashboard or short report, the default blocks should include:

1. mode
2. recording duration distribution
3. quality / fps distribution
4. HLG usage
5. filter and tuning usage
6. preset usage
7. face situation, split by front vs rear only when the data truly supports that split

## Default Output Metrics

For each block, prefer:

- event count
- event ratio
- user count
- user ratio when a stable user id exists

## Duration Distribution

Primary field:

- `video_length` in seconds

Recommended default bucket template for local reports:

- `<1s`
- `1-5s`
- `5-10s`
- `10-15s`
- `15-30s`
- `30-60s`
- `60-180s`
- `180s+`

Reason:

- this follows the current dashboard bucket rule provided by the user
- the user later asked to call out `<1s` explicitly, so use it as the first bucket label
- the user-provided list skipped `1-5s`, so keep it explicitly to avoid a gap in the distribution
- if the dashboard rule changes later, follow the newer user rule instead

Example SQL pattern:

```sql
CASE
  WHEN video_length < 1 THEN '<1s'
  WHEN video_length < 5 THEN '1-5s'
  WHEN video_length < 10 THEN '5-10s'
  WHEN video_length < 15 THEN '10-15s'
  WHEN video_length < 30 THEN '15-30s'
  WHEN video_length < 60 THEN '30-60s'
  WHEN video_length < 180 THEN '60-180s'
  ELSE '180s+'
END AS duration_bucket
```

If the user explicitly wants a bucket named `0-1s` instead of `<1s`, replace the first label consistently across the report. Do not keep both labels at the same time.
 
Default recommendation:

- use `<1s` as the first bucket
- do not keep a separate `0-1s` bucket unless the dashboard owner explicitly defines the split

Reference SQL for the non-overlapping default:

```sql
CASE
  WHEN video_length < 1 THEN '<1s'
  WHEN video_length < 5 THEN '1-5s'
  WHEN video_length < 10 THEN '5-10s'
  WHEN video_length < 15 THEN '10-15s'
  WHEN video_length < 30 THEN '15-30s'
  WHEN video_length < 60 THEN '30-60s'
  WHEN video_length < 180 THEN '60-180s'
  ELSE '180s+'
END AS duration_bucket
```

## Mode

Recommended output:

- `video`
- `slo_mo`
- `time_lapse`
- unknown values should be retained and called out instead of dropped

## Quality / FPS

Use `quality` directly as the primary dashboard dimension.

Typical values:

- `1080p-30`
- `1080p-60`
- `4k-30`
- `4k-60`
- `1080p-120`
- `1080p-240`

If needed, split `quality` into:

- resolution
- fps

But keep the combined field in the main table because product teams often discuss it that way.

## HLG

Primary metric:

- share of `if_HLG = 1`

Recommended output:

- HLG event count and ratio
- HLG user count and ratio
- HLG by `video_mode`
- HLG by `quality`

## Filter And Tuning

Filter section:

- filter usage share: `filter <> '0'`
- top filters by events
- average `filter_strength` for filtered videos

Tuning section:

- tuning usage share: `tuning_apply = 1`
- parameter distributions for `tuning_contrast`, `tuning_saturation`, `tuning_warmth`, `tuning_tint`, `tuning_shapen`, `tuning_grain`, `tuning_vignette`

For dashboard output, keep the summary tight:

- filter on/off
- top filter names
- tuning on/off
- optional average absolute parameter offsets when needed

## Preset

Use the same rule as photo and dashboard documents:

- `preset = 0` means not used and must be excluded from top-preset ranking

Recommended outputs:

- preset usage share
- top preset names
- official vs unofficial split only when an official preset whitelist is available

## Face Situation And Front / Rear Split

Face metrics:

- start-frame face presence: `first_face_count > 0`
- end-frame face presence: `last_face_count > 0`
- face count distributions at start and end

Front / rear split rule:

- only produce front vs rear results when the dataset has a stable camera-facing field, `camera_id`, or another explicit lens-facing marker
- do not infer front vs rear from `first_zoom_ratio` or `last_zoom_ratio` alone

If the split is unsupported, the report should say:

- face presence is available
- front vs rear split is not reliably available in the current local video export

## Report Structure

Use this order:

1. business conclusion
2. key findings by the 7 default blocks
3. data scope and parsing notes
4. limitations, especially front / rear support
5. next steps

For a ready-to-reuse section layout and wording pattern, also read [video-report-template.md](video-report-template.md).

## Example Narrative

Use wording like:

- `当前本地视频样本支持模式、时长、规格、HLG、滤镜/调色、Preset 和人脸基础分析。`
- `环境与主体字段为首帧/末帧双上报，因此报告分别展示开始和结束状态，避免混淆。`
- `前后置拆分仅在存在明确 camera_id 或 facing 字段时输出；当前无稳定标识时应如实说明限制。`
