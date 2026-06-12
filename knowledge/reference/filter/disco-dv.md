# 【PRD】Camera 4\.1\-新增  Disco / DV 特效滤镜

# 前言

在空行输入“/高亮块” 插入高亮块，突出显示重点信息

# 一、 版本信息

版本号：

创建日期

审核人



# 二、 变更日志

|**时间**|**版本号**|**变更人**|**主要变更内容**|
|---|---|---|---|
|2026/3/5|1\.0|Travis|创建文档|
|2026/3/11|1\.1|Travis|1. 新增功能支持范围<br>2. 更新 blader 与 动态照片互斥逻辑<br>3. 更新 toast 词条<br>4. 更新 滤镜名称 与词条|

# 三、 需求背景

## 项目背景

25131主要面向印度市场，目标用户为印度20\-29岁的核心年轻群体（大学生及初入职场的专业人士）。这群用户具备极强的创造力与探索精神，在社交圈层中高度活跃且深度追随KOL的审美趋势。

希望在普通拍照、视频 Motion Photo 中更新一组特效，完善多元风格的覆盖。增加相机的“玩法”，匹配目标市场正在进阶的审美取向，提升用户在社交场景下的影像竞争力。

## 竞品分析

> 列出竞品对比的主要信息和关键结论，可输入 @ 在此附上详细的竞品分析报告并添加在【附录】中
> 
> 

|**效果**|**效果参考**|**实现技术**|**用户场景效果模拟**|
|---|---|---|---|
|kira<br>P0|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MDM0MmY1ZTg0MmM4OTZjMjU1YzJlMmMyMmEwYmE4ZDNfMDNkNTM1ZGNiMTk3ZDZkNzQ2MDA2MGIyODQwYmVkOTNfSUQ6NzYxMzk3NDcwMjgyNjE4MDMyMl8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ODcxZGRlYzM2MmE2NGI1MDM4MmExNjAxYzQwMDA1MzRfNTY1NWFiMTc0MTBlODRlODlhNDExYTdjY2I2ZWY5MDJfSUQ6NzYxMzk3NDcwMTc0ODQyNDQxNV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=N2IyMzdlZDJkZTAyZWNkNzlkMWU5MWMzMmQ1NDZmMThfMTQwYzA4YTQ5MmJiZGFhM2QyZTYwZWQ5YmE2NTRjNzlfSUQ6NzYxMzk3NDcwNDM0MDE5Mjk4OF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>|高光识别<br>https://www\.shadertoy\.com/view/4cBSRz|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZmQxMTI2MjdlM2MwMjM4YzY0YTAxMDNiNmMyOGZmY2NfZTY5MTljY2Y5Yjg3NGMwOThhYTY1MGViZGJiMzEzNDhfSUQ6NzYxMzk3NDcwMDY1OTQxMjcwNV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZWNjZTk0NGYxYzFmY2UwOTA3MGM5YTk2NDgxMjQ3YjZfZjNmM2JhMjA1MjBmYWI5ODFlNzlkZmQ4ODMyNGIyODZfSUQ6NzYxMzk3NDcwMjE5NzEzMzAxOV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YzA0MWI2YjNjNjdjMzNkOGU0YWUxMGI3ZWJmMzQ4NzdfZGFkYmNiZjFkNmVlNGUyNjlmZTNmNDBjYWQ0NGQ4M2VfSUQ6NzYxMzk3NDcwNDM0MDIyNTc1Nl8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NDA4YmZhNmJmMjU4YzMxZmQ3M2QwOGEyNjg5MDQzNWRfZDFjMTk3ZGQ1Mjc2ZGU1MzczMjc4NGQ0MTU4ZDA0OWJfSUQ6NzYxMzk3NDcwMzMwMDMzMzI3OF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MmI3ZDQzODJkMTY3YTY3YzI1ZTVhYzlmZGFlMWU1NDVfZmQ4MjIyMThiNjE5ODcwN2NmZWI2ZjNkODMzZWYyMjlfSUQ6NzYxMzk3NDcwMTg3NDA1NjkzMF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YzYzODRiMjg5NWIxYmM4MjkzYWY1MjcxMDk3ODAyMzBfNzkzOGM0MWMxYTBjYjY5MWMwYWUxMGZmZTU5NzFhMTVfSUQ6NzYxMzk3NDcwNDYxMjg1NTUyMF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)|
|光线拉丝<br>P1|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZDI2NGJmNmNlNmMzNGZlMDM0ZjQ5MDhmMzNmYTc3MTZfOWZhMWY2NjhiOWNhY2Q3NjlkMGU5NzI4MmU4ZDc1MWFfSUQ6NzYxMzk3NDcwMzY4MzQ4OTUwNV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NDRhOTVjYjQ4YjBlMjM0MDllMTZjZjIzZjQwZDUyZjZfODU0MWFiNGE0Mzc0OGRlZDMzYzEwYjk3YzAwMDc2MDVfSUQ6NzYxMzk3NDcwNDg1MTgxNjE1OV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTVhYTViNTUxNmE3N2U5M2IxNzc3MWMwMjMxNTFkZTFfNDIzMGZkNjU4MGFjMWEyNmY2OTM3ZGMzY2YwMWUxYTBfSUQ6NzYxMzk3NDcwMTUzODYxMDkwOF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MzlkMDZjNDhjMjE1NTNkMWU4ODhlMzY5ZDMwMDNmMDhfN2RiNmI4YTJlZWUxYTUxMmM3YTRkMGE0ZGQ2YzVkNjBfSUQ6NzYxMzk3NDcwMDU1NzY1MTY3NV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)|高光识别<br>https://www\.shadertoy\.com/view/MXXXD2|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NDhiMmNmOTg0NTRlNjUzZmMwODdkZDk3MTFhNzdkYjlfZDdlZmVkMzliY2QxN2QxYmIxODg5NTBmMDc0YWZmNDNfSUQ6NzYxMzk3NDcwMjMwMjEzODA3NV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MTdiNGYyZjVkOWU3MTUyMTMwNTE0ODVhOGQwYmQ4ZjBfZWEyMmZhNWZlYTcxYTZlMDNlYWQ0NDkyZDZkYTc1MDdfSUQ6NzYxMzk3NDcwMjUzNzAwMjcxOV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NDQ1N2VhYzIxOTRhMTBjYjhhMWI5MzM3YzYzOWNjNThfMzA3OThiNTlkNmYzMTE2YmUzYTk4MWQ3OGNlMzM5NjJfSUQ6NzYxMzk3NDcwMzMwMDI2Nzc0Ml8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YmYwMmVkN2EyNWQ0MTQ4N2I1OWI1ZWE1YjU4Y2FiOGJfZWI1YzcyMTVlNTc5OGRiY2Y2NmExNjcwMzkxMWRjMGVfSUQ6NzYxMzk3NDcwMzMwMDMxNjg5NF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)|
|低像素ccd<br>P0<br>|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NmE0MjAyNmU0NzVkOThkMjI3NmU3NmViMzZkNjlkYjhfOWFhOTg0ZjEwNmM2Zjc4NDcyN2EzYTE0NGZkZDU5NmJfSUQ6NzYxMzk3NDcwMzg5OTgwNzQ1OF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MjZmMTRlNmMxNDhiMWU5ODMyYmJlNTA2NDgyY2YzYmZfZjMxZTEzYjZiYWIxNTgxYjA2MWQzNjAwMDkyZTYyZDBfSUQ6NzYxMzk3NDcwMzMwMDI1MTM1OF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZmUwY2E2OWZjNTdjNTg5YjI1ZTVjZWU5NTM1ODcwZDdfNGIxZjgyY2NlZTdhZTJjM2M5MzE3MGM2YjM0YWQxYjFfSUQ6NzYxMzk3NDcwMTUzODU5NDUyNF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>|边框（nothing字体时间码且为真实时间可更新）\+特效（低采样、降帧）<br>https://www\.shadertoy\.com/view/NdGyDK （时间码）<br>https://www\.shadertoy\.com/view/MdffD7 （低采样）<br>https://www\.shadertoy\.com/view/Dlf3RN （低采样）<br>https://www\.shadertoy\.com/view/Dsj3Dc （实时时间码边框\+低像素特效）<br>https://www\.shadertoy\.com/view/flG3zd（低像素特效\-buffer B）|\[copy\_7380341D\-28F2\-4069\-A2C5\-5C1980830140\.MOV\]<br>\[3月3日\.mp4\]<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTljMzJlMGY3MGY4ZTExYzQyNzM4ODIzY2ZiYTFiOTdfZmIwMGU2N2Q4MGQyZmRmNTViNzFlNTA5N2JmZjBhOGNfSUQ6NzYxMzk3NDcwMjUzNzAzNTQ4N18xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZDk3ODU3NTIwODc3MmExZDk0MmRjYmY2MjZjMDMzZjRfZDdlNjJlMThiNDc1ZmNhZWFlNTdiNDU0NjI3YmEzYzJfSUQ6NzYxMzk3NDcwNDk0NDEwNzIzMV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)|
|电影胶片<br>后续项目再跟进|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTc3MDU2MzVjNjg4OTM1YmVlYTdlNmNiNzJlZjU5NTRfZGE5NGQ1NmI2ZmZiZjgyN2RiNGM2Y2MxZTg5YjY2ODNfSUQ6NzYxMzk3NDcwMjUzNjk4NjMzNV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=Y2IxNDY1NjI0MzZiMDYyYmI3MGY0OGU2ZjlkNDI4ZGVfZTIzY2ZkODY2ODg1NzFkNGEwYmE0MmY0NzM1NGJiYTVfSUQ6NzYxMzk3NDcwMjgyNjE5NjcwNl8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)|胶片边框\+特效（跳动噪声\+漏光）<br>https://www\.shadertoy\.com/view/Wdj3zV （跳动噪声、闪烁特效）<br>|\[copy\_DE065112\-90D8\-4128\-A865\-F55703CEE6FF\.MOV\]|

# 四、 需求范围

> 可条理性地罗列需求范围或信息架构
> 
> 

1. 项目范围：纯软件需求，对硬件没有限制。首上项项目为25131，后续仅印度项目继承，实际版本根据具体需求而定

2. 功能范围：支持滤镜功能的模式，含 照片、人像、视频、动态照片

3. 老项目回落：25131 首发支持，在 17 版本回落老项目，所有升级老项目均支持，**全地区支持**

4. 需求列表

|需求名称|需求描述|
|---|---|
|新增  **Disco ****/ ****Blader ****/ ****DV** 滤镜<br>|在滤镜列表中新增 **Disco ****/ ****Blader ****/ ****DV**，三个滤镜<br>1. Disco / DV支持照片、人像、动态照片、视频模式。 DV 在静态照片中不支持动画<br>2. Blader 不支持动态照片与视频模式|

# 五、 功能详细说明

## 产品流程图（略）

> 将鼠标悬浮至下方空白图形模块，点击**编辑**，即可进入流程图创作你的产品流程图
> 
> 

## 交互原型图

> 在空白行输入“/Figma” ，插入 Figma 设计稿
> 
> 

## 功能说明

### 支持范围

下表定义了各滤镜在不同拍摄模式下的可用性：

|**滤镜名称**|**照片 \(Photo\)**|**人像 \(Portrait\)**|**动态照片 \(Motion Photo\)**|**视频\-1080P30**<br>**\(Video\)**|**备注**|
|---|---|---|---|---|---|
|**Disco**|●|●|●|●|全滤镜模式支持|
|**DV**|●|●|●|●|照片模式下拍摄，不支持动画效果|

- **Disco 滤镜**：

    - 应用于所有指定模式。

    - 需保证在预览流与生成效果中色彩与光效的一致性。

- **DV 滤镜**：

    - **动态模式（视频/动态照片）**：支持复古录像带的噪点、色偏效果，在左上角右跳动的录制中动画，右下角有录制时长动画。

    - **静态模式（照片/人像）**：仅保留复古色彩与纹理，**不支持**录制中的动画效果。

---

### 交互形式 

#### 滤镜入口与排序

- **列表位置**：新增的 Disco、Blader、DV 滤镜，按顺序放置在滤镜列表的**最前面**。

- 视觉：根据设计稿做取色，视觉同其他滤镜，在小预览框中的预览只做滤镜的叠加，不做其他高光、色散等特效

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YjI4ZWUyZDBkYTk3ZGJkM2NlOGQzNDVhMWU5NjQyZDdfODhkMzY2OTRlYjY3NTk2OThjYjBlZTUwZWU5M2ZiNDBfSUQ6NzYyNjI4MTI1NDYwMTcwNzIzNF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)

---

## 交互设计稿

[https://www.figma.com/design/00upqHPBmH4ohZlewde7qE/Camera-4.0--25111-Bellsprout-?node-id=12308-4037&t=M57uxUXp83wh7OAb-1]()

---

## 效果说明

@Riley Tang

|效果名称（暂定）|说明|具体方案图示|效果配置|
|---|---|---|---|
|**Disco**<br>|复古派对风格，主打强烈的暖色加上粉调氛围感，千禧年复古色调加上kira特效，适用于派对人像<br>|![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZGVkMDY0YzBjYWUwMWQyMzllNmVkODQyMzkyZjM0YjBfZmFjNDMzNzBhZGE5NTkzYTcyYjIwMzZmNWUwYTE2ODNfSUQ6NzYxMzcwMDQwNTY2Njc3ODg0NF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=OTdlNzYyMmY2NWZkZjNkYjEyNmVhZTU3NzdhZDY4OWJfN2U0MDY1ODg4ZjRlNzg5MDAwYzk2OTY4NTFlN2M4MjJfSUQ6NzYxMzcwMDQwMjAxNzgzMjY3MV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=N2I4ZjZjNDU4NGE0NzJiNzRhMDQzOTNkNjU0NjQwYzVfMWE1ZDRhMWZmMGM4ZTI0ZjllY2FmZTJhNzgxMGFhNDRfSUQ6NzYxMzcwMDQwNDIxMTMzODk3M18xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZWYyMzIwZTY4MWI4MDlkN2Q0ZTdiYmM4MGI5OTgxM2VfMDc3MTBjMTNlOGQxM2Q5ZjdhMjQ4NWY2ZjU1NzJkMDdfSUQ6NzYxMzcwMDQwNTIxMzY2Mjk0MV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ODJjYTkyMDhlMjA3ODAwMGNmNjE4MDJiOWFkOGFkZDlfMWYyODE1YjI3ZDc5MmJhMTI1MjA3YTA0NzZhYTFmNjRfSUQ6NzYxMzcwMDQwMzk2MzgyNTg4Nl8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZjczYTVlMDI0ODNkNzJkNWM0ZTkwZmNiODIwNjllY2JfODA4NmI4MTcwYzkwYTIxZTc5MzI4NDY1ZjM5MjUzNWFfSUQ6NzYxMzcwMDQwMjcyNjQyNDI5MF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>|滤镜\+kira素材\+高光识别|
|**Blader**|电影感镜头耀斑特效，搭配电影感城市滤镜，适用夜晚扫街<br>|\[01e6128f071146f9010370038ed190c8a2\_4610\.mp4video\.mov\]<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=OGRkMWM3OWNhMzM4NmJiZDI1ODY4MzUyOTExNzFlYjNfYjA1NTVlOTYyNGMxMzI5MDQxNGFjZmRiMTE5MjVlODNfSUQ6NzYxMzcwMDQwMzk1NTQ1MzY2MF8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZTY3MjFlMjRlYjZiZTY3N2U4NzkxYjUwYzg0YzIzYWJfYWEyYjIwZTcxODBmYzQ0ZWMyNTlkY2ViNmMzYTNlOWNfSUQ6NzYxMzcwMDQwMjQ3MjU1NDIwOV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZjFjZTY1ODJlZDkxNmI2MWRlYjNiZmZlMDRlNmJhYzNfMGZmMDVmM2U2YmI2ZWY1MWViMjU5ZjVlYWI2OGE4OTZfSUQ6NzYxMzcwMDQwNDU4MDMwNjY1M18xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YzhmNzgwZjFhZDU4N2I1NjQ0MGE0YzZlZWNlMTUwOTFfZGNlNjliOGE4ZDQ0NGI1NzRiM2E0NDcwYzU5NzQxYzBfSUQ6NzYxMzcwMDQwNDIxMTM3MTc0MV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>|滤镜\+拉丝耀斑素材\+高光识别|
|**DV**<br>|复古低像素画质，搭配高对比低饱和暖调色彩滤镜，叠加nothing特色时间码，适用于日常vlog记录|\[1291652454\.mp4\]<br>\[copy\_6FBFD28C\-FE48\-4F7F\-9E4A\-38F32CDD6B92\.MOV\]<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZDA5OWQxZDBkNGY2ZWZlOGNmMjk4ZmI3NTQ1NTVlMmVfZDdlZmQ3ZjI5NTYyNzM0MGI1NGYzMTc3ODMwNzE3YTJfSUQ6NzYxMzcwMDQwNTIxMzY3OTMyNV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YmQ5MTAzNTNiYjFkNGRhYzYxNWYzYzFlNGI0ZDMzYTRfMzgzYWQ5OWE4MDQ1ZWE1YTNiMTY2YmI2OWM4YjUwNjBfSUQ6NzYxMzcwMDQwMjQ3MjYwMzM2MV8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NmM1YWFmYzIzNDRhYmY5ODQyYWYzNTQyZjc1Njk0OTRfZGUzNTkwMzcwNzY0OGM3NjFlNWI1Nzc0NjBmODhlNTlfSUQ6NzYxMzcwMDQwNDEwNjM4MzA3Ml8xNzgxMDc3Nzg1OjE3ODExNjQxODVfVjM)<br>|滤镜\+nothing风格字体\+低像素特效|

## 需求词条

|应用场景|中文词条|英文词条|备注|
|---|---|---|---|
|滤镜名称|派对|Disco<br>|特效滤镜，复古派对风格，主打强烈的暖色加上粉调氛围感，千禧年复古色调加上kira特效，适用于派对人像|
|滤镜名称|DV|DV<br>|多语言不翻译，统一用 DV。特效滤镜，复古低像素画质，搭配高对比低饱和暖调色彩滤镜，叠加nothing特色时间码，适用于日常vlog记录|

# 七、 非功能需求

> 可以列举产品营销需求、运营需求、财务需求、法务需求、使用帮助、问题反馈等
> 
> 



# 八、 埋点

延续滤镜埋点，不涉及新埋点

|**参数名**|**参数说明**|**参数值**|
|---|---|---|
||||
||||
||||
||||



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

[效果设计｜25131特效更新](https://nothing-tech.sg.larksuite.com/wiki/CjYDwt5KdisDV0kMRzfl35eqgMh?from=from_copylink)

[Effect Design \| India Market Filter \& Effects Update](https://nothing-tech.sg.larksuite.com/wiki/Zb6kwaxmiiOC52kW2CJljZVugSb)

