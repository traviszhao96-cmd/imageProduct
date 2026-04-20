---
name: lark-template-doc-writer
description: Use when the user wants to create a new Lark or Feishu document from an imageProduct template, especially PRDs, planning docs, release notes, or structured drafts that should be generated directly into a managed docx file.
---

# Lark Template Doc Writer

Use this skill when the user asks to create a fresh Lark document from a project template instead of editing an existing draft.

## Supported Templates

- Default PRD template:
  `Camera-PRD-Template.md`
- PRD normalization target:
  `templates/prd_normalization_template.md`

## Primary Action

Create the document with:

```bash
python3 scripts/create_lark_doc_from_template.py \
  --title "【PRD】Camera 1.0 - 功能名"
```

If the user gives replacement values, pass them with repeated `--replace` flags:

```bash
python3 scripts/create_lark_doc_from_template.py \
  --title "【PRD】Camera 1.0 - Action Mode" \
  --replace PRODUCT_NAME="Camera" \
  --replace FEATURE_NAME="Action Mode"
```

## Workflow

1. Confirm the target document type from the request.
2. Pick the template.
3. If key product facts are missing, leave placeholders in the generated document rather than inventing them.
4. Create a new managed docx instead of overwriting an existing document by default.
5. Return:
   - the new doc link
   - what template was used
   - which fields still need manual completion

## Safety Rules

- Prefer creating a new doc over modifying an existing knowledge-base page.
- Do not claim unsupported fields are already confirmed.
- If the user asks for a direct rewrite of an existing document, use `lark-doc-normalizer` instead.
- Keep template placeholders when the request does not provide enough facts.
