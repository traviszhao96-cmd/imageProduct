# Scripts

Use this folder for small helpers, for example:

- Convert `.docx` to `.md`
- Extract text from `.pdf`
- Rename files to match workspace rules
- Build document indexes
- Prepare Lark document normalization payloads for an external app backend
- Sync an OpenClaw-only imageProduct skill pack
- Create a Lark doc directly from a local Markdown template
- Send local HTML reports by email with inline images
- Serve a shared SQLite database over a read-only HTTP API
- Query that shared database from a local machine

## OpenClaw imageProduct skill pack

Use `configure_openclaw_image_product_skills.py` to build a curated OpenClaw skill pack
for this project and update `~/.openclaw/openclaw.json` so the Lark bot loads only
image-product-related skills.

Example:

```bash
python3 scripts/configure_openclaw_image_product_skills.py
```

The script copies the selected imaging skills into `~/.openclaw/skills-image-product`
and sets that directory as the active `skills.load.extraDirs` source.

## Lark doc from template

Use `create_lark_doc_from_template.py` to create a managed Lark docx from a local
Markdown template and grant yourself `full_access`.

Example:

```bash
python3 scripts/create_lark_doc_from_template.py \
  --title "【PRD】Camera 1.0 - Action Mode"
```

Optional replacements:

```bash
python3 scripts/create_lark_doc_from_template.py \
  --title "【PRD】Camera 1.0 - Action Mode" \
  --replace FEATURE_NAME="Action Mode" \
  --replace VERSION="1.0"
```

## Lark document normalization

Use `lark_doc_normalize_stub.py` to package a Lark-exported document, the workspace rules,
and the target template into one JSON payload for your external app service.

Example:

```bash
python3 scripts/lark_doc_normalize_stub.py \
  --input-file docs/01_prd/camera/PRD_camera_action_mode_v4.1.md \
  --mode suggest \
  --doc-type prd \
  --source-title "Camera Action Mode PRD" \
  --source-url "https://example.feishu.cn/docx/xxx" \
  --output-file outputs/lark_doc_normalize_payload.json
```

Your Lark app backend can then:

1. Read the exported doc content
2. Call this script
3. Send the resulting JSON to a model endpoint
4. Post the issues and normalized draft back to Lark for confirmation

## HTML report email

Use `send_html_report_email.py` to send a local HTML dashboard as an email body.

Example:

```bash
python3 scripts/send_html_report_email.py \
  --html-file outputs/india_camera_dashboard_2026-04-16.html \
  --subject "India Camera Dashboard 2026-04-16" \
  --to travis.zhao@nothing.tech
```

Send a more email-safe version with summary plus cleaned HTML attachment:

```bash
python3 scripts/send_html_report_email.py \
  --html-file outputs/india_camera_dashboard_2026-04-16.html \
  --subject "India Camera Dashboard 2026-04-16" \
  --summary "正文仅保留文字简报，完整看板请见 HTML 附件。" \
  --export-html-attachment \
  --to travis.zhao@nothing.tech
```

Notes:

- Local `<img src="./...">` assets will be converted into inline email images automatically.
- SMTP defaults are loaded from environment variables when available.
- If this workspace does not define SMTP vars, the script also falls back to `/Users/travis.zhao/nt_cam_pulse/.env`.
- `--export-pdf` uses local Chrome headless to render the current HTML into a PDF first, then attaches it to the email.
- `--export-html-attachment` creates a cleaned HTML copy for attachment, currently removing the `Lux / CCT / ADRC` scatter image block.
- When `--summary`, `--export-pdf`, or `--export-html-attachment` is used, the email body stays as plain-text summary only; the full dashboard is kept in the attachment to avoid mail client layout issues.

## Shared Query Service

Start a read-only SQLite service on a server:

```bash
export ANALYTICS_QUERY_TOKEN="replace-with-a-long-random-token"

python3 scripts/server_sqlite_query_service.py \
  --db outputs/local_analytics/india_4_1_4_7.db \
  --host 0.0.0.0 \
  --port 8765
```

Query it locally:

```bash
export ANALYTICS_QUERY_BASE_URL="http://server:8765"
export ANALYTICS_QUERY_TOKEN="replace-with-a-long-random-token"

python3 scripts/server_sqlite_query_client.py tables

python3 scripts/server_sqlite_query_client.py query \
  --sql "SELECT model_name, COUNT(*) AS cnt FROM photo_events_parsed GROUP BY 1 ORDER BY cnt DESC;"
```
