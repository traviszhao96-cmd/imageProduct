# 【PRD】Camera 4\.1 \- 视频前后双录

# 0\. 文档信息

- 文档标题：【PRD】Camera 4\.1 \- 视频前后双录

- 所属版本：4\.1

- 销售地区：Global

- 项目 / 机型 / 代号：Nothing 25131

- 项目阶段：MP1\.5

- 更新时间：2026\-04\-20

- 作者：Tiger

- 评审人：Travis zhao

---

# 变更日志

只记录影响需求理解的修改。

|时间|版本号|变更人|主要变更内容|
|---|---|---|---|
|2026\-4\-8|v0\.1|Tiger|创建|
|2026\-04\-17|v0\.2<br>|OpenClaw|按 Camera PRD 模板重组文档结构，整理背景、目标、范围、功能设计与依赖项|
|2026\-4\-20|v1|Tiger|补充功能设计内容|

---

# 需求背景

> 只回答一个问题：为什么现在要做。这里写现状、问题、证据，不写目标，不写方案。
> 
> 

## 产品 / 数据现状

### 当前现状

- Nothing 历代产品均未支持前后双录，属于品牌谱系中的功能性空白。

- 前后双录已成为苹果、三星、OPPO、vivo、Honor、Moto 等主流厂商的常见能力，在 Android 中、高端机型中普及。

- 行业不是维持现状，而是在持续升级该能力。例如 vivo X300 系列已进一步支持更高规格与更强导出能力。

### 已有方案

- 行业内已有成熟形态，主流方案通常支持前后摄同步录制、实时预览、画中画或分屏布局。

- 竞品方向大致分为两类：

    - 规格领先型：4K、HDR、多镜头选择、双文件导出。

    - 玩法/交互型：布局切换、小窗拖动、窗口大小调整等。

### 已知问题

- 25131 在用户对比、媒体评测和销售话术中，可能被直接识别为缺少行业常见能力。

- 单路录制无法同时记录“眼前发生的事”和“我作为在场者的反应”，用户需要在两者之间二选一，或者通过多段录制补救，无法完整还原时刻关系。

- 当前中端价位竞品虽已具备前后双录，但不少仍停留在“有但体验一般”的水平，存在体验差异化窗口。

### 数据结论

- 印度用户调研显示，约 53% 用户认为该功能是必要或加分项，其中创作者、vlogger 群体需求明显更强。

- 约 36% 用户认为功能有用但场景较窄，主要集中在博主、直播、游戏等人群。

- 仅 11% 用户认为无需求。

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MzJmNDUxOTM4MDRiNzAyZGM4NjY4Yzk0OWU5MTc4ZWZfYzIxZjk4NzI1NDE2Y2UyMzU1MjUzZmZiMDc0ZTkyYTRfSUQ6NzYzMDc1NzQzMzkyMDkzMzU5NV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MDVhYTMzYTE1YTU1MGEyMzM0MTUzNWQ5NDNhMjZhODZfZjgzMzYyNTUxYzc2OTQyNjFjYzdiN2Q4OTg5NmE3YzZfSUQ6NzYzMDc1NzQzNDM5MDcyODQxMV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

*数据来源：Kantar × Nothing 印度用户调研（n=28）。*

### 竞品 / 对标情况

- iPhone 17 将前后双录作为重要功能推出，并在小红书、Instagram 等平台带动大量用户自发分享。

- vivo X300 系列将能力升级为更高规格方案，支持 4K、双文件独立保存，表明头部厂商正从“补齐”走向“升级”。

- 国产中端竞品多数已具备基础前后双录，但在画质、规格或交互细节上仍有限。

- 竞品功能维度对比表

## 用户调研

- 调研方式：印度用户调研，结合竞品社媒案例观察与定性访谈结论。

- 样本情况：Kantar × Nothing 印度用户调研。

- 核心结论：

    - 创作者、vlogger、数码爱好者为高价值高感知人群。

    - Nothing 用户决策中存在明显“专家把关效应”，意见领袖与数码爱好者对品牌认知影响大。

    - 双录功能既能服务真实创作与生活记录需求，也能作为品牌“懂行”与“有思考”的感知载体。

    - 在大型演出、体育赛事、旅行、聚会、宠物/家庭记录等场景中，该功能具备明确使用价值。

- 用户典型反馈

    - 用户希望“同时分享眼前的世界与作为在场者的自己”。

    - 前后双录激活的是“我在场”的记录与分享心理，而不只是多一种拍摄方式。

    - 即便不是高频功能，它也具有明显的“高级感”和“iPhone 感”认知，可为品牌形象加分。

- 典型场景

    - Nothing 印度核心用户以**上进型年轻人**为主——**他们渴望被看见、社交分享意愿强、将手机视为身份表达的载体而非纯粹工具**。这种心理状态与双录的核心价值高度契合：双录不只是多一种拍摄方式，而是"我在场"这件事被完整记录和分享的技术支撑。

    这一心理在以下场景中集中显现：

    - **大型演出 / 体育赛事**：IPL、演唱会——上进型年轻用户最高密度的"我在现场"时刻，记录精彩的同时记录自己作为在场者的激动；Nothing × RCB 合作提供直接的营销落地窗口

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZjdiZDMxZTdkNmFhOTRjYjRlMTY0MTUwNDFhNmUyOTNfZjhkYjMwZmFjODNmMTc1NGE3YzEyMzRkODVjZDZjOTBfSUQ6NzYzMDc1ODczOTU5MDY4MDI4M18xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZjYwYjJmZWRjMTg0NzA1OGRmMmVmNDQ4OTFlMTViMzFfY2EwNmExNjliOWJjZGNmYWU4ODQyNjRmMWYxYzcwNTdfSUQ6NzYzMDc1ODczNzU2OTM4NjIxM18xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZWZhNzgxYjEwNTM0NWY1NmJmM2Q4MDk0ZjI4NjhiYWFfMGNhMjJmMTEwZmE2M2VjZDQ0ZjIwNDA0ZTk0MmJkNDdfSUQ6NzYzMDc1ODczOTU5MDY5NjY2N18xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

    - **旅行打卡 / 街头探索**：内容创作型用户的高频分享场景，双录让"我身处其中"的存在感得以完整呈现

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=ZmEwZjJmM2FhOWI1YTg3OWJlM2NhYjNjMDljYjNmMjJfMGQzY2ZiNDI1NzcwMTYxMjU1NzRiM2I1NDFjOGQzODFfSUQ6NzYzMDc1ODczODkyNTM1ODgyMV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=Zjk4ZDAwMmQ5ODgxYzUxZmIxODRjZDhlNjY2NDdkYWFfMWE0ZmJhZTUyNjNkYTgxYTFjZjZiZWUyN2UzM2ZhZDlfSUQ6NzYzMDc1ODczOTUzMTg3ODExMl8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=MGU2ODlkYTZkNGI5MzE0ZmI4OTU4YTAzZGRmN2U2OTJfZmNiN2M0NmRlZWEyZWI5MDlhNWUyNTEzMDdhYzFjMThfSUQ6NzYzMDc1ODczNzI3NTY1Mzg1NV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NTUyNmU4MzU0ZjczNTI2MmQ5YmMyZGIzMzlmNGE2NWNfYWIzMjQ4NjhlMzkwOWVmYmExZDFjM2FlNTYwM2E5YmRfSUQ6NzYzMDc1ODczNzU1NjY1NTgzN18xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

    - **朋友聚会 / 夜晚社交**：印度用户晚八点后社交最活跃，双录降低了"既想录氛围又想录自己反应"的操作门槛

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NWVmMzVlNzdmNzhiZjZiNWJmNzkwY2ExNDA3NTU5ZDhfYjA3NTNlNjgyOTgyZDMzNTgzMzRjMGU5NGUxOGIwYTVfSUQ6NzYzMDc1ODczODkyNTM3NTIwNV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

    - **家人 / 宠物互动**：孩子的第一次、宠物的可爱瞬间——情感记录场景，使用频率低但情感价值高，也是家庭购机决策者能直接感知到价值的场景

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=NjhmN2QwY2Y0ZTQ0ODA2MTU1NjE1NzNlMzkzNTNlNjJfNzY1NTRlNjZlMWYyNWRkMThlNTQ5NjczMjdiMGNhNjBfSUQ6NzYzMDc1ODczNzk0NjUxMzExOV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YTQyMWM1MmQ1NGU4N2U5ZTQzYWIyN2YwYTJlNWE4YmZfYjA3NmM5MmY0YzI4Njg2YzE1ZTBjNTNkOTA5ZWVhNjBfSUQ6NzYzMDc1ODczNjIwNjIyMTAyOV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

---

# 需求目标

> 只回答一个问题：这次做完后，要得到什么结果。直接写结果，不重复背景，不展开实现方式。
> 
> 

- 在 25131 上引入前后双录功能，为核心用户提供“同时记录眼前内容与在场者自身反应”的完整解决方案。

- 补齐 Nothing 在同档位产品中的前后双录能力缺位，避免在对比与评测中被识别为明显短板。

- 通过入口设计、交互逻辑与细节处理体现品牌对创作者和数码爱好者友好的产品思考。

- 为后续更高规格迭代（如 4K、HLG、双文件导出、更多镜头组合）预留升级路径。

---

# 需求范围

> 写清做什么，不做什么。
> 
> 

## 范围内

- 在 25131 上支持视频前后双录模式。

- 支持前后摄同步录制与实时预览。

- 支持两种布局：画中画、上下均分。

- 支持小窗拖动。

- 支持录制前选择后置主摄或超广。

- 支持录制中拍照（截图）、暂停/继续、前后主副画面互换。

- 支持在画中画模式下调整主画面曝光，在均分模式下分别调整两个画面曝光。

- 支持录制结果以单文件保存，并在命名规则与相册详情中体现 DUAL 标识。

- 支持关键 UI 动画，包括布局切换、镜头切换、主副互换的模糊转场。

## 范围外（需求不包含的内容）

- 4K 分辨率。

- HLG。

- 双文件分开保存。

- 小窗大小两档切换。

- 录制中切换画中画/均分布局。

- 再前后同录模式下的，滤镜，tuning 功能使用

- Log 支持、专业控制、AI 实时字幕、美颜、第三方相机直接调用等后续增强能力。 

---

# 功能设计

> 按功能点写，每个功能点把范围、交互、逻辑、限制放在一起。
> 
> 

## 新增 “前后双录” 模式

### 功能支持范围

- 模式范围：视频前后双录模式

- 摄像头范围：前摄 \+ 后摄（后摄录制前可选主摄/超广）

- 焦段范围： 

    - 超广：0\.6x \- 2x（同非 SAT 规格）

    - 主摄：1x \- 7x （同非 SAT 规格）

- 地区范围：全部

- 项目差异：当前定义面向 25131；26111 后续能力另行定义

### 功能详细说明

#### 功能入口

- 入口位于相机底部模式滑动栏【更多（More）】菜单的最后一项。

- 进入/退出双录模式的转场动画与其他模式一致，采用高斯模糊转场。

- 用户进入前后双录模式后，可同时预览前后摄画面。

- 后摄镜头在录制前可在变焦条中选择主摄/超广；录制开始后不可切换后摄焦段。

#### 开始录制

- 录制过程中，通过与普通拍照/视频模式相同的前后摄切换按钮，可切换前后摄在主窗口与画中画/均分位置之间的主副关系（即主副互换）。

- 后置的变焦范围，根据预览选择的摄像头而定，主摄：1x \- 7x。

- 录制中支持截图、暂停/继续操作。时间、toast 等 其他提示规则与普通均视频一致。

#### 布局设计

- 支持两种布局，分别为 画中画 与 上下分屏。默认为 画中画

- 主副画面互换时提供模糊转场动画，降低视觉跳变。

- 布局切换时提供模糊转场动画。

- 布局切换时，通过 toast 提示当前布局名称："Picture\-in\-Picture" 或 "Split Screen"。

**画中画**

- 后摄为主画面，前摄为小窗，默认位于右上角

- 用户切换前后置，则主画面为前置，小窗为后置

- 小窗尺寸：360\*480

- 宽高比：3:4

- 圆角：13dp

- 轻微阴影（elevation 4\-8dp）

**上下均分**

- 前后摄画面各占屏幕二分之一，上下排列

- 后置开始录制，后置为下，前置为上；用户切换前后置，则后置为上，前置为下

- 布局切换入口：顶部工具栏中的布局切换按钮，点击后在画中画与均分之间切换；仅在录制开始前可操作，录制中不支持切换布局

- 支持小窗随时自由拖动，录制过程中同样支持拖动

- 支持录制中前后摄主副位置互换（使用与普通模式一致的前后摄切换按钮触发）

#### 小窗拖动交互（仅画中画）

- 触发方式：触碰整个小窗区域即可触发拖动，无需长按。

- 拖动动画：支持非线性动画，带有一定延迟跟手效果，提升流畅感。

- 位置约束：小窗不可拖出屏幕边界；可在屏幕范围内任意位置悬停，不自动吸附到四个角。

### 限制与说明

- 当前不支持 4K、HLG、双文件独立保存。

- 录制中不支持切换布局（画中画 ↔ 均分），开始录制后，入口隐藏

- 当前版本不支持双文件保存，录制结果以单文件形式保存。

- 音频录制方案（麦克风策略与音轨合成方式）：与当前普通录像一致

- 具体入口设计与界面示意以设计稿为准。

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YjE4NDhjNTY1Mzg1NzdmMWQ3ZWNiNmUyYjVjMjIzMzRfN2UxOTdhZDM2ZTJmMjhmMTE3YzQ1NjYyZjNjZTQ3ZDVfSUQ6NzY0NDE1MTY4MzUwOTM1ODMwOV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

## 文件与相册标识

### 功能详细说明

- 录制结果合并为单文件保存。

- 命名规则增加 DUAL 后缀：`VID_YYYYMMDD_HHMMSSMMM_DUAL.mp4`

- 相册详情页中增加 DUAL Tag，帮助用户识别素材来源。

![Image](https://internal-api-drive-stream-sg.larksuite.com/space/api/box/stream/download/authcode/?code=YTI4YzI5ZDJjN2NhMzM3NjdkNmY5NzlmOThiZTIwZjRfNTUxM2RiMTMyNTJhZmExNWI1N2ZkMWMzYjllY2YxNDBfSUQ6NzYzMTUxNjgzMTg0OTEzOTkzNV8xNzgxMDc3Nzc3OjE3ODExNjQxNzdfVjM)

### 限制与说明

- 当前不支持双文件分开保存。

## 输出规格与录制策略

### 视频输出规格

- 参数：锁定为1080P 30FPS，不可更改

    - 比例：16:9

    - 分辨率：1080\*1920

- 编码：与普通视频一致

- 录制形式：当前平台限制下，为预览画面的录屏

- 防抖等级：应用为预览等级的防抖

### 录像效果策略

- 前后摄各自均与对应摄像头的普通录像策略保持一致，不做额外处理。

### 录音策略

- 与当前普通录像一致（可同时收到前后声音）

## 功能互斥表

||**FUNCTION**|**25131 Dual\-View Mode**|**不支持原因**|
|---|---|---|---|
|**Toolbar**<br>|Flash|✅||
||HDR|❌|技术不支持|
||Filter|❌|本期范围外|
||Tunning|❌|本期范围外|
||Grid|✅||
||Rec\.light|✅||
||Glyph Mirror|✅||
||4K|❌|技术不支持|
||60FPS|❌|技术不支持|
|**Setting**<br>|Power safing recording|✅||
||Auto FPS|✅||
||level|✅||

## 5\.6 Feature List

|分类||需求描述|25131 预期|当前开发落地|26111 落地|
|---|---|---|---|---|---|
|规格<br>|视频规格<br>|分辨率：1080P|✅|✅||
|||分辨率：4K|❌|❌||
|||帧率：30fps|✅|✅||
|||HLG|❌|❌||
||文件规格<br>|合并为单文件保存|✅|✅||
|||双文件分开保存|❌|❌||
|||命名规则：增加DUAL后缀|✅|❌||
|||[相册详情中添加“DUAL”Tag](https://nothing-tech.sg.larksuite.com/wiki/Okxsws282iq5cckFGH1lrrT3gJJ#share-BqUxdYBujorsJoxMzrvl4Qo9gUd)|✅|❌||
|功能|布局<br>[草图](https://nothing-tech.sg.larksuite.com/wiki/Okxsws282iq5cckFGH1lrrT3gJJ#share-GKvWdog0Yo8D9exSjsDlTWQug8b)<br>|支持2个布局，包括画中画和上下均分|✅|✅||
|||小窗支持大小两档切换|❌|❌||
|||小窗位置随时可自由拖动|✅|✅||
||镜头选择|后置录制前可选主摄/超广（录制时不可调整）<br>变焦范围：超广：0\.6x\-2x；主摄1x\-5x|✅|❌暂做不了||
||更多|支持滤镜（合并套用）|❌|✅||
|||支持Tuning（合并套用）|❌|✅||
||录制中操作<br>|拍照（截图）|✅|✅||
|||暂停/继续|✅|✅||
|||前后摄互换主副位置|❌|❌||
|||切换画中画/均分布局|❌|❌||
|||画中画模式调整主画面曝光|✅|✅||
|||均分模式分别调整两个画面曝光|✅|❌仅可调后置||
|UI动画|模糊转场|切换画中画/均分布局时|✅|❌澄清无需||
|||切换超广角/主摄镜头时|✅|❌澄清无需||
|||切换前后摄主副位置时|✅|❌澄清无需||
||拖拽动画|拖拽小窗动画|✅|❌||
||Preset|Preset创建页面可选 前后双录 模式|✅|||

# 6\. 关键依赖与约束

写会直接影响实现和测试的关键依赖。没有结论就标记待确认。

## 硬件依赖

- 需确认 25131 平台在双路同步录制、实时预览、曝光控制与稳定功耗下的能力边界。

## 平台依赖

- 需依赖 Camera App 模式扩展、预览与录制链路支持。

- 相册详情页需支持新增 DUAL Tag 展示。

## 算法依赖

- 需确认前后双录在曝光控制、画面一致性与画面切换体验上的算法支持边界。

## 性能 / 功耗 / 存储约束

- 双路同步录制会显著增加功耗、热量与系统资源占用。

- 需要重点评估长时间录制稳定性、存储占用、后台调度与异常降级策略。

## 6\.1 技术依赖

- 双摄同步预览与录制链路

- 小窗拖动与布局渲染能力

- 录制中截图能力

- 主副位置互换时的转场动画能力

- 录制结果命名与相册元数据展示支持

## 6\.2 产品与配置依赖

- 开关 / 配置项：待确认

- 地区差异：印度优先，其他地区是否默认开放待确认

- 项目差异：25131 当前版本落地；26111 Pro / Ultra 后续再评估

- 素材 / 文案依赖：需求词条、多语言文案、营销素材待补充

# 7\. 效果定义与验收标准

> 写清怎么判断这次需求是否达成。
> 
> 

## 7\.1 预期效果

- 用户可在 25131 上稳定使用前后双录，完成同步记录“眼前内容 \+ 自身反应”。

- 功能在典型场景下具备可用性，包括演出/体育赛事、旅行、聚会、宠物/家庭互动等。

- 在用户感知上，前后双录不只是“补齐功能”，而是体现 Nothing 对创作与表达场景理解的能力。

## 7\.2 验收口径

- 对比机：待确认（建议覆盖 iPhone、vivo、OPPO 同级对标机）

- 对比版本：待确认

- 场景范围：复用前后置视频场景库

- 核心指标：

    - 前后摄同步录制成功率

    - 录制稳定性

    - 小窗拖动与主副互换可用性

    - 曝光调节能力符合设计预期

    - 单文件保存、DUAL 命名与相册 Tag 展示正确

- 判定方式：按功能清单、典型场景与异常场景进行测试验证，详细测试口径待测试团队补充

# 8\. 词条定义

|应用场景|中文词条|英文词条|备注|
|---|---|---|---|
|模式名称|前后双录|Dual\-View video|模式名|
|布局名称|画中画|Picture\-in\-picture|用户可见文案不建议直接写 PIP|
|布局名称|均分|Split screen|比 Split Mode 更直观|

# 9\. 埋点

## 9\.1 埋点目标

- 记录前后双录拍摄时实际使用的布局类型，为后续评估布局偏好提供依据。

- 不新增点击类埋点，仅在拍摄事件中通过 `video_info` 回传。

## 9\.2 埋点定义

- 不对布局切换按钮点击、主副切换点击、小窗拖动等交互单独上报埋点。

- 在视频拍摄相关事件上报时，于 `video_info` 中新增布局字段。

- 该字段仅在前后双录模式下生效，非前后双录模式不回传或置空。

|event\_name|key|event\_note|string\_value|value\_note|默认值|备注|
|---|---|---|---|---|---|---|
|NTCamera<br>|video\_info\.layout\_type|前后双录拍摄时记录当前布局类型|pip / split|`pip` 表示画中画，`split` 表示均分|\-|仅前后双录模式生效|

# 10\. 项目计划与风险

进入排期后填写；早期阶段至少保留风险。

- 计划版本：待确认

- 预计交付时间：待确认

## 10\.1 项目计划

- 关键里程碑：需求评审、方案冻结、开发联调、测试验收、版本上线

- 责任团队：产品、开发、算法、测试、设计

## 10\.2 风险与兜底

- 风险项：

    - 双路录制带来的性能、功耗、发热风险

    - 机型资源限制导致的画质、帧率或稳定性妥协

    - 交互体验若不够顺滑，容易落入“有但不好用”

    - 若营销节奏与功能交付节奏错位，会削弱传播效果

- 影响：影响用户可用性、口碑、评测结果和营销叙事完整性

- 兜底方案：

    - 优先保证基础录制稳定性

    - 对高风险能力采取范围收敛策略

    - 明确将 4K / HLG / 双文件等能力转为后续迭代项



## 12\.1 原始资料

- Kantar × Nothing 印度用户调研（n=28）

- iPhone 17、vivo X300 等竞品公开信息与社媒案例

- RCB 合作相关场景与营销素材参考（待补充）

- 前后双录竞品功能维度分析表


