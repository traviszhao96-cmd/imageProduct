---
name: gallery-feature-doc
description: Draft and review Chinese product documents for Gallery software features such as Draw, Text, Markup, annotation, editing tools, export flows, and UI interaction improvements. Use when Codex needs to turn scattered Gallery feature notes into a structured PRD-style document, identify missing product inputs without inventing behavior, and add development and testing review for software-focused features that do not depend on specific hardware details.
---

# Gallery Feature Doc

## Purpose

Use this skill to write or review Gallery feature documents for software-centric capabilities.
This skill is for features like `Text`, `Draw`, `Markup`, `Mosaic`, `Sticker`, `Crop`, `Export`, `Revert`, and similar editing or browsing functions inside Gallery.

Do not treat these requests like camera hardware or image quality planning unless the user explicitly introduces hardware dependencies.

## Suitable Requests

Use this skill when the user wants:

- a new Gallery feature PRD in Chinese
- an existing Gallery draft normalized into a clearer structure
- a document patterned after features like `Draw`
- an initial development or test review for a Gallery software feature
- help collecting missing information before writing the final document

## Core Principle

Stay faithful to the feature definition.
Do not invent gestures, menus, persistence rules, or edge-case behavior that the user has not provided.

If the user gives only a rough idea, produce a clear draft with explicit `待确认` markers rather than pretending the details are final.

## Workflow

Follow this sequence unless the user explicitly asks for only one part.

1. Classify the request.
2. Check whether key product inputs are complete.
3. If key details are missing, ask targeted follow-up questions or mark missing fields clearly.
4. Draft the document in the standard Gallery PRD structure.
5. Add an initial development review.
6. Add an initial testing review.
7. Separate confirmed facts, assumptions, and pending decisions.

## Request Modes

Map the request into one of these modes:

- Full drafting: write a full feature document
- Refinement: rewrite or normalize an existing draft
- Review only: inspect an existing document for product, development, and testing gaps
- Gap collection: organize scattered notes and identify what is still missing

If the request spans multiple modes, use this order: gap collection, drafting, review.

## Input Completeness Check

Before drafting, inspect whether the request includes enough information for the feature to be implemented and tested with confidence.

Load [references/required-info-checklist.md](references/required-info-checklist.md) when you need the checklist.

Treat these as the minimum fields for a solid Gallery software PRD:

- feature name and intent
- target user scenario
- entry point and trigger path
- main interaction flow
- toolbar, panel, or page-level UI changes
- editable properties and constraints
- save, cancel, undo, redo, or exit behavior
- scope boundary and unsupported cases
- compatibility or layout requirements
- observability or event tracking needs

If the document would otherwise imply certainty but these are missing, stop and ask for clarification first.

## Allowed vs Not Allowed

Allowed:

- infer a cleaner section title from the feature name
- reorganize user bullets into a more professional PRD structure
- preserve placeholders such as `待确认` or `待补充`
- generalize obvious software concerns such as `Undo/Redo`, `Save/Cancel`, or empty-state handling when the user already implies an editing flow

Not allowed:

- fabricate exact toolbar icons, gestures, timing rules, or animations
- invent technical architecture, owner names, schedule commitments, or KPI values
- claim non-destructive editing, sync behavior, or export rules unless the user provides them
- present assumptions as final requirements

## Output Format

When the inputs are sufficient, use the structure in [assets/gallery-feature-template.md](assets/gallery-feature-template.md).

Output rules:

- Write in concise Chinese unless the user asks otherwise.
- Keep the tone professional and product-facing.
- Prefer explicit headings over long prose.
- Keep feature behavior, boundary conditions, and pending items easy to scan.
- Use product terms consistently throughout the document.
- If the user already has a mandatory template, preserve it first and apply this skill's writing rules second.

## Writing Standards

- Write from background to goal to scope to interaction to non-functional requirements.
- Prefer direct statements over marketing language.
- Keep user value and interaction details concrete.
- Separate `已确认信息` and `待确认信息` when details are incomplete.
- Avoid repeating the same claim across sections.
- For software features, describe UI states and interaction transitions clearly.

## Development Review

After drafting, add a development review unless the user asks to skip it.

Load [references/review-rubric.md](references/review-rubric.md) when needed.

The development review should check:

- whether the entry path and state transitions are clear
- whether the editing model is complete enough to implement
- whether save and recovery behavior is defined
- whether unsupported cases and limits are explicit
- whether analytics and observability need to be added
- whether there are interaction ambiguities that will create implementation churn

## Testing Review

Also add a testing review unless the user asks to skip it.

The testing review should check:

- whether acceptance criteria are testable
- whether normal flows and abnormal flows are both covered
- whether different image sizes, ratios, and layouts need validation
- whether undo, redo, cancel, and save paths are defined
- whether boundary cases such as empty input, max count, or unsupported actions are covered

## Review Output

Use this structure:

- `开发评审`
- `测试评审`
- `高风险项`
- `待补充信息`

Each item should be actionable and specific.

## Handling Existing Drafts

If the user provides an existing draft:

1. Preserve confirmed facts.
2. Normalize wording and structure.
3. Mark unsupported or contradictory claims.
4. Identify missing product decisions.
5. Append development and testing review.

## References

Read these only when needed:

- [references/required-info-checklist.md](references/required-info-checklist.md): input checklist and follow-up prompts
- [references/review-rubric.md](references/review-rubric.md): development and testing review checklist
- [assets/gallery-feature-template.md](assets/gallery-feature-template.md): default PRD structure for Gallery software features
