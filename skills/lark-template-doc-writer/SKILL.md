---
name: lark-template-doc-writer
description: Use when the user wants to create a new Lark or Feishu document from an imageProduct template, especially PRDs, planning docs, release notes, or structured drafts that should be generated directly into a managed docx file.
---

# Lark Template Doc Writer

Use this skill when the user asks to create a fresh Lark document from a project template instead of editing an existing draft.

## Supported Templates

- Default PRD template:
  `/Users/travis.zhao/imageProduct/Camera-PRD-Template.md`
- PRD normalization target:
  `/Users/travis.zhao/imageProduct/templates/prd_normalization_template.md`

## Primary Action

Create the document with:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/create_lark_doc_from_template.py \
  --title "【PRD】Camera 1.0 - 功能名"
```

If the user gives replacement values, pass them with repeated `--replace` flags:

```bash
python3 /Users/travis.zhao/imageProduct/scripts/create_lark_doc_from_template.py \
  --title "【PRD】Camera 1.0 - Action Mode" \
  --replace PRODUCT_NAME="Camera" \
  --replace FEATURE_NAME="Action Mode"
```

## Workflow

1. Confirm the target document type from the request.
2. Pick the template.
3. If the request is based on an existing Lark or Feishu document, create a copy-like working draft first instead of starting from plain text only.
   - Preserve the original document.
   - Prefer a true duplicate or the closest available copy flow so images, tables, multi-column layout, and other rich blocks remain available in the working draft.
   - Only fall back to a fresh managed docx when a duplicate flow is unavailable or the user explicitly wants a clean rebuild.
4. If key product facts are missing, leave placeholders in the generated document rather than inventing them.
5. When rebuilding content into a fresh doc, call out that rich media and layout may not carry over automatically.
6. When the source PRD already provides concrete compatibility rules, project scope, review info, or telemetry conventions from linked companion docs, carry those confirmed items into the draft instead of leaving them as generic risk bullets.
7. For 埋点 sections, prefer the existing camera telemetry workbook conventions.
   - Settings toggles under Camera settings should default to the `General` sheet style.
   - Reuse the existing `NTCamera + key + enum value + trigger timing` pattern instead of inventing a new event family.
   - If the feature is a simple settings switch, draft at least on/off enum rows and mark only unknown keys or trigger details as `待确认`.
8. Return:
   - the new doc link
   - what template was used
   - whether the result is a duplicated working draft or a clean rebuilt draft
   - which fields still need manual completion

## Safety Rules

- Prefer creating a new doc over modifying an existing knowledge-base page.
- Do not claim unsupported fields are already confirmed.
- If the user asks for a direct rewrite of an existing document, use `lark-doc-normalizer` instead.
- Keep template placeholders when the request does not provide enough facts.
