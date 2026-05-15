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

### 十一、埋点设计

> 一行一个参数 key。同一次上报涉及多个 key 时拆为多行。不上报经纬度、地点名、media_id、精确照片数量等敏感信息。

| event_name | parameter | parameter_description | parameter_value | 说明 |
|------------|-----------|----------------------|-----------------|------|
| gallery_view | tab_name | 当前 Tab 名称 | map | 进入 Map Album 时上报 |
| gallery_view | entry_source | 上一级入口 | albums / photo_details | 同上 |
| gallery_view | has_location_media | 是否有可展示的 GPS 媒体 | true / false | 不包含数量 |
| gallery_view | locate_action | 主动触发定位 | click | 点击定位按钮 |
| gallery_view | locate_result | 定位结果 | success | 定位成功，不上报坐标 |
| gallery_view | locate_result | 定位结果 | fail | 定位失败 |
| gallery_view | fail_reason | 失败原因 | permission_denied / no_signal / timeout / other | 与 `locate_result=fail` 同一条 |
| gallery_view | marker_type | 标记类型 | single / cluster | 点击地图标记，不上报精确数量 |
| gallery_view | map_load_result | 加载结果 | success | 地图加载成功 |
| gallery_view | map_load_result | 加载结果 | fail | 地图加载失败 |
| gallery_view | fail_reason | 失败原因 | network / tile_load_failed / other | 与 `map_load_result=fail` 同一条 |
| gallery_view | duration | 停留时长 | number | 退出地图相册，单位秒 |
| media_manage | action | 管理动作 | favorite / share / delete / edit / hide | 适用于照片和视频 |
| media_manage | source_view | 操作来源 | map_album | 同上 |

```json
{ "event_name": "gallery_view", "tab_name": "map", "entry_source": "albums", "has_location_media": true }
```

### 十二、干系人
- 有序列表格式（完整内容未渲染）

### 十三、待确认/待补充
- 有序列表格式（完整内容未渲染）

### 十四、初步评审
- 有序列表格式，无 agent 前缀

### 十五、附录
- 有序列表格式（完整内容未渲染）
