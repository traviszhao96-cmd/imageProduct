---
name: mobile-imaging-planning-doc
description: Generate and review Chinese planning documents for mobile imaging products such as camera features, image quality directions, computational photography capabilities, tuning projects, and release plans. Use when Codex needs to draft a structured product planning document, normalize fragmented notes into a formal PRD-style output, identify missing dependency information without inventing facts, ask the user to补齐关键输入, or perform an initial requirement review from development and testing perspectives.
---

# Mobile Imaging Planning Doc

## Overview

Produce a structured Chinese planning document for mobile imaging work and keep the writing concise, professional, and logically ordered.
Stop fabrication of dependency details by checking input completeness first, then request missing information before drafting the final document.

## Workflow

Follow this sequence unless the user explicitly requests only one part.

1. Classify the request.
2. Check whether required inputs are complete.
3. If key dependencies are missing, stop drafting and ask targeted follow-up questions.
4. If information is sufficient, generate the document in the standard format.
5. Run an initial review from development and testing perspectives.
6. Clearly separate confirmed facts, assumptions, and open issues.

## Request Classification

Map the user's request into one of these modes before writing:

- Full drafting: The user wants a complete planning document.
- Refinement: The user already has a draft and wants it normalized, expanded, or tightened.
- Review only: The user wants a development or test review of an existing document.
- Gap collection: The user provides scattered inputs and needs help identifying what is still missing.

If the request spans multiple modes, do them in this order: gap collection, drafting, review.

## Input Completeness Check

Before drafting, inspect whether the request includes enough information for claims that would affect product scope, development effort, or test strategy.

Load [references/required-info-checklist.md](references/required-info-checklist.md) when you need the detailed checklist.

Treat the following as critical dependencies. Do not invent them:

- Product context: product line, target market, target release window, applicable region, project stage.
- User value: target scenario, target users, expected experience improvement, benchmark or pain point.
- Functional scope: feature boundaries, in-scope behavior, out-of-scope behavior, configurable items.
- Technical dependencies: algorithm capability, hardware or sensor dependency, ISP or SoC dependency, platform version, cross-team support.
- Quality targets: image quality goal, performance target, power or thermal budget, storage cost, compatibility boundary.
- Delivery dependencies: milestone, owner, external dependency, certification or legal constraint, fallback plan.

If any critical dependency is missing and the document would otherwise imply certainty, stop and ask for clarification first.

## Clarification Rules

When information is incomplete, ask only focused questions that unblock the next draft. Prefer grouped prompts over broad brainstorming.

Use this response pattern:

1. State that key information is missing and the current document cannot be finalized reliably.
2. List the missing fields grouped by theme.
3. For each missing field, explain why it matters in one short clause.
4. Ask the user to supplement only the missing parts.

Keep the tone firm and collaborative. Do not silently fill gaps with plausible guesses.

Allowed:

- Infer a section title from the request.
- Reorganize fragmented notes into a cleaner structure.
- Mark an item as `待补充` when the user explicitly wants a placeholder draft.

Not allowed:

- Fabricate hardware support, schedule commitments, KPI values, owner names, test conclusions, or algorithm status.
- Present assumptions as confirmed facts.
- Hide unresolved external dependencies inside polished prose.

## Output Format

When the inputs are sufficient, follow the structure in [assets/mobile-imaging-planning-template.md](assets/mobile-imaging-planning-template.md).

Output rules:

- Use Chinese throughout unless the user asks otherwise.
- Keep sentences short, direct, and professional.
- Prefer declarative statements over marketing language.
- Use explicit section headings.
- Keep each section focused on one topic.
- Separate `已确认信息` from `待确认/待补充信息` when needed.
- If the user provides a different mandatory template, preserve their template first and apply this skill's style constraints second.

## Review Pass

After drafting, always add an initial review section unless the user asks to skip it.

Load [references/review-rubric.md](references/review-rubric.md) when reviewing.

The review must include:

- Development review: feasibility, dependency clarity, scope boundary, implementation risk, observability needs, rollback or downgrade considerations.
- Test review: acceptance criteria clarity, testability, environment dependency, compatibility coverage, abnormal flow coverage, objective pass/fail signals.

Review output format:

- `开发评审`
- `测试评审`
- `高风险项`
- `需要补充的信息`

Each point should be actionable. Prefer statements such as `需明确夜景模式与高像素模式是否互斥，否则实现链路和测试矩阵无法收敛`.

## Lark Publishing

If the user wants the result written back to a Lark or Feishu document, treat publishing as a separate output step after drafting and review.

Load [references/lark-doc-publish.md](references/lark-doc-publish.md) when this is requested.

Apply these rules:

- Do not assume the target document is editable until the document link or token, app credentials, and permission scope are confirmed.
- Prefer updating a managed section rather than replacing the whole document.
- Keep a stable section marker so later runs can update the same content safely.
- If the target is a Lark doc rather than a Bitable table, generate section-structured content first, then map it into document blocks.
- If the user only wants a draft for manual paste, skip API publishing and return the formatted body directly.

## Writing Standards

Apply these writing constraints to every output:

- Use concise Chinese with minimal filler.
- Keep terminology consistent across the whole document.
- Write from goal to scope to dependency to plan.
- Prefer concrete nouns and verbs over abstract summaries.
- Avoid duplicated claims across sections.
- If trade-offs exist, state them explicitly.

## Handling Existing Drafts

If the user provides an existing document:

1. Preserve confirmed facts.
2. Normalize structure and wording.
3. Mark contradictions or unsupported claims.
4. Add missing dependency prompts.
5. Append the review section without rewriting facts that are already confirmed.

## References

Read these files only when needed:

- [references/required-info-checklist.md](references/required-info-checklist.md): required input checklist and question prompts
- [references/review-rubric.md](references/review-rubric.md): development and test review checklist
- [references/lark-doc-publish.md](references/lark-doc-publish.md): Lark document publishing workflow and prerequisites
- [assets/mobile-imaging-planning-template.md](assets/mobile-imaging-planning-template.md): standard output template
