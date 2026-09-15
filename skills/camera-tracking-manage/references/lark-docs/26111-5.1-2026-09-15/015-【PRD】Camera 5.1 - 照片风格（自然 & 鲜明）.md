<!-- source: https://nothing-tech.sg.larksuite.com/docx/OmaEd4Re8oKF5WxHd5glNVjGgbd | fetched: 2026-09-15 | revision: 554 -->
# 【PRD】Camera 5.1 - 影像基调（Image Tone）— 自然 & 标准风格

文档状态: Draft | 版本: v0.2 | 更新: 2026-06-09 | 作者: Travis Zhao | 审核: [TBD]

## 变更日志

| 日期 | 版本 | 变更人 | 变更内容 |
|-|-|-|-|
| 2026-06-08 | v0.1 | Travis Zhao | 创建文档 |
| 2026-06-09 | v0.2 | Travis Zhao | 重命名(Standard→Standard)；首次弹窗改为选择卡片(Lia 7/9确认)；补充自然/标准风格定义；重写问题陈述为审美偏好分群；删除具体参数数值 |

## 1. 背景与目标

### 问题陈述

效果分析显示，大多数用户偏好高对比度、高饱和度的照片效果，但存在另一部分用户非常反感这种处理带来的不真实感。两类用户的偏好是审美取向差异，与拍摄场景无关。需要在不增加操作门槛的前提下，同时服务两类人群。

### 目标用户与场景

- 大多数用户：追求"出片感"，希望拍完即用，不关心参数
- 少数用户：追求真实感，反感过度处理，偏好保留细节层次的克制风格

使用频率：风格按需设置，设置后长期保持（低频）。

### 预期收益

[TBD — 需量化：风格使用率、照片分享率提升目标]

## 2. 功能定义

### 功能描述

功能名称：影像基调（Image Tone），提供自然和标准两种风格（Style）  
一句话描述：相机默认以「标准」风格输出照片；首次进入相机时通过 onboarding 引导选择，完成后可在 Camera settings > Photo > Image tone 中随时切换。

### 范围

In Scope:

- 两种内置风格：自然（Natural）、标准（Standard）。自然风格饱和度和对比度接近真实效果，保留细节层次。标准风格更加标准，饱和度和对比度略高，出片感更强。
- 标准为默认风格，开箱即用
- 首次进入相机时提供影像基调 onboarding；完成引导后，用户可在 Camera settings > Photo > Image tone 中随时切换自然 / 标准风格
- 风格基于底层 ISP 参数（tone mapping 等）实现
- 与滤镜及其他调色功能兼容
- Preset 中支持风格配置

**适用范围：**仅后置主摄与广角摄像头的 Photo、Portrait 模式支持自然 / 标准双风格。Image Tone 作为全局选择状态，Photo 与 Portrait 同步切换；其他镜头和模式维持当前默认调校，不区分双风格。

**Portrait 调校规则：**标准风格沿用现有 feature1、bokeh、bokeh2x 等 tuning；仅选择自然风格时，切换至 bokeh_natural、bokeh2x_natural。现有 tuningmode 在 Feature1 中已有 key 时，需增加对应的 \_Natural 分支。

Out of Scope:

| 不做什么 | 原因 | 未来是否考虑 |
|-|-|-|
| 更多风格（超过 2 种） | MVP 不做 | 考虑 |
| AI 智能场景识别自动推荐 | MVP 不依赖 AI 推理 | 后续版本 |
| 用户自定义风格参数 | 复杂度高 | 不考虑 |
| 视频风格 | 编码复杂度 | 不考虑 |
| 前置摄像头风格 | 前置一致性要求 | 考虑 |

## 3. 需求说明

### 3.1 标准 & 自然（Standard & Natural）

优先级：Must-have

标准风格为相机默认输出风格，以增强视觉冲击力为目标。标准风格为相机默认输出风格，饱和度和对比度略高于实际效果，提供更加标准的视觉感受。

自然风格服务于追求真实感、反感过度处理的用户群。通过调整 tone mapping 曲线增强立体感和层次感，保留高光和阴影细节，饱和度和对比度接近真实效果，更克制、更接近肉眼所见。

Pipeline 参数调整：

- AE & Tone：调整 tone mapping 曲线
- Color：调整饱和度、对比度、色温
- ISP 锐化：调整锐化程度

### 3.2 Onboarding 首次使用引导

首次进入相机时展示影像基调 onboarding；默认选中 Standard。用户完成引导后，可通过 Camera settings > Photo > Image tone 再次进入并修改，onboarding 与设置项共用同一选择状态。

首次使用路径：

- 首次进入相机 → 展示「Choose your image tone」onboarding 底部弹层
- 展示 Standard / Natural 两个样图选项；默认选中 Standard，选中项以白色外框高亮
- 用户点击选项后切换选中态，点击「OK」保存并关闭 onboarding，后续照片按所选风格处理

![The image shows the onboarding interface of Camera 5.1 for choosing image tone. On the left, there is a pop-up window with "Choose your image tone" at the top, displaying two sample photos: "Standard" (left) and "Natural" (right), with "Standard" selected and highlighted in white. Below the samples, there's a note that the choice will be saved and can be changed anytime in Camera settings, and an "OK" button at the bottom. On the right, the main camera interface is shown with a photo of buildings, and the "PHOTO" mode is selected at the bottom.](https://feishu.cn/file/QlKfbbU2toCfGAxcvl8lnMMEgtc)

### 3.3 设置项入口

优先级：Must-have

- Camera settings > Photo > Image tone
- 进入后展示 Standard / Natural 两个样图选项，并高亮当前已保存的风格
- 选择其他风格后立即保存；返回相机后，后置主摄与广角摄像头的 Photo、Portrait 模式同步按最新风格处理，且不影响已拍摄照片

状态与边界：

- onboarding 与设置项共用同一状态，切换风格不影响已拍摄照片。
- 不支持老项目升级

![The image shows the camera settings interface on a mobile device. On the left, under the "Photo" section, the "Image tone" option is expanded, with "Standard" and "Natural" as the two style options. On the right, the "Image tone" page displays two peacock images side by side, labeled "Standard" and "Natural", respectively, and a description below explaining that "Standard" adds richer color and contrast for a more vivid look, while "Natural" delivers balanced tones and colors closer to real life. This corresponds to the document's description of the Image Tone setting entry, showing the two style options and their descriptions.](https://feishu.cn/file/XK3pb3aPSoqzNqxBhzgl1GzIgae)

### 3.4 兼容范围

优先级：Must-have

影像基调与所有拍摄模式及功能兼容，风格作用于 ISP 管线层，其他功能叠加在风格之上。

影像基调配置可保存到 Preset 中。

兼容范围：

- 仅拍照模式：照片、人像、夜景、专业、运动 以及其他拓展的静态照片模式
- 滤镜、调色等其他图像处理功能可以兼容，在管线中处理位置更加靠前
- Preset、焦段切换等相机功能

### 兼容性要求

| ID | 要求 | 优先级 |
|-|-|-|
| C1 | 后置主摄与广角摄像头在 Photo、Portrait 模式下兼容两种风格 | Must-have |
| C2 | Photo、Portrait 共用同一 Image Tone 状态；其他模式维持当前默认调校，不区分双风格 | Must-have |
| C3 | JPEG 编码时间不因风格而显著增加 | Should-have |

## 4. 方案说明

### 核心行为

风格通过调整 ISP pipeline 三个阶段参数实现：

1. AE & Tone — 自动曝光与 Tone mapping 曲线
2. Color — 饱和度（Saturation）、对比度（Contrast）、色温
3. ISP 锐化 — 锐度（Sharpness）

风格作用于 ISP 管线层，滤镜叠加在风格之上。风格对 JPEG 输出生效，RAW 不受影响。Preset 存储风格配置项。默认以标准参数输出，用户切换后以所选风格参数输出。

### 风格参数参考 <cite type="user" user-id="ou_bde858e2c287e45bb799791c3cea03c7" user-name="Alex Huang"></cite>

<table><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th vertical-align="middle">视觉优先级/风格</th><th vertical-align="middle">标准 风格</th><th vertical-align="middle">自然 风格</th><th vertical-align="middle"></th></tr></thead><tbody><tr><td vertical-align="middle">动态范围</td><td>动态范围优先，避免过曝</td><td>自然影调优先，避免断层，halo，影调反转</td><td><img name="image.png" alt="The image shows two side-by-side views of a street scene, likely used to compare the &#34;standard style&#34; and &#34;natural style&#34; of Camera 5.1&#39;s Image Tone. On the left, the scene has a dynamic range prioritizing avoiding overexposure, with a more vibrant and contrasted appearance. On the right, the scene focuses on natural影调, avoiding halos and shadow loss, presenting a more balanced and realistic look. This aligns with the context&#39;s description of dynamic range and shadow handling in different styles." mime="image/png" scale="1.000000" src="B6a1bLQRSonia4xLfuNlUXAZgzd"/></td></tr><tr><td vertical-align="middle">影调</td><td>通透优先，提升画面层次关系避免死黑沉闷</td><td>材质可信度优先，影调干净自然避免过度提亮，导致失真</td><td><grid><column width-ratio="0.499249"><img name="image.png" alt="The image shows two side-by-side photos of a green boot-shaped object with a metal handle, placed on a tiled floor. The left photo has a standard style, with a more vibrant green color and a clear shadow. The right photo has a natural style, with a slightly duller green color and a less distinct shadow. Both photos feature a small white umbrella-shaped object on the floor and a sign on the wall in the background." mime="image/png" scale="0.190154" src="WLvDbq8HKouFdcxf9m1l0wZhgxf"/></column><column width-ratio="0.500751"><img name="image.png" alt="The image shows two side-by-side photos of green palm leaves, likely used to compare the natural and standard styles of Camera 5.1&#39;s Image Tone. The left photo may represent the standard style with dynamic range prioritization to avoid overexposure, while the right photo could illustrate the natural style focusing on natural shadow and highlight details to prevent halo and shadow inversion. This visual comparison aligns with the document&#39;s scheme explanation of style parameters, aiding in understanding the differences between the two styles." mime="image/png" scale="0.190154" src="YBjMbfKNNoOHvwxNN18lmJh6gie"/></column></grid><grid><column width-ratio="0.501249"><img name="image.png" alt="The image presents a comparison of two camera imaging styles: standard and natural. On the left is the standard style, which prioritizes dynamic range with通透优先 (transparency priority) and sharpness with清晰优先 (clarity priority). On the right is the natural style, focusing on natural shadow and highlight details with自然影调优先 (natural tonality priority) and avoiding halo and shadow inversion. Both styles maintain the yellow chair and gray wall as key elements, showcasing the differences in visual effect between the two styles." mime="image/png" scale="0.190154" src="GJFDbG88ko7rIuxwSXxl0xf6gyh"/></column><column width-ratio="0.498751"><img name="screenshot-20260910-171420.png" alt="The image presents two side-by-side views of a room interior, likely used to compare the &#34;standard style&#34; and &#34;natural style&#34; in Camera 5.1&#39;s Image Tone scheme. The left view shows a scene with vibrant colors, including red, yellow, and green, possibly indicating dynamic range or color grading effects. The right view appears to have a more balanced and natural color palette, with less intense hues, aligning with the context that natural style prioritizes natural影调 and avoids halos and shadow reversal." mime="image/png" scale="0.190154" src="LoRYb4uJUoj4s8xuqWolwoe1gIc"/></column></grid></td></tr><tr><td vertical-align="middle">色彩</td><td>鲜明优先，一眼讨喜，色彩鲜艳活力</td><td>还原优先，有微调空间</td><td><img name="image.png" alt="The image shows two side-by-side views of a restaurant interior, likely used to compare the &#34;standard style&#34; and &#34;natural style&#34; of Camera 5.1&#39;s Image Tone. Both views feature a wooden floor, red wooden doors with glass panels, and beige armchairs. The left view appears to have a more vibrant, &#34;standard style&#34; look with brighter lighting and more saturated colors, while the right view has a &#34;natural style&#34; appearance with softer lighting and more subdued colors, demonstrating the different visual priorities mentioned in the context." mime="image/png" scale="1.000000" src="CM0sbNLqToUiGrxwdJYlhQNngqf"/></td></tr><tr><td vertical-align="middle">锐化</td><td>清晰优先，更强的锐化和噪声处理</td><td>直觉优先，避免过度涂抹加锐带来的Ai味导致的反直觉。允许均匀黑白噪声</td><td><img name="image.png" alt="The image shows three side-by-side views of a building entrance area. On the left, there is a red arrow pointing to a person in the foreground. The middle and right views are similar, with people walking around the entrance and some umbrellas set up. The sky is blue with some clouds, and the building has a mix of light and dark-colored walls. This image is related to the context discussing camera imaging tone styles, likely illustrating differences in visual effects or style parameters between standard and natural styles as mentioned in the document." mime="image/png" scale="1.000000" src="QRMOb5jXUoi9nYxMGkBlr47Tgob"/><br/>避免地板过锐显脏</td></tr></tbody></table>

<bookmark name="docs.google.com" href="https://docs.google.com/presentation/d/1NyvImycPhZSTZNPz_TAjyPbWvd7IdLV7LYvRz6bPDro/edit?slide=id.g3f6bfbddee5_0_2#slide=id.g3f6bfbddee5_0_2"></bookmark>

![The image presents six side-by-side photos labeled "Standard" and "Natural", likely illustrating the camera's image tone styles. The first three photos under "Standard" show buildings with clear skies, while the last three under "Natural" display a street scene with a Starbucks. A text below states "Photography isn't measured in brightness, resolution or specs. It's measured in feeling" and emphasizes "Nothing Natural" as a quiet invitation to create, aligning with the document's context about camera image tone styles.](https://feishu.cn/file/Caz1bi3pUo5Nz9xUX50ly1fRgQf)

![The image presents two side-by-side photos of a green plant under different tone settings. On the left is the "Standard Tone" with labels "Vivid", "Bold", "Bright", and "Made for impact and loved by many". On the right is the "Natural Tone" with labels "Neutral", "Restrained", "True to life", and "for those who shoot with intention". This visual comparison illustrates the style differences between the two tone modes as described in the context, showing how they affect the plant's appearance in terms of color vibrancy and naturalness.](https://feishu.cn/file/YrowbkiSmoK19uxputGlaihqgsR)

| Pipeline 阶段 | 参数 | 自然 | 标准 |
|-|-|-|-|
| AE & Tone | Tone mapping 曲线 | [TBD] S 型，中间调对比度↑ | [TBD] 标准曲线 |
| Color | 饱和度偏移 | [TBD] | [TBD] |
| Color | 对比度偏移 | [TBD] | [TBD] |
| Color | 色温偏移 | [TBD] | [TBD] |
| ISP 锐化 | 锐度偏移 | [TBD] | [TBD] |

注：具体参数数值由算法/ISP 团队调优后确定。

## 5. 需求词条

| 应用场景 | 中文词条 | 英文词条 | 备注 |
|-|-|-|-|
| 自然风格 | 自然  <br/>均衡、细腻的影调 | Natural  <br/>Balanced, nuanced tones | 真实感、层次感、克制 |
| 标准风格 | 标准  <br/>鲜明、高对比度 | Standard  <br/>Vibrant, high-contrast | 色彩与对比度更丰富，出片感更强 |
| Onboarding 说明 | 影像基调决定每张照片的基础风格。  <br/>你可以随时在相机设置中更改。 | Your image tone sets the foundation for every photo.  <br/>You can change it anytime in Camera settings. | 首次引导，说明作用并告知后续修改入口 |
| 设置页入口 | 影像基调 | Image Tone | Camera settings > Photo > Image tone |
| 设置页说明 | 选择你偏好的影像风格。标准呈现更丰富的色彩和对比度，让画面更鲜明；自然则呈现均衡细腻的影调，让色彩更接近真实。 | Choose the look you prefer. Standard adds richer colour and contrast for a more vivid look, while Natural delivers balanced tones and colours closer to real life. | 仅说明设置作用，不重复引导用户进入设置 |

## 6. 关键依赖

| 依赖项 | 负责方 | 状态 | 风险 |
|-|-|-|-|
| ISP 管线风格参数调优（Tone mapping 等） | 算法 / ISP 团队 | [TBD] | 风格调优需要大量场景测试 |
| Camera HAL 支持风格参数注入 | 底层软件 | [TBD] | 低风险 |
| Preset 存储结构扩展 | 相机 App 开发 | [TBD] | 低风险 |

## 7. 指标与验收

### 成功指标

| 指标 | 基线 | 目标 | 测量方式 | Owner |
|-|-|-|-|-|
| 风格使用率 | 无此功能 |  | 埋点 | [TBD] |
| 照片分享率 | [TBD] | 提升 [TBD] | 埋点 | [TBD] |
| 用户满意度 | [TBD] | NPS > [TBD] | 调研 | [TBD] |

### 验收条件

- 默认风格为标准，拍照输出符合标准参数预期
- 自然/标准风格效果在样片上可辨识、无偏色
- 滤镜 + 风格叠加效果正确
- Preset 保存/恢复风格配置正常
- 首次进入相机时 onboarding 正常展示，Standard 默认选中且白色外框明确；点击 OK 后选择被保存且不再重复展示；设置项显示相同状态并支持后续切换。后置主摄与广角摄像头的 Photo、Portrait 模式同步生效；其他镜头与模式维持当前默认调校。Portrait 下标准风格沿用现有 tuning，自然风格使用对应的 \_natural tuning。

## 8. 埋点设计

埋点分为交互行为与拍照结果属性两类。交互行为用于分析 onboarding 和设置项的使用情况；拍照结果属性用于记录每张照片实际生效的影像基调。

**交互行为**

| event_name | action | parameters | parameter_value | 触发时机 |
|-|-|-|-|-|
| NTCamera | image_tone_select | image_tone, source | natural / standard; onboarding / settings | 用户点击 Natural 或 Standard 且选择值发生变化时上报 |
| NTCamera | image_tone_guide | action | show / ok | 首次进入相机展示影像基调引导时，以及点击 OK 保存时上报；保持默认 Standard 直接点 OK 同样上报 |

**拍照结果属性**

| event_name | key | key_description | parameter_value | 触发时机 |
|-|-|-|-|-|
| NTCamera | photo_info.image_tone | 拍照时实际生效的影像基调 | natural / standard | 每次拍照时随 photo_info 上报；记录最终实际生效值，而非最近一次点击值。仅后置主摄与广角的 Photo / Portrait 模式上报；其他镜头与模式维持默认调校、不上报，字段为空即表示不适用。 |

> 2026-09-15 本地对齐：以上「交互行为」表已整体重建为 3 行（新增 image_tone_guide），「拍照结果属性」表已补写上报范围。

示例：

```JSON
{
  "event_name": "NTCamera",
  "action": "image_tone_select",
  "image_tone": "natural",
  "source": "onboarding"
}

{
  "event_name": "NTCamera",
  "photo_info": {
    "image_tone": "natural"
  }
}
```

## 9. 干系人

| 角色 | 姓名 | RACI | 沟通频率 |
|-|-|-|-|
| PM | Travis Zhao | A |  |
| 算法/ISP | [TBD] | R | 周会 |
| 相机 App 开发 | [TBD] | R | 周会 |
| 设计 | [TBD] | R | 评审节点 |
| 测试 | [TBD] | C | 评审节点 |

## 10. 待确认/待补充

|  | 待确认项 | 章节 | 阻塞级别 |
|-|-|-|-|
| 1 | 风格参数具体数值（Tone mapping 曲线、饱和度偏移量等） | 方案 | 阻塞 |
| 2 | 风格对 HDR/夜景多帧融合的影响 | 方案 | 阻塞 |
| 3 | 风格元数据写入 EXIF | 需求 | 不阻塞 |
| 4 | 风格切换入口 UI 图标设计 | 需求 | 不阻塞 |

⚠️ 7/9 更新（Lia）：首次进入相机，弹出卡片让用户选择影像风格（Natural vs Standard，即自然 vs 标准）。Standard 已更名为 Standard（标准）。

## 11. 初步评审

### agent 开发评审

方案可行性：高 — 通过 ISP 参数调优实现，架构改动小  
依赖就绪度：[TBD] — 主要依赖 ISP 团队的参数调优  
实现风险：中等 — 风格参数调优需要大量场景回归测试

### agent 测试评审

验收标准可测试性：高 — 风格参数可通过客观指标验证  
场景覆盖：多种光照条件、多种拍摄对象、滤镜组合  
异常路径覆盖：快速切换风格、Preset 加载/卸载

### agent 全文评分

| 维度 | 满分 | 得分 | 说明 |
|-|-|-|-|
| 问题定义清晰 | 15 | 13 | 问题明确 |
| 假设明确可验证 | 10 | 7 | 部分假设待数据支撑 |
| 范围边界明确 | 15 | 13 | In/Out Scope 清晰 |
| 需求可测试 | 20 | 15 | 有量化验收条件 |
| 依赖完整 | 10 | 6 | ISP 调优依赖待确认 |
| 指标有基线+目标 | 15 | 5 | 缺少基线数据 |
| 风险有兜底 | 10 | 7 | 回退策略待补充 |
| 埋点覆盖 | 5 | 4 | 已覆盖核心事件 |

| 维度 | 满分 | 得分 | 说明 |
|-|-|-|-|
| **总分** | **100** | **70** |  |

结论: `NEEDS_CONTEXT` — 需要 ISP 团队确认风格参数和实现方案

## 12. 附录

### 考虑过但放弃的方案

- 方案 A：AI 智能场景识别自动推荐风格 — 复杂度高，MVP 不做
- 方案 B：用户可自定义风格参数（滑块调色调/色温）— 交互复杂，未来版本考虑
- 方案 C：拍摄后弹窗推荐风格 — 打断拍摄流程，用户体验差。改为默认标准 + 手动切换

## 正式设计稿（Camera 5.1）

[Image Tone](https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=2963-30291&p=f)