# Full Analysis Template

Use this template when the user wants a full camera behavior report rather than one isolated metric.

## Recommended Structure

1. Executive summary
2. Data scope
3. Activity trend
4. Portrait / Lifestyle Portrait
5. Photo and video baseline usage
6. Video capability analysis
7. Feature analysis
8. Performance block
9. Compare block
10. Limitations and next steps

## Executive Summary

Always answer these first when the data supports them:

- What is the dominant shooting mode
- How strong is portrait usage
- How strong is 4k-30 video usage
- Which device is heavier on photo / video usage when comparing base vs pro
- Which features already show meaningful adoption, such as preset, HLG, EV adjustment, watermark, retouching

Prefer short business wording, not SQL wording.

## Data Scope

Always state:

- database path
- date range
- key tables used
- whether the data is local-only or includes cloud comparison
- whether the data is India-only, ROW-only, or mixed

## Activity Trend

When daily dates are present, add:

- daily photo events
- daily photo users
- daily photo APU
- daily video events
- daily video users
- daily video APU

Use this block to describe weekday / weekend rhythm or launch-week ramp.

## Portrait / Lifestyle Portrait

Default mapping:

- `Lifestyle Portraits` -> treat as portrait mode usage
- normalize `portrait` and `protrait` together

Recommended metrics:

- portrait event count
- portrait user penetration
- portrait share by model
- portrait share by front / rear
- portrait + retouching cross
- face count distribution split by front / rear
- beauty penetration
- beauty user APU
- camera × beauty ratio
- front/rear × mode × beauty ratio

## Photo / Video Baseline Usage

Recommended metrics:

- photo events
- photo users
- photo APU
- video events
- video users
- video APU
- lens usage
- mode usage
- `photo_mode='video_shot'` as recording-photo behavior in the photo section

## Video Capability Analysis

Recommended metrics:

- quality distribution
- 4k-30 ratio
- HLG ratio
- duration distribution with buckets:
  - `<1s`
  - `1-5s`
  - `5-10s`
  - `10-15s`
  - `15-30s`
  - `30-60s`
  - `60-180s`
  - `180s+`
- tuning usage
- filter usage

## Feature Analysis

Use the following mapping rules.

- EV adjustment -> `exposure_adjust` and, when available, `exposure_new`
- Watermark -> `watermark`
- Preset -> `preset`
- Retouching / beauty -> `retouching`
- Auto night trigger -> `nightmode` ratio from photo rows
- AI Moon -> `if_moon`
- Fallback -> `macro_fb_ctrl`
- Touch AE/AF -> if missing, state `当前无对应埋点`
- AI Zoom -> if missing, state `当前无对应埋点`
- `ai_zoom` may exist as a newer event, but do not claim support unless it is present in the current dataset

## Performance Block

Only include this block when the current source has `pef_info` or a parsed performance table.

Recommended performance dimensions:

- shutter delay / `capturePrepare`
- mode switch / `switchMode`
- camera switch / `switchCamera`
- app launch performance
- capture to thumbnail / `capture2Thumbnail`

Preferred output style:

- percentile table such as P50 / P90 / P95 / P99
- one short paragraph on key risk
- one short paragraph on recommended action

If the current local DB does not contain performance events, say:

- `当前数据库不包含 pef_info / 性能事件，本轮不输出性能结论`

## Compare Block

Keep local-only findings and cross-series comparison separate.

- Local data can support current-device behavior analysis
- `24111` / `23112` comparison must be backed by cloud SQL when the local DB does not contain those projects

Do not mix the two in one ratio unless both sources are confirmed aligned.

## Output Habits

- Prefer event ratio plus user ratio for adoption topics
- Prefer base vs pro side-by-side when both are present
- Call out missing fields explicitly instead of guessing
- Use short business takeaways after each section
