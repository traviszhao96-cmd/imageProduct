【PRD】Camera 4.1-Action Mode
前言

在空行输入“/高亮块” 插入高亮块，突出显示重点信息
一、 变更日志


时间

版本号

变更人

主要变更内容

2026/4/1

1.0

赵子聪

创建文档，补充基本交互逻辑








二、 需求背景
产品 / 数据现状
简要说明调研方法、样本情况及关键结论，输入 @ 在此附上详细的数据分析报告并添加在【附录】中
25111 项目与板球球队联名（为期一年），为了提升营销的宣传效果，新增了一个 Cricket Preset，在该 Preset 中支持了“类似” action mode 的调试，但是却没有该独立模式，并且由于 该 preset 在印度地区独占，导致 其他地区用户并不能体验到抓拍调试带来的优势，抓拍功能的使用范围也收到很大限制
手机相机随手拍是用户最高频的拍摄场景，场景复杂多样，保障这些场景的出片率，是提升用户拍照满意度的关键。
当前很多机型并没有 flicker sensor 选型，导致在直接进行场景检测的时候无法应用较为灵活的 “运动检测-降低快门速度-降低运动模糊” 链路，但是用户仍然有抓拍场景的拍摄需求
用户调研

简要说明调研方法、样本情况及关键结论，输入 @ 在此附上详细的数据分析报告并添加在【附录】中
Shutter speed is slow, shutter speed too late, cannot capture sometimes...
Moving objects get blurry images
image.png

image.png

image.png

image.png

image.png

image.png

三、需求目标
25131 项目，支持独立的 action mode，提升该模式下的抓拍性能
25131 默认的 photo 模式支持轻量的抓拍功能，提升抓拍体验
重新组合 cricket preset 。将当前 cricket preset 拆解为一个支持 action mode 的 preset；在 ROW 地区机型上重新组合为 sports preset，让所有机型都能支持
提升用户在运动场景的拍摄成片率，提升使用体验
四、 需求范围

可条理性地罗列需求范围或信息架构

五、产品流程图

将鼠标悬浮至下方空白图形模块，点击编辑，即可进入流程图创作你的产品流程图
六、需求说明
功能说明
「照片模式」 支持 轻量运动抓拍
功能支持范围
模式范围：照片模式
焦段范围：支持 前置、 超广角、广角（主摄）、长焦 镜头，根据项目硬件配置的镜头范围灵活适配，如果没有特殊说明，所有镜头都支持
待评估：照片模式下的抓拍支持的具体焦段？
功能详细说明
在照片模式后置下支持轻量的运动检测，在检测到物体运动时，提升快门速度，降低运动模式模糊，提升在日常拍摄场景下的成片率
功能互斥表
无，不涉及互斥
新增 「Action」 运动模式
功能支持范围
模式范围：action mode
焦段范围：支持 超广角、广角（主摄）、长焦 镜头，根据项目硬件配置的镜头范围灵活适配，如果没有特殊说明，所有镜头都支持
待评估：是否支持所有摄像头？是否支持所有焦段以及中间焦段？
23112，仅支持主摄和长焦镜头，即 1x & 3x，不支持滑动变焦仅支持点切
功能详细说明
在 模式选择栏 的最左侧新增一个 action mode，默认位置在portrait 左侧
在该功能下，支持更为激进的运动检测与快门速度策略，提升在较为激烈的运动场景下的成片率，降低运动模糊，详细效果定义见「效果说明」
变焦控件与照片模式保持一致 
同上，需要对支持的焦段范围做评估
在该模式下，部分照片模式功能不支持，包括：闪光灯，motion photo，高像素。详见功能互斥表
image.png

功能互斥表




FUNCTION

Action Mode

不支持原因

Top Toolbar


Flash

❌

@Maico Ma



Timer

✅ 





HDR

✅ 





Exposure

✅





Filter

✅





Tunning

✅





Auto Tone

❌





Motion Photo

❌





Quality(50mp)

❌





Grid

✅





ratio(4:3)

✅



Setting

watermark

✅





level

✅





Ultra HDR

✅



Waist

Retouching

❌





bokeh

❌



Instant

暂态夜景-Night mode

✅


Cricket preset 改为 应用 Action mode 并新增 Sports preset
功能详细说明
Cricket 中的 mode 改为 action，仅在 India 地区支持
新增 Sports，配置参考如下，描述复用原 Cricket ，仅在 ROW 地区支持
封面待更新

效果说明
关于 抓拍模式的效果说明，在什么场景达到怎样的效果，验收对比机选择等 @Alex Huang
alex补充：场景达成效果如PRD文档描述；
验收对比机和项目强相关，25131抓拍对比机是vivoV60；
【PRD】Camera—运动抓拍
交互设计稿
需求词条


应用场景

中文词条

英文词条

备注

Preset 名称

运动

Sports

应用 action mode 的 preset 名称，在 ROW 地区使用








九、 非功能需求

可以列举产品营销需求、运营需求、财务需求、法务需求、使用帮助、问题反馈等

十、 埋点
补充运动检测相关的埋点


参数名

参数说明

参数值



抓拍算法





运动检测结果相关








附录
