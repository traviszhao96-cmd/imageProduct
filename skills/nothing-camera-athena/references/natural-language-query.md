# 自然语言查数模式

## When To Use

Use this mode when the user asks a camera analytics question in natural language, for example:

- “查 4a Pro 最近 7 天夜景触发率”
- “看一下 CMF Phone 3 的录像 4k-30 渗透率”
- “想分析 macro fallback 在海外大盘的用户风险”

## Goal

Translate the business question into Athena / Presto SQL that matches the workbook semantics and the team's reporting rules.

## Minimal Parsing Checklist

Before writing SQL, extract these elements from the user's request:

1. Analysis object
   - settings behavior / photo / video / performance
2. Core metric
   - feature penetration / trigger rate / latency / mode mix / defect rate
3. Population scope
   - model / region / date range / app mode / scene
4. Granularity
   - overall / by day / by model / by country / by version

If a critical field is missing:

- For date range: do not silently invent one. Either ask once, or leave a clear SQL placeholder comment if the user mainly wants query logic.
- For model mapping: infer from [project-mapping.md](project-mapping.md) when possible.
- For region: if the request implies overseas / 出海, apply the exclusion rule automatically.

## Time Guardrail

- Telemetry is retained for only about 6 months.
- Do not produce SQL for dates older than roughly 6 months from the current date.
- If the user gives an out-of-retention date, say so explicitly and convert the request to the nearest in-retention interpretation only when that intent is obvious.
- If the user gives an ambiguous partial date such as “3月21日”, resolve it to the current-year date first; if that would fall outside retention, call out the conflict instead of querying an older year by default.

## Query Construction Rules

1. Pick the correct payload key:
   - `General` -> usually settings-style fields or app enter behavior
   - `Photo` -> `photo_info`
   - `Video` -> `video_info`
   - `性能` -> `pef_info`

2. Use workbook labels, not guessed field names.

3. Keep SQL modular with CTEs:
   - base / exploded
   - parsed
   - denominator
   - numerator
   - final select

4. If the request is feature penetration, defect trigger, or anomaly rate:
   - always output both event share and user penetration

5. If the request touches low-light / brightness:
   - first derive distribution stats for `lux`
   - then use percentile-based thresholds

## Output Contract

Default response structure:

1. One short sentence restating the business question.
2. Assumptions or missing-info notes, if any.
3. A single Athena SQL block with short Chinese comments.
4. A short note explaining what the result table will mean.

## Good Defaults

- Prefer `project_name` as the model dimension and map it to marketing names in the output note.
- Keep aliases readable: `base`, `parsed`, `agg`, `final`.
- Use `NULLIF` in denominators to avoid division-by-zero.

## Example Intent Mapping

- “4a Pro” -> usually `project_name = 'FroggerPro'`, optionally `model_code = 'A069P'`
- “2a Plus” -> usually `project_name = 'PacmanPro'`
- “录像性能” -> likely `pef_info` or `video_info`, depending on whether the user wants latency or content settings
