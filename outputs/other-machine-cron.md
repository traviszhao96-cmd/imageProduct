# 另一台 OpenClaw 机器的定时任务

> 前提：另一台机器已安装 WorkBuddy/OpenClaw，且 `~/.openclaw/openclaw.json` 已配置。

---

## 任务 1：凌晨 12:00 — Git 拉取同步

```
名称: 每日 Git 拉取
时间: FREQ=DAILY;BYHOUR=0;BYMINUTE=0
目录: /path/to/imageProduct

拉取 GitHub 最新代码，并汇报变更：
1. cd /path/to/imageProduct
2. git pull origin main
3. git log --oneline --since="24 hours ago" -- knowledge/ skills/
4. 如果有新提交，输出变更的文件和 commit message
5. 检查 knowledge/CHANGELOG.md 是否有新增条目
```

## 任务 2：凌晨 12:30 — Lark 核心对话整理

```
名称: Lark 核心对话整理
时间: FREQ=DAILY;BYHOUR=0;BYMINUTE=30
目录: /path/to/imageProduct

整理过去 24 小时内的重要 Lark 对话：

1. 读取 knowledge/CHANGELOG.md 了解最新需求变更
2. 读取 outputs/26111-26121-需求列表-v3.0.md 了解当前 RL 状态
3. 如有 PRD 巡检任务，执行并汇总
4. 生成「今日同步简报」：
   - 昨日需求变更数
   - PRD 更新情况
   - 待确认事项
5. 简报写入 outputs/daily-brief-{YYYY-MM-DD}.md
6. 通过 Lark IM 发送简报给 ou_1e068f80b2831f5bc95787032143a546
```

---

## 一键设置

在另一台机器的 WorkBuddy 中执行：

```
# 创建 Git 拉取任务
自动任务: 每日 0:00, 从 GitHub 拉取最新代码

# 创建对话整理任务
自动任务: 每日 0:30, 整理 Lark 核心对话并生成简报
```

---

## 时间线

| 时间 | 机器 | 动作 |
|------|------|------|
| 23:00 | 工作机 (Mac) | Git commit + push |
| 00:00 | OpenClaw 机 | Git pull |
| 00:30 | OpenClaw 机 | 对话整理 → 简报 → Lark 推送 |
| 09:00 | OpenClaw 机 | PRD 巡检 → Lark 推送 |

建议把 09:00 的 PRD 巡检也挪到 OpenClaw 机，这样不用依赖工作机开机。
