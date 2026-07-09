#!/usr/bin/env python3
"""Update 硬件配置 table in Lark Bitable with corrected specs."""

import json, urllib.request, ssl, time
from pathlib import Path

BITABLE_TOKEN = "YJSObjrqmamennsGWE5lqYdogFh"
HARDWARE_TABLE_ID = "tblusQMW1R6XprIx"
BASE_URL = "https://open.larksuite.com/open-apis"

# Auth
config = json.loads(Path.home().joinpath('.openclaw/openclaw.json').read_text())
account = config['channels']['feishu']['accounts']['main']
app_id, app_secret = account['appId'], account['appSecret']
req = urllib.request.Request(
    f'{BASE_URL}/auth/v3/tenant_access_token/internal',
    data=json.dumps({'app_id': app_id, 'app_secret': app_secret}).encode(),
    headers={'Content-Type': 'application/json'}
)
token = json.loads(urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()).read())['tenant_access_token']
HEADERS = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

def api_get(path, params=None):
    url = f"{BASE_URL}{path}"
    if params: url += '?' + '&'.join(f'{k}={v}' for k,v in params.items())
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=30, context=ssl.create_default_context()).read())

def api_post(path, body):
    url = f"{BASE_URL}{path}"
    data = json.dumps(body).encode()
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, data=data, headers=HEADERS, method='POST'), timeout=60, context=ssl.create_default_context()).read())

# Delete all existing records
print("🗑️  Deleting existing hardware records...")
deleted = 0
page_token = None
while True:
    params = {'page_size': 500}
    if page_token: params['page_token'] = page_token
    resp = api_get(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables/{HARDWARE_TABLE_ID}/records', params)
    items = resp.get('data', {}).get('items', [])
    if not items: break
    record_ids = [r['record_id'] for r in items]
    if record_ids:
        api_post(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables/{HARDWARE_TABLE_ID}/records/batch_delete', {'records': record_ids})
        deleted += len(record_ids)
        print(f"  Deleted {deleted}...", end='\r')
    if not resp.get('data', {}).get('has_more'): break
    page_token = resp.get('data', {}).get('page_token')
    time.sleep(0.3)
print(f"  🗑️  Deleted {deleted} records total")

# Hardware records from spec table
RECORDS = [
    # 26111 Base
    {"fields": {"项目代号": "26111", "机型": "Base", "相机位置": "主摄 / Main",
     "Sensor 型号": "S5KHP5SP05-FGX9", "分辨率": "200MP", "Sensor 尺寸": "1/1.56\"", "像素大小": "0.5um",
     "OIS": "YES", "光圈": "F1.88", "等效焦距": "23.5mm", "对焦类型": "PDAF",
     "Fallback支持": "YES", "备注": "200MP→50MP remosaic HDR upscale; VCM: HFC66B5003, OIS Driver: DW9828N; 一供盛泰(旭业)/二供盛泰(舜宇)"}},
    {"fields": {"项目代号": "26111", "机型": "Base", "相机位置": "超广角 / UW",
     "Sensor 型号": "OV08J10-GA5A-001A", "分辨率": "8MP", "Sensor 尺寸": "1/3.953\"", "像素大小": "1.116um",
     "OIS": "NO", "光圈": "F2.2", "等效焦距": "15mm", "对焦类型": "FF",
     "Fallback支持": "YES", "备注": "盛泰; 6P lens; FOV 120.2°"}},
    {"fields": {"项目代号": "26111", "机型": "Base", "相机位置": "前置 / Front",
     "Sensor 型号": "OV32D40-GA5A-002A", "分辨率": "32MP", "Sensor 尺寸": "1/3.6\"", "像素大小": "0.612um",
     "OIS": "NO", "光圈": "F2.2", "等效焦距": "23.21mm", "对焦类型": "FF",
     "Fallback支持": "NO", "备注": "盛泰; 5P lens; FOV 89°; Focus 34.8cm~47cm"}},
    # 26121 Pro
    {"fields": {"项目代号": "26121", "机型": "Pro", "相机位置": "主摄 / Main",
     "Sensor 型号": "IMX896", "分辨率": "50MP", "Sensor 尺寸": "1/1.57\"", "像素大小": "1.0um",
     "OIS": "YES", "光圈": "F1.88", "等效焦距": "23mm", "对焦类型": "PDAF",
     "Fallback支持": "YES", "备注": "盛泰; VCM: OJJ35F5032, OIS Driver: AW86033/DW9828N; 复用25111 Pro"}},
    {"fields": {"项目代号": "26121", "机型": "Pro", "相机位置": "超广角 / UW",
     "Sensor 型号": "IMX355", "分辨率": "8MP", "Sensor 尺寸": "1/4\"", "像素大小": "1.12um",
     "OIS": "NO", "光圈": "F2.2", "等效焦距": "15mm", "对焦类型": "FF",
     "Fallback支持": "YES", "备注": "丘钛; 5P lens; FOV 120.2°"}},
    {"fields": {"项目代号": "26121", "机型": "Pro", "相机位置": "长焦 / Tele",
     "Sensor 型号": "JN5-05", "分辨率": "50MP", "Sensor 尺寸": "1/2.75\"", "像素大小": "0.64um",
     "OIS": "YES", "光圈": "F2.85", "等效焦距": "80.5mm", "对焦类型": "PDAF",
     "Fallback支持": "NO", "备注": "3.5x; VCM: 磁化+DW9827C, OIS Driver: AK7323; 一供丘钛/二供AAC; Stroke AF 650um, OIS +/-210um"}},
    {"fields": {"项目代号": "26121", "机型": "Pro", "相机位置": "前置 / Front",
     "Sensor 型号": "KD1", "分辨率": "32MP", "Sensor 尺寸": "1/3.44\"", "像素大小": "0.64um",
     "OIS": "NO", "光圈": "F2.2", "等效焦距": "24mm", "对焦类型": "FF",
     "Fallback支持": "NO", "备注": "丘钛; 5P lens; FOV 89°; Focus 34.6cm~47.4cm"}},
]

# Upload
print(f"\n📤 Uploading {len(RECORDS)} hardware records...")
resp = api_post(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables/{HARDWARE_TABLE_ID}/records/batch_create', {'records': RECORDS})
code = resp.get('code', -1)
if code == 0:
    print(f"  ✅ {len(RECORDS)}/7 records uploaded")
else:
    print(f"  ❌ Failed: {resp.get('msg', 'unknown')}")

print("\n✅ 硬件配置表已更新")
