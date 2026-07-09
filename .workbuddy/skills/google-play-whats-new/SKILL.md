---
name: google-play-whats-new
description: Write English Google Play "What's New" update copy for app releases, especially from product docs, PRDs, release notes, or feature summaries. Use when Codex needs to turn feature changes into concise store-ready changelog text with hard character limits, plain feature explanations, source checking, and multiple candidate versions.
---

# Google Play What's New

## When to use

Use this skill when the user wants:

- Google Play update logs or `What's New` copy
- English release notes based on PRDs, PDFs, DOCXs, or feature bullets
- Character-limited changelog variants such as `80`, `100`, `200`, `300`, or `500` characters
- A draft checked against source docs so unsupported claims are not introduced

## Goal

Turn product changes into short, natural English store copy that:

- stays within the requested character limit
- explains the user-facing value simply
- matches the source documents closely
- avoids overclaiming or inventing unsupported behavior

## Workflow

Follow this order unless the user asks for only one part.

1. Identify the target store and language.
2. Confirm the character limit. If none is given, default to `500 characters`, which is the common Google Play `What's New` limit.
3. Read the provided source material first: PRD, release notes, spec, or user bullet list.
4. Extract only user-visible changes. Ignore internal-only details unless they affect the user-facing explanation.
5. Check whether the draft wording is fully supported by the source.
6. Write one or more concise English versions.
7. Report the character count for each version.

## Source Priority

Use the strongest source available in this order:

1. Explicit product documents provided by the user
2. Existing release notes or version summaries in the workspace
3. The user's direct feature bullets
4. Careful inference from the materials above

If a claim is not clearly supported, soften it or leave it out.

Examples:

- Prefer `Add shapes like lines, arrows, rectangles, and circles` over naming unsupported gestures.
- Prefer `hide sensitive details with Mosaic` over promising privacy guarantees.
- Prefer `edit or remove shapes` only if selection and editing behavior is documented.

## Writing Rules

- Write in English unless the user asks otherwise.
- Focus on user-facing functionality, not implementation details.
- Keep the tone clear, lightweight, and store-appropriate.
- Prefer short sentences and active verbs.
- Avoid marketing exaggeration such as `best ever`, `revolutionary`, or `powerful` unless the user explicitly wants that tone.
- Avoid vague filler such as `various improvements` when concrete features are known.
- Keep terminology consistent with the product docs.
- Use feature names exactly when they are defined in the source, such as `Draw`, `Mosaic`, or `Motion Photo`.

## Hard Constraints

- Respect the requested character cap exactly.
- Count spaces and punctuation in the total.
- Do not fabricate gestures, menus, settings, or UI labels.
- Do not claim a feature is reversible, non-destructive, AI-powered, faster, or easier unless the source supports it.
- Do not mention unfinished, tentative, or experimental items unless the user asks for them.

## Output Format

Default output should be compact and ready to use.

Provide:

1. A recommended version
2. Character count
3. Optional alternates if useful
4. A brief note if any wording was adjusted to stay closer to the source

Example shape:

- `V2.8 – What's New`
- `Introducing Draw in Gallery...`
- `Characters: 382`

If the user asks for several lengths, provide one version per target length and label each clearly.

## Fact-Checking Against Docs

When documents are provided, verify these before writing:

- official feature name
- actual user actions supported
- whether the feature is new or improved
- whether limits or exclusions exist
- whether detailed interactions are documented or only implied

If a document is hard to extract cleanly, say so briefly and draft a cautious version instead of inventing details.

## App Store Style Heuristics

For Google Play `What's New`, prefer:

- one short paragraph
- `2` to `4` user-facing feature points compressed into prose
- simple benefit wording such as `add`, `hide`, `export`, `edit`, `save`, `highlight`

Avoid:

- long bullet lists unless the user requests list format
- engineering terms
- release-plan language
- uncertain roadmap wording

## Image Product Defaults

For gallery, camera, and video products, bias toward these explanation patterns:

- editing tools: what users can now do directly
- privacy tools: what can be hidden or blurred
- creative tools: what can be drawn, adjusted, or exported
- workflow improvements: what can now be edited, reverted, or reused more easily

Translate technical feature notes into plain user value, but stay faithful to the source.

## If the user provides an existing draft

Review it against the source and fix:

- unsupported claims
- awkward English
- missing core features
- character-limit overflow
- inconsistent terminology

Then return the corrected version with character count.

## References

Read only if needed:

- [references/examples.md](references/examples.md): example prompts and output patterns
