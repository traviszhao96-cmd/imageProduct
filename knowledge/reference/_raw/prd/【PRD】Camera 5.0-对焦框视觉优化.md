# 【PRD】Camera 5\.0\-对焦框视觉优化

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
|2026/5/11|2\.0|Travis |根据澄清问题，更新确认需求细节|

# 三、 需求背景

## 产品 / 数据现状

当前相机中的各种识别框存在以下问题：

1. 人脸识别框简陋，且不稳定，只是一个细线方框，比较欠缺美感的同时，在识别到人脸后会不停跳动

2. 不支持宠物识别框，导致宠物的对焦准确性并不高，而该功能在iPhone和绝大多数安卓机上都支持

3. 点击对焦时，对焦框没有缩放的动画效果

4. 二维码识别框一次识别很多，而且也并不稳定，不方便用户点击跳转，看起来也混乱

## 竞品分析

> 列出竞品对比的主要信息和关键结论，可输入 @ 在此附上详细的竞品分析报告并添加在【附录】中
> 
> 

* [x] 分别测试iPhone，OPPO，三星，pixel 的人脸框，宠物框，二维码识别，点击对焦动画效果，并录屏

||人脸框|宠物框|点击对焦|二维码|其他||
|---|---|---|---|---|---|---|
|iPhone|最多 9 个<br>有较为平滑的切换弹跳动画<br>有淡出的消失动画|只识别猫狗<br>最多识别 7 个<br>有较为平滑的切换弹跳动画<br>有淡出的消失动画|快速的动画，淡入淡出效果<br>锁定动效效果|只识别一个最大的<br>有稳定动效<br>|在人像模式下由白色框变为黄色的锁定动效<br>照片/人像/视频的识别框都有所不同|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=M2I2ZDlhMmNiOTFlM2E0ZmY0ZjFkMDAyNTRlYjYwZjFfZTlkODZlZGUzYjljMGJlMGI4NDQ3Y2Q2YjRlMmI4Y2NfSUQ6NzU5NzMzODEyNjg0NzQzMDM2Nl8xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=OTEzZjBkNGQzNGNiZmNlZDFmODRkM2Q2ZjA1YzIyNTFfOTI1ZmU4MDdmYzc4MGE4ZWJmOTBiODY5YWJiYjA4ZTZfSUQ6NzU5NzMzODM1ODk5Mzg5OTIzM18xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MTNhMjEwYjMzOWU4MGU1MzUzOTY4ZWMzZmQwZDA0NDlfZTQ1OTI5ZWNjYTRhMzk5MThkMmQyODI5ZDJjYzljZDVfSUQ6NzU5NzMzODUxMDE1MjIyNDQ3Nl8xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)<br>|
|OPPO|最多 6 个<br>只有稳定动画，帧率较低<br>没有淡入淡出的动画|只识别猫狗<br>最多识别 5 个<br>有稳定动画|淡入淡出动画<br>锁定对焦动画<br>帧率相比iPhone看起来更低|默认模式下不支持|人像和照片模式下的识别框有不同<br>人像模式通过白色转为橙色，提示识别成功<br>没有平滑的切换动画||
|4a|最多 6 个<br>没有稳定动画，没有切换动画，没有出现和消失淡入淡出动画|没有宠物识别功能|没有动画|识别数量没有限制<br>没有稳定动效|各种模式的识别框完全一致<br>没有稳定动画，没有平滑切换动画||

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZDFhMGU1M2Q1YzZjNTEwMmE0YzViYjA0OTA1NDUwNjhfOWQ0Y2I4MTJmM2U5MGQ2ZWZhNDdlZmY1YWZmZmZmZTBfSUQ6NzU5NDc4NTE3NDAyMjkzNDI0MV8xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MmQ1YTM2YzMxZGIyNGY2ODgxNTFmMWI4NmZiZGNlMmNfOWY5Zjc0M2I4MzIwMGNkYTE1YzAzZjU3NDM2M2EzNmZfSUQ6NzU5NDc4NTc3MjIxMDEzMDY1N18xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZTMyMjRmODQ2YWMzNjEyMDdkMTFkMTRlYjI5YzQ2OTlfNTYzOWQ5YjY5YzM1NDVlZGVmNjVkMWM0MmMwYWFkMGNfSUQ6NzU5NDc4NjUzNTM1NDk0NTI0M18xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)

\[ScreenRecording\_01\-19\-2026 18\.mov\]



# 四、需求目标



### 五、 需求范围

> 可条理性地罗列需求范围或信息架构
> 
> 

1. 项目范围：纯软件需求，对硬件没有限制。预计分 2\-3 期完成，均支持回落。

2. 模式范围：覆盖所有模式

3. 焦段范围：覆盖所有焦段

4. 老项目回落：支持回落，老项目默认 NOS 5\.0 升级带出

## 需求列表\&需求单

# 六、 功能详细说明

### 对焦框视觉样式优化

当前的识别框为较为简陋的不规则矩形线条框，优化为更为美观的圆角矩形设计

1. 对焦框视觉设计优化，包括对焦框变为圆角矩形，曝光滑动条，上锁按键

2. 上下滑动时，滑动条上的 小太阳 icon，跟随曝光的变化改变大小

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=Y2JiM2RkMjYzNDg5ODg5ZDMxYmQ5MDc2MTdmNTE1NmVfMmMzZjFmNGU5NTg0ZGI5ZjZiYTlkODNiODI0YzYwMGNfSUQ6NzYzODQ3Nzg2MzcyNTE1ODExNF8xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)

## 需求词条\-不涉及

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

## 取消需求

### 人脸识别框动效

1. 样式优化，圆润识别框

2. 支持稳定动效，当前识别框会一直晃动，没有平滑效果

3. 识别数量不做调整，保持最多7个

4. 出现消失动效

5. 人脸在画面运动时的运动曲线

6. 最小框 的 大小 \- 需要定义

\[ScreenRecording\_01\-19\-2026 18\.MP4\]

\[record\.mp4\]

### 点击对焦框动效优化

当前 touch AF 的视觉较为简单，可以从点击对焦动效，滑动调整曝光视觉，多个维度做效果优化

1. 对焦框视觉更新，视觉更加专业，变化更流畅

2. 滑动曝光调整视觉更新

3. 点击弹出对焦框新增放大缩小的动效

4. 滑动调整曝光时的平滑性优化

### 人像模式识别框高亮

加入识别成功之后，对焦框高亮提示逻辑

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YWY3ZjY2OWQ3MjQ3YTM3ODlkNjYwM2EwNDBlOTk0YmRfMTdhYzMxODNmMjIwNjFjODcyMTFlMjA3Nzc5NzAzZmNfSUQ6NzYzODQ3NDUzNjAwNjIyNTYzMl8xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NjBmZjlmN2MzMmUxZDBmODQxOTVkZDExM2NmMWU5NjdfMTM4ZGQwNWY0MzA5NDI3MmYyYzVjNjY3YTQwMzQ2ZjlfSUQ6NzYzODQ3NDUzOTY4MDIyMjk0MF8xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)

### 宠物识别框

对画面中的宠物识别成功之后，使用外框框选

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MzkzMmExNWE2MzEzYzYxMzQ3NGM1NTExZWM1MjkwNzRfMzRmMzcxNDQzZTNiMjNkNzk0NmJkODRiNzE2NTFmMDdfSUQ6NzYzODQ3NDY5ODU3NjcyNzc3NV8xNzgxMDc3MjI0OjE3ODExNjM2MjRfVjM)



