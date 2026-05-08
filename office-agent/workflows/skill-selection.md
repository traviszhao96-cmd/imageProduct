# Skill Selection

This workflow defines how the office agent should choose and combine skills.

## Core Principle

Choose the narrowest skill that can solve the real task well.

Do not load many skills by default just because they look related.

## Selection Order

1. classify the task
2. identify the primary deliverable
3. choose the best-fit primary skill
4. add supporting skills only when they materially improve the result
5. keep the execution path easy to explain

## Task Categories

Common office-agent task categories include:

- product planning and PRD writing
- product document normalization
- analytics and SQL work
- workflow or process design
- external system operations such as Jira
- template-driven document publishing
- rule, knowledge, or agent-profile maintenance

## Single-Skill Bias

Use one primary skill when possible.

Examples:

- Gallery software PRD -> `gallery-feature-doc`
- imaging planning doc -> `mobile-imaging-planning-doc`
- local exported camera analytics -> `local-camera-analytics`
- Athena camera SQL -> `aws-athena-camera-sql`
- Jira issue operations -> `jira-automation`

## Multi-Skill Use

Use multiple skills only when the task naturally spans stages.

Examples:

- normalize product notes -> draft planning doc -> publish to Lark
- inspect local analytics -> summarize findings -> generate a follow-up document
- draft a requirement -> review gaps -> create Jira follow-up items

## Reuse Rules

- prefer existing skills before writing a new one
- prefer an existing template before inventing a new structure
- prefer promoting repeated manual patterns into reusable assets
- if no skill fully fits, use the closest one and state the missing edge clearly

## Clarification Before Selection

When the task could map to multiple skills with meaningfully different outputs:

- ask a short clarification question first
- do not arbitrarily pick the wrong workflow just to move faster

## Office-Agent Specific Bias

For this user:

- favor workflows that reduce ambiguity early
- favor reusable structure over one-off polish
- favor stable source assets over temporary output fragments

## Maintenance Note

When a task pattern repeats often but still requires manual orchestration, that is a signal to add:

- a new workflow note
- a new template
- or a new skill
