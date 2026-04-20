# Imaging Product Workspace

This workspace is organized to make product documents easy for both humans and assistants to find, compare, and reuse.

## Structure

- `docs/00_inbox`: New files waiting to be sorted.
- `docs/01_prd`: Product requirement documents.
- `docs/02_design`: Design specs, interaction notes, and visual references.
- `docs/03_tech_spec`: Technical implementation notes and engineering specs.
- `docs/04_release`: Release notes, store copy, rollout plans, and version summaries.
- `docs/05_testing`: Test plans, validation checklists, bug bash notes, and QA reports.
- `docs/06_analytics`: Event specs, dashboards, metrics definitions, and data analysis.
- `docs/07_research`: User research, interview notes, and market findings.
- `docs/08_competitor`: Competitive analysis and benchmark references.
- `docs/09_assets`: Supporting assets such as screenshots, exports, mockups, and attachments.
- `docs/10_archive`: Older or deprecated materials kept for reference.
- `knowledge`: Stable reference notes that summarize repeated product knowledge.
- `templates`: Reusable document templates.
- `outputs`: Assistant-generated drafts, summaries, and derived materials.
- `scripts`: Small utilities for import, conversion, or cleanup.

Each `docs/*` folder is split into:

- `gallery`
- `camera`
- `video`
- `system`
- `shared`

## Suggested Workflow

1. Put newly downloaded files into `docs/00_inbox/<module>`.
2. Move confirmed documents into the right category folder.
3. Keep original source files when layout matters, such as `.pdf`, `.docx`, or `.xlsx`.
4. Add assistant-friendly summaries or extracted notes into `knowledge/` or `outputs/`.

## Naming Rules

Use consistent file names so documents are easy to search:

`<type>_<module>_<topic>_v<version>_<yyyy-mm-dd>.<ext>`

Examples:

- `PRD_gallery_draw_v1.1_2026-03-12.docx`
- `release_gallery_v2.8_2026-04-15.md`
- `analytics_camera_event_map_v2_2026-04-01.xlsx`
- `design_gallery_draw_markup_2026-03-20.pdf`

If a source file already has an official name, you can keep it and add a cleaned summary in `outputs/`.

## Assistant Tips

- Put raw source documents in `docs/`.
- Put cross-document summaries in `knowledge/`.
- Put generated copy, release notes, review comments, and comparison results in `outputs/`.
- When asking for help, mention the exact file path or the folder scope to search.

## Lark Document Automation

This workspace now includes a first-pass document normalization path for Lark or Feishu docs:

- Rules live in `knowledge/doc_normalization_rules.md`
- Target PRD structure lives in `templates/prd_normalization_template.md`
- The Codex skill lives in `outputs/skills/lark-doc-normalizer/`
- The backend bridge stub lives in `scripts/lark_doc_normalize_stub.py`

Recommended flow:

1. Export the Lark document as Markdown or plain text
2. Build a normalization payload with `scripts/lark_doc_normalize_stub.py`
3. Let your external app or service send that payload to a model
4. Return a suggested draft first, then write back after confirmation

This workspace also now supports a curated OpenClaw skill pack for imaging work:

- Sync the project skill pack with `scripts/configure_openclaw_image_product_skills.py`
- Create a fresh Lark PRD doc from template with `scripts/create_lark_doc_from_template.py`
- Use the direct template-writing skill in `outputs/skills/lark-template-doc-writer/`

This keeps the Lark bot focused on image-product work instead of loading unrelated personal skills.

## Send Local HTML Report

This workspace includes a local email helper for dashboard-style HTML reports:

```bash
python3 scripts/send_html_report_email.py \
  --html-file outputs/india_camera_dashboard_2026-04-16.html \
  --subject "India Camera Dashboard 2026-04-16" \
  --to travis.zhao@nothing.tech
```

The script will inline local image assets referenced by the HTML before sending.

For the most stable delivery in email clients, you can send a plain-text summary plus a cleaned HTML attachment:

```bash
python3 scripts/send_html_report_email.py \
  --html-file outputs/india_camera_dashboard_2026-04-16.html \
  --subject "India Camera Dashboard 2026-04-16" \
  --summary "正文仅保留文字简报，完整看板请见 HTML 附件。" \
  --export-html-attachment \
  --to travis.zhao@nothing.tech
```

## GitHub Sync

This workspace can be synced through GitHub for cross-machine skill reuse.

- Portable assets live mainly under `outputs/skills/`
- Supporting scripts live under `scripts/`
- Machine-local secrets such as `~/.openclaw/openclaw.json` must stay out of Git

See `GITHUB_SYNC.md` for the recommended publish and pull flow.

## Shared Server Query

This workspace also includes a minimal shared-query path for analytics SQLite databases:

1. Upload the database to a server
2. Run `scripts/server_sqlite_query_service.py` on that server
3. Use `scripts/server_sqlite_query_client.py` locally
4. Let teammates load the `outputs/skills/server-camera-analytics/` skill in Codex

See:

- `knowledge/server_sqlite_query_workflow.md`
- `scripts/server_sqlite_query_service.py`
- `scripts/server_sqlite_query_client.py`
