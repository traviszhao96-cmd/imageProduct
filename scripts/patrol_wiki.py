#!/usr/bin/env python3
"""Camera 5.1-26111 Wiki 每日巡检脚本"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# 配置
TOKEN = "t-g2067b0PCSOJ4LKHW5LP5OAR4YMIOIPRLZTXOLFY"
SPACE_ID = "7623306205619867360"
PARENT_NODE_TOKEN = "EIipweDIeiQ0hYkHkCRlrXpvg1d"
RECEIVE_OPEN_ID = "ou_1e068f80b2831f5bc95787032143a546"
PAGE_SIZE = 50

# 24 小时前的时间戳（毫秒）
now = datetime.now(timezone.utc)
cutoff = now - timedelta(hours=24)
# 对齐到昨天 00:00:00+08:00 到 23:59:59+08:00
cst = timezone(timedelta(hours=8))
now_cst = datetime.now(cst)
yesterday_start = now_cst.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
yesterday_end = yesterday_start + timedelta(days=1)
cutoff_ms = int(yesterday_start.timestamp() * 1000)
cutoff_end_ms = int(yesterday_end.timestamp() * 1000)

print(f"巡检时间范围: {yesterday_start.strftime('%Y-%m-%d %H:%M:%S')} ~ {yesterday_end.strftime('%Y-%m-%d %H:%M:%S')} CST")
print(f"时间戳范围: {cutoff_ms} ~ {cutoff_end_ms}")
print()

def api_get(url):
    """调用飞书 API"""
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"HTTP Error {e.code}: {body}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def api_post(url, data):
    """调用飞书 POST API"""
    body = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=body)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        print(f"HTTP Error {e.code}: {body}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Step 1: 分页获取所有子节点
all_nodes = []
page_token = None
page = 1

while True:
    url = f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{SPACE_ID}/nodes?parent_node_token={PARENT_NODE_TOKEN}&page_size={PAGE_SIZE}"
    if page_token:
        url += f"&page_token={page_token}"
    
    print(f"正在获取第 {page} 页...")
    resp = api_get(url)
    if resp is None or resp.get("code") != 0:
        print(f"获取节点失败: {resp}")
        break
    
    data = resp.get("data", {})
    items = data.get("items", [])
    all_nodes.extend(items)
    print(f"  获取到 {len(items)} 个节点")
    
    if not data.get("has_more"):
        break
    page_token = data.get("page_token")
    page += 1

print(f"\n共获取 {len(all_nodes)} 个节点\n")

# Step 2: 分类节点并筛选昨日更新
# obj_type: doc, folder, etc.
folders = []
docs = []
updated_docs = []

for node in all_nodes:
    obj_type = node.get("obj_type", "")
    title = node.get("title", "无标题")
    edit_time = int(node.get("obj_edit_time", "0"))
    owner = node.get("owner", "未知")
    node_token = node.get("node_token", "")
    
    entry = {
        "title": title,
        "edit_time": edit_time,
        "edit_time_str": datetime.fromtimestamp(edit_time / 1000, tz=cst).strftime("%Y-%m-%d %H:%M:%S") if edit_time else "未知",
        "owner": owner,
        "node_token": node_token,
        "obj_type": obj_type,
    }
    
    if obj_type == "folder":
        folders.append(entry)
    else:
        docs.append(entry)
        # 检查是否在昨天范围内更新
        if cutoff_ms <= edit_time < cutoff_end_ms:
            updated_docs.append(entry)

# Step 3: 生成报告
today_str = now_cst.strftime("%Y-%m-%d")
yesterday_str = yesterday_start.strftime("%Y-%m-%d")
total = len(docs)

if updated_docs:
    report_lines = [f"📋 Camera 5.1 PRD 巡检 {today_str}"]
    report_lines.append(f"更新 {len(updated_docs)}/{total} 份文档（昨日 {yesterday_str}）：")
    for i, doc in enumerate(updated_docs, 1):
        type_label = "📄" if doc["obj_type"] == "doc" else "📁"
        report_lines.append(f"  {i}. {type_label} {doc['title']} — {doc['edit_time_str']}")
else:
    report_lines = [f"📋 Camera 5.1 PRD 巡检 {today_str}"]
    report_lines.append("✅ 昨日无文档更新")

report = "\n".join(report_lines)
print("=" * 60)
print("巡检报告")
print("=" * 60)
print(report)
print()

# 输出调试信息
print(f"全部文档数: {total}")
print(f"文件夹数: {len(folders)}")
print(f"昨日更新文档数: {len(updated_docs)}")
print()

# Step 4: 发送 Lark IM 消息
im_url = f"https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id"
im_data = {
    "receive_id": RECEIVE_OPEN_ID,
    "msg_type": "text",
    "content": json.dumps({"text": report})
}

print("正在发送 Lark 消息...")
im_resp = api_post(im_url, im_data)
if im_resp and im_resp.get("code") == 0:
    msg_id = im_resp.get("data", {}).get("message_id", "unknown")
    print(f"✅ 消息发送成功! message_id: {msg_id}")
else:
    print(f"❌ 消息发送失败: {im_resp}")

# 输出 JSON 格式结果供后续使用
result = {
    "report": report,
    "total_docs": total,
    "total_folders": len(folders),
    "updated_count": len(updated_docs),
    "updated_docs": updated_docs,
    "message_sent": im_resp is not None and im_resp.get("code") == 0,
    "message_id": im_resp.get("data", {}).get("message_id", "") if im_resp else "",
}
print("\n--- JSON RESULT ---")
print(json.dumps(result, ensure_ascii=False, indent=2))
