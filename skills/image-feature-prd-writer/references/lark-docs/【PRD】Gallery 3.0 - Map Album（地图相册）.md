# 【PRD】Gallery 3.0 - Map Album（地图相册）

> 从飞书 API 提取的结构概要（部分嵌套内容未完整渲染）

## 结构分析

文档共 87 个 top-level blocks，结构如下：

### 一、变更日志 ✓ 已有
- 2x4 表格，1 条记录（2026/05/07, 1.0, Travis, 创建文档）

### 二、需求背景 ✓ 已有
- 问题陈述：Gallery 仅支持时间维度浏览，用户无法按地理位置管理和查看照片
- 用户场景：多个场景描述（嵌套列表）
- 竞品分析：4x4 表格（iPhone Photos / OPPO Gallery / Google Photos 对比）
  - 列：竞品 | 实现方式 | 定位触发 | 封面定位策略  
- 共性结论：多条要点

### 三、假设 ✓ 已有
- 多条假设（有序列表格式）

### 四、需求目标（模板对应 四）
- （该 PRD 将需求目标合并到其他章节）

### 五、需求范围 ✓ 已有
- In Scope：多条（有序列表）
- 🙅 Out of Scope：多条（有序列表，使用 emoji 标题）

### 六、需求
- 使用了特殊 block（type 43），可能是嵌入的任务/组件
- 非标准叙事格式，混合了有序列表和特殊组件

### 七、产品流程 ✓ 已有
- 入口、交互流程、边界情况等
- 含边界情况表格（4x2）：权限被拒绝、无网络连接、定位超时

### 八、需求词条 ✓ 已有（很完整）
- 8x4 表格：功能入口、无位置照片空状态、定位权限引导、GPS 定位失败、定位按钮无障碍描述、照片/视频聚合标记、单张照片/视频标记
- 每个词条都有中/英文 + 备注

### 九、关键依赖 ✗ 标记为"略"
- 仅写了"略"，缺失完整依赖表

### 十、指标与验收
- 验收条件以有序列表列出（block_type=12）

### 十一、埋点设计（v2 — 开发反馈修订版）

说明：
- 同一次用户行为只上报一条 event。
- 如果一次行为包含多个参数，多个 parameters 随同一条 event 一起上报。
- 不上报经纬度、城市、地点名、media_id、精确照片/视频数量等敏感信息。

| event_name | event_description | 触发时机 | parameters | 备注 |
|---|---|---|---|---|
| gallery_view | 进入地图相册视图 | 用户进入 Map Album 页面时 | `tab_name=map`；`entry_source=albums / photo_details`；`has_location_media=true / false` | `has_location_media` 仅表示是否有可展示的 GPS 媒体，不包含数量 |
| gallery_view | 点击定位按钮 | 用户点击地图相册中的定位按钮时 | `locate_action=click` | 仅表示用户主动触发定位 |
| gallery_view | 定位成功 | 点击定位按钮后，成功获取当前位置时 | `locate_result=success` | 不上报当前位置坐标 |
| gallery_view | 定位失败 | 点击定位按钮后，定位失败时 | `locate_result=fail`；`fail_reason=permission_denied / no_signal / timeout / other` | `fail_reason` 与 `locate_result=fail` 同一条 event 上报 |
| gallery_view | 点击地图标记进入媒体浏览 | 用户点击地图上的单张或聚合标记时 | `enter_from=map_marker`；`marker_type=single / cluster` | 点击后进入对应媒体浏览/Grid；不上报精确媒体数量 |
| gallery_view | 地图加载成功 | 地图资源加载成功时 | `map_load_result=success` | 不包含地图位置、缩放级别等信息 |
| gallery_view | 地图加载失败 | 地图资源加载失败时 | `map_load_result=fail`；`fail_reason=network / tile_load_failed / other` | 仅在明确加载失败时上报 |
| gallery_view | 退出地图相册 | 用户离开 Map Album 页面时 | `duration=number` | 单位：秒 |

**地图相册管理**

| event_name | event_description | 触发时机 | parameters | 备注 |
|---|---|---|---|---|
| media_manage | 在地图相册中进行媒体管理操作 | 用户在 Map Album 来源的媒体浏览/管理场景中执行操作时 | `action=favorite / share / delete / edit / hide`；`source_view=map_album` | 适用于照片和视频 |

**字段说明**

| parameter_name | parameter_value | 说明 |
|---|---|---|
| `tab_name` | `map` | 当前进入的 Gallery 视图为地图相册 |
| `entry_source` | `albums / photo_details` | 进入 Map Album 的来源 |
| `has_location_media` | `true / false` | 当前是否存在可在地图展示的带 GPS 媒体 |
| `locate_action` | `click` | 用户点击定位按钮 |
| `locate_result` | `success / fail` | 定位结果 |
| `fail_reason` | `permission_denied / no_signal / timeout / network / tile_load_failed / other` | 失败原因，根据对应事件场景取值 |
| `enter_from` | `map_marker` | 从地图标记进入媒体浏览 |
| `marker_type` | `single / cluster` | 地图标记类型 |
| `map_load_result` | `success / fail` | 地图资源加载结果 |
| `duration` | number | 地图相册停留时长，单位秒 |
| `source_view` | `map_album` | 媒体管理操作来源为地图相册 |

### 十二、干系人
- 有序列表格式（完整内容未渲染）

### 十三、待确认/待补充
- 有序列表格式（完整内容未渲染）

### 十四、初步评审
- 有序列表格式，无 agent 前缀

### 十五、附录
- 有序列表格式（完整内容未渲染）
