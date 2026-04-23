---
name: gallery-event-tracking
description: Design and review Gallery analytics event tracking for product documents and feature specs. Use when Codex needs to add埋点内容 for Gallery features, align event names and parameter structures with the existing NTGallery event tracking workbook, avoid inventing inconsistent naming, and propose save-time settlement events for edit features such as Text, Draw, Crop, Erase, or other Gallery modules.
---

# Gallery Event Tracking

## Purpose

Use this skill when the user wants埋点内容 for Gallery features.
This skill aligns new tracking proposals with the existing `NTGallery App Event Tracking Spec 2026` workbook rather than inventing a new style from scratch.

## Default Source

Prefer the extracted reference note:

- [references/ntgallery-event-patterns.md](references/ntgallery-event-patterns.md)

If the user provides a newer workbook or a different source of truth, use that first.

## Existing Pattern

The current Gallery workbook uses:

- `event_name`
- `event_description`
- `parameter_name`
- `parameter_value`
- `value_note`

For Edit features, the pattern is usually:

1. `edit_action`
   For entering the一级模块 or clicking specific sub-tools.
2. `edit_<feature>`
   For save-time settlement of final effective parameters.
3. `UUID`
   For session correlation.

## Workflow

1. Identify the feature and whether it belongs to `Manage`, `Edit`, or `Settings`.
2. Check whether the new feature should reuse an existing event family.
3. For editing features, default to:
   - one `edit_action` row for module entry
   - one `edit_<feature>` event family for save-time settlement
4. Only add process events if the business need is explicit.
5. Output in the workbook-style table format.
6. Mark unsupported or undecided enums as `待确认`.

## Rules

- Keep event names short and consistent with the workbook.
- Prefer enum-style parameter values over free text.
- Reuse `UUID` when the feature belongs to an edit session.
- Do not mix entry events and final settlement events into the same semantic bucket.
- Do not create overly granular events for every gesture unless explicitly required.
- If the exact enum set is unknown, keep the event row and mark the values as `待确认`.

## Output Format

Default to this table:

| event_name | event_description | parameter_name | parameter_value | value_note |
| --- | --- | --- | --- | --- |

If the user asks for PRD-ready text, you may additionally provide a short explanation below the table.

## Review Focus

When reviewing埋点内容, check:

- whether names follow existing Gallery conventions
- whether parameters are enum-friendly
- whether save-time and process-time events are separated
- whether there are too many low-value events
- whether key funnel stages are missing

## References

- [references/ntgallery-event-patterns.md](references/ntgallery-event-patterns.md): extracted structure and naming patterns from the existing workbook
