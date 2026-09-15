<!-- source: https://nothing-tech.sg.larksuite.com/docx/Ny4HdTqI3oLtYLx2m1wlDP9Mgdg | fetched: 2026-09-15 | revision: 945 -->
<title>【PRD】Camera 5.1 - 视频曝光与白平衡调节</title>

版本：v1.0｜更新：2026-08-17｜作者：Tiger Xu

# 变更日志

| **日期** | **版本** | **变更人** | **变更内容** |
|-|-|-|-|
| 2026-07-08 | v0.1 | Tiger Xu | 基于早期产品原型建立初版，形成统一 Pro Control 的初步交互设想。历史方案，已失效。 |
| 2026-07-13 | v0.2 | Tiger Xu | 收敛控制范围、兼容关系与参数记忆策略，并移除 AF 手动调节。历史方案，已失效。 |
| 2026-07-15 | v0.3 | Tiger Xu | 形成 EV、WB 偏移与 AE Lock 组成的旧版统一 Pro Control 方案。历史方案，已失效。 |
| 2026-08-17 | v1.0 | Tiger Xu | 根据最终产品与交互设计重构：EV 与 WB 改为独立控制项，WB 改为绝对 K 值控制，并完善状态、记忆、兼容、镜头切换与验收定义；补充 AE Lock 的用户价值、状态语义与验收结果。正文以本版本为准。 |

# 1. 需求背景与目标

## 战略对齐

本需求承接 <cite doc-id="VPYHwL7vOiOUYEkS0nulJXJIg3B" file-type="wiki" title="26111/26121 视频需求 Overview" type="doc"></cite> 中的「创作控制力」方向，服务于具备基础视频拍摄知识、理解手机影像能力边界，并在日常拍摄和轻量创作中具有曝光与白平衡控制习惯的用户。

这类用户不期待手机承担完整的专业视频制作工作流，但希望在自动结果不符合拍摄意图时，能够主动控制画面。由于手机通常缺少可变光圈和内置 ND，传统以固定快门、光圈与 ISO 为核心的专业视频控制方式难以直接迁移到日常手机拍摄。

## 核心问题

标准视频模式主要依赖自动曝光与自动白平衡。当画面亮度、色温或曝光变化不符合用户意图时，用户缺少一个能够在当前拍摄流程中快速介入的控制方式。传统专业模式虽然提供快门与 ISO 等参数，但在手机的能力边界下，其控制自由度和日常使用价值有限。

## 需求定位

本需求不复刻完整的专业参数体系，而是在标准视频模式中提供低成本、可随时介入的结果控制：通过 EV 调整画面亮度，通过 WB 控制色温，并在需要时锁定当前曝光结果。

## 目标结果

用户可在录制前和录制过程中快速调整画面亮度与色温，并在需要时保持曝光稳定；整个过程无需切换拍摄模式，也不会中断录制。

# 2. 需求定义

## 2.1 需求组成与适用范围

- 适用于 26111、26121 的标准视频模式。
- EV 与 WB 分别提供独立入口。
- AE Lock 位于 EV 调节界面内，不作为第三个顶层控制项。
- EV、WB 与 AE Lock 均支持录制前和录制过程中操作。

## 2.2 入口与状态反馈

录制前，用户通过标准视频模式的设置面板分别进入 EV 或 WB 调节；录制中，用户可点击顶部常驻的 EV / WB 状态入口，呼出对应调节栏。

| **阶段** | **状态** | **顶部反馈** |
|-|-|-|
| 录制前 | 默认状态，未进行调整 | 不显示 EV / WB 状态 |
| 录制前 | 正在调节 EV 或 WB | 对应图标与数值显示红色 |
| 录制前 | 已调整并收起调节栏 | 对应图标与当前数值显示灰色 |
| 录制中 | 未打开调节栏 | EV 与 WB 图标常驻显示为灰色；已调整项同时显示当前数值 |
| 录制中 | 正在调节 EV | EV 显示红色，WB 保持灰色 |
| 录制中 | 正在调节 WB | WB 显示红色，EV 保持灰色 |

红色仅表示用户正在调节当前参数，不表示该参数已被修改；灰色图标与数值表示参数已修改但调节栏已收起。录制前将参数恢复为默认值后，顶部状态消失；录制中即使处于默认值，EV 与 WB 图标仍保持灰色常驻。

## 2.3 EV 调节与 AE Lock

EV 与 AE Lock 解决不同问题：EV 用于调整自动曝光的目标亮度，但不会阻止自动曝光继续响应画面变化；AE Lock 用于在用户确认当前曝光后保持该结果，避免运镜、主体移动或背景明暗变化引起不符合拍摄意图的亮度波动。锁定后仍允许通过 EV 主动微调。

- 范围：−2 EV 至 +2 EV。
- 实际步进：1/3 EV；界面以一位小数显示近似值，如 −1.7、−1.3。
- 默认值：0.0。
- 调节结果实时作用于取景预览和最终视频；还原后回到 0.0。
- AE Lock 用于暂停自动曝光并保持当前曝光结果；锁定后 EV 仍可继续调节。
- 解除 AE Lock 后恢复自动曝光，并继续应用当前 EV 值。锁定期间，用户在 EV 调节界面中必须能够明确识别当前锁定状态；具体图标、颜色与动效以正式设计稿为准。

<readonly-block href="https://www.figma.com/embed?embed_host=share&amp;url=https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=3735-9664&amp;p=f&amp;t=AyrXZCYWL8DzPxmQ-0" type="iframe"></readonly-block>

## 2.4 WB 调节

- Auto 状态下使用自动白平衡。
- 用户开始滑动时，以当时的自动白平衡检测值作为起点；发生移动后，进入固定绝对色温控制，而非相对偏移控制。
- 范围：2300K 至 10000K；步进：100K，与照片专业模式一致。
- 界面显示当前绝对 K 值，调节结果实时作用于取景预览和最终视频。
- 点击 Auto 后退出手动色温控制并恢复自动白平衡。
- 手动调整时，色调固定为调整前的值，而非直接归零。

<readonly-block href="https://www.figma.com/embed?embed_host=share&amp;url=https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=3735-9664&amp;p=f&amp;t=AyrXZCYWL8DzPxmQ-0" type="iframe"></readonly-block>

## 2.5 录制与镜头切换

- 录制过程中打开、调节或收起 EV / WB 不得结束或中断当前录制。
- 收起调节栏后，当前设置继续生效。
- 切换镜头时保留当前 EV 值、WB 的 Auto / 手动状态及手动 K 值，以及 AE Lock 状态。
- AE Lock 开启时，镜头切换后继续维持当前曝光结果；不要求不同镜头使用相同的快门或 ISO 参数。

## 2.6 记忆规则

- EV 作为用户偏好长期保留，直至用户主动还原为 0.0。
- WB 与 AE Lock 遵循[相机五分钟记忆规则](https://nothing-tech.sg.larksuite.com/wiki/Yi5iwRJSPit8LfkeT2ClUbJlgOd)：退出后 5 分钟内重新进入时保留原状态；超过 5 分钟后，WB 恢复 Auto，AE Lock 恢复未锁定。进程被杀不作为独立的重置条件。
- 重新进入相机时，顶部状态必须与实际生效状态一致；EV 非 0.0 时显示灰色图标与数值，红色调节态不被记忆。

## 2.7 兼容范围

- 在标准视频模式内兼容 SDR、HDR、Log 与 Style。
- 不兼容前后双录及标准视频之外的其他视频相关模式，包括慢动作、延时摄影等。
- 不兼容模式中不提供 EV / WB 相关入口。

## 2.8 正式设计稿

<readonly-block href="https://www.figma.com/embed?embed_host=share&amp;url=https://www.figma.com/design/ZwVgD7LD46VUntRPmFcp4U/Camera-5.1---26111-Caterpie-?node-id=3735-9664&amp;p=f&amp;t=AyrXZCYWL8DzPxmQ-0" type="iframe"></readonly-block>

设计稿定义布局、视觉与动效表现；本 PRD 定义功能范围、状态语义与行为规则。若二者出现冲突，应由产品与设计共同确认后同步更新，不以任一单方文档静默覆盖。

## 2.9 本代不包含

- 手动快门与 ISO。
- 手动对焦。
- 独立的专业视频模式。
- Tint 调节。

# 3. 验收标准

本章只定义产品验收结果；具体测试场景、方法与质量阈值由软测与 IQA 在测试方案中展开。

- **范围符合：**26111、26121 的标准视频模式提供本能力，支持 SDR、HDR、Log、Style；前后双录及其他视频相关模式不提供入口。
- **状态正确：**录制前与录制中的入口、顶部图标、颜色和数值符合第 2.2 节定义；红色仅用于正在调节的参数，调节栏收起后恢复灰色。
- **控制有效：**EV 与 WB 的默认值、范围、步进、还原 / Auto 行为正确，取景预览与最终视频结果一致；AE Lock 开启后，自动曝光不再随构图或环境变化自行调整，EV 仍可调节，解除后恢复自动曝光。
- **记忆正确：**EV 长期保留，WB 与 AE Lock 遵循五分钟记忆规则；重新进入后的顶部反馈与实际生效状态一致。
- **录制与镜头切换可用：**录制中调节和镜头切换不结束录制，相关状态按定义保留，输出文件可正常播放与编辑。
- **质量达标：**除用户主动调节或场景变化外，不出现异常曝光 / 色温跳变、持续震荡、录制中断、崩溃或文件损坏。

# 4. 附录

## 竞品参考

本节保留需求形成阶段的竞品实测记录，用于说明同类能力的产品形态、参数范围与记忆策略。竞品方案不直接定义本需求的功能范围、状态规则或验收标准，当前产品定义以第二章及正式设计稿为准。

**参考结论：**Pixel 9 Pro 在标准视频模式中分别提供 Exposure 与 White Balance 调节，并支持录制前和录制中操作，验证了轻量控制直接进入日常视频流程的可行性。本需求参考其控制位置与操作路径的简洁性，但 EV / WB 参数模型、状态反馈、AE Lock 与记忆规则均按本项目目标独立定义。

| **能力** | **Pixel 9 Pro** | **三星 S25 Ultra** | **iPhone 17 Pro** | **Vivo X300** | **Vivo V70** | **Reno 15** | **25111Pro** |
|-|-|-|-|-|-|-|-|
| 视频模式是否有独立 EV 调节 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ 只能拉小太阳 |
| EV 调节范围 | 未标注；约 −3 EV 至 +4 EV | −2 EV 至 +2 EV | −2 EV 至 +2 EV | −100 至 +100；只能拉小太阳 | −100 至 +100；约 −2 EV 至 +2 EV | −2 EV 至 +2 EV | 未标注；约 −2 EV 至 +2 EV |
| 是否有白平衡调节 | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| 白平衡调节路径 | 视频模式－右下角参数 | 专业视频 | ／ | 专业视频 | ／ | ／ | ／ |
| 是否有预设值 | 无 | 无 | ／ | 晴、阴、多云、白炽灯、钨丝灯、夕阳；灰卡自动校准 | ／ | ／ | ／ |
| 白平衡调节范围 | 检测值 −2000K 至检测值 +3500K | 2300K 至 10000K | ／ | 2300K 至 10000K；Tint −100 至 +100 | ／ | ／ | ／ |
| 如何处理色调 | 保留检测值 | 手动时还原为 0 且不可调整 | ／ | 手动设置 | ／ | ／ | ／ |
| 录制中实时调节 | EV 与白平衡均可随时调整 | 视频模式只能拉小太阳；专业视频可调全部参数 | 只能拉小太阳 | 视频模式只能拉小太阳；专业视频可调全部参数 | 只能拉小太阳 | 只能拉小太阳 | 只能拉小太阳 |
| 参数持久化 | 关闭相机后还原至自动 | 视频 EV 关闭相机后还原；专业视频一直保留 | 视频 EV 一直保留 | 视频 EV 一直保留；专业视频退出相机后还原 | 视频 EV 一直保留 | 视频 EV 一直保留 | 对焦框消失后失效 |

## Pixel 9 Pro 参考详解

Pixel 在普通视频模式中分别提供 Exposure 与 White Balance 调节，并支持在录制前和录制过程中直接操作。其主要参考价值在于控制能力的位置与操作路径；本需求的参数模型、状态反馈和记忆规则以第二章定义为准。

<grid>
<column width-ratio="0.500000">
**曝光调整**
- 简化的曝光调整模块，不显示具体 EV 值。
- 调整范围约 −3 EV 至 +4 EV。
- 录制开始前和录制中均可自由调整。
- 调整后出现还原按钮，支持一键归零。
- 彻底退出相机后还原至自动。
![The image shows the camera interface with a grid background. At the top, there is a "4K" label and a question mark icon. In the middle, there is a horizontal slider with a blue indicator. Below the slider, there are three icons: a square, a circular button, and a refresh symbol. At the bottom, there are three buttons labeled "Reset All", "Exposure", and "White Balance" with corresponding icons. This interface is related to the white balance adjustment mentioned in the context, which includes a simplified module showing specific偏移量, adjustable range of -2000K to +3500K based on current AWB detection value, and a还原button for one-click reset.](https://feishu.cn/file/S1I3bkV5yoeiFFxaMPzlIo1DgIx)
</column>
<column width-ratio="0.500000">
**白平衡调整**
- 简化的白平衡调整模块，调整时显示具体偏移量。
- 以当前 AWB 检测值为基准，在 −2000K 至 +3500K 范围内偏移。
- 调整白平衡不影响系统对色调的自动判断。
- 录制开始前和录制中均可自由调整。
- 调整后出现还原按钮，支持一键归零。
- 彻底退出相机后还原至自动。
![The image shows the camera interface with a simplified white balance adjustment module. There is a "Auto" label in the center, and a slider with a blue and red icon at the bottom. Three icons are below: a square, a circle, and a refresh symbol. At the bottom, there are "Reset All", "Exposure", and "White Balance" buttons, with "White Balance" highlighted. This corresponds to the context describing the white balance adjustment module, which adjusts within -2000K to +3500K from the current AWB detection value, supports free adjustment before and during recording, has a还原 button, and returns to auto when exiting the camera.](https://feishu.cn/file/RcoWbBDgKokJZ6xq7hxlr0h6gkH)
</column>
</grid>