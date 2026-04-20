# 服务器 SQLite 查数工作流

目标：

- 把当前本地 SQLite 数据库放到服务器上
- 通过服务器统一查数
- 同事本地安装 Codex 后，加载 skill 即可做交互式查询

当前推荐先用 MVP 方案：

1. 服务器继续使用 SQLite
2. 启一个只读 HTTP 查询服务
3. 本地通过查询脚本或 Codex skill 调这个服务

## 1. 服务器准备

把数据库文件上传到服务器，例如：

```bash
scp /Users/travis.zhao/imageProduct/outputs/local_analytics/india_4_1_4_7.db user@server:/data/camera_analytics/india_4_1_4_7.db
scp /Users/travis.zhao/imageProduct/scripts/server_sqlite_query_service.py user@server:/data/camera_analytics/server_sqlite_query_service.py
```

## 2. 启动只读查询服务

在服务器上执行：

```bash
export ANALYTICS_QUERY_TOKEN="replace-with-a-long-random-token"

python3 /data/camera_analytics/server_sqlite_query_service.py \
  --db /data/camera_analytics/india_4_1_4_7.db \
  --host 0.0.0.0 \
  --port 8765
```

建议：

- 先放在内网
- 用 Nginx / Caddy 做反向代理
- 最少加 token
- 更稳的话再加 IP 白名单

## 3. 本地直接查服务

```bash
export ANALYTICS_QUERY_BASE_URL="http://server:8765"
export ANALYTICS_QUERY_TOKEN="replace-with-a-long-random-token"

python3 scripts/server_sqlite_query_client.py tables
```

执行 SQL：

```bash
python3 scripts/server_sqlite_query_client.py query \
  --sql "SELECT model_name, COUNT(*) AS cnt FROM photo_events_parsed GROUP BY 1 ORDER BY cnt DESC;"
```

## 4. 建议给同事的 Codex 配置

同事本地需要：

1. 安装 Codex
2. 拿到这个 workspace 或其中的 skill 文件夹
3. 配置环境变量：

```bash
export ANALYTICS_QUERY_BASE_URL="http://server:8765"
export ANALYTICS_QUERY_TOKEN="replace-with-a-long-random-token"
```

然后让 Codex 使用 `outputs/skills/server-camera-analytics/` 这套 skill。

## 5. 什么时候升级到 PostgreSQL

后面如果出现这些情况，建议迁到 PostgreSQL：

- 多人同时查数明显变多
- 数据库按国家 / 周期持续扩大
- 需要更细的权限控制
- 需要更正规的备份和审计

在当前阶段，先用“SQLite + 只读服务 + skill”起步最快。
