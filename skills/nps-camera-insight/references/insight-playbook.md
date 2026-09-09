# NPS × Camera insight playbook

## Minimum analysis input

The refid/deviceId mapping alone is insufficient for NPS insight. Retain or obtain the survey export containing at least:

- `refid`;
- NPS score or promoter/passive/detractor label;
- response/completion time;
- campaign or survey identifier;
- optional free-text feedback and device metadata.

Do not treat the NPS system's `Found` status as survey completion.

## Recommended cohorts

Use the product's approved NPS segmentation. If none is supplied, the conventional grouping is:

- detractors: 0–6;
- passives: 7–8;
- promoters: 9–10.

Label this as a conventional assumption and confirm it before publishing a formal report.

## Useful Camera metrics

Choose only metrics supported by the tracking specification and the selected date window:

- active Camera days and Camera event count per device;
- photo versus video usage;
- photo/video mode distribution;
- front/rear camera or lens distribution through `camera_id`;
- filter, preset, watermark, tuning, EV adjustment, motion photo, HDR/HLG, and other tracked features;
- behavior before versus after the survey, when response timestamps are available.

For cohort comparison, report both event volume and device penetration. A few heavy users can dominate event counts.

## Analysis windows

Prefer a relative window around each response time, such as the 7 or 30 days before completion. If only a campaign date is available, state the fixed calendar window explicitly. Stay within Athena retention.

## Data-quality gates

Report these before conclusions:

1. refid lookup success rate;
2. unique device rate and duplicate-device rate;
3. Athena aid match rate;
4. NTCamera-active device rate;
5. sample size per NPS cohort;
6. missing score/response-time rate.

Avoid percentage comparisons for very small cohorts. Show the numerator and denominator, and suppress or qualify results that could expose individual behavior.

## Interpretation rules

- Describe associations, not causation.
- Separate non-use from missing telemetry.
- Compare like-for-like regions, projects, builds, and time windows.
- Do not infer dissatisfaction from a single feature's absence.
- Use free-text feedback to form hypotheses, then check whether aggregate behavior supports them.

## Suggested Friday review output

Keep the review compact:

1. mapping and data coverage;
2. two or three largest behavioral differences between NPS cohorts;
3. relevant user-comment themes;
4. limitations and confidence;
5. one or two follow-up questions or product actions.
