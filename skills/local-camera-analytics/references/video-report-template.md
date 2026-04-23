# Video Report Template

## When To Use

Use this template when the user asks for a local video dashboard summary, a short report, or a natural-language recap based on `video_info`.

## Default Structure

1. sample scope
2. business conclusion
3. mode
4. recording duration distribution
5. quality and fps
6. HLG usage
7. filter and tuning
8. preset
9. face situation
10. data limitations
11. next steps

## Suggested Section Wording

### 1. Sample Scope

- date range
- country
- model coverage
- total video count
- total video users

Example:

`本次分析基于本地 2026-04-01 至 2026-04-07 的 India 视频成片数据，共覆盖 2 个机型、X 条视频记录、Y 个录制用户。`

### 2. Business Conclusion

Write 2-4 lines that summarize:

- dominant video mode
- whether long videos are common or short clips dominate
- whether high-spec recording is niche or mainstream
- whether HLG / filter / preset are early-stage or mature

### 3. Mode

Report:

- event count by mode
- event ratio by mode
- user count by mode
- user ratio by mode

### 4. Recording Duration Distribution

Use the current bucket rule:

- `<1s`
- `1-5s`
- `5-10s`
- `10-15s`
- `15-30s`
- `30-60s`
- `60-180s`
- `180s+`

Report:

- top duration buckets
- median or average video length
- whether the product is dominated by short capture or longer creation

### 5. Quality And FPS

Report:

- `quality` distribution
- highlight high-spec combinations such as `4k-30`, `4k-60`, `1080p-60`
- optionally separate by mode if the user asks for deeper detail

### 6. HLG Usage

Report:

- HLG event count and ratio
- HLG user count and ratio
- HLG by `quality` if useful

### 7. Filter And Tuning

Report:

- filtered video share: `filter_name <> '0'`
- top filter names
- tuning-on share: `tuning_apply = 1`
- if tuning is rare, say so directly instead of overexplaining

### 8. Preset

Rule:

- `preset = '0'` means no preset and should be excluded from top preset rankings

Report:

- preset usage share
- top preset names
- official vs unofficial only when an official preset whitelist is available

### 9. Face Situation

Report:

- start-frame face presence share
- end-frame face presence share
- if the data lacks explicit front / rear camera markers, state that front / rear split is not reliably available

### 10. Data Limitations

Call out:

- first-frame / last-frame fields are separate
- front / rear split requires a stable camera-facing marker
- local export may not support app-level DAU denominator

### 11. Next Steps

Examples:

- parse video rows into `video_events_parsed`
- add camera-facing field when available
- combine with performance or general events for deeper dashboard coverage
