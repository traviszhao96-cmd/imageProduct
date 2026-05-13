# Analysis Playbook

## Core Local Metrics

When the local table is `photo_events_raw`, common metrics include:

- sample range: `MIN(event_date)`, `MAX(event_date)`
- capture count: `COUNT(*)`
- shooting users: `COUNT(DISTINCT user_pseudo_id)`
- mode share: `photo_mode`
- lens share: `camera_id`
- environment distribution: `lux`, `adrc`, `cct`, `exp_time_ns`
- subject and posture: `face_count`, `orientation`
- feature usage: `nightmode`, `preset`, `retouching`, `watermark`, `exposure_adjust`

## Camera Name Mapping

Use this mapping when the user asks for camera-level analysis by name:

| camera_id | camera_name | aliases |
| --- | --- | --- |
| `0` | 主摄 / 后置广角 / Wide | 主摄, 广角, rear wide, main camera, wide |
| `1` | 前置 / Front | 前置, 自拍, front, selfie |
| `2` | 超广 / 后置超广 / UW | 超广, ultra wide, uw |
| `3` | 长焦 / 后置长焦 / Tele | 长焦, tele, telephoto |
| `4` | 未明确 | do not guess; call out mapping gap |

Preferred SQL pattern:

```sql
CASE camera_id
  WHEN 0 THEN '主摄(Wide)'
  WHEN 1 THEN '前置(Front)'
  WHEN 2 THEN '超广(UW)'
  WHEN 3 THEN '长焦(Tele)'
  ELSE '未知'
END AS camera_name
```

If the user writes camera names instead of IDs, map them to the corresponding `camera_id` in filters.

## Output Habits

For preference or adoption topics, output both:

- event ratio
- user ratio

For example:

```sql
SELECT
  photo_mode,
  COUNT(*) AS events,
  COUNT(DISTINCT user_pseudo_id) AS users,
  ROUND(COUNT(*) * 1.0 / (SELECT COUNT(*) FROM photo_events_raw), 4) AS event_ratio,
  ROUND(COUNT(DISTINCT user_pseudo_id) * 1.0 / (SELECT COUNT(DISTINCT user_pseudo_id) FROM photo_events_raw), 4) AS user_ratio
FROM photo_events_raw
GROUP BY photo_mode
ORDER BY events DESC;
```

## Common Caveats

- `lux` is not physical lux; describe it as an internal AEC brightness index.
- `photo_mode='protrait'` should often be standardized to `portrait`.
- `preset='0'` means no preset.
- If the dataset only contains photo rows, do not over-claim video, DAU, or performance conclusions.

## Dashboard Readiness

Usually directly supportable from local photo exports:

- mode penetration
- lens preference
- night mode distribution
- preset usage
- subject / posture distribution
- beauty feature usage
- environment distribution

Usually not fully supportable unless extra exports are present:

- phone DAU and APU denominator from OS activity
- performance / latency
- third-party camera usage
- settings behavior from `general`

## Extra Dimensions Often Worth Adding

When the report is intended for management review, check whether these dimensions can be added:

- daily active trend
- beauty penetration
- beauty user APU
- camera distribution + beauty ratio
- front / rear × mode cross
- performance percentile block when `pef_info` exists

Video behavior is supportable when local data contains `video_info`. In that case, route to [video-analysis-playbook.md](video-analysis-playbook.md) and do not answer with photo-only logic.

## Field Clarifications

Use these clarified mappings when the user has already defined them:

- `Lifestyle Portraits` -> treat as portrait mode usage
- `Touch AE/AF` -> if no field is present, state `当前无对应埋点`
- `Fallback` -> `macro_fb_ctrl`
- `AI Zoom` -> if no field is present in the current dataset, state `当前无对应埋点`
- `AI Moon` -> `if_moon`
- 自动夜景触发 -> `nightmode` ratio from photo rows
- 视频录制拍照 -> analyze in the photo section as `photo_mode='video_shot'`

## Report Structure

Use this order when writing a short report:

1. business conclusion
2. key metrics
3. data scope / limitations
4. recommended next steps

For mixed photo + video dashboard requests:

1. summarize photo section
2. summarize video section
3. clearly split unsupported blocks
4. call out which source tables backed each section
