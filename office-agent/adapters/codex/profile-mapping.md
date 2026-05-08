# Codex Profile Mapping

This file explains how to map the office-agent source profile into Codex environments on different devices.

## Goal

Keep one stable source profile in Git and reuse it across Codex sessions without maintaining separate behavior definitions per machine.

## Source Files To Load

Codex should inherit behavior from these files:

- `office-agent/soul/core-identity.md`
- `office-agent/soul/communication-style.md`
- `office-agent/soul/language-policy.md`
- `office-agent/style-profile/user-working-style.md`
- `office-agent/style-profile/coworker-persona-dagong-xiaogou.md` when teammate-facing mode is desired
- `office-agent/workflows/clarify-first.md`
- `office-agent/workflows/skill-selection.md`
- `office-agent/workflows/output-standards.md`

## Recommended Integration Pattern

Use the Git repo as the source of truth.

For each Codex environment:

1. pull the latest repo version
2. read the source files above
3. summarize or inject them into the active Codex system/developer setup
4. keep machine-local secrets outside the repo

## Practical Mapping

Map the source files into Codex behavior like this:

- `core-identity.md` -> agent role and long-term purpose
- `communication-style.md` -> response tone and collaboration style
- `language-policy.md` -> output language behavior
- `user-working-style.md` -> user preference layer
- `coworker-persona-dagong-xiaogou.md` -> optional teammate-facing personality overlay
- `clarify-first.md` -> intake and clarification behavior
- `skill-selection.md` -> how to choose and chain skills
- `output-standards.md` -> quality bar for final responses

## Device Consistency Rules

- do not create separate rewritten personalities on different devices
- do not manually tweak one machine and forget to mirror it into the source files
- if a behavior change should persist, change the source profile in Git first

## Recommended Sync Flow

On any Codex machine:

1. `git pull`
2. review the changed files under `office-agent/`
3. refresh the local Codex setup that uses this profile
4. run a small test prompt to verify behavior

## Smoke Test Suggestions

After syncing, test with one prompt from each category:

- a Chinese office task to verify language following
- an under-defined planning task to verify clarify-first behavior
- a simple mechanical task to verify direct execution behavior
- a task that could match multiple skills to verify routing behavior

## Non-Goals

This mapping file does not define:

- machine-local secrets
- project-specific product rules
- per-task temporary instructions

Those should stay outside the stable office-agent profile.
