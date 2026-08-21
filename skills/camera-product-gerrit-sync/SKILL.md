---
name: camera-product-gerrit-sync
description: Use when the user wants to access internal Camera/Gallery Gerrit repositories or sync, package, submit, update, review, rerun CI, or merge product skills to `Nothing/AIAgent/Skills` on branch `cameraProduct`.
---

# Camera Product Gerrit Sync

## Scope

Use this skill for Camera/Gallery product skill delivery to the company internal Gerrit repo.

Do not use this skill for normal GitHub work. Keep personal GitHub and company Gerrit separate.

## Canonical Target

- Gerrit repo: `Nothing/AIAgent/Skills`
- Remote URL: `ssh://dev.nothing.local/Nothing/AIAgent/Skills`
- Branch: `cameraProduct`
- Skill path: `skills/camera_product_skills/`
- Gitiles URL: `http://dev.nothing.local:8282/plugins/gitiles/Nothing/AIAgent/Skills/+/refs/heads/cameraProduct/skills/camera_product_skills/`
- Local Gerrit clone: `/Users/travis.zhao/imageProduct-repo/.tmp-gerrit-skills`

Current default Camera/Gallery product skill set. Treat this as a known baseline, not a closed list; the actual sync scope is whatever valid skill directories exist under `skills/camera_product_skills/`:

- `image-product-doc-writer`
- `image-event-tracking`
- `camera-athena-sql`
- `camera-local-analytics`
- `jira-automation`

## SSH / Account Assumptions

Company Gerrit should use the dedicated company SSH config, not the personal GitHub key:

```sshconfig
Host dev.nothing.local
  HostName dev.nothing.local
  User travis.zhao
  Port 29418
  IdentityFile ~/.ssh/id_rsa_nothing_gerrit
  IdentitiesOnly yes
```

Verify connection with:

```bash
ssh -p 29418 dev.nothing.local
```

Expected success text includes `Welcome to Gerrit Code Review`.

Do not copy passwords, private-key contents, access tokens, or browser cookies into this skill. The SSH host alias and identity-file path are connection metadata only; authentication remains local to the user's machine.

The in-app browser does not automatically inherit the local Git/SSH session. If an internal Gerrit page shows a sign-in screen or 404, verify access through SSH before concluding that the repository or branch is unavailable.

## CameraApp Source Access

Use the local Gerrit SSH identity for read-only CameraApp source and branch checks:

- Gerrit project: `Nothing/app/CameraApp`
- SSH URL: `ssh://travis.zhao@dev.nothing.local:29418/Nothing/app/CameraApp`
- Primary development branch for current product checks: `develop2`
- Gerrit web URL: `http://dev.nothing.local:8282/admin/repos/Nothing/app/CameraApp`

Verify authentication and resolve the canonical project name with:

```bash
ssh -o BatchMode=yes -p 29418 travis.zhao@dev.nothing.local gerrit version
ssh -o BatchMode=yes -p 29418 travis.zhao@dev.nothing.local gerrit ls-projects --match CameraApp
```

Check the current `develop2` ref without cloning:

```bash
git ls-remote --heads \
  ssh://travis.zhao@dev.nothing.local:29418/Nothing/app/CameraApp \
  refs/heads/develop2
```

This access was verified on 2026-08-21. Treat the returned commit SHA as live state and query it again when current branch state matters.

## Sync Workflow

1. Open or clone the internal Gerrit worktree:

```bash
cd /Users/travis.zhao/imageProduct-repo/.tmp-gerrit-skills
git checkout cameraProduct
git pull origin cameraProduct
```

If the clone is missing:

```bash
git clone --branch cameraProduct ssh://dev.nothing.local/Nothing/AIAgent/Skills /Users/travis.zhao/imageProduct-repo/.tmp-gerrit-skills
cd /Users/travis.zhao/imageProduct-repo/.tmp-gerrit-skills
git config user.name "Travis Zhao"
git config user.email "travis.zhao@nothing.tech"
```

2. Put skills under the exact CI-expected path:

```text
skills/camera_product_skills/<skill-name>/
```

Never put them at repo root as `camera_product_skills/`; NT-EvalRunner expects the `skills/` prefix.

This path can contain more than the default five skills. When adding new skills, each skill directory must include a valid `SKILL.md` with frontmatter `name` matching the directory name and a useful `description`.

3. Validate before commit:

```bash
python3 - <<'PY'
from pathlib import Path
import re
root = Path("skills/camera_product_skills")
errors = []
for skill in sorted(p for p in root.iterdir() if p.is_dir()):
    md = skill / "SKILL.md"
    if not md.exists():
        errors.append(f"{skill.name}: missing SKILL.md")
        continue
    text = md.read_text(encoding="utf-8")
    if not re.search(r"^name:\s*" + re.escape(skill.name) + r"\s*$", text, re.M):
        errors.append(f"{skill.name}: name mismatch")
    if not re.search(r"^description:\s*\S", text, re.M):
        errors.append(f"{skill.name}: missing description")
    for rel in re.findall(r"`([^`]+)`", text):
        if rel.startswith(("references/", "assets/", "scripts/")) and not (skill / rel).exists():
            errors.append(f"{skill.name}: missing referenced path {rel}")
print("\n".join(errors) if errors else "validation=OK")
PY

find skills/camera_product_skills -path '*/scripts/*.py' -print0 | xargs -0 python3 -m py_compile
find skills/camera_product_skills -type d -name '__pycache__' -prune -exec rm -rf {} +
find skills/camera_product_skills -name '*.pyc' -delete
```

4. Commit with the company message format:

```bash
git add skills/camera_product_skills
git commit -m "[Camera][common][AgentSkill][TFT-000] update camera product skills"
```

If `Change-Id` is missing, install Gerrit hook and amend:

```bash
scp -O -p -P 29418 travis.zhao@dev.nothing.local:hooks/commit-msg .git/hooks/
chmod +x .git/hooks/commit-msg
git commit --amend --no-edit
```

Preferred full commit message:

```text
[Camera][common][AgentSkill][TFT-000] update camera product skills

[Description]
Update Camera/Gallery product AI skills under skills/camera_product_skills.

[Test]
Validated SKILL.md metadata and referenced paths for all skills under skills/camera_product_skills.
Ran python3 -m py_compile for bundled Python scripts.

Change-Id: I...
```

5. Push to Gerrit review:

```bash
git push origin HEAD:refs/for/cameraProduct
```

Do not direct-push to `refs/heads/cameraProduct` unless explicitly granted and requested.

## CI / Review Handling

If NT-EvalRunner says a skill path does not exist, first check that the path starts with:

```text
skills/camera_product_skills/
```

If `agent_review` leaves a stale `Verified -1`, trigger rerun by commenting on the current patch set:

```bash
printf '{"message":"retry_cov"}\n' | ssh -p 29418 dev.nothing.local gerrit review --json <change>,<patchset>
```

If the rerun does not happen, ask a reviewer/admin to clear the stale `agent_review Verified -1` or manually rebuild the Jenkins job.

Check state with:

```bash
ssh -p 29418 dev.nothing.local gerrit query --format=JSON --current-patch-set --all-approvals --submit-records change:<change>
```

## Submit

When Gerrit has `Code-Review +2`, `Verified +1`, and no blocking label, submit with:

```bash
ssh -p 29418 dev.nothing.local gerrit review --submit <change>,<patchset>
```

Confirm merge:

```bash
ssh -p 29418 dev.nothing.local gerrit query --format=JSON --current-patch-set change:<change>
git ls-remote origin refs/heads/cameraProduct
```

Merged status should be `MERGED`, and `refs/heads/cameraProduct` should point to the submitted revision.
