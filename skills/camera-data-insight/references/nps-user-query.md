# NPS 用户相机埋点查询方案

## 1. 目标与结论

目标是根据 NPS 问卷中的 `refid` 定位同一设备的相机使用行为。

已验证的完整链路为：

```text
问卷 refid
  → NPS 服务查询 ContactLedger
  → 返回 16 位 deviceId（Android ID）
  → Athena items[key='aid'].string_value
  → NTCamera 相机埋点
```

NPS `deviceId` 可以直接匹配 Athena 的 `aid`，不需要 MD5、去连字符或 16 位转 32 位。

## 2. 职责边界

| 环节 | 负责人 | 输出 |
|---|---|---|
| `refid → deviceId` | NPS 服务端 | 真实的 16 位 `deviceId` |
| 调用与加解密 | NPS 接口或其调用封装 | 可被调用方读取的接口响应 |
| `deviceId → aid → 埋点` | 数据查询侧 | 相机事件明细或汇总 CSV |

当前 `/push/nps/survey/lookup` 已有接口和加解密框架，但上游确认尚未实现真实的 ContactLedger 查询。上游完成后，业务响应只需提供 `deviceId`；接口同时保留 `code`、`message` 等基本状态即可。

建议的最小业务响应语义：

```json
{
  "code": 0,
  "message": "success",
  "deviceId": "<16位Android ID>"
}
```

实际请求、响应外层结构及加解密方式继续遵循 NPS 接口文档，不由埋点查询侧重新定义。

## 3. 已完成验证

使用一组已知的 `ContactLedger refid/deviceId` 样本，在印度 Athena 区域完成闭环验证：

- Athena 字段：`items` 数组中 `key='aid'` 对应的 `string_value`
- 设备：SuperContra / A009P
- 设备信息：颜色、RAM、存储、OS 和软件版本均与 NPS 记录一致
- 时间：2026-08-14～2026-08-21
- 命中：1493 条设备行为事件，其中 38 条 `NTCamera` 事件

这证明 `deviceId → items.aid → 相机行为` 已可用。当前待上游完成的是 `refid → deviceId`。

## 4. 本地查询方法

脚本位置：

```text
skills/camera-data-insight/scripts/nps_camera_query.py
```

脚本不包含任何 AWS 凭证，使用本机已有的 AWS profile。

安装依赖：

```bash
python3 -m pip install boto3
```

印度设备查询：

```bash
python3 skills/camera-data-insight/scripts/nps_camera_query.py \
  --device-id <NPS_DEVICE_ID> \
  --start-date 2026-08-14 \
  --end-date 2026-08-21 \
  --region ap-south-1 \
  --project SuperContra \
  --mode summary
```

其他全球数据将区域改为：

```text
--region eu-north-1
```

输出相机事件明细时使用：

```text
--mode detail --output ./nps-camera-detail.csv
```

查询前只检查 SQL、不访问 Athena：

```text
--dry-run
```

## 5. Athena 查询核心

```sql
SELECT event_date,
       project_name,
       device.model_name,
       device.sw_build_info,
       count(*) AS camera_events
FROM dc_database.data_mobile_behavior
WHERE event_date BETWEEN '<START_DATE>' AND '<END_DATE>'
  AND event_name = 'NTCamera'
  AND lower(
        element_at(
          filter(items, x -> lower(x.key) = 'aid'),
          1
        ).string_value
      ) = lower('<NPS_DEVICE_ID>')
GROUP BY 1,2,3,4
ORDER BY event_date;
```

不要使用以下字段替代 `items.aid`：

- `user_pseudo_id`
- `device.device_id`
- `device.device_id_2`
- `event_params.aid`
- `user_properties.aid`

## 6. 联调验收

1. 使用 Typeform 中一条真实 `refid` 调用 NPS lookup。
2. 响应必须包含真实的 16 位 `deviceId`，不能只固定返回 success。
3. 用该值执行本地查询脚本。
4. 能命中与 NPS 记录一致的设备信息和 `NTCamera` 事件。
5. 对无效 `refid`，NPS 接口应返回明确的查无资料状态。

完成以上步骤后，即可认为 `refid → deviceId → 相机埋点` 端到端联调通过。
