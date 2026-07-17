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

> 一行一个 parameter value 组合。不上报经纬度、地点名、media_id、精确照片数量等敏感信息。Bitable 共 10 条（已同步）。

#### 🆕 `map_album_view` — 新增 event

| event_name | event_note | label | label_note | value | value_note | 操作场景说明 |
|---|---|---|---|---|---|---|
| map_album_view | 地图相册内地图相关行为时上报 | action | 地图行为类型 | map_load | 地图加载 | 进入地图相册后加载地图 |
| | | | | locate | 定位 | 点击定位按钮 |
| | | result | 执行结果 | success | 成功 | 地图加载 / 定位完成 |
| | | | | fail | 失败 | 地图加载 / 定位失败 |
| | | fail_reason | 失败原因 | permission_denied | 无定位权限 | 地图加载 / 定位失败原因 |
| | | | | timeout | 定位超时 | 地图加载 / 定位失败原因 |
| | | | | network | 没有网络 | 地图加载 / 定位失败原因 |

#### ➕ `gallery_view` — 已有 event，新增参数

| event_name | event_note | label | label_note | value | value_note | 操作场景说明 |
|---|---|---|---|---|---|---|
| gallery_view | 进入地图相册查看时上报 | album_type | 当前进入的相册/视图类型 | map_album | 地图相册 | 进入地图相册 |
| | | entry_source | 进入来源 | albums | 从 Albums 页面进入 | 进入地图相册 |
| | | | | photo_details | 从图片详情页进入 | 进入地图相册 |

---

#### 上报示例

```json
// 从 Albums 进入地图相册
{ "event_name": "gallery_view", "album_type": "map_album", "entry_source": "albums" }

// 从图片详情页地图缩略图进入
{ "event_name": "gallery_view", "album_type": "map_album", "entry_source": "photo_details" }

// 地图加载成功
{ "event_name": "map_album_view", "action": "map_load", "result": "success" }

// 点击定位成功
{ "event_name": "map_album_view", "action": "locate", "result": "success" }

// 定位失败 — 无权限
{ "event_name": "map_album_view", "action": "locate", "result": "fail", "fail_reason": "permission_denied" }

// 定位失败 — 超时
{ "event_name": "map_album_view", "action": "locate", "result": "fail", "fail_reason": "timeout" }
```

### 十二、干系人
- 有序列表格式（完整内容未渲染）

### 十三、待确认/待补充
- 有序列表格式（完整内容未渲染）

### 十四、初步评审
- 有序列表格式，无 agent 前缀

### 十五、附录
- 有序列表格式（完整内容未渲染）
