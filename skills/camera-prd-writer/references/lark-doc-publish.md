# Lark Doc Publish

Use this guide when the user wants the generated planning document to be written into a Lark or Feishu document automatically.

## Capability Boundary

Separate two targets clearly:

- Bitable: structured table sync
- Document: rich text body or section update

If the reference project already supports Bitable only, do not claim that document editing is already implemented. Reuse only the authentication, retry, and config patterns.

## Recommended Publish Modes

Use one of these modes:

1. Manual paste mode
- Return the final Markdown-like body
- User pastes into Lark manually
- Lowest integration cost

2. Append mode
- Append a new generated section to the end of the target document
- Suitable for report-style output
- Risk of duplicate sections across runs

3. Managed section replace mode
- Reserve a stable heading or marker such as `## Codex 自动生成区`
- On each run, replace only that section
- Best default for planning documents

4. Full overwrite mode
- Replace the entire document body
- Only use when the user explicitly asks for full ownership of the document

Default to managed section replace mode.

## Required Inputs

Before promising direct publishing, confirm:

- target document link or token
- app id and app secret
- document write permission scope
- target environment: Feishu CN or Lark global
- preferred update mode: append, managed section replace, or full overwrite

If any of these are missing, say that direct publishing cannot be completed yet and request only the missing items.

## Mapping Strategy

Draft content in a neutral section model first:

- title
- metadata
- headings
- paragraphs
- bullet lists
- tables

Then convert into target document blocks. Do not build the document request payload directly from raw user notes.

## Safety Rules

- Preserve user-authored content outside the managed section.
- Do not delete unknown sections unless the user explicitly requests full overwrite.
- If the target section marker is missing, append a new managed section instead of guessing.
- Keep a publish summary: document target, update mode, updated sections, skipped sections.

## Practical Reuse From Existing Lark Integrations

Existing Lark Bitable integrations can usually be reused for:

- config layout
- tenant access token retrieval
- request retry logic
- environment switching between `open.feishu.cn` and `open.larksuite.com`

They usually cannot be reused as-is for:

- document block tree parsing
- rich text section replacement
- inline image and table insertion
- locating and updating a specific document heading

## Suggested Implementation Order

1. Build a lightweight Lark client with shared auth and retry utilities.
2. Support creating or finding a managed section by heading marker.
3. Support writing headings, paragraphs, and bullet lists first.
4. Add tables and images only if the user needs them.
5. Add idempotent update behavior after basic publishing works.
