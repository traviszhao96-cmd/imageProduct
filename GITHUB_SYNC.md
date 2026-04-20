# GitHub Sync Guide

This workspace can be synced through GitHub, but only a small portable subset should
be versioned for cross-machine skill reuse.

## Recommended Git Scope

Commit these folders and files:

- `outputs/skills/`
- `scripts/`
- `templates/`
- `knowledge/`
- `Camera-PRD-Template.md`
- `README.md`
- `GITHUB_SYNC.md`
- `.gitignore`

Keep these machine-local:

- `~/.openclaw/openclaw.json`
- any API token, app secret, or `.env` file
- `docs/` content unless you intentionally want product documents in GitHub
- large generated reports under `outputs/`
- local databases under `outputs/local_analytics/`

## First-Time Publish

From the repo root:

```bash
git init
git add .gitignore README.md GITHUB_SYNC.md Camera-PRD-Template.md knowledge templates scripts outputs/skills
git commit -m "Prepare portable imaging skills"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Setup On Another Machine

1. Clone the repo:

```bash
git clone <your-github-repo-url>
cd imageProduct
```

2. Make sure OpenClaw is already installed on that machine.

3. Sync the repo skills into the local OpenClaw skill pack:

```bash
python3 scripts/configure_openclaw_image_product_skills.py
```

4. Recreate machine-local secrets and service config:

- add the correct `~/.openclaw/openclaw.json`
- restore any required `ANALYTICS_QUERY_BASE_URL`
- restore any required `ANALYTICS_QUERY_TOKEN`

## Daily Update Flow

On the current machine:

```bash
git add outputs/skills scripts templates knowledge README.md GITHUB_SYNC.md .gitignore Camera-PRD-Template.md
git commit -m "Update imaging skills"
git push
```

On the other machine:

```bash
git pull
python3 scripts/configure_openclaw_image_product_skills.py
```

## Notes

- The sync script updates `~/.openclaw/openclaw.json` to load the curated skill pack.
- Do not commit a copied `~/.openclaw/openclaw.json`; it contains machine-local credentials.
- Some scripts rely on local Python packages or network access. Syncing the repo does not sync those system dependencies.
