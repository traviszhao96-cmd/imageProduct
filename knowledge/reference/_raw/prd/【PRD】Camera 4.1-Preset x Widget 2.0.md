# 【PRD】Camera 4\.1\-Preset x Widget 2\.0

# 前言

在空行输入“/高亮块” 插入高亮块，突出显示重点信息

# 一、 版本信息

版本号：

创建日期

审核人



# 二、 变更日志

|**时间**|**版本号**|**变更人**|**主要变更内容**|
|---|---|---|---|
|2025/10/23|1\.0|Travis|创建文档|
|2025/11/17|2\.0|Travis|拆分出单独需求文档，并且根据设计稿更新文档|
|||||



# 三、 需求背景

## 产品 / 数据现状

Preset 的使用比例不断提升，也是 camera 的长期特色重点功能。但是在很多层面上仍然存在问题：

1. 与 playground 互联体验差。在2025年10月，首次推出了 nothing playground，在这个网站上用户可以轻松的分享共创出的手机配置功能，比如widget，EQ，Preset 等等。但是当前 Preset 分享和导入路径较长，依赖用户存储和上传 preset share card，体验不佳。

2. Preset 导入数量存在上限（20个）。很多用户反馈不能导入足够多的自己喜欢的 preset，体验不佳。

3. Widget 体验不佳。当前桌面的 widget 中显示的内容信息量较小，并且没有默认常驻，在 OS 中未来会默认支持，需要提高支持 preset 的信息量

## 竞品分析

> 列出竞品对比的主要信息和关键结论，可输入 @ 在此附上详细的竞品分析报告并添加在【附录】中
> 
> 

略。该功能为产品特有功能。

# 四、需求目标

1. 通过 preset 功能使用路径优化，进一步提高 preset 的使用频率，期望提高 20%

# 五、 需求范围

> 可条理性地罗列需求范围或信息架构
> 
> 

1. 项目范围：纯软件需求，对硬件没有限制。25131/25141 首发上项，后续项目默认支持，老项目升级支持

2. 模式范围：不限制模式，核心是 preset 功能架构的优化

3. 焦段范围：所有

4. 老项目回落：支持回落，老项目默认 NOS 5\.0 升级带出

## 需求列表\&需求单

# 六、 功能详细说明

## New Preset Widget 

### 功能描述

#### 添加新 preset 样式 \- Preset Widget 2

- 新增 2×2 样式的 Preset Widget，新增在 widget 列表中

- 保持原先支持的 widget 样式。在 Camera widget 选择栏中，保持支持用户选择原样式的 widget。由于 25111 mp 版本时间紧迫，所以在该版本中没有支持原样式的 widget，而是直接替换。这样会导致老用户在相机升级后原先的widget 格式错乱，该问题需要在老项目升级前修复，最好在mp1\.5版本支持

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZDM3NGNjOGUyMmU3MDc3ZDYzYmNiYWUyYjdmMzM3NTVfODJmNzAzOGUyZGM0Y2M3YjM0YThlMzY0MzFiODhkYTZfSUQ6NzU3NjkxNTQxMzk3NjUzNDc0OV8xNzgxMDc3ODEwOjE3ODExNjQyMTBfVjM)

#### Preset Widget 2 样式说明

- 支持显示封面、模式、焦段、滤镜、名称。

- 封面使用 1:1 比例，中心自动裁切。在当前版本的 B\&W Film 封面中，会出现边框，短期无法解决

- 模式，焦段，滤镜，名称，与 分享卡片展示逻辑保持一致。Photo, video, portrait, expert 等均全大写单行显示，超长名称 landscape 拆分两行显示，其他多语言超长打点显示。

- Preset 有两种字体大小，如果名字不超过一行，使用32px大小字体，超过一行，则使用 24px 大小字体。详情参考设计稿

- 底色支持 深色\&浅色 模式的适配，详情参考设计稿

- 支持 resize 到2\*4 样式，用更大的空间 2\*2 来显示封面图片，右侧显示当前的 preset 信息

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTE1NTRmNzcyOWE1NGZiYTI2ODQ0OTM3NmFkYjgzNjBfNGZhYTMwZjkyYzVjZDA3MTE2ODdkZDUxNzExNDkxY2VfSUQ6NzU3NjkzMDA0NDU4OTcyMzM2MF8xNzgxMDc3ODEwOjE3ODExNjQyMTBfVjM)

#### Preset Widget 2 支持最多 5 个 Preset 聚合

- 新 Preset 样式支持选择 5 个 preset，用户可以上下滑动选择 preset。在页面中有 5 个小点，支持用户上下滑动选择 preset，点击后唤起相机并使用该 preset。

- 支持勾选最多 5 个 preset 。用户可以在 preset widget list 中，最多勾选5个 preset 。如果已经勾选 5 个，列表中的其他 preset 置灰。如果用户继续点击已置灰 preset ，toast 提示用户：“微件最多支持展示 5 个预设”。若预设数量不足 5 个，则自动减少展示数量。

- 内容与顺序逻辑。widget list 与 setting list 中的内容与顺序保持一致，widget 中 preset 的顺序，与这两个列表中保持一致

    - 如果用户在 preset setting list 中，手动调整在 widget 中已经选中的 preset 顺序，则 widget 中同步调整。widget 固定按照在 list 中从高到低顺序展示

    - 如果用户在 preset setting list 中，手动删除 preset。如果用户手动删除已经选中的 preset，则自动减少展示数量。用户如果手动删除掉所有预设，无 preset 时，仅显示文字 “Tap to add presets”。此时如果用户点击 widget，直接跳转到 preset 勾选界面

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YjA4NDJkOTAyZjc3YjhiNmQ0YjE0N2M4YTE5MDMxNzZfYTdmNWUwMGVlNzkyNTA1YTdjMTE1MmM5YzZhZDY0ZjNfSUQ6NzU3NjkzMDIwOTE5OTM5NDUyNl8xNzgxMDc3ODEwOjE3ODExNjQyMTBfVjM)

### 交互设计

[https://www.figma.com/design/00upqHPBmH4ohZlewde7qE/Camera-4.0--25111-Bellsprout-?node-id=5709-17345&t=3BqVC8kGR6IQ3Fqc-1]()

---

## New preset widget 支持聚合与预装

- 装机默认支持聚合 Widget，默认支持三个 preset，分别是 Cold retro future, Urban，Cine Amber

- 机型出场自带该 widget，用户可以通过滑动选择 preset，并重新编辑在该 widget 中支持的 preset

- 从 widget 首次进入相机后弹出 preset on boarding 页面

    - 弹出页面的选项做修改，只有「OK」，用户点击之后弹出的页面收起

    - 原首次进入相机的 on boarding 逻辑不变

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZjVmNmYwMDAyOWZiMjQ2ZTlhYjkxNGU2MTk0N2UyY2RfM2UxNjZiNzJjYzUyYzNkMWFkZDdlMzgyOWUzNWEwMzhfSUQ6NzU3MzUzMTUxOTY1OTgwNjQzMl8xNzgxMDc3ODEwOjE3ODExNjQyMTBfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YmZhNzNiOGIwMjBhYTc2NWU0NWI1ZGZiZWVkZWZhZWJfNjY1NDBiNzY0M2NhM2QyMWI3NjU4Nzg0ZWM0NWY5MjJfSUQ6NzU3MzUzMTUxOTM5MTQ4NTY1OV8xNzgxMDc3ODEwOjE3ODExNjQyMTBfVjM)

## 需求词条

|应用场景|中文词条|英文词条|备注|
|---|---|---|---|
|Preset 为空时的 widget 标题|点击添加预设|Tap to add camera presets||
|用户在已经达到选择上限后继续点选 preset 时的提示|每个微件最多支持 %d 个预设|Each widget supports up to %d presets||
|||||

# 七、 非功能需求

> 可以列举产品营销需求、运营需求、财务需求、法务需求、使用帮助、问题反馈等
> 
> 



# 八、 埋点

|事件名|**参数名**|**参数值**|**参数说明**|上报方式|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||
||||||



# 九、 项目规划

> 输入 @ 把正文提及的项目管理文档附在此处
> 
> 



# 附录

> 输入 @ 把正文提及的具体文档，或需求相关的其他说明文档附在此处以供查阅
> 
> 

数据分析报告

- 此处插入数据分析报告

用户调研报告

- 此处插入用户调研报告

设计分析报告

- 此处插入设计分析报告



