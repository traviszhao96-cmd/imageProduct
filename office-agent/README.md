# Office Agent Profile

This directory stores the platform-neutral source profile for a cross-device office agent.

Goals:

- keep the core behavior stable across Codex and OpenClaw
- separate global agent behavior from product-specific imaging skills
- preserve the user's preferred collaboration style
- make sync simple through GitHub

Structure:

- `soul/`: stable agent identity and response policy
- `style-profile/`: user-specific working style and preferences
- `workflows/`: repeatable collaboration rules
- `adapters/`: platform-specific mapping notes for Codex and OpenClaw

Design rules:

- write core policy in English for cross-platform portability
- keep personal style notes close to the user's real language habits
- force final output language to follow the user's input language
- prefer clarify-first collaboration for non-trivial office work

This layer should stay lightweight and durable.
Do not put temporary task notes, per-project PRDs, or generated outputs here.
