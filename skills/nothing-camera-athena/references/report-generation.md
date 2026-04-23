# 一键生成报告模式

## When To Use

Use this mode when the user wants a report directly from:

- an Athena history URL
- a `queryExecutionId`
- SQL text
- query results
- SQL + workbook reference + a business question

## Goal

Produce a concise, decision-ready business report in one pass. If the SQL is weak or the evidence is insufficient, say so clearly and repair the SQL logic before concluding.

## Accepted Inputs

Any one of the following is enough to start:

1. Athena URL or `queryExecutionId`
2. SQL text plus result rows
3. SQL text only
4. Result table only, if the metric meaning is still obvious from context

If the user already gave an Athena link, do not ask them to paste the SQL again unless retrieval is blocked.

## Workflow

1. Identify the analysis scope.
   - photo / video / settings / performance

2. Validate SQL against:
   - [sql-playbook.md](sql-playbook.md)
   - relevant sheet reference
   - [project-mapping.md](project-mapping.md)

3. Check whether the result table can really answer the question.
   - If yes, interpret directly.
   - If partially, mark the gap and provide a better SQL draft.
   - If not, say “证据不足”.

4. Write the report in the fixed section order below.

## Time Guardrail

- Assume telemetry older than about 6 months may already have been cleaned.
- If a requested date is outside retention, say that the requested period is likely unavailable before discussing SQL details.
- When the user uses relative dates, resolve them against the current date and mention the exact date in the report or SQL note.

## Fixed Output Structure

1. 业务结论
2. 核心指标解读
3. SQL 口径校验
4. 修正建议 SQL
5. 后续分析建议

If no SQL change is needed, section 4 should say `无需修正`.

## Evidence Rules

- Do not over-explain the mechanics unless it affects trust in the conclusion.
- Quantify with ratios whenever possible.
- For defects / anomalies / feature adoption:
  - include both event share and user penetration
- For low-light or brightness claims:
  - explicitly mention that `lux` is an AEC index, not physical lux
- For grouped project rows:
  - call out whether `project_name` alone is enough, or whether `model_code` should also be split

## Tooling Preference

- If the current workspace already has an Athena helper CLI or fetch script, prefer using it to obtain SQL and result metadata before writing the report.
- If no helper exists, work from the user-provided SQL/results and explain any resulting limitation briefly.

## Output Style

- Chinese, concise, professional, flat tone
- Business conclusion first
- Avoid repeating raw metadata unless it changes interpretation
