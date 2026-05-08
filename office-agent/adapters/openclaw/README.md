# OpenClaw Adapter Notes

Use the files in `office-agent/soul/`, `office-agent/style-profile/`, and `office-agent/workflows/` as the source profile.

For OpenClaw:

- keep platform-specific loader details outside the core profile
- map this profile into the OpenClaw configuration layer without rewriting the source intent
- keep machine-local credentials and service config out of Git

OpenClaw should follow:

- the language policy
- the clarify-first workflow
- the user working style
