---
name: lark-doc-normalizer
description: Use when the user wants to normalize or rewrite Lark or Feishu product documents into a consistent internal format, especially PRDs, review docs, release notes, and other Markdown-like drafts that should follow workspace templates and safe write-back rules.
---

# Lark Doc Normalizer

Use this skill when the task is to clean up document structure, unify section naming, or prepare a safer draft before writing content back to Lark.

## Quick Start

1. Start in `suggest` mode unless the user explicitly asks for direct overwrite.
2. Read the normalization rules:
   `/Users/travis.zhao/imageProduct/knowledge/doc_normalization_rules.md`
3. For PRDs, use:
   `/Users/travis.zhao/imageProduct/templates/prd_normalization_template.md`
4. If the task is wiring an app or service, use:
   `python3 /Users/travis.zhao/imageProduct/scripts/lark_doc_normalize_stub.py --help`

## Workflow

1. Identify the document type.
   - Default to `prd` when the content is clearly a product requirement draft.
   - If uncertain, say that the type is inferred.
2. Separate three kinds of content:
   - confirmed facts
   - unclear or missing facts
   - formatting or structure issues
3. Normalize only the structure and expression that can be changed safely.
4. Mark unknown required fields as `待确认`.
5. Return:
   - issue summary
   - normalized draft
   - short change summary
6. Recommend confirmation before write-back to Lark.

## Safety Rules

- Never invent launch plans, owners, metrics, or implementation details.
- Never silently drop information that may affect scope, dependency, or acceptance.
- If a paragraph does not map cleanly, keep it in `附录 / 原始内容保留`.
- Prefer preserving meaning over making the document look polished.

## Output Contract for App Integration

When working with a Lark app or backend service, structure the response in three blocks:

1. `issues`
2. `normalized_markdown`
3. `change_summary`

If the app supports confirmations, keep `apply` as a second step.

## Notes for Cam Pulse Integration

- Let the Lark app own authentication, webhook verification, and document read/write APIs.
- Let this skill own normalization policy and target structure.
- Keep the bridge thin: exported text in, normalized text out.
