---
name: jira-automation
description: Use when the user wants to create, update, search, assign, transition, comment on, or manage Jira issues through the Jira REST API with a local token-backed CLI.
---

# Jira Automation

## Overview

Use this skill when the user wants Codex to manage Jira issues directly from the local workspace.

For Atlassian Cloud sites like `https://nothingtech.atlassian.net`, the Jira API base URL should usually be the site root, not a browser page path such as `/jira/for-you`.

This skill uses:

- `JIRA_BASE_URL`
- `JIRA_TOKEN`

It also supports optional variables:

- `JIRA_AUTH_MODE` -> `bearer` or `basic`
- `JIRA_EMAIL` -> required for `basic` auth on Jira Cloud

Default auth mode is:

- `bearer` when only `JIRA_TOKEN` is set
- `basic` when both `JIRA_EMAIL` and `JIRA_TOKEN` are set

The main entrypoint is:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py --help
```

If the user gives a raw token in chat, do not write it into the skill files. Prefer telling them to export it into the environment for the current shell or store it in their own local secret manager.

## Workflow

1. Confirm the Jira site base URL and auth mode from environment variables.
2. If the user asks to create an issue, collect or infer:
   - project key
   - issue type
   - summary
   - description
3. If the user asks to modify an existing issue, get the issue key first and then use the matching subcommand.
4. Prefer explicit operations over free-form edits:
   - `create`
   - `get`
   - `search`
   - `update`
   - `comment`
   - `assign`
   - `transitions`
   - `transition`
5. Show the key result in plain language after running the command.

## Command Patterns

Create an issue:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py create \
  --project IMGP \
  --issue-type Task \
  --summary "Add Gallery edit telemetry audit" \
  --description "Need a first-pass telemetry gap review for edit actions."
```

Get an issue:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py get --issue IMGP-123
```

Search issues:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py search \
  --jql 'project = IMGP AND statusCategory != Done ORDER BY updated DESC' \
  --limit 20
```

Update fields:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py update \
  --issue IMGP-123 \
  --summary "Refine Gallery edit telemetry audit" \
  --description "Include Draw, Text, Crop, Erase, Export."
```

Add a comment:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py comment \
  --issue IMGP-123 \
  --body "Spec draft is ready for engineering review."
```

Assign an issue:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py assign \
  --issue IMGP-123 \
  --account-id 5b10a2844c20165700ede21g
```

List available transitions:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py transitions --issue IMGP-123
```

Move an issue:

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py transition \
  --issue IMGP-123 \
  --transition-id 31
```

## Field Notes

- For Jira Cloud, assignment usually needs `accountId`, not email.
- Some Jira projects require extra fields on create. If create fails with a field error, inspect the error message and retry with the required custom field.
- Use [references/api-notes.md](references/api-notes.md) when you need request shape examples or common failure handling.

## Safety Rules

- Never store live tokens in repo files.
- Prefer environment variables over inline command arguments for secrets.
- Echo only necessary issue data back to the user.
- If the API returns validation errors, surface them clearly instead of guessing hidden field values.
