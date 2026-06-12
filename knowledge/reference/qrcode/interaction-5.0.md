# 【PRD】Camera 5\.0\-二维码识别交互优化

# 前言

在空行输入“/高亮块” 插入高亮块，突出显示重点信息

# 一、 版本信息

版本号：

创建日期

审核人

# 二、 变更日志

|**时间**|**版本号**|**变更人**|**主要变更内容**|
|---|---|---|---|
|2026/1/13|1\.0|Travis |梳理当前存在问题|
|||||



# 三、 需求背景

## 产品 / 数据现状

1. 二维码识别框一次识别很多，而且也并不稳定，不方便用户点击跳转，看起来也混乱

## 竞品分析 \- QR code 识别框

1. 只识别主体性最高的一个对象，而不是所有对象

2. 点击跳转的按键移动到画面底部。识别二维码成功后，在变焦条区域新增跳转按键

\[screen\-20260227\-160626\.mp4\]

\[ScreenRecording\_02\-27\-2026 16\-26\-29\_1\.mov\]

||网址|wifi|电话|邮箱|联系人|纯文本|地点|日期|
|---|---|---|---|---|---|---|---|---|
|iPhone|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YTI2YWE2OTc1MWY0NmY5ZjAwOTEwYzQ4OTY0YjU2ZmVfODBkZDQ2MmE3MTQ4YmUwMDdkOWY4YTVmZGEzZWNkNjVfSUQ6NzYzODUyNzE0MTQyODcxMTEzM18xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=Mjg3YWM1N2Q3MWMyYTE2ZDU5N2I5YzZjZWQ0YWZiMjRfZDQwMWMxYThlNWM4M2M5MDIwMmZiOTkwYWI0MmY4N2RfSUQ6NzYzODUyNzEwMjkzMzMzOTg3Ml8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=Y2JjODhhYjFkNTExMGUyNjA1MDZhNjI3ZTI0ZjJmN2ZfM2UzZGM2NjAxY2NjNjZiZjJiN2FhZDNkYzVlYWYzNDZfSUQ6NzYzODUyNjc0MTk5NjE2Mjc4MF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=OTE1MTQwOGU2NDk3NWMxMjRiZmYyZGE0MzY0ZTlmZDhfMTM3MTM3MzJkN2E5YTk4OWRkOWI1ODg1OTIwZTA4MzNfSUQ6NzYzODUyNzA2Nzc0Njg5NzYzNF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MjFmMTBkNDFiMTMyNzNmZTM4MDU5YzNkNDM1NzRhMGZfNTk1YjZjNDJmZWNmMTk4MDY2YjNjMzgyMzJkYWYwMTRfSUQ6NzYzODUyNjc4MDU4ODQ5NDU1OF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTA1MmY0YWQxMzhmMDhmNTYwODEwZDRkNTVlZDZlNGFfOWEwOTQ4MjdiNzI1ZWQ0OWRhZGNiMjBhYjNkMzE5NWNfSUQ6NzYzODUyNjgyMzYwMDYwNjk0OV8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YzFiMzkzZWY4NDk4YmJjMGNjZDBmZWI2ZWU1MmRiY2VfNmYzMmE0Y2ZkNTFjM2NkNWYyNDBmODZhYTA1MjlmMGZfSUQ6NzYzODUyNjk5NjIyOTkzNDgxNV8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MDI4YmUxMjQ5M2JmNTI4MzhmNjNlNjljMDI5NDMzODZfNWZhNjc5NWIzYjk3MTNlNmZjMmJiNTgyNjljMThkYmNfSUQ6NzYzODUyNzAyNjI2MTQyOTk3OV8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|
|Sumsung|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTdhNzE1MDI4MWRmZDZmOTU2YjUzYzFjM2RlNjAxNGJfNGQ2ZTRkOTkwNDY3NGE2ZmQ4M2E2NTFhMmNjY2NkMWNfSUQ6NzYzODUyNzk2Mzc1MTE0MTA4NV8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YzgzZGQ0ODg5NjlmMWJhNmFlYjhiMGM2ODAyM2FjOTlfZTVkNWMyMTUxZjNiNzI0ZjczODM3YTk4NzZjZTg2ZDZfSUQ6NzYzODUyODAxOTIyODAyMDQ1M18xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ODc0OTdiZDVjMWRjMzM2MmFlZjU5NmYwNDU5MjhlYWNfNzgwMzM5NzYxNmNhY2YyZGY5YTM4NzY5NTUwMjJmMmNfSUQ6NzYzODUyNzY2Mzg5MTg3NzU5Nl8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MjQ1NTViMTI5Mjc1YjlhNjljYzgxZThhYmQ3MjEyMGFfNDdiY2VjNjQyMDAxYWQzY2FmYTE5NTJjN2ZjMjgwOTFfSUQ6NzYzODUyNzk4NzUzODkwNjg1M18xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YTllNjY5YWFhZWQwMjU3YmE0YzY2MDcyOWM5Njk0NTVfNDRiYWQ1NmNmYzBiN2FjNjA1ZmViMjkzNzU2ZTM5MGZfSUQ6NzYzODUyNzYzODA1OTI0MTE4MF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MTZmODJhYzIxNTRmZjEyYzAyY2U0OTIwZTJhMWMxZjlfMzZjZGRlNjJjOGVhMTY1MmMzNDUzYjJhOTY2NjZlNzZfSUQ6NzYzODUyNzYwNzk4NjUwNzQ4NV8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTM0ZDljNTVjMzY5ZTg3YmIxNDA3MTllZmIwYzg5ODRfNmE3Y2Y4M2E2ZDU5NzAxOGQ1YjNiOTI2NTczYWQyZDhfSUQ6NzYzODUyODU4ODM5NjM4Mzk2Nl8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MzA5N2YzNWZiN2Y1ZGU4YjI0MDgwZjFhMGUxMDg3NTJfYzg5YmY0ZTk0YjJiMjk2MDExZDI2ZTk0ODAyMGM1YThfSUQ6NzYzODUyNzU1NTM2ODYwMzM1OV8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|
|pixel|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZjJmMmNjMWM5NjQxMjAwYWIwODgwMGFmNDA0YmZmNDJfOTcxNWI5OGI4NDc1YTcwOTMxZDI1ODRjMzFjMjAwZjZfSUQ6NzYzODUyOTQ1MDQ3MjE0ODcwMF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=Zjk0NTgwY2ZmNWRjN2E4ZTM4ZDNjYzNlMTU2YmM1YjdfNzgzMTAyZjkyNDhmZmIyODk2ODVlNTNkZTg0NzUzNGZfSUQ6NzYzODUyOTQ4NjA0MjE1Njc2OF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTRiMGVlN2U5ZDk5MTExNGQ3ZTUwOTc5MDRkNGUxYzVfY2RmNTMzNmRjMWZiNjM5YzQyOGFjYzc2ZWRhNGI2NTJfSUQ6NzYzODUyOTQwNDgxMzEwMjgxNF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NDI4YWMzMjVlM2I5YjNkOGUwZTQyY2ZkZjRhMTYyZDFfZmE4MTc3NTExMTE1NjNjOWM2MzVkNTE1ZDhhY2M3NzRfSUQ6NzYzODUyOTUyMzgyNjc5MDEwOF8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NDE4MDA3NmM5N2ZmZDVmNzUwZTdhZDJmZjkwNmU4MzVfZmFlY2E2OTdhZmNmMTZkNWE2ZGRkZDk1M2JiZGU3MjNfSUQ6NzYzODUyOTM2Njk0NzQ4MzM1OV8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YTMwZDRjN2IzYWY3OGIwM2I5NTI2ZThmYjZkNDdjNDNfMmEwMTA0NWY0ZmYxZjE4ZjcwMjU4ZWQzYjNjNDIyYTlfSUQ6NzYzODUyOTI0MzI5NDY5OTIzN18xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZDQ3MmE4MjQ2NDdjZmUzMjFlZjAzZTJkNzY2ZGM2MDJfNDc3NDE1NWNhYWMzOGE2Y2MxZThkNTQwMTExNDYxZjVfSUQ6NzYzODUyOTIwNzMwNzcwMTk4M18xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MmI3OWZhNWU2MGM0NDYzODc1NDg4NDBiNGMzZjg5NDlfNTYxNjlkZWZhOTllY2VjODRhNjMxNzg5MDdkNGZlMzJfSUQ6NzYzODUyOTU2ODAxODEwODEzM18xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)|

# 四、 需求范围

> 可条理性地罗列需求范围或信息架构
> 
> 

1. 项目范围：纯软件需求，在23112 NOS 5\.0 升级首发支持，支持回落。

2. 模式范围：仅照片模式，触发二维码识别时

3. 焦段范围：覆盖所有焦段

4. 老项目回落：支持回落，老项目默认 NOS 5\.0 升级带出

# 五、需求说明

## 5\.1 交互说明

#### **展示规则**

- 同一时间只展示 1 个识别结果，识别成功之后用红色框对焦框，跟踪显示

- 识别结果以底部浮层形式展示

- 当画面中同时存在多个二维码时，优先展示更靠近画面中心、面积更大的二维码

- 如果多个二维码同时出现且条件接近，保持当前结果不变，不频繁切换

#### **动画与时机规则**

- 二维码被稳定识别后，浮层再出现，避免瞬时闪现

- 建议稳定识别 300ms 后展示

- 浮层出现时使用淡入动画，时长建议 200ms

- 当二维码短暂离开画面时，不立即隐藏浮层

- 若在 600ms 内再次识别到同一二维码，则保持当前浮层不变

- 若超过 600ms 仍未识别到该二维码，则浮层淡出消失

- 浮层消失时使用淡出动画，时长建议 180ms

#### **标签定义**

- wifi

    - icon：Wi\-Fi icon

    - 文案：Connect to Wi\-Fi

    - 点击：进入 Wi\-Fi 连接流程

- qrcode

    - icon：二维码 icon

    - 文案：QR Code Detected / Scan Result

    - 点击：进入二维码结果详情页

#### **分类规则**

- 能明确识别为 Wi\-Fi 配网信息的二维码，展示为 wifi

- 除 Wi\-Fi 外，其余所有二维码统一展示为 qrcode

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MjgwNzI2YTc1Mzc0MzExMzllZjk2NGVmMTBlNThjYTZfYjI1MWY5MGY5MTY2YzJiMmMwMWEyOTgwODRkNThhYjVfSUQ6NzYzODQ2NjQxMDE1NDcwODcwMl8xNzgxMDc3MjMwOjE3ODExNjM2MzBfVjM)

**浮层位置与关闭行为**

识别到二维码后，禁用变焦条（缩放功能仍可用），浮层展示在底部原变焦条位置，避免与变焦栏重叠。对齐 iPhone 交互。

**关闭后重新识别**

用户关闭浮层后，若画面中继续识别到二维码，立即再次弹出浮层，不设冷却时间。

## 5\.2 需求词条\-不涉及

|应用场景|中文词条|英文词条|备注|
|---|---|---|---|
|||||
|||||
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



