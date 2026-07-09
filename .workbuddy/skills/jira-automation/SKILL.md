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

## PM Issue 内容规范

作为 PM，创建 issue 时 description 必须包含简明扼要的关键信息。一个合格的 story 至少要有：

### 最低内容要求

| 章节 | 必填 | 说明 |
|------|------|------|
| 需求背景 | ✅ | 为什么做这个需求，解决什么问题 |
| 需求描述 | ✅ | 具体做什么，功能范围 |
| PRD 链接 | 按需 | 有正式 PRD 时必须附上 |
| Figma 链接 | 按需 | 有设计稿时必须附上 |

### 模板

```
## 需求背景
[简述问题/机会，1-3 句话]

## 需求描述
[功能范围，3-5 个要点]

## 相关链接
- PRD: [链接]（如有）
- Figma: [链接]（如有）
```

### CLI 示例

```bash
python3 outputs/skills/jira-automation/scripts/jira_cli.py create \
  --project NOS \
  --issue-type Story \
  --summary "Add album sort by captured date" \
  --description "## 需求背景
当前相册仅支持按文件导入时间排序，用户无法按拍摄日期浏览。

## 需求描述
- 相册主页新增排序选项：最近添加 / 拍摄日期
- 排序选择跨 session 记忆
- 默认排序为最近添加

## 相关链接
- PRD: https://nothing-tech.sg.larksuite.com/wiki/xxx
- Figma: https://www.figma.com/design/xxx"
```

## Safety Rules

- Never store live tokens in repo files.
- Prefer environment variables over inline command arguments for secrets.
- Echo only necessary issue data back to the user.
- If the API returns validation errors, surface them clearly instead of guessing hidden field values.

## NOS Project 已知陷阱

### Issue Type 差异

| Type | 额外必填字段 |
|------|------------|
| Story | `customfield_10101` (Device), `components`, `assignee` |
| Task | 上述全部 + `customfield_10041` (Severity) |

建议 Gallery 功能需求统一用 Story。

### 必需字段速查

| 字段 | ID | 格式 | 示例值 |
|------|-----|------|-------|
| Device | `customfield_10101` | 多选数组 | `[{"value": "all_phones"}]` |
| Components | `components` | 对象数组 | `[{"name": "NTGallery"}]` |
| Assignee | `assignee` | accountId 对象 | `{"accountId": "712020:3b...dff"}` |
| Epic Link | `customfield_10014` | 字符串 | `"NOS-10644"` |

**常见错误：**
- Epic Link 误用 `parent` 字段 → 静默失败，parent 始终为 null
- Device 误用 `{"value": "all_phones"}`（单选格式）→ 需要数组 `[{...}]`
- Components 空数组 `[]` → API 拒绝，必须选已有组件名
- 不指定 assignee → "默认经办人没有分配权限"
- Task 类型不填 Severity → 创建失败

### CLI update 命令陷阱

`jira_cli.py update --fields-json` 在 HTTP 204 (成功但无返回体) 时返回 `{}`，与静默失败无法区分。**关联 Epic Link 建议直接用 REST API PUT**：

```python
# 可靠方式
PUT /rest/api/3/issue/{key}
{"fields": {"customfield_10014": "NOS-10644"}}
```

`jira_cli.py create --fields-json` 同理，不可靠的字段（如 parent）会静默丢弃不报错。创建后必须 `get` 验证关键字段。
