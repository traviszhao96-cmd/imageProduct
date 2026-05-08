# OpenClaw Profile Mapping

This file explains how to map the office-agent source profile into OpenClaw on multiple machines.

## Goal

Keep OpenClaw behavior aligned with Codex by reusing the same office-agent source files instead of maintaining a separate personality definition.

## Source Files To Load

OpenClaw should inherit behavior from these files:

- `office-agent/soul/core-identity.md`
- `office-agent/soul/communication-style.md`
- `office-agent/soul/language-policy.md`
- `office-agent/style-profile/user-working-style.md`
- `office-agent/style-profile/coworker-persona-dagong-xiaogou.md` when teammate-facing mode is desired
- `office-agent/workflows/clarify-first.md`
- `office-agent/workflows/skill-selection.md`
- `office-agent/workflows/output-standards.md`

## Recommended Integration Pattern

Use this repo as the stable source layer and keep OpenClaw-specific loading logic separate.

For each OpenClaw machine:

1. clone or pull the repo
2. sync the relevant imaging skills if needed
3. load the office-agent source profile into the OpenClaw configuration layer
4. keep credentials, tokens, and machine-local service paths out of Git

## Practical Mapping

Map the source files into OpenClaw behavior like this:

- `core-identity.md` -> base office-agent role
- `communication-style.md` -> response style and collaboration tone
- `language-policy.md` -> user-facing language behavior
- `user-working-style.md` -> personalized preference layer
- `coworker-persona-dagong-xiaogou.md` -> optional teammate-facing personality overlay
- `clarify-first.md` -> question-first collaboration behavior
- `skill-selection.md` -> skill routing behavior
- `output-standards.md` -> quality constraints on final output

## OpenClaw-Specific Notes

- keep the office-agent profile independent from machine-local OpenClaw config files
- do not commit secrets such as local OpenClaw JSON config, tokens, or private service endpoints
- if OpenClaw requires a generated or merged config, generate it from this profile instead of editing separate copies by hand

## Recommended Sync Flow

On any OpenClaw machine:

1. `git pull`
2. refresh any skill-pack sync step required by your existing OpenClaw setup
3. reload the profile layer that consumes `office-agent/`
4. run a small behavior test

## Smoke Test Suggestions

After syncing, test:

- Chinese input -> Chinese final output
- under-defined office task -> short clarification round
- clear formatting task -> direct execution
- task with multiple possible skills -> explicit routing choice

## Maintenance Rule

If you discover a behavior gap on one OpenClaw machine:

- do not patch only that machine if the change should be durable
- update the source profile in Git first
- then pull and reload on both OpenClaw machines

## Non-Goals

This mapping file does not define:

- credentials
- local service addresses
- project-specific temporary prompts
- one-off experiments that should not become global behavior
