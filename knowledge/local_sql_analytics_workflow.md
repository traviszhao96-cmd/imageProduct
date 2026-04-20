# 本地 SQL 查数工作流

适用场景：

- 服务器上能导出数据，但不方便交互式查数
- 只有有限权限，无法直接调用高权限分析 API
- 导出的 7 天数据体量还可以放本地，但手工筛选太慢

推荐流程：

1. 在服务器上按天或按模块导出 `CSV / JSON / JSONL`
2. 下载到本地，例如 `docs/00_inbox/shared/raw_data/`
3. 用脚本导入 SQLite
4. 直接写 SQL 查询

## 1. 导入数据

```bash
python3 scripts/local_sql_analytics.py import \
  --db outputs/local_analytics/analytics.db \
  --table event_log \
  --source docs/00_inbox/shared/raw_data/day1.csv docs/00_inbox/shared/raw_data/day2.csv \
  --if-exists replace
```

说明：

- `--db` 是本地数据库文件
- `--table` 是目标表名
- `--source` 支持多个文件一起导入
- `--if-exists replace` 表示重建该表
- `--if-exists append` 表示继续追加

脚本会自动做这些事情：

- 把列名清洗成适合 SQL 的格式
- 把嵌套 JSON 拍平成列
- 把数组保存成 JSON 字符串
- 尝试把数字字符串转成整数或浮点数

## 2. 看有哪些表

```bash
python3 scripts/local_sql_analytics.py tables \
  --db outputs/local_analytics/analytics.db
```

## 3. 执行 SQL

```bash
python3 scripts/local_sql_analytics.py query \
  --db outputs/local_analytics/analytics.db \
  --sql "SELECT event_name, COUNT(*) AS cnt FROM event_log GROUP BY 1 ORDER BY cnt DESC LIMIT 20;"
```

也可以把 SQL 放到文件里：

```bash
python3 scripts/local_sql_analytics.py query \
  --db outputs/local_analytics/analytics.db \
  --sql-file docs/06_analytics/shared/sample_query.sql
```

## 4. 常见查询示例

按事件统计：

```sql
SELECT event_name, COUNT(*) AS cnt
FROM event_log
GROUP BY event_name
ORDER BY cnt DESC;
```

看某个用户的行为路径：

```sql
SELECT user_id, event_name, event_time
FROM event_log
WHERE user_id = '123456'
ORDER BY event_time;
```

筛选某个页面的点击：

```sql
SELECT *
FROM event_log
WHERE page_name = 'editor'
  AND event_name LIKE '%click%';
```

## 5. 什么时候建议升级到 DuckDB

如果你后面遇到这些情况，可以考虑升级：

- 单次导入数据达到几千万行
- 需要直接查 parquet
- 需要更强的聚合性能
- 经常做宽表分析

在当前环境下，先用 SQLite 起步最稳，后面如果你愿意，我可以再帮你把同一套命令迁到 DuckDB。
