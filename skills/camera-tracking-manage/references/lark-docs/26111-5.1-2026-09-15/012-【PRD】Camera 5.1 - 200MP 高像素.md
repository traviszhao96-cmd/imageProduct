<!-- source: https://nothing-tech.sg.larksuite.com/docx/QCdGdErD6omTlzx9AtzlgxpIgWe | fetched: 2026-09-15 | revision: 1004 (埋点章节已于 rev 1013 对齐，见第八章) -->
<title>【PRD】Camera 5.1 - 高像素独立模式</title>

# 前言

<callout emoji="💡">
在空行输入“/高亮块” 插入高亮块，突出显示重点信息
</callout>

# 一、 版本信息

<grid>
<column width-ratio="0.333333">
<callout emoji="⏰">
版本号：1.1
</callout>
</column>
<column width-ratio="0.333333">
<callout emoji="📆">
20251023
</callout>
</column>
<column width-ratio="0.333333">
<callout emoji="👮">
审核人
</callout>
</column>
</grid>



# 二、 变更日志

| **时间** | **版本号** | **变更人** | **主要变更内容** |
|-|-|-|-|
| 2025/10/23 | 1.0 | Lia | 创建文档 |
| 2026/7/15 | 2.0 | Lia | 根据最新算法流程刷新交互 |
| 2026/7/30 | 2.1 | Lia | 增加环境亮度提示toast |
| 2026/9/3 | 2.2 | Lia | 26121 高像素不在顶部栏显示，改为toast提示 |



# 三、 需求背景

## 产品 / 数据现状

1. 26111 首次采用**200MP（HP5）**主摄，具备输出200MP高像素照片的能力，我们需要结合技术实现和用户拍摄需求制定高像素模式的功能交互



## 竞品分析

> 列出竞品对比的主要信息和关键结论，可输入 @ 在此附上详细的竞品分析报告并添加在【附录】中



<table><colgroup><col/><col/><col/><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>机型</td><td>摄像头</td><td>高像素-入口</td><td>记忆状态</td><td>快门体验</td><td>后处理</td><td>相册管理</td><td>特性功能</td></tr><tr><td>x300 pro</td><td>长焦</td><td><img name="1.jpeg" alt="The image shows a hand holding a smartphone displaying the camera interface. The top of the screen shows &#34;5000万像素&#34; (50 million pixels) and &#34;2亿像素&#34; (200 million pixels) with a yellow &#34;关闭&#34; (Close) button. Below, there are multiple camera modes including &#34;拍照&#34; (Take Photo), &#34;录像&#34; (Record Video), and &#34;人像&#34; (Portrait). The background features a display stand with a Vivo X30 Pro phone and some circular lights. This image is related to the竞品分析 (Competitor Analysis) section, likely illustrating a competitor&#39;s camera interface as part of the analysis." mime="image/jpeg" scale="0.675926" src="HCYYbewqAo0mMjxaXikl3yvMgMe"/></td><td>杀进程后恢复默认</td><td>快门动画3s+<figure view-type="Preview"><source name="20251030-204502.mp4" mime="video/mp4" origin-height="960.000000" origin-width="540.000000" size="2071705" token="T3SibsbVeo7fdPxxQGklU3oZgcd"/></figure><br/><a href="https://www.xiaohongshu.com/discovery/item/6a3e7c50000000001603ffec?source=webshare&amp;xhsshare=pc_web&amp;xsec_token=ABUxBABF2_SCSsmS_HQtRoyPOuBYme8RHS3usM6VU-N_Y=&amp;xsec_source=pc_share">vivox300pro 2亿像素这样是正常的吗 - 小红书</a></td><td>/</td><td>有单独的高像素相册<img name="image.png" alt="The image shows a hand holding a smartphone displaying the album interface. The screen shows various photo albums, including &#34;高像素&#34; (High Pixel), &#34;人像&#34; (Portrait), &#34;电影分镜&#34; (Film Storyboard), and others. There is a search bar at the top and a plus sign for adding albums. The context mentions that the product has a separate high pixel album and supports features like portrait mode and film storyboard automatic crop and stitch." mime="image/png" scale="1.000000" src="VZiAbu8VeoAJxOxQX0jluhCogZc"/></td><td>支持人像2亿、支持电影分镜自动裁图拼图<img name="image.png" alt="The image shows the camera interface of a product. At the top, there is a yellow bar labeled &#34;电影感三拼AI电影分镜&#34;. Below it, there are three options: &#34;无&#34;, &#34;电影感三拼&#34;, and &#34;胶片风双拼&#34;, with &#34;电影感三拼&#34; highlighted in yellow. At the bottom, there is an &#34;AI电影分镜&#34; label and a circular shutter button. This interface is related to the product&#39;s feature of supporting movie split automatic cropping and stitching, as mentioned in the context." mime="image/png" scale="0.109687" src="XbXpbtsO7oVcAsx1PgHlF77agvb"/></td></tr><tr><td>x90 pro</td><td colspan="7">https://www.xiaohongshu.com/discovery/item/68f24ca8000000000402a770?source=webshare&amp;xhsshare=pc_web&amp;xsec_token=ABFumpxspHsAdVdupdXEMFjj85Uia5_4uzfPKPdr-4JAg=&amp;xsec_source=pc_share</td></tr><tr><td>荣耀600</td><td>主摄</td><td><figure view-type="Preview"><source name="荣耀600 超清.mp4" mime="video/mp4" origin-height="960.000000" origin-width="540.000000" size="796368" token="Z38AbQ32JoKoV5xsOD9lRYuJgIf"/></figure></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Vivo 70 fe</td><td>主摄</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

# 四、 需求范围

> 可条理性地罗列需求范围或信息架构

1. 项目范围：对硬件。首上项项目为26111，后续200MP项目默认继承
2. 老项目回落：不支持回落，具体回落计划根据回落排期确

## 需求列表&需求单

<table><colgroup><col/><col/></colgroup><tbody><tr><td>需求名称</td><td>需求描述</td></tr><tr><td>26111-高像素独立模式</td><td><ol><li seq="1">首次进入高像素模式，对200MP的入口、使用体验做个说明</li><li>有200MP Ultra、200MP、50MP 3个选项</li><li>200MP Ultra预计取帧700ms;拍后需要在相机界面进行后处理，预计7s+</li><li>6G 有200MP Ultra选项，但不走50MP HDR算法，无需相机预览后处理</li></ol></td></tr><tr><td>26111-高像素独立模式</td><td><ol><li seq="1">取消拍照模式高像素入口，将高像素挪到独立高像素模式</li><li>只有50MP 默认选项，无需提供切换按钮</li><li>支持1x\3.5x点切</li><li>其他流程follow 25111 pro</li></ol></td></tr></tbody></table>

# 五、 功能详细说明

## 产品流程图（略）

> 将鼠标悬浮至下方空白图形模块，点击**编辑**，即可进入流程图创作你的产品流程图

## 交互原型图

> https://www.figma.com/design/4pThI4KHFBCQ8WWXGpujDr/Camera-Product-26111---26121---App-Prototype-Hub?node-id=62-178&t=ElaUfwMuFJVVRbxU-0

## 交互设计稿

<readonly-block href="https://www.figma.com/embed?embed_host=share&amp;url=https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=3272-31329&amp;t=8rSEX2SFQO3totFE-1" type="iframe"></readonly-block>

## 功能说明

### 入口说明

#### 26111

1. 进入高像素模式，弹出 on boarding 页面
2. 顶部工具栏中新增不同的像素模式选项，包括 50MP，200MP，200MP ULTRA
3. 200MP Ultra - 默认，点击切到200MP 标准，再次点击到50MP，以此轮巡
4. 均支持1x (50MP 是否支持2x点切待确认)

![The image shows three mobile phone screens related to the high-resolution camera mode. The left screen is the onboarding page with a photo of a spinning disc and the text "Higher photo quality" and "Try now". The middle screen displays a photo of tall buildings with the "200MP Ultra" label at the top. The right screen shows the settings panel with options like "200MP", "200MP Ultra", "200MP Standard", "50MP", "1x", "3.5x", "Flash", "Timer", "Exposure", "Quality", "Grid", "Watermark", "Stabilizer", and "Settings". This corresponds to the context about the high pixel independent mode, including the onboarding page, pixel mode options, and settings panel.](https://feishu.cn/file/UxdHb8FMioZnUexE8Hcl7XeDgFb)

#### 26121

将高像素模式从照片模式中的子功能独立出来，作为一个全新的模式

1. 无新增算法，将高像素模式从拍照工具栏移出，成立高像素独立模式
2. 仅支持成 50MP，不支持切换像素模式
3. 支持 1x\3.5x 点切
4. 顶部栏和工具面板无需展示高像素选项，每次进入该模式，toast提示：50MP,3s后消失

![The image shows the interface of the Camera 5.1 high pixel independent mode. At the top, there is a "50MP" label. Below the image of a snowy mountain, there is a "1x" and "3.5x" zoom slider. At the bottom, there are mode options: "ACTION", "HIGH-RES", "PORTRAIT", etc. This interface corresponds to the 26121 feature, which is to make high pixel mode an independent mode, only supporting 50MP, with 1x and 3.5x point cutting, and no high pixel options displayed in the top bar and tool panel, with a 50MP toast提示 appearing when entering the mode.](https://feishu.cn/file/P6NGb3q46oPzfFxfLFElqe1kgIf)



#### 50MP、200MP 功能兼容情况

| 像素 50MP/200MP/200MP ultra | 兼容情况 | 交互 |
|-|-|-|
| HDR | ✓ | 无特殊交互，同25111 |
| 夜景 | ✓ | 无特殊交互，同25111 |
| 滤镜 | ✓ | 无特殊交互，同25111 |
| tuning | ✓ | 无特殊交互，同25111 |
| 变焦 | × | 不支持变焦，变焦控件只有支持该像素的光变点，双指缩放时提示不可变焦，follow 25111 |
| Motion Photo | × | 互斥交互follow 25111 |
| 水印 | ✓ | 无特殊交互  <br/>vivo200亿支持边框等类型的水印 |
| preset | ✓ | 在创建preset的时候，像素支持选择12\50\200MP |





### 200MP ULTRA 拍摄交互

预计上帧700ms，预览会定住；拍后需要在相机进行后处理，冻结其他功能

1. 点击快门后，增加快门转圈动画，动效复用已有快门动画
2. 拍照过程中，快门不再响应，其他功能也不支持点击
3. 上帧后，进入相机后处理动画界面动效-snow-

   1. 过程预计7s+,有进度条和文案说明
   2. 隐藏其他功能按钮
   3. 若退出相机，则终止拍摄 ，界面：提示不要退出相机 ~~（或者能否在后台，再次进入相机还在处理界面？）~~
   4. 处理完成后，回到拍摄预览界面，缩图刷新完成，可继续拍摄

交互流程原型

![The image shows the interaction process of the 200MP ULTRA shooting mode in the Camera app. It starts with clicking the shutter button, followed by the shutter button capture animation. Then there is the camera interface processing animation, which displays "Camera processing in progress" and "Do not allow other functions, exit to suspend the current shooting content". After that, it shows the示意动画界面 (indicative animation interface) with a red circle, and finally, the processing is complete, the thumbnail is refreshed, and you can continue shooting.](https://feishu.cn/file/C013bWh7xoIVW3xSDVvlhdCjg5b)

设计稿

<grid><column width-ratio="0.500000"><img name="image.png" alt="The image shows a camera app interface with a black background and a photo of tall buildings. At the top left, there are &#34;50MP &amp; 200MP&#34; labels. The bottom has a white shutter button and mode options like &#34;EXPERT&#34;, &#34;HIGH-RES&#34;, and &#34;PORTRA&#34;. A yellow box on the right contains the text &#34;快门loading: 使用night mode已有的loading即可&#34;, which means &#34;Shutter loading: Use the existing loading of night mode&#34;. This relates to the context about 200MP ULTRA shooting interaction, specifically the shutter loading process." mime="image/png" scale="1.000000" src="QH8FbJmJVodJQFx8ab7lS0VugNb"/></column><column width-ratio="0.500000"><figure view-type="Preview"><source name="20260812120243_rec_.mp4" mime="video/mp4" origin-height="1736.000000" origin-width="780.000000" size="3456425" token="NSbSbo2D0oXSDzxuJKdlaSgIg4c"/></figure></column></grid>

### Toast 环境提示：new

在环境光线不足，会影响成片质量时，弹出 toast 提示用户在明亮环境使用。3.5s后自动消失，在单次使用该功能时只弹出一次

判断条件：进入高像素模式后，平台检测到 Lux Index > 280 时，判定为环境亮度不足并触发提示。Lux Index 由平台侧提供，不等同于物理照度 Lux。

toast 限制：每次进入该模式，只弹出1次。切换模式，或相机退出之后，达到触发亮度阈值再次提示

![The image shows a camera interface with a "High-res 200MP Ultra" label at the top. The main screen displays a photo of tall buildings with a "Recommended for bright lighting conditions" message. Below the photo, there are zoom options: 0.6, 1x, 2, 3.5, 7. At the bottom, there are mode options: EXPERT, HIGH-RES (highlighted in red), PORTRA, and a refresh icon. This interface is related to the high-pixel independent mode's Toast environment prompt, which triggers when Lux Index > 280 in dark environments.](https://feishu.cn/file/VWF7bOcJLoIlvvxKqRWlVHcsgLc)



### 附：高像素算法、tuning、底层策略文档<cite doc-id="CI1fwlRCfiQIekkK7iVlpq7Igb1" file-type="wiki" title="高像素模式策略" type="doc"></cite>



## 词条与文案规范

| 应用场景 | 中文词条 | 英文词条 |
|-|-|-|
| 首次弹窗标题 | 高像素 | High resolution |
| 首次弹窗正文 | 使用高像素模式捕捉更多细节。处理期间请保持设备稳定，并在光线充足的环境中拍摄，以获得最佳效果。 | Capture more detail with High-Resolution mode. Keep your device steady during processing, and shoot in good lighting for the best results. |
| 首次弹窗按钮 | 立即体验 | Try now |
| 对比标签 | 默认 / 高像素 | Default / High-res |
| 低照环境 Toast | 建议在光线充足的环境中拍摄 | Recommended for bright lighting conditions |
| 拍摄处理状态 | 当前设计无文案；仅展示加载/倒计时动效 | No copy in the current design; loading/countdown animation only |
| 高像素模式名称 | 高像素 | High-res |

# 七、 非功能需求

> 可以列举产品营销需求、运营需求、财务需求、法务需求、使用帮助、问题反馈等



# 八、 埋点

| event_name | key | label | 参数值 | 说明 |
|-|-|-|-|-|
| NTCamera | photo_info | high_res_spec | 50MP / 200MP / 200MP Ultra | 随成片上报实际像素档位；26111 支持三档，默认 200MP Ultra；26121 仅 50MP。 |
| NTCamera | photo_info | photoMode | high_res | 高像素独立模式；沿用 photoMode 枚举新增 high_res，与 PRD 词条 High-res 一致。 |
| NTCamera | high_res_guide | action | show / try_now | 高像素模式首次进入的 onboarding；引导展示 / 点击立即体验。 |
| NTCamera | high_res_capture | result | success / user_stop | 高像素拍摄结果；成片成功 / 快门转圈阶段再次按快门停止。中断的拍摄不产生成片，需独立上报；三档像素均适用，档位看 high_res_spec。 |
| NTCamera | photo_info | shot_algo | 实际算法名称 | 复用既有字段，记录高像素拍摄实际采用的算法。 |
| NTCamera | pef_info | capture2Photo | 毫秒数 | 复用既有字段，记录从点击快门到成片完成的耗时。 |

> 2026-09-15 本地对齐：以上为线上实际内容（整表重建为 7×5）。原模板行为「50MP\200MP\200MP Ultra使用率」「高像素模式拍摄时走的算法」。







# 附录

更新说明卡片为统一卡片样式：

<grid>
<column width-ratio="0.226829">
![The image shows a smartphone screen with the "HIGH-RES" mode interface. At the top, there's a description: "Capture richer image detail in High-Res mode. For best results, shoot in bright, well-lit scenes. Choose from three options based on your shooting needs, and switch between them from the top toolbar or the tools panel." Below is a photo of a snowy mountain. Underneath the photo, there are three options: "50MP Balanced detail" (good for everyday high-res photos with smaller file size), "200MP Maximum pixels" (best when you want more room to crop or capture fine details), and "200MP Ultra Enhanced clarity" (uses multi-frame processing for extra detail, best for bright, stable scenes).](https://feishu.cn/file/GuP9bunmWoG7W9xAcyglUxoLg2g)
</column>
<column width-ratio="0.773171">
主标题：HIGH-RES
正文：
Capture richer detail in High-Res mode.  Works best in bright scenes.
图片：1张
50MP 图标：
标题1:Balanced detail 
正文1:Good for everyday high-res photos with smaller file size.
标题2：Maximum pixels
正文2:Best when you want more room to crop or capture fine details.
标题3:Enhanced clarity
正文4:Uses multi-frame processing for extra detail. Best for bright, stable scenes.
</column>
</grid>