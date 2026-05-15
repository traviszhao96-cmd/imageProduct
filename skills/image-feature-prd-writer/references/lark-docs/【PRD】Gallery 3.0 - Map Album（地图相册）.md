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

### 十一、埋点设计（v2 — 按模板格式）

> 同一次行为只上报一条 event，多个参数随同一条 event 上报，不上报经纬度、地点名、media_id、精确照片数量等敏感信息。

| event_name | key | parameter | 说明 |
|------------|-----|-----------|------|
| gallery_view | enter_map_album | `tab_name=map`；`entry_source=albums / photo_details`；`has_location_media=true / false` | 进入 Map Album 页面时上报。`has_location_media` 仅表示是否有可展示的 GPS 媒体，不包含数量 |
| gallery_view | click_locate | `locate_action=click` | 用户点击定位按钮 |
| gallery_view | locate_success | `locate_result=success` | 定位成功，不上报坐标 |
| gallery_view | locate_fail | `locate_result=fail`；`fail_reason=permission_denied / no_signal / timeout / other` | 定位失败，`fail_reason` 与 `locate_result=fail` 同一条上报 |
| gallery_view | marker_click | `enter_from=map_marker`；`marker_type=single / cluster` | 点击地图标记进入媒体浏览；不上报精确媒体数量 |
| gallery_view | map_load_success | `map_load_result=success` | 地图资源加载成功 |
| gallery_view | map_load_fail | `map_load_result=fail`；`fail_reason=network / tile_load_failed / other` | 地图资源加载失败 |
| gallery_view | exit_map_album | `duration=number` | 离开 Map Album 页面时上报，单位秒 |
| media_manage | map_album_action | `action=favorite / share / delete / edit / hide`；`source_view=map_album` | 在 Map Album 来源的媒体浏览中执行管理操作 |

```json
{ "event_name": "gallery_view", "key": "enter_map_album", "tab_name": "map", "entry_source": "albums", "has_location_media": true }
```

### 十二、干系人
- 有序列表格式（完整内容未渲染）

### 十三、待确认/待补充
- 有序列表格式（完整内容未渲染）

### 十四、初步评审
- 有序列表格式，无 agent 前缀

### 十五、附录
- 有序列表格式（完整内容未渲染）
