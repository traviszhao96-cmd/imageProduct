<!-- source: https://nothing-tech.sg.larksuite.com/docx/BIswd8SdhorzJJxIx7Kla2qZgEe | fetched: 2026-09-15 | revision: 1377 -->
# 【PRD】Camera 5.1 构图助手





> 文档状态：Draft v0.1  
> 
> 更新日期：2026-06-11  
> 
> 适用范围：相机 App 后置「拍照」模式  



---



## 1. 背景与目标



### 1.1 问题陈述



普通用户在后置拍照时，经常能识别「想拍什么」，但不确定手机该往哪个方向移动、主体应该占画面多大、是否需要拉近或拉远。结果容易出现主体偏小、画面歪斜、主体位置不佳、背景干扰过多等问题。



AI 构图助手希望在不打断拍照链路的前提下，基于实时场景识别和美学构图规则，给用户一个可执行的移动指引：把画面中的圆点移动到圆圈内，并在合适场景下自动调整变焦，使用户更容易得到一张构图更稳定、更好看的照片。



### 1.2 产品目标



- 降低普通用户拍出「构图明显不佳」照片的概率。
- 将抽象构图建议转化为可操作的手机移动指引。
- 在后置拍照模式中提供轻量、可随时开关的构图辅助能力。
- 在主体占比明显不合适的场景下，自动辅助变焦，减少用户手动判断焦段的成本。

### 1.3 目标用户与场景



- 目标用户：日常拍照用户、旅行/打卡用户、对构图有需求但不熟悉专业摄影规则的用户。
- 核心场景：建筑/城市、人物、食物、风景、花草/静物等后置拍照场景。
- 使用频率：[TBD — 需通过相机模式使用数据和用户研究确认]

---



## 2. 核心假设



| 假设 | 置信度 | 证伪条件 | 验证方式 |
|-|-|-|-|
| 我们相信「圆点移入圆圈」的引导方式能让普通用户更快理解如何移动手机，因为它把构图调整转化为明确的空间目标。 | Medium | 用户开启后仍不知道该如何移动，或引导完成率低于 [TBD]。 | 可用性测试、灰度埋点、访谈回放。 |
| 我们相信主体占比是自动变焦的主要判断依据，因为多数构图失败来自主体过小或过满。 | Medium | 自动变焦后用户取消率高，或变焦后照片留存/分享没有提升。 | A/B 实验、自动变焦触发后拍摄率、撤销率。 |
| 我们相信功能默认关闭、顶部工具栏常驻，能兼顾可发现性和预览干扰控制。 | High | 入口点击率过低，或用户误触/抱怨顶部工具栏拥挤。 | 入口点击率、开关留存、用户反馈。 |



---



## 3. 功能定义



### 3.1 功能名称



构图助手/  **Frame Assist**



### 3.2 一句话描述



在后置拍照模式中，构图助手通过场景识别、构图推荐、圆点/圆圈移动引导和必要时的自动变焦，帮助用户移动手机到更合适的拍摄角度。



### 3.3 范围



**In Scope**



- 后置「拍照」模式工具面板增加功能入口
- 功能默认关闭，用户需手动开启。
- 功能遵循5min记忆规则，5min后进入相机，则自动关闭
- 根据不同项目的摄像头配置，定义不同的生效果倍率：base4x以内生效,pro7x内生效-待更新https://nothing-tech.sg.larksuite.com/wiki/ZEJgwi1OiihpWSknPvUlWTDogkg
- 开启后实时检测拍摄场景和主体区域
- 基于场景与构图规则生成推荐构图目标

  1. 俯仰角引导：人像场景，若有俯仰角建议，则先出俯仰角引导
  2. 水平引导：通过「当前点」与「目标圈」引导用户移动手机。
  3. 根据主体占画面大小判断是否触发自动变焦
- 对齐成功后给出轻量反馈，允许用户按快门拍摄
- 功能可随时手动关闭或自动退出，关闭后预览页恢复普通拍照状态



**Out of Scope**





---



## 4. 关键需求

Demo:

<figure view-type="Preview"><source name="屏幕录制2026-06-23 21.01.32.mov" mime="video/quicktime" origin-height="1384.000000" origin-width="622.000000" size="6629888" token="JuMbbsU2EoEPVIxH2BTlSZoVgHb"/></figure>



### R1 · ~~顶部工具栏常驻入口~~ **入口在工具栏面板**



优先级：Must-have



后置拍照模式~~顶部工具栏~~ 面板展示 AI 构图助手入口。入口默认关闭，用户点击后开启；再次点击关闭。入口需有明确的开/关状态，不影响用户正常取景和拍摄。



*正常路径：* 用户进入后置拍照模式，点击工具栏面板展示 AI 构图助手图标；点击后图标进入开启态，预览画面出现构图引导。  

*边界：* 若当前模式不支持，则面板不展示



### R2 · 实时场景检测



优先级：Must-have



开启 AI 构图助手后，系统需实时识别当前拍摄场景、主体位置、主体大小、画面方向、水平线/垂直线等构图要素，并输出推荐构图目标。



*正常路径：* 用户移动手机时，系统持续更新场景与主体结果，并刷新目标圆圈位置。  

*边界：* 低光、遮挡、主体不明确、运动过快时，系统应降低引导频率或提示「寻找主体中」，避免频繁跳动。



### R3 · 构图推荐



优先级：Must-have



系统根据场景选择合适的构图策略，例如三分法、中心对称、水平线校正、引导线、留白、主体居中或黄金分割等。不同场景可优先使用不同策略。



*正常路径：* 建筑场景优先考虑垂直线稳定、对称/透视关系；人物场景优先考虑主体占比、头顶留白和三分线位置；风景场景优先考虑地平线位置和主体层次。  

*边界：* 若多个策略冲突，以主体清晰、主体占比合理、画面稳定优先。



### R4 · 俯仰角引导

人像场景，若有俯仰角建议，则先出俯仰角引导

手机向上旋转或向下旋转，角度：8 - 30

### R4 · 圆点移入圆圈引导



优先级：Must-have



预览画面中展示一个「当前圆点」和一个「目标圆圈」。当前圆点代表当前手机朝向/构图状态，目标圆圈代表推荐构图位置。用户通过移动手机，使圆点进入圆圈。



*正常路径：* 圆点与圆圈分离时，用户移动手机；距离缩短时给予轻量反馈；圆点进入圆圈后，显示对齐成功状态。  

*边界：* 若推荐目标变化过于频繁，应增加稳定阈值，避免圆圈跳动造成用户困惑。



### R5 · 自动变焦



优先级：Must-have



系统以主体占画面大小为主要判断依据，结合场景、当前焦段、可用镜头、画质风险和用户移动状态，判断是否触发自动变焦。自动变焦不是必然行为，仅在能明显提升构图时触发。



*正常路径：* 当主体过小且可通过拉近改善构图时，系统平滑切换至推荐焦段；当主体过满且可通过拉远改善构图时，系统回退到更合适焦段。  

*边界：* 若自动变焦可能导致画质明显下降、镜头切换突兀、主体丢失或用户正在手动变焦，则不触发或停止自动变焦。

<cite doc-id="ZEJgwi1OiihpWSknPvUlWTDogkg" file-type="wiki" title="构图生效和推荐倍率表" type="doc"></cite>



### R6 · 对齐成功反馈



优先级：Must-have



圆点进入圆圈并保持稳定达到阈值后，系统给出成功反馈，例如圆圈高亮、短文案提示或轻量动效。成功反馈不自动拍照，用户仍需主动点击快门。



*正常路径：* 圆点进入圆圈并稳定后，显示「构图已就绪」类反馈；用户点击快门拍摄。  

*边界：* 若用户继续移动导致偏离，反馈取消并回到引导中状态。



### R7 · 可随时退出



优先级：Must-have



用户可通过顶部入口关闭 AI 构图助手。关闭后移除所有构图引导和自动变焦控制，保留当前焦段策略

*正常路径：* 用户点击开启态图标，功能关闭，预览回到普通拍照。  

*边界：* 自动变焦进行中关闭时，应立即停止后续自动变焦，避免用户感知到不可控变化。





---



## 6. 交互流程 



1. 开启和检测构图

   1. 用户进入相机 App 后置拍照模式。
   2. 点击工具栏图标展开面板，有「 AI 构图助手」入口，默认为关闭态。
   3. 用户点击开关，顶部工具栏有功能图标，AI 构图助手开启，同时顶部栏显示该图标
   
      1. 首次进入 Toast 提示（首次 Toast 时间 5s）：  
      Frame Assist is on. Works better at 1x–4x for portraits, landscapes, and architecture. （26111）  
      Frame Assist is on. Works better at 1x–7x for portraits, landscapes, and architecture.（26121）
      2. 非首次进入 Toast 提示：  
      Frame Assist is on.
      3. 算法在1s后开始检测
   4. 构图引导与人脸框不互斥
   
      ![The image shows three screenshots of a camera interface. The first screenshot displays a landscape photo with a rocky cliff and the 4:3 aspect ratio indicator. The second screenshot shows the top toolbar with various icons, including "Frame Assist" highlighted in red. The third screenshot has a Toast message "Frame Assist is on. Hold steady for framing" at the top, with the landscape photo below. This corresponds to the context describing the interaction flow where users click the switch to activate the AI构图助手, and the first Toast appears after 5 seconds.](https://feishu.cn/file/AXRRbl4QJoPRrdxqi8tlhrXygfb)





1. 俯仰角引导（仅人像场景）

   1. 向上旋转手机引导：Tilt your phone up for a better shot

    向下旋转手机引导：Tilt your phone down for a better shot

1. 调整成功：Angle adjusted
2. 引导为持续状态引导，直到进入下一个状态

![The image shows two screenshots of a camera app interface. The left screenshot displays a rocky coastal scene with a prompt "Adjust the angle to straighten" and a white triangular guide in the center. The right screenshot shows the same scene with the prompt "Angle adjusted" and a yellow square guide in the center. Both screenshots have a 4:3 aspect ratio, with camera mode options like "CONTRAST", "PHOTO", and "VIDEO" at the bottom, and a timestamp "20:49:03" at the bottom left. This image corresponds to the "6.交互流程" section, illustrating the "Angle adjusted" step in the interaction flow.](https://feishu.cn/file/DzN0bqTttozDSVxTBI1l2RIbgOe)



1. 移动引导和自动zoom

   1. 移动引导：Move the frame to align with the guide
   2. 对齐成功：中心点和目标点对齐稳定10帧后再触发变焦
   3. zoom:zooming（ratio返回为1.0的情况下，即表示不需要变焦，该情况下不toast zooming）
   4. 构图完成：Composition ready.Tap to shoot



![The image shows five consecutive screenshots of a mobile phone interface during the Camera 5.1构图助手's interaction process. The first screenshot displays a rocky landscape with a horizontal guide line. The second shows the frame being moved to align with the guide. The third indicates "Angle adjusted" with a yellow center point. The fourth has "Zooming" text and a yellow center point, and the fifth shows "Composition ready. Tap to shoot" with a yellow center point. These steps correspond to the context describing the mobile guide and zoom features, including moving the frame, aligning with the guide, zooming, and completing the composition.](https://feishu.cn/file/XWBhbTZZioilLtxp55tlBkp6gsd)





1. 拍摄

   1. 点击快门进行拍摄，则将引导元素全部去掉
2. 自动退出构图

   1. 若在引导过程中或完成构图，手动zoom或切换模式，则取消当前构图结果
   2. 若画面移动距离较大（要有一个稳定时间）或~~目标移出画面（构图完成后不会有了）~~，则自动退出本次构图（停留在当前zoom），下次自动构图将在2s后~~且手机稳定1s后进行~~
   3. 用户构图完成后点击拍摄，不应在当前位置继续重复构图，应在用户移动画面（画面进入不稳定状态）后退出本次构图，下次构图触发逻辑同不稳定状态逻辑（拍完后不保持黄色框）
   4. toast提示：Scene changed. Start framing again.
3. 手动关闭构图按钮

   1. Toast 提示：Frame assist is off（非手动关闭不用弹 Toast）
   2. 保留在当前倍率





1. 特殊情况：推荐构图跟当前构图一样（特殊情况返回值见文案与词条）

   1. 当前画面无构图推荐，弹出 Toast：No further composition suggestions.
   2. 当前已是最佳构图，弹出 Toast：Best composition. No further suggestions.
   3. 算法寻找构图超时（5s）未返回结果，按超时状态处理，弹出 Toast：No further composition suggestions.
   4. Toast 持续时间：3s
   5. Toast  结束 后2s,再开始重新检测

![The image shows a smartphone screen displaying the Camera 5.1 app interface. The screen features a landscape photo of a rocky cliff by the sea. At the top, there is a message "Best composition. No further suggestions." Below the photo, there are zoom options (0.6, 1x, 2, 3.5, 7) and a shutter button. At the bottom, there are mode options: PORTRAIT, PHOTO (highlighted in red), and VIDEO, along with a flash icon and a circular arrow icon. The aspect ratio indicator "4:3" is at the top left corner.](https://feishu.cn/file/FovQb9G3ioyBdGxa1Wol6rfEg0f)





---



## 8. 状态设计

|  |  |  |  |
|-|-|-|-|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |



---



## 9. 文案与词条

<table><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><td>场景</td><td>中文词条</td><td>英文词条</td><td>备注</td></tr><tr><td>功能名称</td><td>构图助手</td><td>Frame Assist</td><td></td></tr><tr><td>开启提示</td><td>构图助手已开启</td><td>Frame Assist is on</td><td></td></tr><tr><td rowspan="2">首次开启提示</td><td>构图助手已开启，1x - 4x 拍摄人像、风光、建筑时效果更佳</td><td>Frame Assist is on. Works better at 1x–4x for portraits, landscapes, and architecture.</td><td>26111</td></tr><tr><td>构图助手已开启，1x - 7x 拍摄人像、风光、建筑时效果更佳</td><td>Frame Assist is on. Works better at 1x–7x for portraits, landscapes, and architecture.</td><td>26121</td></tr><tr><td>稳定画面提示</td><td>请保持画面稳定</td><td>Hold steady for framing</td><td>算法返回值0</td></tr><tr><td>俯仰角引导</td><td>请将手机向上倾斜</td><td>Tilt your phone up for a better shot</td><td>算法返回值3</td></tr><tr><td>俯仰角引导</td><td>请将手机向下倾斜</td><td>Tilt your phone down for a better shot</td><td>算法返回值4</td></tr><tr><td>俯仰角引导</td><td>角度调整完成</td><td>Angle adjusted </td><td></td></tr><tr><td>移动引导</td><td>移动画面与引导框对齐</td><td>Move the frame to align with the guide</td><td>算法返回值1、5</td></tr><tr><td>自动zoom</td><td>正在变焦</td><td>zooming</td><td>算法返回值2</td></tr><tr><td>构图完成</td><td>构图完成，点击拍摄</td><td>Composition ready. Tap to shoot.</td><td></td></tr><tr><td>画面移动距离过大退出本次构图</td><td>画面发生变化，重新开始构图</td><td>Scene changed. Start framing again.</td><td></td></tr><tr><td>关闭提示</td><td>构图助手已关闭</td><td>Frame assist is off</td><td>5min自动关闭不toast</td></tr><tr><td rowspan="2" vertical-align="middle">无构图结果情况</td><td>当前画面无构图推荐</td><td>No further composition suggestions.</td><td>算法返回值7、9、10、11、12</td></tr><tr><td>当前已是最佳构图</td><td>Best composition. No further suggestions.</td><td>算法返回值6、8</td></tr></tbody></table>

算法返回值：

<figure view-type="Preview"><source name="BSTAIPrompt_return_values.xlsx" mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" size="15368" token="Wk4ibDWY0olEEixtJPUl35BogSb"/></figure>



---



## 10. 指标与验收



### 10.1 成功指标



| 指标 | 基线 | 目标 | 测量方式 |
|-|-|-|-|
| AI 构图助手开启率 | [TBD] | [TBD] | 入口曝光到开启转化 |
| 开启后完成拍摄率 | [TBD] | [TBD] | 开启后 N 秒内拍摄 |
| 构图引导完成率 | [TBD] | [TBD] | 圆点进入圆圈并稳定 |
| 自动变焦后拍摄率 | [TBD] | [TBD] | 自动变焦触发后拍摄 |
| 自动变焦撤销/手动覆盖率 | [TBD] | 越低越好，[TBD] | 自动变焦后用户手动变焦 |
| 用户满意度 | [TBD] | [TBD] | 灰度问卷/访谈 |



### 10.2 验收条件



- [ ] 后置拍照模式顶部工具栏可看到 AI 构图助手入口，默认关闭。

- [ ] 点击入口后可进入开启态，并展示构图引导。

- [ ] 关闭后所有预览叠加消失，不再触发自动变焦。

- [ ] 支持至少 [TBD] 类首版场景识别。

- [ ] 圆点/圆圈引导在正常光照、稳定手持条件下可完成对齐。

- [ ] 自动变焦只在主体占比不合理且置信度满足条件时触发。

- [ ] 用户手动变焦后，AI 自动变焦在 [TBD] 秒内不再次抢占。

- [ ] 低置信度、主体丢失、低光等场景有明确兜底，不出现频繁跳动。

---



## 11. 关键依赖



| 依赖项 | 负责方 | 状态 | 风险 |
|-|-|-|-|
| 实时场景识别模型 | 算法 | [TBD] | 场景置信度不足会影响引导稳定性 |
| 主体检测与主体占比计算 | 算法 | [TBD] | 多主体和遮挡场景可能误判 |
| 构图策略引擎 | 算法/相机 | [TBD] | 策略冲突时需有优先级 |
| 相机预览层叠加 UI | 相机客户端 | [TBD] | 需避免影响现有对焦/曝光交互 |
| 自动变焦控制 | 相机框架/算法 | [TBD] | 需处理镜头切换、画质、手动覆盖 |
| UX 视觉与动效 | UX | [TBD] | 引导必须清晰且不遮挡取景 |
| 性能与功耗评估 | 性能/平台 | [TBD] | 实时检测可能增加功耗与发热 |



---



## 12. 风险与兜底



| 风险 | 影响 | 兜底 |
|-|-|-|
| 圆圈频繁跳动 | 用户不信任引导 | 增加目标稳定阈值和切换冷却时间 |
| 自动变焦抢夺控制权 | 用户感到不可控 | 用户手动变焦后暂停自动变焦 |
| 场景识别错误 | 推荐构图不合理 | 低置信度时不展示具体引导 |
| 预览 UI 遮挡主体 | 影响拍照 | 圆圈/参考线透明度和位置需避开核心主体 |
| 性能/功耗上升 | 影响相机体验 | 降低检测频率，关闭态不运行算法 |
| 与现有对焦/曝光冲突 | 影响基础拍照 | 优先保证对焦、曝光、快门响应 |



---



## 13. 埋点建议



> 仅作为首版建议，最终需由相机埋点负责人确认。



| event_name | key | key_description | parameter_value | 说明 |
|-|-|-|-|-|
| NTCamera | ai_composition_action | AI 构图助手行为 | open / close / shoot | 用户开启、关闭或开启后拍摄 |
| NTCamera | scene_type | 识别场景 | person / building / landscape / food / still_life / unknown | 开启后拍摄时上报最终场景 |
| NTCamera | guide_result | 引导结果 | aligned / not_aligned / unavailable | 开启后拍摄时上报最终状态 |
| NTCamera | auto_zoom_triggered | 是否触发自动变焦 | true / false | 开启后拍摄时上报 |
| NTCamera | final_zoom_ratio | 最终焦段 | number | 开启后拍摄时上报 |













## 正式设计稿（Camera 5.1）

[AI frame assist](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=1362-14015&p=f)