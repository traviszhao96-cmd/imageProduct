# Language Policy

The office agent must keep internal portability and user-facing language behavior separate.

## Core Rule

Always match the user's language in the final response by default.

## Rules

- If the user writes in Chinese, reply in Chinese.
- If the user writes in English, reply in English.
- If the user explicitly asks for another language, follow that request.
- Do not switch to English just because internal skills, prompts, templates, or workflows are written in English.
- Do not assume bilingual output is helpful unless the user asks for it.

## Internal vs Final Language

These may stay in English without changing the final response language:

- skill names
- file names
- workflow rules
- adapter notes
- implementation references

The final user-facing answer must still follow the user's language.

## Mixed-Language Cases

- If the user mixes Chinese and English, follow the dominant working language of the request.
- If the request contains English product terms inside Chinese instructions, keep the main response in Chinese and preserve necessary product terms.
- If the request is mostly English but asks for Chinese output explicitly, reply in Chinese.

## Default Safety Behavior

When the correct output language is ambiguous, prefer the language used in the user's latest instruction instead of the language used in internal source files.
