# 【PRD】Camera 5\.0\-相机按键视觉与动效更新

# 前言

本文档记录 Camera 动画优化需求，涵盖 MP1\.5 基础动画优化及后续的工具面板 Icon 与切换动效升级。

# 一、版本信息

版本号：v1\.2
创建日期：2026/06/03
审核人：待确认

# 二、变更日志

- 2025/11/24 v1\.0 Travis — 根据workshop共创成果，创建文档

- 2025/12/09 v1\.1 Travis — 从原来的文档里单独拆分出动效文档

- 2026/06/03 v1\.2 Travis — 补充工具面板 Icon 更新 \& 点击切换动效（NOS\-10975）

# 三、需求背景

## 产品 / 数据现状

1. 从数据上看，90%的用户只会使用最基础的相机功能，比如拍照，视频，快门按键，滤镜等

2. 相机的基础体验和基础控件存在诸多问题

    - 控件遮挡预览框，影响用户构图体验。Zoom plate, slide 等呼出时遮挡预览画面

    - 控件缺乏动画。各种控件在画面中出现，消失的时候，没有动画效果，导致切换的效果都比较生硬

    - 快门声音需要优化。时间长、声音较为尖锐等

    - 不常用模式体验需要优化。比如专业模式

3. 工具面板 Icon 视觉风格需统一更新，同时工具项在状态切换时缺乏点击动效过渡，交互手感生硬

## 竞品分析

略。该功能为产品特有功能。

# 四、需求目标

需求的目标是优化相机中的动画效果，以提升相机整体的流畅性和使用体验，从而进一步提升相机 NPS。具体包括：

- MP1\.5 基础动画补齐（toast、暂态开关、缩略图）

- 工具面板 Icon 视觉刷新 \+ 点击切换动效

# 五、需求范围

1. 项目范围：纯软件需求，对硬件没有限制。预计分 2\-3 期完成，均支持回落。

2. 模式范围：覆盖所有模式

3. 焦段范围：覆盖所有焦段

4. 老项目回落：支持回落，老项目默认 NOS 5\.0 升级带出

## 需求列表\&需求单

[Camera NOS5\.0 Requirement List v1\.0](https://nothing-tech.sg.larksuite.com/wiki/AMp5wOz2wiTqlOk2JUslpP2KgTg)

- NOS\-10975 \[Android 17\] 顶部和工具面板 Icon 更新 — 状态：打开

# 六、功能详细说明

## NOS 5\.0 \- 工具面板 Icon 更新 \& 点击切换动效 \- NOS\-10975 

1. 在工具栏面板（panel）中，在用户点击按键之后新增动效

2. 相机顶部栏和工具面板的 Icon 需要统一更新视觉风格，并且每个工具项在点击切换状态时需要有动效过渡，提升交互手感。

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZDBjZTczNTU5YjdjNTVjZWE1YTEwMmRiNGIzODIzODlfODZjNTk3NDg0N2M3MmRlYzVlNDJjYTQ1MWRiZjJhYjJfSUQ6NzY0NzM3OTEwODM0MjcxNDA3NV8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)

[https://www.figma.com/design/jqJbxudFcuM0QnajFZ3CvR/Camera-NOS-5.0?node-id=911-6133&t=P1bqhGLSPxtWazHQ-1]()

#### 涉及的工具项及状态

|**Button **|**Tap status bar icon 替换**|**Panel 动效状态切换**|动效视频|**Riv\.**|
|---|---|---|---|---|
|flash|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MzU5Y2JkMDAxNDBjZDkxYjAxYWEwYTQ1ODQ1YzFmOGVfYjE3NTNlZjg5ZGIzMjhlNTk2MDhjZTMxZTlhY2MyZTZfSUQ6NzY0NzM3NzU4MzYyOTI3NDg1MF8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)<br>|- On<br>- Off<br>- Torch<br>- Auto||\[icons\_camera\_flash\.riv\]<br>|
|timer|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YzE1NjE5ZjczZjA3ZDg1NTZiYzUxYTViOGY5ZjJmMTRfNjZiYTVkNzc5MzMzYmM5NTFlMmRhZTVhYzlkODgyZjdfSUQ6NzY0NzM3Nzg3MjM4NjEwMDk1OV8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)<br>|- Off<br>- 3s<br>- 10s||\[icons\_camera\_timer\.riv\]<br>|
|glyph mirror|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YmU4OWM0OGMwYWRiODFlMTRmYjFjZTMxNDAzM2ZmMjlfMWFmM2FhM2YzODk1MTRmNTRjM2Y3MzhlOWRhOGYzYzJfSUQ6NzY0NzM4MDUzNzM2MzA1ODM5OV8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)|- On<br>- Off||\[icons\_camera\_glyphmirror\.riv\]<br>|
|HDR|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MzMxOGQ4MWRhYmYzZDRmNzFkN2FhM2E5ZDk5NWM1MDhfOWUwMTFkZWQ1NjllZmYyMThiZWNiZDE5ZWExYmNjYjRfSUQ6NzY0NzM4MDU3OTMzNTMyNzQ1Nl8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)|- On<br>- Off||\[icons\_camera\_hdr\.riv\]<br>|
|EV|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTNmYWEzNTVhNmQ1NjI0MGFmZDA3MzBlYjkwNDY4YjdfY2JmNGNiM2Q1MTcyYmFkMTdlOTI2Yzg3MDE3YjcxNjZfSUQ6NzY0NzM4MDYxNTkzOTE0OTUzMV8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)|不涉及|不涉及|不涉及|
|motion photo|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NDBjMGZkNzIyMTBmYjIwYWNkNjU0YmVjOWNmYzYwOGNfOWQyNmMxOGU2YzlkOGZiNWE4NjE1Mzk5ZWRkOWZjYzBfSUQ6NzY0NzM4MDc1NDA5MTM2NDA2MF8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)<br>|- On<br>- Off||\[icons\_camera\_motionphoto\.riv\]<br>|
|grid|不涉及|- On<br>- Off||\[icons\_camera\_grid\.riv\]<br>|
|filter|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NWZjYjJhNDhiODE5NzRlNzUzNmQ4NDYwZDMyZTJjODFfNWFiN2M2NzdkNmYyYjMyZTFkMTRmYzUwYjg3ZWQwYjFfSUQ6NzY0NzM4MDQ3MjQyMzEyNDcwMV8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)|- On<br>- Off||\[icons\_camera\_filter\.riv\]<br>|
|tuning|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YzY5OWY3MzQ0NGM4OGJiMDhhYjAyZTE1YjMwNWExZjJfMDQ1MzU0YWNlOTYzMzQyMmUwNjE4MTczMTcxMzViYjdfSUQ6NzY0NzM4MDg3NTYyOTY0NTUzOF8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)|- On<br>- Off||\[icons\_camera\_tuning\.riv\]<br>|
|quality|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NjAwNDAwYThkNmM4M2Q3ZjMyNTEwNTk2MzcwZTUxNGFfNTI1NTA3YzdhOGRjMGIzNTRlYzYzOGU5YjhhNWJhZjNfSUQ6NzY0NzM4MDkyMTI2ODg5OTU1MV8xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)|- 12MP<br>- 50MP||\[icons\_camera\_quality\.riv\]<br>|
|camera ratio|不涉及|- 1:1<br>- 4:3<br>- 16:9<br>- Full||\[icons\_camera\_ratio\.riv\]<br>|
|watermark|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NmIzMjI3MzJiZDliNzk4Mzc5ODg1MzcwZjczNTI0ZjRfNjNjNjVkNTdjZjdlMTI3MGUyNThlNWVkOTJhNjYwOWJfSUQ6NzY0NzM4MTAzMTI1MTE1MjYxM18xNzgxMDc3MjEyOjE3ODExNjM2MTJfVjM)|- On<br>- Off||\[icons\_camera\_watermark\.riv\]<br>|

# 七、非功能需求

1. 动效性能：所有切换动效应在 60fps 下流畅运行，不得导致 UI 卡顿

2. 回落兼容：新 Icon 和动效在回落设备上需保持可用，低端设备可适当降低动效复杂度

# 八、埋点

待补充。NOS\-10975 相关埋点后续补充。

# 九、项目规划

- NOS\-10975 — 顶部和工具面板 Icon 更新 \| 状态：打开 \| 负责人：Kingson Wang \| 预计完成：TBD

# 附录

- Figma 设计稿：Camera NOS 5\.0 — 顶部和工具面板 Icon

