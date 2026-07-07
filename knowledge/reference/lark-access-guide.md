# 飞书/Lark 文档访问指南（标准化）

> 使用官方 `lark-*` skill 体系，不再手拼 API。此文档是 Agent 访问飞书资源的权威参考。

## URL → Skill 路由表

飞书资源 URL 格式为 `https://{tenant}.larksuite.com/{type}/{token}`，按类型路由：

| URL 路径 | 资源类型 | 使用 Skill |
|----------|---------|-----------|
| `/wiki/{token}` | 可能是 Sheet/Wiki节点/Docx | 先试 `lark-sheets`→`lark-wiki`→`lark-doc` |
| `/sheets/{token}` | 电子表格 | `lark-sheets` |
| `/docx/{token}` | 文档 | `lark-doc` |
| `/base/{token}` | 多维表格 (Bitable) | `lark-base` |
| `/drive/{token}` | 云空间文件 | `lark-drive` |
| `/slides/{token}` | 幻灯片 | `lark-slides` |

## 常见任务 × 标准流程

### 任务 1：从分享链接读取 Sheet

收到 `https://...larksuite.com/wiki/{token}` 时：

1. 用 `lark-sheets` skill 的 `+info` 命令获取表格元数据
2. 用 `lark-sheets` skill 的 `+read` 命令读取数据
3. 如果 `lark-sheets` 失败，说明 token 不是 Sheet → 改用 `lark-wiki`

### 任务 2：读取 Wiki 文档内容

1. 用 `lark-wiki` skill 获取节点信息 → 得到 `obj_token`
2. 用 `lark-doc` skill 的 `+fetch --doc {obj_token}` 读取内容

### 任务 3：从 Sheet 提取文档链接

Sheet 中"需求文档"列的链接以 `mentionType: 22` 的 JSON 格式嵌入：
```json
{
  "type": "mention",
  "mentionType": 22,
  "text": "【PRD】文档标题",
  "link": "https://...",
  "token": "文档token"
}
```
用 Python 解析 API 返回的 JSON，筛选 `mentionType: 22` 即可提取所有链接。

### 任务 4：搜索文档

- 用 `lark-doc` skill 的 `+search` 命令
- 用 `lark-drive` skill 搜索云空间文件

## 已验证可用的 API 调用（bot 身份）

以下调用无需 user login，bot 有权限即可：

| API | 用途 |
|-----|------|
| `GET /open-apis/sheets/v3/spreadsheets/{token}` | 判断 token 是否为 Sheet |
| `GET /open-apis/sheets/v2/spreadsheets/{token}/metainfo` | 获取 Sheet 元数据（sheet列表） |
| `GET /open-apis/sheets/v2/spreadsheets/{token}/values/{sheetId}` | 读取 Sheet 数据 |
| `GET /open-apis/wiki/v2/spaces` | 列出可访问的 Wiki 空间 |
| `GET /open-apis/wiki/v2/spaces/{id}/nodes` | 列出空间下节点 |
| `GET /open-apis/drive/v1/files` | 列出 Drive 文件 |
| `GET /open-apis/drive/v1/files/{token}` | 获取文件信息 |

## 已知陷阱

1. **`/wiki/` URL 不等于 wiki node** — 飞书的 `/wiki/{token}` 可能指向 Sheet、Docx 或 Bitable，不能用单一 API 假设类型
2. **Sheet v2 values API 的 range 参数不可靠** — 有时 API 会忽略 `range` 参数返回固定范围，此时需要换用 `lark-sheets` skill 的 `+read` 命令
3. **Bitable 需要专用 API** — `/open-apis/bitable/v1/apps/{token}` 容易返回 `WrongBaseToken`，bot 可能没有该 Bitable 的权限
4. **链接中的 disposable token** — 复制来的链接可能带 `disposable_login_token` 参数（一次性），提取纯 token 即可
5. **`--as user` 需先 login** — user 身份调用需要先 `lark-cli auth login` 做 Device Flow

## 知识库中已缓存的文档

- `knowledge/reference/26111-prd-links.md` — 26111 Camera Feature List 全部 PRD 链接（26 个 P0/P1/P2 文档）
