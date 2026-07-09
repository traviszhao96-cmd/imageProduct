#!/usr/bin/env python3
"""Upload 26111/26121 FL CSVs to Lark Bitable. Batch 200 rows per call.
Usage: python3 upload_fl_to_bitable.py [--force]"""

import json, csv, urllib.request, ssl, sys, time
from pathlib import Path

BITABLE_TOKEN = "YJSObjrqmamennsGWE5lqYdogFh"
BASE_URL = "https://open.larksuite.com/open-apis"
CSV_DIR = Path("/Users/travis.zhao/imageProduct/knowledge/_output/fl_draft_26111_26121")
FORCE = "--force" in sys.argv

# Auth
config = json.loads(Path.home().joinpath('.openclaw/openclaw.json').read_text())
account = config['channels']['feishu']['accounts']['main']
app_id, app_secret = account['appId'], account['appSecret']

req = urllib.request.Request(
    f'{BASE_URL}/auth/v3/tenant_access_token/internal',
    data=json.dumps({'app_id': app_id, 'app_secret': app_secret}).encode(),
    headers={'Content-Type': 'application/json'}
)
resp = json.loads(urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()).read())
token = resp['tenant_access_token']
print(f"✅ Auth OK")

HEADERS = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}


def api_get(path, params=None):
    url = f"{BASE_URL}{path}"
    if params:
        url += '?' + '&'.join(f'{k}={v}' for k, v in params.items())
    req = urllib.request.Request(url, headers=HEADERS)
    return json.loads(urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()).read())


def api_post(path, body):
    url = f"{BASE_URL}{path}"
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers=HEADERS, method='POST')
    return json.loads(urllib.request.urlopen(req, timeout=60, context=ssl.create_default_context()).read())


def api_delete(path):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, headers=HEADERS, method='DELETE')
    return json.loads(urllib.request.urlopen(req, timeout=30, context=ssl.create_default_context()).read())


def delete_all_records(table_id):
    """Delete all records from a table."""
    deleted = 0
    page_token = None
    while True:
        params = {'page_size': 500}
        if page_token:
            params['page_token'] = page_token
        resp = api_get(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables/{table_id}/records', params)
        items = resp.get('data', {}).get('items', [])
        if not items:
            break
        
        record_ids = [r['record_id'] for r in items]
        if record_ids:
            api_post(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables/{table_id}/records/batch_delete', {
                'records': record_ids
            })
            deleted += len(record_ids)
            print(f"  🗑️  Deleted {deleted}...", end='\r')
        
        if not resp.get('data', {}).get('has_more'):
            break
        page_token = resp.get('data', {}).get('page_token')
        time.sleep(0.3)
    
    print(f"  🗑️  Deleted {deleted} records total")
    return deleted


def csv_to_records(csv_path):
    """Convert CSV rows to Lark Bitable record format."""
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        csv_rows = list(reader)
    
    records = []
    for row in csv_rows:
        fields = {}
        for col_name, value in row.items():
            val = str(value).strip()
            # Skip empty fields — Lark API doesn't need all fields
            if val:
                fields[col_name] = val
        records.append({'fields': fields})
    return records


def batch_create(table_id, records, batch_size=200):
    """Upload records in batches."""
    total = len(records)
    uploaded = 0
    batch_num = 0
    for i in range(0, total, batch_size):
        batch = records[i:i+batch_size]
        batch_num += 1
        body = {'records': batch}
        
        try:
            resp = api_post(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables/{table_id}/records/batch_create', body)
        except Exception as e:
            print(f"  ❌ Batch {batch_num} HTTP error: {e}")
            # Try smaller batch
            if len(batch) > 100:
                print(f"  🔄 Retrying with batch size 50...")
                for j in range(0, len(batch), 50):
                    small = batch[j:j+50]
                    try:
                        api_post(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables/{table_id}/records/batch_create', {'records': small})
                        uploaded += len(small)
                    except Exception as e2:
                        print(f"  ❌ Small batch also failed: {e2}")
                        return uploaded
                continue
            return uploaded
        
        code = resp.get('code', -1)
        if code == 0:
            uploaded += len(batch)
            pct = uploaded * 100 // total
            print(f"  ✅ Batch {batch_num}: {uploaded}/{total} ({pct}%)")
        else:
            msg = resp.get('msg', 'unknown')
            print(f"  ❌ Batch {batch_num} failed (code={code}): {msg}")
            # Print first record for debugging
            if batch:
                first_fields = batch[0].get('fields', {})
                print(f"     First record sample keys: {list(first_fields.keys())[:5]}")
            return uploaded
        
        time.sleep(0.5)
    
    return uploaded


def main():
    tables_resp = api_get(f'/bitable/v1/apps/{BITABLE_TOKEN}/tables')
    tables = tables_resp.get('data', {}).get('items', [])
    
    table_map = {}
    for t in tables:
        if t['name'] in ('26111', '26121'):
            table_map[t['name']] = t['table_id']
    
    for csv_file, table_name in [
        ("26111_fl_final.csv", "26111"),
        ("26121_fl_final.csv", "26121"),
    ]:
        if table_name not in table_map:
            print(f"❌ Table '{table_name}' not found in Bitable")
            continue
        
        tid = table_map[table_name]
        csv_path = CSV_DIR / csv_file
        records = csv_to_records(csv_path)
        print(f"\n📤 {table_name}: {len(records)} rows → table {tid}")
        
        if not FORCE:
            print(f"  DRY RUN — use --force to actually upload")
            continue
        
        # Delete existing
        delete_all_records(tid)
        time.sleep(2)
        
        # Upload new
        uploaded = batch_create(tid, records)
        print(f"  🎯 Final: {uploaded}/{len(records)} rows uploaded")
    
    print("\n✅ Done!")


if __name__ == "__main__":
    main()
