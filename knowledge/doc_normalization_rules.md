# Document Normalization Rules

This note defines the guardrails for assistant-driven document cleanup in this workspace.

## Goal

Turn an existing draft into a cleaner, more reviewable document without changing the author's intended facts.

The default target in the first MVP is a product requirement document written in Markdown or plain text.

## Allowed Changes

- Normalize title format and section numbering.
- Reorder content to match the target template when the mapping is clear.
- Rewrite headings so they are shorter and more consistent.
- Merge duplicated statements that describe the same point.
- Convert vague bullets into explicit placeholders such as `待确认`.
- Standardize terminology when the original meaning is clear.
- Convert mixed Chinese and English punctuation into a consistent style.
- Preserve tables, lists, and links when possible.

## Forbidden Changes

- Do not invent product facts, metrics, dates, owners, or launch scope.
- Do not silently delete requirements, constraints, or known risks.
- Do not turn uncertain statements into confirmed conclusions.
- Do not rewrite business meaning for the sake of tone.
- Do not overwrite source content directly in production flows without a confirmation step.

## Output Modes

Use one of these modes for every run:

1. `diagnose`
   Return only issues, missing sections, and normalization suggestions.
2. `suggest`
   Return a full rewritten draft plus a short change summary.
3. `apply`
   Only for confirmed runs. Return the final draft intended for write-back.

The recommended default for Lark automation is `suggest`.

## PRD Normalization Checklist

- Title follows `【文档类型】产品域 版本 - 功能名` when enough metadata exists.
- The document contains clear sections for background, goal, scope, flow, requirement details, dependencies, metrics, and acceptance.
- Scope in and scope out are explicit.
- Every feature point has support range, behavior, and constraints when applicable.
- Missing key information is marked as `待确认` instead of being guessed.
- Statements that belong to other sections are moved instead of duplicated.
- Marketing phrasing is reduced in favor of product and implementation clarity.

## Safe Write-Back Policy

- Keep the original source snapshot before any write-back.
- Prefer writing the normalized draft into a new document, comment, or approval card first.
- If the user chooses direct overwrite, include the change summary in the write-back result.
- If the parser cannot confidently map a block, keep it under `附录 / 原始内容保留`.

## Suggested Lark App Flow

1. Receive a document link or slash command.
2. Export document content as Markdown or plain text.
3. Detect the document type. Start with `prd` if uncertain.
4. Run the normalizer in `suggest` mode.
5. Send back:
   - issue summary
   - normalized draft
   - apply button or confirmation command
6. Only write back after explicit confirmation.
