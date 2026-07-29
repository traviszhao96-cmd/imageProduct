#!/usr/bin/env python3
"""Build canonical Camera KB and its FL projection metadata.

This script intentionally does not transform the old FL-derived KB because that
file contains duplicated mode rows, copied support marks, and target-project
source notes. The canonical table below is the source of truth for the KB stage.
Project Feature Lists are downstream projections. Whether a KB node becomes an
FL row, and which dimensions it expands by, is carried by the node itself.
"""

from __future__ import annotations

import json
import re
from hashlib import sha1
from collections import Counter
from pathlib import Path

from normalize_kb_catalog_20260715 import normalize


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "knowledge" / "_output"
OUT_CANONICAL = OUT / "kb-functions-algorithms.json"
OUT_JSON = OUT / "kb-functions-algorithms.v7.json"
OUT_COMPAT = OUT / "kb-functions-algorithms.v6.json"
OUT_AUDIT = OUT / "kb-functions-algorithms.v7.audit.md"
OUT_COMPAT_AUDIT = OUT / "kb-functions-algorithms.v6.audit.md"

SOURCE = "25111 / 25131"
CODE_BASELINE = "CameraApp origin/develop@c97b3137b6 (2026-07-27)"
KB_FIELDS = [
    "模式", "节点 ID", "父节点 ID", "节点类型", "一级分类", "二级分类",
    "名称", "交互位置", "说明", "判断依据", "依赖", "验证方法",
    "App 绑定", "配置门控", "实现状态", "FL 投影", "FL 展开维度",
    "FL 展开条件", "摄像头范围", "规格范围", "代码基线", "来源项目", "备注",
]


def row(
    modes: str,
    level1: str,
    level2: str,
    name: str,
    desc: str,
    judgement: str,
    dependency: str,
    verify: str,
    note: str = "",
    *,
    node_id: str = "",
    parent_id: str = "",
    node_type: str = "",
    interaction: str = "",
    app_binding: str = "",
    config_gate: str = "",
    implementation_status: str = "已实现",
    fl_projection: str = "",
    fl_dimensions: str = "",
    fl_condition: str = "",
    camera_scope: str = "按项目确认",
    spec_scope: str = "按项目确认",
) -> dict[str, str]:
    return {
        "模式": modes,
        "节点 ID": node_id,
        "父节点 ID": parent_id,
        "节点类型": node_type,
        "一级分类": level1,
        "二级分类": level2,
        "名称": name,
        "交互位置": interaction or level2,
        "说明": desc,
        "判断依据": judgement,
        "依赖": dependency,
        "验证方法": verify,
        "App 绑定": app_binding,
        "配置门控": config_gate,
        "实现状态": implementation_status,
        "FL 投影": fl_projection,
        "FL 展开维度": fl_dimensions,
        "FL 展开条件": fl_condition,
        "摄像头范围": camera_scope,
        "规格范围": spec_scope,
        "代码基线": CODE_BASELINE,
        "来源项目": SOURCE,
        "备注": note,
    }


ALL_STILL = "照片 / 人像 / 夜景 / 高像素 / 专业"
ALL_CAPTURE = "照片 / 人像 / 运动 / 视频 / 夜景 / 慢动作 / 全景 / 专业 / 前后双录 / 高像素 / 延时摄影"


ROWS = [
    row(
        "通用",
        "功能",
        "模式栏 / Mode Switch",
        "模式栏",
        "相机默认进入 Photo/照片；模式栏按项目支持范围展示人像、运动、视频、夜景、慢动作、延时摄影、全景、专业、前后双录等模式。",
        "生成项目 FL 时，先确认项目模式清单，再按每个模式支持的工具栏、算法和摄像头能力展开。",
        "依赖项目模式配置、模式入口、每个模式的摄像头/算法/交互能力。",
        "打开相机并滑动模式栏，确认项目要求的模式是否存在且能进入。",
    ),
    row(
        "通用",
        "功能",
        "模式栏 / Mode Switch",
        "快速模式切换 / Quick Mode Switch",
        "模式栏中的快速切换交互，使用户可以在项目支持的相机模式之间快速切换；该功能描述模式切换效率与状态衔接，不等同于前后摄像头切换。",
        "RL 明确要求快速模式切换，且项目模式栏提供对应手势或快捷交互时填写支持；具体覆盖模式、触发方式和状态保留规则需按项目确认。",
        "依赖模式栏 UI、模式生命周期、摄像头与算法 pipeline 启停、切换动画、状态保存和异常恢复。",
        "在项目支持的相邻及非相邻模式间连续快速切换，确认入口、响应时延、动画、预览恢复、参数状态和拍摄可用性符合规格。",
        "来源：项目 RL；目标项目支持范围待 Product 确认。",
    ),
    row(
        "照片 / 人像 / 视频 / 夜景",
        "功能",
        "前后翻转 / Camera Switch",
        "前后翻转 / Front-Rear Camera Switch",
        "拍摄或录制开始前，通过独立翻转入口在前置摄像头与后置摄像头组之间切换；它不属于模式栏，也不等同于录制中的前后置切换。",
        "当前模式同时允许前置和后置预览，并提供独立前后翻转入口时填写支持；只支持单侧摄像头的模式不支持。",
        "依赖前后摄可用范围、摄像头 open/close 与预览恢复、模式状态迁移、翻转入口 UI 和项目摄像头配置。",
        "在支持模式的前置与后置预览间反复翻转，确认入口可用、预览恢复、默认焦段、模式参数和异常恢复符合规格。",
    ),
    row(
        "照片 / 人像 / 视频 / 夜景 / 高像素 / 专业",
        "功能",
        "预览框",
        "人脸检测",
        "检测预览中的人脸并驱动人脸框、Face AE/AF、美颜、人像、FRT 等后续能力。",
        "当前模式需要基于人脸做对焦、测光、美颜、人像、FRT 或 UI 提示时填写支持。",
        "依赖人脸检测算法、预览流、AE/AF/美颜/人像等消费方。",
        "在单人、多人、逆光、口罩/墨镜等场景下预览，确认人脸框和相关策略稳定。",
    ),
    row(
        "照片 / 人像 / 夜景 / 高像素",
        "算法",
        "后处理算法 / Post-processing Algorithm",
        "FRT / 人像清晰度提升",
        "独立的人脸清晰度增强后处理算法。FRT（Face Restoration Technology）在人脸检测成立时恢复和增强人脸细节，重点改善人脸区域清晰度；它不是美颜参数或肤质修饰功能。",
        "项目算法链路明确接入 FRT，且当前模式、摄像头和输出规格允许在人脸场景启用人像清晰度提升时填写支持。",
        "依赖人脸检测、FRT 模型、拍照/夜景/人像/高像素后处理链路，以及人脸尺寸、姿态、遮挡和置信度判断。",
        "逐模式、逐摄像头拍摄单人/多人、远近人脸、侧脸、遮挡和低照样张，结合算法 tag 确认 FRT 生效，并检查细节提升、身份特征保持、伪影和过度锐化。",
    ),
    row(
        "照片 / 人像",
        "算法",
        "后处理算法 / Post-processing Algorithm",
        "美颜算法 / Beauty Algorithm",
        "独立的美颜后处理算法，仅用于照片和人像模式的前置摄像头。能力包括磨皮、美白、亮眼、胡须保护、匀肤、肤色分层、性别分层、年龄分层和脸型流畅等参数与效果处理；目标是在保留真实肤色、纹理、毛发和个人特征的前提下提升自然度。",
        "仅当模式为照片或人像、摄像头为 Front，用户启用美颜且检测到人脸时填写支持；Main、UW、Tele 不支持本期美颜升级。",
        "依赖人脸检测、肤区/肤色识别、性别与年龄分层、置信度及中性回退、美颜参数配置、多人逐人策略、前置拍照 pipeline 和地区参数下发。",
        "在照片与人像模式使用 Front 验证 Natural/Strong 档位、首次引导、磨皮/美白/亮眼/胡须保护、匀肤和脸型流畅；覆盖多肤色、性别、年龄、多人、低光、逆光、遮挡与浓妆，确认不可靠识别回退到中性策略且无假白、塑料感、毛发损失或背景形变。",
        "需求来源：美颜能力升级需求整理文档（TBC9d6cwIolGWmxzBdglZjdZgxd，revision 604）。",
    ),
    row(
        "人像",
        "算法",
        "后处理算法 / Post-processing Algorithm",
        "人像虚化 / Portrait Bokeh",
        "人像模式的核心背景虚化算法，通过主体分割或双摄深度信息区分人物与背景，并对背景施加景深虚化。单摄链路依赖语义分割，双摄链路依赖主副摄 Depth；发丝分割用于改善头发等复杂边缘，但是否启用需按项目、摄像头和资源配置确认。",
        "人像模式的当前输出摄像头实际进入主体分割、Depth 和背景虚化链路时填写支持；辅助摄像头仅参与 Depth、但不作为用户可选输出镜头时，不得在该摄像头支持列中标记支持。",
        "依赖人脸/人体检测、主体与发丝分割、单摄或双摄 Depth、镜头标定、背景虚化渲染、内存与处理耗时预算。",
        "逐输出摄像头覆盖单人、多人、半身/全身、复杂发丝、透明物体、前后景遮挡和低照场景，确认主体边缘、景深层次、背景光斑、预览与成片一致性；结合日志确认单摄/双摄链路及发丝分割是否实际生效。",
        "开发算法清单同时包含单摄虚化、双摄虚化和发丝分割；KB 合并为一条能力，项目差异在 FL 摄像头列和说明中表达。",
    ),
    row(
        "照片（其他模式按项目确认）",
        "算法",
        "实时算法",
        "ASD / AI场景检测",
        "ASD（AI Scene Detection）通过 AI 模型识别画面语义场景，例如绿植、舞台、室外天空等需要特殊调试策略介入的场景；不包含仅基于亮度、DRC 等基础信号的普通场景判断。",
        "当项目明确接入 ASD 模型，且语义场景输出会影响 UI 提示、ISP 调试策略或算法策略时填写支持。",
        "依赖 ASD 模型、预览流、场景策略表、ISP/算法消费方。",
        "使用绿植、舞台、天空等 ASD 定义场景集验证识别结果、触发时机和对应调试策略。",
    ),
    row(
        ALL_CAPTURE,
        "功能",
        "预览框",
        "脏污检测",
        "检测镜头脏污并在 UI 中提示用户清洁镜头。",
        "项目接入脏污检测策略并会在预览中展示提示时填写支持。",
        "依赖脏污检测算法、预览流、提示 UI、项目地区/策略开关。",
        "制造镜头脏污场景，确认提示出现、消失和误触发情况。",
    ),
    row(
        "照片 / 人像 / 视频 / 夜景 / 高像素 / 专业",
        "功能",
        "AE/AF",
        "自动对焦-自动曝光",
        "统一描述 Touch AE/AF、Face AE/AF、Touch AE/AF Lock、CAF 和 EV 补偿等对焦测光能力。",
        "当前模式允许点击/人脸驱动对焦测光、连续对焦、锁定或曝光补偿时填写支持；固定焦摄像头需注明仅 AE 或不支持 AF。",
        "依赖 AF 马达或固定焦策略、AE/AF 算法、触控/人脸输入、预览 UI。",
        "点击预览、人脸入镜、长按锁定、移动被摄体，确认对焦/测光/锁定/CAF 行为符合模式定义。",
    ),
    row(
        ALL_CAPTURE,
        "功能",
        "Zoom",
        "变焦",
        "变焦栏位于模式栏上方，默认变焦点应覆盖硬件光学点，并覆盖可用 In-Sensor Zoom 点。变焦方式需要在项目 FL 中说明：SAT 平滑镜头切换、硬切镜头切换，或纯数码变焦。",
        "按项目摄像头硬件倍率、ISZ/crop 能力、SAT 能力、硬切策略和当前模式允许的摄像头/倍率范围判断。",
        "依赖摄像头硬件倍率、sensor crop/ISZ、模式可用摄像头列表、zoom range 配置、SAT 标定或硬切转场动画。",
        "检查默认变焦点、双指缩放、滑动变焦和跨镜头切换；确认倍率、预览、成片路径和切换方式（SAT/硬切/数码变焦）一致。",
    ),
    row(
        "照片 / 夜景 / 专业 / 高像素",
        "算法",
        "实时算法",
        "Photo EIS",
        "照片电子防抖能力，通过陀螺仪运动信息和画面裁切补偿手持抖动，通常在项目定义的高倍率拍照或高倍率预览链路生效。",
        "当前拍照模式、镜头和倍率进入照片 EIS 链路时填写支持；触发倍率按项目和镜头组合决定。",
        "依赖陀螺仪、裁切空间、照片 EIS 算法和当前镜头/倍率。",
        "在项目定义的高倍率手持场景拍摄，确认取景稳定、裁切范围、OIS/EIS 叠加关系和成片清晰度。",
    ),
    row(
        "视频 / 慢动作 / 延时摄影 / 前后双录",
        "算法",
        "实时算法",
        "Video EIS",
        "视频电子防抖。与照片 EIS 不同，视频 EIS 通常作为录制过程中的全局稳定能力，在支持的视频规格和倍率范围内持续生效。",
        "当前视频模式/规格/镜头支持录制防抖链路时填写支持；用户可通过 Settings > Video 的视频防抖开关控制是否启用。",
        "依赖陀螺仪、裁切空间、视频 EIS 算法、当前镜头/倍率/分辨率/帧率和视频防抖设置项。",
        "在支持规格下手持录制，确认开启/关闭视频防抖后的稳定性、视角裁切、果冻效应和发热功耗符合规格。",
    ),
    row(
        "视频",
        "算法",
        "实时算法",
        "Video HDR 算法",
        "视频录制时通过 Sensor HDR 曝光/读出模式与 ISP/算法处理扩展动态范围，保留高光和暗部细节，并按支持的 HDR 格式编码输出。功能说明只定义能力本身；项目 FL 需逐摄像头确认分辨率、帧率、Sensor mode、输出格式，以及与 EIS、变焦、风格/LUT、Log 的兼容关系和功耗温升。",
        "仅在当前摄像头、视频规格和 Sensor mode 明确进入 Video HDR 算法链路，并输出项目定义的 HDR 编码/元数据时填写支持；仅具备 HLG/HDR 编码器不等同于 Video HDR 算法已启用。",
        "依赖支持 HDR 的 Sensor mode、ISP/Video HDR 算法、HDR 编码器与元数据、视频规格、EIS/变焦/风格/Log 互斥策略及性能功耗预算。",
        "对支持摄像头逐项验证 1080P30/60、4K30/60，确认 Sensor mode、HDR 编码/元数据、动态范围、EIS/变焦/风格/Log 互斥以及功耗温升；不支持摄像头确认入口不可用。",
    ),
    row(
        "照片 / 视频 / 夜景 / 专业 / 高像素",
        "功能",
        "Zoom",
        "OIS",
        "光学防抖能力，通过镜组或 Sensor 的物理位移补偿手持抖动，可提升预览、视频和低照长曝光的稳定性。当前硬件范围：26111 Main（HP5）支持；26121 Main（IMX896）和 Tele（JN5）支持；两项目 UW/Front 均不支持。摄像头具备 OIS 硬件后仍需由 SE 确认各模式是否正确启用及与 EIS 的叠加策略。",
        "仅对应摄像头硬件具备 OIS，且当前模式链路正确初始化并启用 OIS 时填写支持；不得因设备无独立长焦而把主摄 OIS 判为不支持。",
        "依赖摄像头 OIS 硬件、驱动、当前模式调用的摄像头链路。",
        "查硬件物料和驱动日志确认 OIS 初始化；在照片、视频、夜景、专业和高像素模式使用对应摄像头手持拍摄，验证稳定性，并检查 OIS/EIS 叠加与模式切换。",
    ),
    row(
        "专业",
        "功能",
        "Toolbar",
        "各项专业模式参数极值范围",
        "专业模式手动参数的可调边界定义，覆盖 ISO、快门速度、WB/AWB 色温、EV 和手动对焦。支持范围为专业模式下全部后置摄像头：26111 Main/UW；26121 Main/UW/Tele；Front 不支持。WB/AWB 色温范围沿用原项目，为 2300K–10000K。ISO 上下限不使用跨镜头统一值，必须根据每颗 Sensor、平台与 HAL 实际性能支持范围逐摄像头确认。",
        "对应后置摄像头可进入专业模式并提供手动参数控制时填写支持。WB/AWB 固定检查 2300K–10000K；ISO 最小值和最大值必须结合 Sensor 规格、HAL 静态 metadata、模拟/数字增益能力和画质/性能限制确认，不得直接沿用其他项目或其他镜头数值。",
        "依赖 Sensor ISO/曝光能力、HAL CameraCharacteristics 静态 metadata、3A 手动控制接口、专业模式 UI 配置和逐镜头调试结果。",
        "逐个后置摄像头读取并记录 HAL 的 sensitivity/exposure range，验证 ISO 最小值、最大值及边界档位可正常预览和拍摄；验证 WB/AWB 可从 2300K 调至 10000K；同时检查快门、EV、Focus 的首尾值、步进、显示和成片一致性。",
    ),
    row(
        "照片",
        "算法",
        "后处理算法",
        "AIGC SR",
        "面向高倍率变焦的 AI 细节重建能力，通过模型恢复或生成传统超分难以保留的纹理；它不同于常规多帧 SR。核心验收范围是实际生效摄像头、起止倍率、生成错误、文字真实性、性能和功耗。",
        "仅在项目明确接入 AIGC SR/AISR 模型并冻结实际摄像头与生效焦段后填写支持；算法仍处于方案、内存或性能评估时填写 TBD。",
        "依赖高倍率输入、AIGC SR/AISR 模型、平台 AI 算力、内存和功耗预算，以及焦段触发策略。",
        "在候选生效焦段前后拍摄纹理、文字、人脸和重复图案，结合算法 tag 检查清晰度、生成错误、真实性、耗时、内存和功耗。",
    ),
    row(
        "照片",
        "算法",
        "后处理算法",
        "HDSR",
        "HDR 与 Super Resolution 的组合成像链路，在高动态且需要超分增强的场景同时改善动态范围和高倍率细节；需确认实际生效摄像头、焦段，以及与普通 HDR、SR 的切换边界。",
        "当前模式、摄像头和焦段明确进入 HDR+SR 组合链路时填写支持；只有 HDR 或只有 SR 均不等同于 HDSR。",
        "依赖 HDR 检测、多帧 HDR、SR、运动检测、帧对齐融合和焦段触发策略。",
        "在高动态细节场景覆盖触发边界前后焦段，结合算法 tag 确认 HDSR，并检查动态范围、细节、鬼影和处理耗时。",
    ),
    row(
        "照片",
        "算法",
        "实时算法",
        "运动抓拍",
        "针对运动主体和手持运动场景进行运动检测，并联动曝光、取帧、HDR 与多帧融合策略，提高高速场景的成片清晰度和成功率；需确认触发场景、摄像头范围及运动伪影。",
        "照片模式明确接入运动检测与抓拍优化链路，并在项目定义的运动场景实际触发时填写支持。",
        "依赖运动检测、AE、HDR/多帧策略、快门与取帧控制、项目场景配置和性能预算。",
        "覆盖人物、宠物、车辆、流水和手持晃动场景，结合算法 tag 检查触发准确率、快门响应、主体清晰度、背景表现、鬼影和误触发。",
    ),
    row(
        "照片",
        "算法",
        "后处理算法",
        "RAW HDR",
        "在 RAW 域对多帧不同曝光图像进行对齐与融合，扩展动态范围并保留高光、暗部和颜色信息。FL 只确认模式、摄像头和输出规格是否接入该链路，具体亮度阈值与帧策略属于软件设计。",
        "当前模式和摄像头明确进入 RAW 域多帧 HDR 链路时填写支持；用户侧 HDR 开关状态不能单独证明底层一定使用 RAW HDR。",
        "依赖 RAW 多帧输入、曝光控制、运动检测、对齐融合、Tone Mapping 和项目 HDR 决策策略。",
        "覆盖高动态、低照、运动和 HDR 开关组合，结合算法 tag 确认 RAW HDR 生效，并检查高光、暗部、颜色、鬼影和耗时。",
    ),
    row(
        "照片",
        "算法",
        "后处理算法",
        "CFR / 紫边去除",
        "检测并抑制高反差边缘附近由镜头色散产生的紫边或彩边，尽量保持真实边缘颜色与细节；需按模式、摄像头和 HDR/非 HDR 链路确认生效范围。",
        "当前摄像头和成像链路加载 CFR 模块，并在高反差边缘场景实际生效时填写支持。",
        "依赖镜头色散特征、边缘检测、CFR 参数和当前 HDR/非 HDR 后处理链路。",
        "拍摄逆光树枝、金属边缘和黑白高反差目标，结合算法 tag 检查紫边抑制、颜色准确性和细节损失。",
    ),
    row(
        "照片",
        "算法",
        "实时算法",
        "ISZ / In Sensor Zoom",
        "通过 Sensor 内部裁切或专用读出模式，在指定倍率输出接近原生分辨率的图像。ISZ 点必须来自项目 Camera/HAL 配置，不得由 UI 默认变焦点反推；视频 ISZ 需独立确认。",
        "当前摄像头在项目定义的倍率和亮度条件下切换到 ISZ Sensor mode 时填写支持，并记录实际生效倍率和是否支持 seamless 切换。",
        "依赖 Sensor ISZ/crop mode、HAL Camera 配置、倍率和亮度触发条件，以及预览/成片链路适配。",
        "在候选倍率和亮度边界前后检查 Sensor mode、算法 tag、FOV、清晰度、切换跳变和功耗，确认实际 ISZ 焦段。",
    ),
    row(
        "照片",
        "算法",
        "后处理算法",
        "Hex Zoom",
        "26111 主摄 4x 高倍率成像路径，使用 HP5 hex/4x4 RAW 输入并由外部软件完成 remosaic 和细节重建；它不是 ISZ，也不是长焦摄像头。",
        "仅在项目 HAL 和算法方案明确使用 hex/4x4 RAW 与外部软件 remosaic 的倍率点填写支持。",
        "依赖支持 hex/4x4 RAW 的 Sensor、HAL stream 配置、外部软件 remosaic、内存与性能预算。",
        "在 4x 前后拍摄细节和运动目标，检查输入格式、算法 tag、清晰度、伪影、处理时间、内存和功耗。",
    ),
    row(
        "视频",
        "算法",
        "实时算法",
        "视频夜景",
        "视频录制中的低照增强与时域降噪能力，在控制噪声的同时维持曝光、颜色、运动连续性和实时帧率；需确认支持的摄像头、分辨率、帧率、倍率及功耗温升。",
        "低照视频录制实际进入项目定义的视频夜景或时域降噪链路时填写支持。",
        "依赖低照检测、视频时域降噪/增强、EIS、编码规格和实时性能功耗预算。",
        "在不同低照等级、运动速度、摄像头和视频规格下录制，结合算法 tag 检查噪声、拖影、曝光、颜色、帧率和温升。",
    ),
    row(
        "人像",
        "算法",
        "实时算法",
        "人像 HDR",
        "人像拍摄中的 HDR 组合链路，在保持主体虚化边界和肤色的同时扩展背景与人物动态范围；可与美颜、FRT 等人像后处理协同，但不是这些算法的总称。",
        "当前人像模式、摄像头和输出规格明确进入 HDR 人像链路时填写支持。",
        "依赖人像分割/虚化、HDR 多帧、人物运动检测、肤色保护以及美颜/FRT 兼容策略。",
        "在逆光人像、多人、运动人物和复杂发丝边缘场景结合算法 tag 检查动态范围、虚化边界、肤色、鬼影和处理耗时。",
    ),
    row(
        "照片 / 夜景 / 高像素",
        "算法",
        "后处理算法",
        "超分 / Super Resolution（SR）",
        "高倍率变焦或裁切拍照链路上的超分辨率能力，用于提升细节清晰度；核心项目结论是每个模式、物理摄像头对应的实际生效焦段。",
        "按项目、模式和物理摄像头确认 SR 的起始倍率、结束倍率及分段策略；普通数字变焦不等同于 SR，YUV 4x、RAW 2x 只能作为旧方案参考，不能直接作为当前项目结论。",
        "依赖项目 zoom range、sensor crop/长焦链路、SR 算法配置、触发阈值和平台算力。",
        "在 SR 生效边界的前一档、边界点和后一档分别拍摄细节目标，结合算法 tag 确认实际生效焦段，并检查清晰度、伪影、耗时和功耗。",
    ),
    row(
        "照片 / 人像 / 夜景",
        "算法",
        "后处理算法",
        "多帧降噪 / MFNR",
        "Multi-Frame Noise Reduction。拍摄多张短曝光帧并完成对齐、融合，在尽量保留细节的同时降低随机噪声。主要用于 HDR 关闭或场景未进入 HDR / Super Night 的普通拍照链路，尤其是中低照静态场景；运动场景可能切换到更短取帧或其他策略。",
        "按模式、摄像头和亮度区间确认 MFNR 是否生效，并记录与 HDR、Super Night、Motion Capture 的互斥或切换条件；仅存在多帧库不等于当前场景进入 MFNR。人像链路使用 UW 作为 depth 辅助输入不等于 UW 可独立出图，项目 FL 的 UW 列仍按用户可选输出摄像头判断。",
        "依赖 AE/场景检测、运动检测、ZSL 多帧缓存、帧对齐与融合、降噪参数和内存性能预算。",
        "在正常光、中低照、HDR 场景、超级夜景阈值附近及运动场景拍摄，结合算法 tag 确认 MFNR 的生效区间、帧数和切换策略，并检查噪声、细节、鬼影和耗时。",
    ),
    row(
        "照片 / 人像 / 夜景",
        "功能",
        "系统 / System",
        "Ultra HDR",
        "支持 Google 通用 Ultra HDR 照片格式编码。文件包含兼容 SDR 显示的基础图像及 HDR gain map / 相关元数据，支持的查看器可还原更高动态范围，不支持的查看器仍按 SDR 显示。",
        "成片按 Google Ultra HDR 兼容格式完成编码，且在支持与不支持 Ultra HDR 的查看器中分别呈现正确的 HDR 和 SDR 结果时填写支持。",
        "依赖 HDR 成像结果、Ultra HDR 编码器、gain map 和元数据写入、相册/系统查看器兼容性。",
        "拍摄高动态范围场景，检查文件编码、gain map / 元数据；分别在支持 Ultra HDR 和仅支持 SDR 的查看器中验证显示兼容性。",
    ),
    row(
        "照片 / 人像 / 夜景",
        "算法",
        "后处理算法",
        "人脸畸变矫正",
        "针对广角画面边缘人脸被拉宽、拉长或形变的问题，通过人脸检测和关键点定位对人脸区域做局部几何形变矫正，同时尽量保持背景结构自然。它只处理人脸区域，不等同于整幅画面的光学畸变矫正。",
        "当前模式和摄像头启用人脸检测/关键点，并在人脸位于大视场角边缘时调用局部人脸形变矫正链路，才填写支持。人像链路内部使用 UW 辅助 depth 不代表用户可从 UW 出图，不得因此把人像 FL 的 UW 列标为支持。",
        "依赖人脸检测与关键点、镜头视场角/标定信息、局部图像 warp、多人脸冲突处理。",
        "将单人和多人放在画面中心、边缘及角落拍摄，对比开关或算法 tag，检查脸型比例、边缘连续性、背景形变和多人一致性。",
    ),
    row(
        "照片 / 夜景 / 专业",
        "算法",
        "后处理算法",
        "LDC / 光学畸变矫正",
        "根据镜头标定参数对整幅画面的桶形、枕形等几何畸变进行矫正，主要用于超广角等大视场角镜头；矫正通常伴随画面裁切和视场角变化。它处理镜头造成的全局几何畸变，不等同于人脸畸变矫正。",
        "摄像头存在需要矫正的镜头几何畸变，且当前模式的预览或成片链路加载对应标定参数和 LDC/几何矫正模块时填写支持。",
        "依赖镜头畸变标定、LDC/几何 warp、输出裁切策略以及预览和成片链路一致性。",
        "使用网格、建筑直线和画面边缘目标分别检查预览与成片，确认直线弯曲得到修正，同时记录裁切、视场角、边缘拉伸和分辨率损失。",
    ),
    row(
        "照片",
        "功能",
        "右侧暂态开关",
        "AI Zoom 开关 / AI Zoom Switch",
        "右侧暂态控制开关，用于让用户启用或关闭高倍率拍摄中的 AI Zoom 增强；它是 AIGC SR/AISR 算法的交互入口，不代表算法能力本身。",
        "仅当项目具备 30x+ 变焦能力、平台达到 SM7750 级及以上，并接入 AISR/AI Zoom 算法时填写支持。",
        "依赖长焦/高倍裁切链路、SM7750 级平台能力、AISR/AI Super Zoom 算法、右侧暂态开关 UI。",
        "在 30x 以上场景确认 AI Zoom 暂态开关出现；点击后拍摄高细节目标，检查成片清晰度和生成伪影。",
    ),
    row(
        "照片",
        "功能",
        "左侧暂态开关",
        "自动微距控制",
        "左侧暂态开关。近距离对焦时，如果项目支持 fallback，可提示/控制自动切换到更近对焦距离的摄像头。",
        "仅 fallback 机型填写支持；不支持 fallback 的项目不应出现该开关。",
        "依赖 fallback 能力、可承担微距的摄像头、近距检测、左侧暂态开关 UI。",
        "近距离拍摄目标，确认开关出现；关闭后确认不再自动切换微距/近距摄像头。",
    ),
    row(
        "照片",
        "功能",
        "右侧暂态开关",
        "自动夜景开关 / Auto Night Switch",
        "右侧暂态控制开关。低照且夜景算法效果优于普通拍照时出现，用户未关闭时按 Super Night 链路拍照；它是控制入口，不代表超级夜景算法本身。",
        "照片模式具备低照检测、夜景收益判断和 Super Night 链路时填写支持。",
        "依赖低照/场景检测、AE 策略、Super Night 算法、右侧暂态开关 UI。",
        "在低照场景确认夜景暂态开关出现；拍照后检查算法 tag、曝光时间和成片效果。",
    ),
    row(
        "照片",
        "功能",
        "右侧暂态开关",
        "Text Mode（文本模式）",
        "右侧暂态开关。预览识别到文本后弹出，点击后框选文本边缘，做透视矫正并增强文本清晰度。",
        "项目支持文本检测、边缘检测、透视矫正和文本增强，并在检测到文本时弹出右侧暂态开关时填写支持。",
        "依赖文本检测、文本边缘检测、透视矫正、文本增强算法、右侧暂态开关 UI。",
        "用照片模式预览文档/文字内容，确认开关出现；点击后确认边缘框选、透视矫正和清晰度增强。",
    ),
    row(
        "照片 / 夜景",
        "功能",
        "Toolbar",
        "Flash",
        "工具栏补光入口。照片后置可支持 Off / On / Torch，前置无物理闪光灯时使用屏幕补光并可提供 Auto；Glyph 补光仅适用于具备对应硬件的项目。夜景是否开放补光需独立按项目判断，不能继承照片模式结论。",
        "按模式、摄像头位置和硬件判断：后置依赖 LED flash，前置依赖屏幕补光，Glyph 依赖对应灯效硬件；夜景还需确认补光是否允许进入 Super Night 曝光与多帧链路。",
        "依赖 LED flash、屏幕补光、Glyph 硬件/项目配置、Toolbar UI、夜景曝光与多帧策略及模式状态隔离。",
        "逐模式、逐前后摄检查 Flash 入口和选项；验证后置 Off/On/Torch、前置屏幕补光/Auto，并确认夜景模式的入口、状态隔离和实际补光行为符合项目规格。",
    ),
    row(
        "视频 / 慢动作 / 延时摄影 / 前后双录",
        "功能",
        "Toolbar",
        "录影灯 / Recording Light",
        "录制状态指示能力。开始录制后，通过机身后侧录影灯/Glyph 指示当前正在录像，停止录制后关闭。Nothing 品牌项目默认支持所有后置摄像头录制场景（Main/UW/Tele），Front 不在默认支持范围。需确认常亮/闪烁方式、启停时序、模式切换和异常退出后的灯效状态。",
        "项目品牌为 Nothing，且具备后侧录影灯/Glyph 指示硬件与录制状态联动时，后置摄像头默认填写支持；Front 不从品牌默认规则推断支持。",
        "依赖后侧录影灯/Glyph 硬件、录制状态回调、灯效控制、模式与异常状态清理。",
        "分别使用每个后置摄像头开始、暂停/停止录制，确认录影灯按定义亮起/闪烁并及时关闭；检查切换模式、锁屏、来电或异常退出后无错误残留。",
    ),
    row("照片", "功能", "Toolbar", "Timer", "倒计时入口，支持 Off / 3s / 10s。", "照片模式提供倒计时拍照入口时填写支持。", "依赖延迟触发、倒计时 UI。", "切换 Off / 3s / 10s 后拍照，确认延迟触发。"),
    row(
        "照片",
        "功能",
        "Toolbar",
        "HDR 开关 / HDR Switch",
        "照片工具栏中的 HDR 控制开关。当前项目只有 Auto / Off，无强制 On；它只描述用户控制入口，不代表 RAW HDR、Ultra HDR 或其他具体 HDR 算法。不同项目中 Auto/Off 对应的算法链路可能不同。",
        "只按 Auto / Off 两种状态写功能；具体算法链路必须按项目算法文档确认。",
        "依赖 HDR 检测/决策、MFNR、RAW HDR/HDR 算法、Toolbar UI。",
        "切换 Auto / Off，在普通和高动态场景拍照，确认 UI 状态、算法 tag 和成片动态范围。",
    ),
    row("照片", "功能", "Toolbar", "Exposure", "全局曝光调节，范围 -2EV 到 +2EV，步进 0.3EV。", "当前模式提供全局 EV 调节滑杆时填写支持。", "依赖 AE/EV 控制、预览曝光同步、slider UI。", "调节 -2/0/+2 EV，确认预览和成片亮度变化。"),
    row("照片", "功能", "Toolbar", "Filter", "内置滤镜和用户导入滤镜入口；不在 KB/FL 展开每个滤镜名。", "支持内置 LUT、滤镜强度或用户导入 LUT 时填写支持。", "依赖滤镜/LUT 渲染、导入管理、filter 管理文档。", "选择内置和导入滤镜，确认预览/成片效果；具体列表看 filter 文档。"),
    row(
        "视频 / 前后双录",
        "功能",
        "风格-滤镜 / Style-Filter",
        "风格-滤镜 / Style-Filter",
        "视频 LUT 滤镜能力。当前风格/LUT pipeline 仅支持 1080P 30FPS；1080P 60FPS、4K 30FPS、4K 60FPS 及 HLG/HDR 视频规格均不支持。摄像头列只表示该摄像头在 1080P30 下是否具备该能力。",
        "仅当当前摄像头可在普通 SDR 1080P 30FPS 视频链路中加载并输出滤镜/LUT 效果时填写支持；其他视频规格不得由摄像头列的勾选推断为支持。",
        "依赖 1080P30 视频 pipeline、LUT/滤镜渲染、预览与录像输出链路、规格互斥 UI。",
        "在 1080P30 下验证预览和成片滤镜一致；切换 1080P60、4K30、4K60、HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。",
    ),
    row(
        "视频 / 前后双录",
        "功能",
        "风格-调色 / Style-Tuning",
        "风格-调色 / Style-Tuning",
        "视频风格调色能力。当前风格/LUT pipeline 仅支持 1080P 30FPS；1080P 60FPS、4K 30FPS、4K 60FPS 及 HLG/HDR 视频规格均不支持。摄像头列只表示该摄像头在 1080P30 下是否具备该能力。",
        "仅当当前摄像头可在普通 SDR 1080P 30FPS 视频链路中应用调色参数并正确写入成片时填写支持。",
        "依赖 1080P30 视频 pipeline、调色参数/LUT 渲染、预览与录像输出链路、Preset 和规格互斥 UI。",
        "在 1080P30 下验证预览、成片、参数和 Preset；切换其他帧率、分辨率或 HLG/HDR 时确认入口禁用、隐藏或提示切回 1080P30。",
    ),
    row(
        "视频 / 前后双录",
        "功能",
        "风格-调色盘 / Style-Tuning Palette",
        "风格-调色盘 / Style-Tuning Palette",
        "视频风格调色盘子能力，通过 Palette Mode 调整风格效果。它使用同一风格/LUT pipeline，因此仅支持 1080P 30FPS，不支持 1080P60、4K30、4K60 或 HLG/HDR 视频规格。",
        "仅当当前摄像头在普通 SDR 1080P 30FPS 下可进入调色盘、实时预览并把效果写入视频时填写支持。",
        "依赖 1080P30 视频 pipeline、Palette Mode、LUT/调色渲染、预览与录像输出链路、规格互斥 UI。",
        "在 1080P30 下验证调色盘交互、预览和成片；切换其他视频规格时确认入口禁用、隐藏或提示切回 1080P30。",
    ),
    row("照片", "功能", "Toolbar", "Tuning", "Preset 2.0 / Tuning Palette 七参数调节。", "七个参数能写入预览/成像或 Preset 时填写支持。", "依赖 Tuning Palette、参数渲染链路、Preset 保存。", "分别调节七个参数，确认预览/成片变化，并验证可存入 Preset。"),
    row("照片", "功能", "Toolbar", "Motion Photo", "动态照片入口；摄像头范围、录音、片段截取等差异写说明，不默认拆行。", "项目支持 Motion Photo 拍摄时填写支持。", "依赖预录缓存、封面帧选择、动态照片封装。", "开启 Motion Photo 后拍摄，确认相册中可播放动态照片。"),
    row(
        "照片",
        "功能",
        "Toolbar",
        "动态照片 - 无效信息截取",
        "动态照片子能力。根据快门动作和有效内容区间，从动态照片视频片段中裁掉用户按下快门后快速移开设备等造成的无效尾帧，保留可观看的有效片段。",
        "项目的 Motion Photo 链路具备无效片段识别与裁剪能力，且该能力需要独立验收时填写支持。",
        "依赖 Motion Photo 预录/后录缓存、快门时序、有效片段判断、视频裁剪和动态照片封装。",
        "开启 Motion Photo 拍摄后快速移开设备，检查相册播放片段是否裁掉无效尾帧，同时确认正常拍摄不会误裁有效内容。",
    ),
    row(
        "照片",
        "功能",
        "Toolbar",
        "动态照片-视频支持录制声音",
        "动态照片子能力。拍摄 Motion Photo 时为动态视频片段同步录制环境声音，并在动态照片封装和相册播放时保留音频。",
        "项目的 Motion Photo 链路支持音频采集、封装和播放，且产品范围允许动态照片携带声音时填写支持。",
        "依赖麦克风权限、音频采集、音画同步、动态照片封装、相册播放和隐私/静音策略。",
        "分别在允许和拒绝麦克风权限、系统静音及不同环境声场景拍摄，确认音频、音画同步、权限提示、静音策略和相册播放符合规格。",
    ),
    row("照片", "功能", "Toolbar", "Motion Photo cover HDR", "动态照片封面帧 HDR 支持，可作为单独验收点。", "Motion Photo 封面帧可输出或显示 HDR/Ultra HDR 时填写支持。", "依赖 Motion Photo、HDR/Ultra HDR 输出、查看器显示能力。", "HDR 场景拍摄动态照片，确认封面帧 HDR 信息和显示效果。"),
    row(
        "照片",
        "算法",
        "后处理算法 / Post-processing Algorithm",
        "动态照片插帧 / Motion Photo Frame Interpolation",
        "动态照片封面 HDR 链路中的插帧算法，用于生成或补充封面处理所需的时序信息，在保留快门时刻主体状态的同时改善封面帧的 HDR 效果。它不是相册侧的封面重选或封面帧增强功能。",
        "项目 Motion Photo 的封面 HDR 明确接入插帧算法，且当前摄像头拍摄后实际生成 HDR 封面时填写支持；仅支持普通 Motion Photo 或仅支持相册重选封面不等同于支持。",
        "依赖 Motion Photo 前后帧缓存、时序对齐、运动检测、HDR 封面生成、内存与处理耗时预算。",
        "逐摄像头在静态、高动态、人物运动和手持移动场景拍摄动态照片，结合算法日志确认插帧与封面 HDR 生效，并检查快门时刻一致性、运动伪影、鬼影、动态范围和保存耗时。",
        "开发算法清单名称为 Live photo（插帧）；Travis 确认其对应动态照片封面 HDR 算法，不包含相册侧封面重选。",
    ),
    row("照片", "功能", "Toolbar", "Quality", "输出像素数量选择，常见为 20MP / 50MP；支持 200MP 的项目增加 200MP。", "按 sensor 输出、ISZ/crop、高像素/200MP 链路判断可选档位。", "依赖 sensor 输出规格、ISZ/crop、高像素/200MP 链路、内存和耗时。", "切换各像素档位，确认入口、成片分辨率、处理耗时和互斥关系。"),
    row(
        "照片 / 人像 / 运动 / 夜景 / 全景 / 专业 / 高像素",
        "功能",
        "Toolbar",
        "Grid",
        "预览构图辅助线开关，帮助用户判断水平、垂直和主体位置；默认关闭，开启后只影响预览叠加，不写入成片。25111 MP1.5 基线在切换模式、摄像头、图库/设置、前后台及安全相机场景均记忆当前状态。",
        "当前模式提供可开关的构图网格，并能在预览稳定叠加且不进入成片时填写支持；目标项目需确认默认值和九场景记忆规则是否沿用基线。",
        "依赖预览 overlay、Toolbar UI、设置状态保存和模式/摄像头切换时的状态恢复。",
        "默认关闭时确认网格不显示；开启后确认预览显示且成片不包含网格，并覆盖切换模式、切换摄像头、进入图库/设置、前后台 5 分钟内外和安全相机验证记忆/重置行为。",
        "记忆规则基线：knowledge/reference/memory-mutex.json；来源为 Camera 互斥记忆默认值列表 v2.0.xlsx。",
    ),
    row("照片", "功能", "Toolbar", "Ratio", "画幅比例入口，支持 1:1 / 4:3 / 16:9 / Full；50MP 等最大像素输出时不支持切换。", "支持画幅裁切时填写支持；最大像素输出时应禁用或隐藏。", "依赖裁切输出、预览比例适配、Quality 互斥策略。", "普通质量下切换比例；切到最大像素后确认 Ratio 不可切换。"),
    row("照片", "功能", "Toolbar", "Watermark", "水印快捷入口。点击 On / Off；长按跳转 Settings > Photo > Watermark。", "支持照片水印且工具栏提供快捷入口时填写支持。", "依赖水印渲染、Toolbar 入口、Settings 水印页。", "点击切换并拍照确认；长按进入水印设置页。"),
    row("照片", "功能", "Toolbar", "More settings", "进入 Camera Settings 的工具栏入口。", "Toolbar 提供 More settings 入口时填写支持。", "依赖 Camera Settings 页面和工具栏入口。", "点击 More settings，确认进入 Camera Settings。"),
    row("照片", "功能", "Toolbar", "Glyph Mirror", "使用背面大尺寸 Glyph LED 预览构图，让用户使用后置摄像头自拍。", "仅具备大尺寸 Glyph Mirror 所需硬件并开放该功能的项目支持；已知 25111 Pro 支持，25111 不支持。", "依赖后置大尺寸 Glyph LED、后摄自拍预览策略、Toolbar UI。", "开启 Glyph Mirror 后使用后摄自拍，确认背面 Glyph 预览和拍摄流程。"),
    row(
        "通用",
        "Preset",
        "Preset",
        "Preset",
        "底部独立功能区域，支持默认/自定义 Preset、选择、保存、卡片信息、封面、导入和分享。",
        "项目支持 Camera Preset 能力时填写；不要按每个模式重复写 Preset。",
        "依赖 Preset 配置、默认 Preset 列表、滤镜/Tuning/参数保存恢复、Preset Bitable。",
        "进入底部 Preset 区域，验证选择、保存、导入、分享和卡片展示。",
    ),
    row(
        "通用",
        "Widget",
        "Widget",
        "Preset Widget",
        "桌面相机小组件能力，支持 Preset Widget 2 聚合多个 Preset，并从桌面点击后唤起相机并应用对应 Preset。",
        "项目引入 Camera/Preset Widget、出厂预装 Widget 或支持用户配置 Preset Widget 时填写支持。",
        "依赖系统 Widget 框架、Preset 列表、Widget 配置页、相机冷启动/唤起参数和 Preset 应用链路。",
        "添加或使用预装 Preset Widget，选择最多 5 个 Preset，点击不同卡片唤起相机，确认应用的 Preset、顺序同步、空状态和上限提示符合规格。",
        "参考 `knowledge/reference/preset/preset-widget-2.0.md`。",
    ),
    row("通用", "Settings", "General settings", "Save location", "保存位置设置。", "Settings > General 存在保存位置设置时填写。", "依赖存储权限、可用存储位置、Settings UI。", "进入设置切换保存位置，确认照片/视频保存路径。"),
    row("通用", "Settings", "General settings", "Shutter sound", "快门声音设置，部分地区/SKU 可能强制开启。", "Settings > General 提供快门声设置或存在地区策略时填写。", "依赖地区/SKU 策略、音频播放、Settings UI。", "切换快门声并拍照验证；地区 SKU 验证强制策略。"),
    row("通用", "Settings", "General settings", "Mirror front camera", "前置镜像设置，影响前置拍照/录像输出方向。", "Settings > General 提供前置镜像设置时填写。", "依赖前置摄像头、镜像处理、Settings UI。", "切换后用前置拍摄，确认输出方向。"),
    row("通用", "Settings", "General settings", "Level", "水平仪/水平辅助线设置。", "Settings > General 提供 Level 设置时填写。", "依赖姿态传感器、预览叠加层、Settings UI。", "开启后旋转设备，确认水平辅助显示和随姿态变化。"),
    row("通用", "Settings", "Photo settings", "Auto Tone", "照片类模式的色调处理设置，会影响 still photo 出片效果。", "Settings > Photo 存在 Auto Tone，且会影响照片输出时填写。", "依赖照片色调处理策略、Settings UI、成像链路。", "开关 Auto Tone 后拍摄相同场景，确认色调变化。"),
    row(
        "通用",
        "Settings",
        "Photo settings",
        "影像基调 / Image Tone",
        "Camera Settings 中的全局影像基调设置，作用于支持的静态照片成像 pipeline，不在各模式 Toolbar 中重复提供入口。提供自然与标准两种基调，默认标准：自然强调接近真实的饱和度和对比度，标准提供更鲜明、略高饱和度和对比度的效果；首次开启相机时显示选择提示。",
        "Settings > Photo 提供影像基调设置，且选择结果会统一应用于支持的照片类模式时填写支持；模式内不得重复展开该功能行。",
        "依赖 Settings UI、首次启动引导、配置持久化、静态照片色彩处理 pipeline，以及与 Auto Tone、滤镜、调色、Preset 和 Ultra HDR 的优先级策略。",
        "首次启动相机验证影调提示；在 Settings > Photo 切换自然/标准，确认默认值和持久化，并逐摄像头验证预览与成片效果；检查各照片类模式 Toolbar 中不存在重复入口。",
    ),
    row(
        "通用",
        "Settings",
        "Photo settings",
        "色彩模式 / Color Mode",
        "Camera Settings 中的全局照片色彩处理设置，用于选择项目定义的成片色彩处理策略。入口仅位于 Settings > Photo，不再出现在任何模式的 Toolbar；修改后应用于支持的拍照类模式和摄像头。需确认选项、默认值、持久化，以及与 Auto Tone、影像基调、滤镜/调色和 Ultra HDR 的优先级。",
        "项目在 Settings > Photo 提供全局色彩模式设置，并能按配置影响支持的拍照类成片链路时填写支持；模式 Toolbar 中不得重复提供入口。",
        "依赖 Settings UI、色彩处理 pipeline、配置持久化，以及 Auto Tone/影像基调/滤镜/调色/Ultra HDR 的互斥与叠加策略。",
        "进入 Settings > Photo 切换色彩模式，确认各拍照类模式 Toolbar 中不存在该入口；逐摄像头拍摄并检查设置生效、默认值、持久化及与 Auto Tone、影像基调、滤镜/调色、Ultra HDR 的关系。",
    ),
    row("通用", "Settings", "Photo settings", "Watermark settings", "水印详细设置，包括样式和自定义信息。", "Settings > Photo 提供 Watermark 设置且会写入照片输出时填写。", "依赖水印渲染、照片输出链路、Settings UI。", "调整水印设置后拍照，确认成片水印内容和样式。"),
    row("通用", "Settings", "Photo settings", "Tap to take a photo", "点击预览区域触发拍照的设置。", "Settings > Photo 提供该开关且开启后点击预览可拍照时填写。", "依赖预览触控事件、快门触发链路、Settings UI。", "开启后点击预览区域，确认触发拍照。"),
    row("通用", "Settings", "Photo settings", "QR code scanner", "二维码扫描设置，控制预览中二维码识别和跳转提示。", "Settings > Photo 提供 QR code scanner 设置，且开启后可识别二维码时填写。", "依赖二维码检测/识别、预览浮层、Settings UI。", "开启后对准二维码，确认识别浮层和点击跳转。"),
    row("通用", "Settings", "Photo settings", "Press and hold shutter", "长按快门行为设置，如连拍或快录。", "Settings > Photo 提供长按快门行为选项时填写；快门按键本身不作为 KB 功能行。", "依赖快门长按事件、连拍/快录链路、Settings UI。", "切换选项后长按快门，确认行为符合设置。"),
    row("通用", "Settings", "Photo settings", "Ultra XDR", "照片设置中的产品开关名称。用于控制拍照模式是否输出 Google 通用 Ultra HDR 格式；模式内实际编码能力统一称为 Ultra HDR。", "Settings > Photo 提供 Ultra XDR 开关，且开关会控制 Ultra HDR 格式输出时填写。", "依赖 Ultra HDR 编码能力、相册/系统查看器兼容性、Settings UI 和配置持久化。", "分别开启和关闭后拍摄高动态范围场景，检查 Ultra HDR 编码/gain map 是否随设置生效，并验证设置持久化。"),
    row("通用", "Settings", "Video settings", "Video encoding", "视频编码设置，用户可选择 H.264 或 H.265。", "Settings > Video 提供 H.264/H.265 选择或项目默认编码策略变化时填写。", "依赖平台视频编码器、视频录制链路、Settings UI。", "切换 H.264/H.265 后录制视频，确认文件编码格式。"),
    row("通用", "Settings", "Video settings", "Power saving recording", "省电录制。设备静止时自动关闭预览屏幕以节省功耗。", "Settings > Video 提供该设置且静止录制场景会触发省电策略时填写。", "依赖运动/静止检测、录制状态、屏幕控制、省电策略。", "开启后开始录制并保持设备静止，确认预览屏幕关闭且录制不中断。"),
    row("通用", "Settings", "Video settings", "Auto FPS", "自动帧率设置，用户可选择 Off、Auto 30 FPS、Auto 30 & 60 FPS。", "Settings > Video 提供 Auto FPS 并能根据场景/光照调整视频帧率时填写。", "依赖视频帧率策略、AE/低照判断、平台视频规格。", "切换 Off / Auto 30 / Auto 30&60，在不同光照场景录制并确认帧率策略。"),
    row("通用", "Settings", "Video settings", "视频防抖开关", "视频设置项。用于控制支持 EIS 的视频录制规格是否启用电子防抖，默认开启。", "Settings > Video 提供视频防抖开关，且当前视频模式/规格支持 EIS 时填写。", "依赖 EIS 算法、视频规格、Settings UI、录制链路和默认开关策略。", "进入 Settings > Video 切换视频防抖开关，在支持 EIS 的规格下录制并确认防抖开关生效；在不支持规格下确认置灰或隐藏策略。"),
    row("通用", "Settings", "Video settings", "锁定镜头", "视频设置项。开启后录制中禁用 SAT，不切换物理镜头，后续变焦保持当前镜头并走数码变焦。", "Settings > Video 提供锁定镜头开关，且项目继承或新增录制中锁定物理镜头能力时填写。", "依赖 SAT/变焦策略、视频录制链路、Settings UI 和当前镜头可用倍率范围。", "开启锁定镜头后开始录制，跨镜头倍率点变焦，确认不发生物理镜头切换且录制不中断。", "待确认：目标项目是否继承该基线能力仍需 Product / HAL SE 确认。"),
    row("通用", "Settings", "Video settings", "锁定白平衡", "视频设置项。默认关闭；录制开始后锁定起始白平衡，录制过程中不随场景色温变化重新收敛。", "Settings > Video 提供锁定白平衡开关，且视频链路支持录制起始 WB 锁定时填写。", "依赖 AWB/WB 锁定策略、视频录制链路、Settings UI，以及与手动白平衡调节的优先级规则。", "开启锁定白平衡后在不同色温光源间移动录制，确认白平衡保持起始状态；关闭后确认 WB 正常收敛。"),
    row("通用", "Settings", "Help & Support", "Tips and feedback", "Camera Settings 中的帮助与反馈入口，跳转系统 Tips and feedback；Camera 内不自建反馈表单。", "Settings 页面提供 Tips and feedback 入口时填写。", "依赖系统 Tips and feedback 页面、Settings UI 和跳转返回链路。", "进入 Camera Settings 点击 Tips and feedback，确认跳转系统帮助/反馈入口，并能返回 Camera。"),
    row("夜景 / 照片", "算法", "后处理算法", "超级夜景", "低照拍照核心算法链路；夜景模式直接使用，照片模式可由自动夜景暂态开关触发。", "低照检测、曝光策略和算法配置允许进入 Super Night 链路时填写。", "依赖低照检测、Super Night 算法、多帧合成、AE/曝光策略。", "低照场景拍摄，确认算法 tag、曝光时间、噪声、亮度和细节。"),
    row("夜景", "算法", "后处理算法", "极夜", "极低照增强分支，用于比普通夜景更暗的场景。", "亮度低于极夜阈值且摄像头、曝光、防抖、平台能力满足要求时填写。", "依赖极低照检测、极夜算法、多帧合成、平台算力。", "极低照场景拍摄，确认亮度、噪声、细节和伪影控制。"),
    row(
        "夜景 / 人像",
        "算法",
        "后处理算法",
        "超级夜景+美颜",
        "面向低照人脸拍摄的组合后处理能力，在超级夜景提升主体与背景亮度、噪声和细节的同时应用人脸美颜，使暗光人像保持自然肤色和纹理，并降低多帧合成与美颜叠加造成的鬼影、塑料感或边缘异常。",
        "当前输出摄像头同时接入 Super Night、人脸检测和美颜链路，并允许低照人脸策略叠加时填写支持。人像链路内部使用 UW 辅助 depth 不代表 UW 可独立出图，项目 FL 的 UW 列仍应按用户可选输出摄像头判断。",
        "依赖 Super Night、多帧对齐、人脸检测、美颜算法、低照人脸策略，以及人物运动和多人场景下的融合稳定性。",
        "在不同低照等级覆盖单人、多人、运动人物和画面边缘人脸，结合算法 tag 确认夜景与美颜同时生效，并检查肤色、纹理、噪声、鬼影、虚化/发丝边缘和处理耗时。",
    ),
    row("高像素 / 夜景", "算法", "后处理算法", "Remosaic", "将 Quad Bayer、Tetra、Nonacell 等多像素合一 Sensor 的 CFA 像素排列重建为全分辨率 Bayer/图像，用于原生 50MP、200MP 等高像素输出。Remosaic 不等同于把低分辨率图像简单 upscale；实现可位于 Sensor、ISP 或软件链路。", "按项目、摄像头、输出档位和场景确认实际使用 Sensor/HW remosaic、ISP/软件 remosaic，还是 binning 后算法 upscale；只有明确进入 remosaic 路径时填写支持。", "依赖 Sensor CFA/输出模式、remosaic 实现、ISP/软件链路、内存、处理耗时和高像素产品配置。", "逐摄像头、逐高像素档位并覆盖高亮/中亮/低照场景拍摄，结合 Sensor mode 和算法 tag 确认实际路径、输出分辨率、耗时、内存及伪色/摩尔纹。"),
    row(
        "高像素",
        "算法",
        "后处理算法 / Post-processing Algorithm",
        "TF 50MP HDR/MMF",
        "高像素 50MP 档位的 HDR/MMF 成像链路，通过多帧融合改善高像素照片的动态范围、噪声和细节质量；它是高像素模式中的具体算法路径，不等同于 50MP 规格入口本身。",
        "当前项目、摄像头和 50MP 档位明确进入 TF 50MP HDR/MMF 链路时填写支持；仅具备 50MP Sensor 输出或普通 Remosaic 不等同于支持。",
        "依赖 50MP Sensor 输出或重建输入、TF HDR/MMF、帧对齐融合、运动检测、内存、处理耗时与功耗预算。",
        "在 50MP 档位覆盖高亮/低动态、逆光、中低照和运动场景，结合算法日志确认 HDR/MMF 路径，检查输出分辨率、动态范围、噪声、细节、鬼影、耗时、内存和功耗。",
        "开发算法清单：TF 50MP HDR/MMF 高像素成像链路。",
    ),
    row("视频 / 前后双录", "功能", "前后翻转 / Camera Switch", "录制中前后置切换 / Front-Rear Switch While Recording", "视频录制过程中不中断录制地切换前置与后置摄像头。该功能属于前后翻转能力，不属于模式栏。", "项目明确支持录制中切换前后置摄像头且不中断录制时填写；需与前后双录中的主副画面互换区分。", "依赖录制中摄像头切换链路、编码连续性、音视频同步、预览恢复和独立切换 UI。", "普通视频及前后双录分别验证录制中前后置切换，确认录制不中断、时间轴连续、音画同步、预览与文件正常。"),
    row(
        "视频", "功能", "视频规格 / Video Specs", "视频规格 / Video Specs",
        "视频输出分辨率、帧率和 HDR/HLG 组合的规格族。项目 FL 必须把 1080P30、1080P60、4K30、4K60 及对应 HLG 组合拆成独立验收行，并按每颗摄像头填写支持；规格越高通常带来更高细节或流畅度，也会增加编码带宽、功耗和温升。25111 MP1.5 基线默认 1080P30，规格选择在九种标准场景中记忆。",
        "先按平台编码能力和 Sensor mode 生成候选规格，再按摄像头、EIS、HDR/HLG、风格/LUT、Log、功耗和温升限制逐行裁剪；项目级支持某规格不等于所有摄像头支持。",
        "依赖 Sensor 输出模式、ISP/视频 pipeline、编码器、存储带宽、EIS/HDR/HLG/风格兼容性，以及功耗和温升预算。",
        "逐摄像头选择每个可见规格录制，检查文件分辨率、帧率、HDR/HLG 元数据、画质、EIS、变焦、音画同步、长录稳定性、功耗和温升；同时验证默认 1080P30 与规格记忆规则。",
        "记忆规则基线：knowledge/reference/memory-mutex.json；目标项目默认值与记忆差异需确认。",
    ),
    row(
        "慢动作", "功能", "慢动作规格 / Slow Motion Specs", "慢动作规格 / Slow Motion Specs",
        "慢动作录制的分辨率与高帧率规格族。项目 FL 按 1080P120、1080P240、720P120/240/480 等实际候选规格独立展开；更高帧率可放慢快速运动，但会降低可用曝光时间并提高带宽、光照和温升要求。25111 MP1.5 基线默认 1080P120，规格选择在九种标准场景中记忆。",
        "仅当 Sensor 高帧率模式、平台 pipeline 和编码/封装链路共同支持时填写；必须逐摄像头确认，不能从平台最大帧率或旧项目勾叉推导 Tele/UW/Front 支持。",
        "依赖 Sensor high-speed mode、ISP/内存带宽、编码封装、AE 曝光、存储、功耗和温升预算。",
        "逐规格和摄像头录制高速运动，核对文件分辨率、采集帧率和播放时长，检查曝光、清晰度、掉帧、闪烁、温升和长录稳定性，并验证默认规格与记忆规则。",
        "记忆规则基线：knowledge/reference/memory-mutex.json；目标项目默认值与记忆差异需确认。",
    ),
    row(
        "延时摄影", "功能", "视频规格 / Video Specs", "延时摄影规格 / Timelapse Specs",
        "延时摄影输出分辨率与采样倍速的规格族，用较低采样频率压缩长时间过程并输出视频。项目 FL 应把 1080P、4K 等输出规格和需要独立确认的倍速范围表达清楚。25111 MP1.5 基线默认 1080P30、15x，规格与倍速按各自记忆规则处理。",
        "按平台长时间录制、Sensor/编码规格、倍速调度、存储、功耗和温升能力生成项目范围；每颗摄像头和输出规格需单独确认。",
        "依赖定时采样、视频编码、倍速调度、长时间 AE/AWB 稳定、存储空间、功耗和温升控制。",
        "逐摄像头、输出规格和倍速录制，核对采样间隔、输出分辨率/帧率、时长换算、画面连续性、长录稳定性，并验证默认值与记忆/重置规则。",
        "记忆规则基线：knowledge/reference/memory-mutex.json；目标项目默认值与记忆差异需确认。",
    ),
    row(
        "高像素", "功能", "高像素规格 / High Resolution Specs", "高像素输出规格 / High Resolution Specs",
        "高像素模式可选择的输出分辨率和质量档位规格族，例如 50MP、200MP、200MP Ultra。它让用户在细节、动态范围、处理时间、文件大小和功耗之间选择；默认返回普通像素输出，25111 MP1.5 基线为关闭高像素/12MP，退出超过 5 分钟或进入安全相机后恢复默认。",
        "按每颗 Sensor 的高像素输出、Remosaic/binning/upscale/HDR 链路和产品选项生成具体档位；不同项目的 Ultra 定义必须来自已评审 PRD，不能仅按名称推断算法。",
        "依赖 Sensor 高像素模式、Remosaic 或场景自适应 upscale/HDR 链路、内存、处理耗时、存储空间和温升预算。",
        "逐档位和摄像头拍摄不同亮度/动态范围场景，核对输出分辨率、实际算法路径、细节、动态范围、耗时、文件大小、内存和温升，并验证默认普通像素输出及记忆/重置规则。",
        "记忆规则基线：knowledge/reference/memory-mutex.json；Ultra 定义和目标项目默认值需按最新版 PRD 确认。",
    ),
    row("视频", "功能", "录制中拍照 / Capture While Recording", "录制中拍照 / Video Snapshot", "视频录制过程中点击拍照入口，在不中断视频录制的情况下输出一张静态照片。当前需求方向是从视频截帧升级为独立拍照流，并保持照片与视频的视场角和色彩一致。", "项目视频链路支持录制中并行输出静态照片时填写；需按摄像头、分辨率、帧率、SDR/HDR、风格和防抖状态确认实际支持范围。", "依赖视频录制链路、并行拍照流或视频帧提取、编码带宽、内存、功耗、快门交互，以及与 HDR、风格和 EIS 的兼容策略。", "逐摄像头和视频规格在录制中拍照，确认视频不中断、不丢帧，照片分辨率、FOV、色彩、时间点、保存耗时和兼容限制符合规格。"),
    row("视频", "功能", "录制中拍照 / Capture While Recording", "录制中拍摄动态照片 / Motion Photo While Recording", "视频录制过程中点击拍照入口，在不中断当前视频录制的情况下生成一张包含静态封面和快门前后动态片段的 Motion Photo。", "只有项目同时支持视频录制、录制中拍照和 Motion Photo 并行采集/封装，且当前摄像头与视频规格允许该组合时填写支持；需确认 SDR/HDR、分辨率、帧率、声音和风格范围。", "依赖视频录制链路、Motion Photo 前后片段缓存、封面取帧、音视频时间戳、动态照片封装、编码带宽、内存、功耗和相册播放能力。", "逐摄像头和视频规格在录制中拍摄动态照片，确认主视频连续、动态照片封面与片段时间点正确、音画同步、相册可播放，并检查掉帧、发热和不支持组合的入口限制。", "项目 RL 新增能力；目标项目支持范围待 Product、APP 和 HAL SE 确认。"),
]


# Nodes present in the current application structure but missing from the old
# FL-derived catalog. These are knowledge nodes first; their FL behaviour is
# defined independently through projection metadata.
CODE_STRUCTURE_ROWS = [
    row(
        "通用", "功能", "启动与入口 / Launch & Entry", "相机启动入口 / Camera Launch Entry",
        "统一描述桌面图标、热启动、锁屏安全相机、快捷方式、语音和 Widget 等进入 Camera 的入口及上下文。",
        "项目暴露对应入口，且入口会改变启动模式、权限、可访问相册范围或恢复策略时记录。",
        "依赖 Activity 路由、Intent、权限、安全上下文和模式恢复。",
        "分别从桌面、锁屏、快捷方式、语音和 Widget 启动，核对模式、权限、返回与相册访问。",
        node_id="kb.launch.entry", parent_id="kb.launch", node_type="入口",
        app_binding="CameraActivity; SecureCameraActivity; CameraShortCutActivity; VoiceCameraActivity; WidgetCameraActivity",
        fl_projection="条件展开", fl_dimensions="项目 / 入口", fl_condition="入口策略、默认模式或安全权限存在项目差异时展开。",
    ),
    row(
        "照片", "功能", "模式栏 / Mode Switch", "照片模式 / Photo Mode",
        "默认静态拍摄模式，承载普通拍照、工具栏、暂态开关和主要计算摄影链路。",
        "ModeIndex.PHOTO 在生产模式数组中可见且可进入时支持。",
        "依赖照片 Mode、摄像头列表、拍照 pipeline、工具栏与后处理算法。",
        "进入照片模式，逐摄像头验证预览、拍摄、保存和模式恢复。",
        node_id="kb.mode.photo", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.PHOTO; NcfPhotoMode", fl_projection="独立行", fl_dimensions="项目 / 摄像头",
        fl_condition="项目是否保留该模式，或可用摄像头存在差异时展开。",
    ),
    row(
        "视频", "功能", "模式栏 / Mode Switch", "视频模式 / Video Mode",
        "普通视频录制模式，承载视频规格、HDR、防抖、录制中拍照、暂停和音频控制。",
        "ModeIndex.VIDEO 在生产模式数组中可见且录制链路可用时支持。",
        "依赖视频 Mode、编码器、音频、规格、EIS/HDR 和存储。",
        "逐摄像头及规格录制，检查开始、暂停、恢复、停止、文件与音画同步。",
        node_id="kb.mode.video", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.VIDEO; NormalVideoMode; CameraVideoMode", fl_projection="独立行",
        fl_dimensions="项目 / 摄像头 / 规格", fl_condition="摄像头或可录规格不同即展开。",
    ),
    row(
        "人像", "功能", "模式栏 / Mode Switch", "人像模式 / Portrait Mode",
        "以人物主体、景深虚化和人像处理为核心的静态拍摄模式。",
        "ModeIndex.PORTRAIT/BOKEH 在生产模式数组中可见，且输出摄像头具备对应人像链路时支持。",
        "依赖人像 Mode、单/双摄虚化、人脸与主体分割。",
        "逐输出摄像头覆盖单人、多人和复杂边缘，验证入口、预览和成片。",
        node_id="kb.mode.portrait", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.PORTRAIT; ModeIndex.BOKEH; BokehMode; BokehModeV2",
        fl_projection="独立行", fl_dimensions="项目 / 摄像头", fl_condition="输出镜头或虚化链路不同即展开。",
    ),
    row(
        "夜景", "功能", "模式栏 / Mode Switch", "夜景模式 / Night Mode",
        "面向低照和极低照场景的独立拍照模式，不等同于照片模式中的自动夜景暂态开关。",
        "ModeIndex.NIGHT 在生产模式数组中可见且 Super Night 链路可进入时支持。",
        "依赖夜景 Mode、低照检测、曝光、多帧与防抖。",
        "逐摄像头在低照和极低照拍摄，核对模式入口、曝光、算法 tag 和成片。",
        node_id="kb.mode.night", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.NIGHT; CameraNightMode", fl_projection="独立行",
        fl_dimensions="项目 / 摄像头", fl_condition="模式入口或摄像头夜景链路不同即展开。",
    ),
    row(
        "慢动作", "功能", "模式栏 / Mode Switch", "慢动作模式 / Slow Motion Mode",
        "以高帧率采集并低速播放的独立视频模式。",
        "ModeIndex.SLOW_MOTION 在生产模式数组中可见，且至少一种高帧率规格可录制时支持。",
        "依赖 high-speed Sensor mode、带宽、编码封装、曝光与温升。",
        "逐摄像头和规格录制高速运动并检查采集帧率、播放倍速、掉帧和温升。",
        node_id="kb.mode.slow_motion", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.SLOW_MOTION; CameraSlowMotionMode", fl_projection="规格展开",
        fl_dimensions="项目 / 摄像头 / 规格", fl_condition="始终按摄像头×分辨率×高帧率候选规格展开。",
    ),
    row(
        "延时摄影", "功能", "模式栏 / Mode Switch", "延时摄影模式 / Timelapse Mode",
        "按采样间隔压缩长时间过程并输出视频的独立模式。",
        "ModeIndex.TIMELAPSE 在生产模式数组中可见且定时采样及长录链路可用时支持。",
        "依赖定时采样、编码、倍速、长录稳定、存储、功耗和温升。",
        "逐摄像头、分辨率和倍速验证采样间隔、输出时长与长录稳定性。",
        node_id="kb.mode.timelapse", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.TIMELAPSE; CameraTimeLapseMode", fl_projection="规格展开",
        fl_dimensions="项目 / 摄像头 / 规格", fl_condition="输出规格或倍速范围不同即展开。",
    ),
    row(
        "全景", "功能", "模式栏 / Mode Switch", "全景模式 / Panorama Mode",
        "引导用户移动设备并拼接多帧图像，生成宽视场照片的独立模式。",
        "ModeIndex.PANORAMA 在生产模式数组中可见且拼接 SDK、方向与输出摄像头可用时支持。",
        "依赖 Panorama Mode、拼接 SDK、陀螺仪、运动引导、曝光锁定和内存。",
        "按支持方向和摄像头完成全景拍摄，检查引导、拼接缝、运动物体、曝光和输出尺寸。",
        node_id="kb.mode.panorama", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.PANORAMA; Morpho Panorama SDK", fl_projection="独立行",
        fl_dimensions="项目 / 摄像头 / 规格", fl_condition="输出摄像头、方向或夜景全景能力不同即展开。",
    ),
    row(
        "专业", "功能", "模式栏 / Mode Switch", "专业模式 / Expert Mode",
        "向用户开放 ISO、快门、白平衡、对焦等手动参数，并可承载 RAW、直方图和专业辅助能力。",
        "ModeIndex.MANUAL 在生产模式数组中可见，且当前摄像头具备可用手动参数时支持。",
        "依赖 Manual Mode、HAL 手动控制、参数 UI、状态记忆和 RAW pipeline。",
        "逐摄像头调节每项参数，核对预览、Capture Result、成片、记忆和互斥。",
        node_id="kb.mode.expert", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.MANUAL; CameraManualMode", fl_projection="父节点汇总",
        fl_dimensions="项目 / 摄像头", fl_condition="专业模式本身一行；参数边界由子规格节点按摄像头条件展开。",
    ),
    row(
        "微距", "功能", "模式栏 / Mode Switch", "微距模式 / Macro Mode",
        "直接使用微距摄像头或近摄链路的独立模式，与照片模式中的自动微距切换是两个不同能力。",
        "ModeIndex.MACRO 可作为生产模式显示且 MacroMode 可进入时支持；只有 Fallback 自动微距不等同于独立模式。",
        "依赖微距摄像头、最近对焦距离、Macro Mode、变焦与切镜策略。",
        "进入微距模式，在不同物距验证对焦、倍率、输出摄像头和模式退出恢复。",
        node_id="kb.mode.macro", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.MACRO; MacroMode", config_gate="mode array / ProductConfig",
        fl_projection="条件展开", fl_dimensions="项目 / 摄像头", fl_condition="仅项目暴露独立微距模式时展开；自动微距保留为独立节点。",
    ),
    row(
        "运动", "功能", "模式栏 / Mode Switch", "运动模式 / Action Mode",
        "面向运动主体的独立模式入口，与照片模式内部的运动抓拍算法不是同一层级。",
        "ModeIndex.MOTION 在生产模式数组中可见且 Motion Mode 可进入时支持。",
        "依赖运动模式、运动检测、快门/曝光策略、对焦与连拍处理。",
        "进入运动模式拍摄不同速度主体，核对入口、快门、对焦、运动清晰度和保存。",
        node_id="kb.mode.action", parent_id="kb.modes", node_type="模式",
        app_binding="ModeIndex.MOTION; MotionCapture", config_gate="mode array / ProductConfig",
        fl_projection="条件展开", fl_dimensions="项目 / 摄像头", fl_condition="项目暴露独立运动模式时展开；算法能力另行判断。",
    ),
    row(
        "照片 / 人像", "功能", "工具栏 / Toolbar", "美颜控制 / Beauty Control",
        "用户可见的美颜开关、档位和参数交互；它负责控制美颜算法，但不等同于算法本身。",
        "当前模式和摄像头显示美颜入口并可改变算法参数时支持。",
        "依赖 Beauty UI、人脸检测、美颜参数、预览与拍照 pipeline。",
        "逐模式和摄像头验证入口显隐、默认值、参数变化、记忆与成片一致。",
        node_id="kb.toolbar.beauty", parent_id="kb.toolbar", node_type="交互",
        app_binding="BeautyMode; Beauty UI nodes", fl_projection="独立行",
        fl_dimensions="项目 / 模式 / 摄像头", fl_condition="入口或参数集在模式/摄像头间不同即展开。",
    ),
    row(
        "人像", "功能", "工具栏 / Toolbar", "虚化控制 / Bokeh Control",
        "用户调节人像虚化强度、光圈或虚化样式的交互控制；与人像虚化算法节点分离。",
        "人像模式显示可调虚化入口并能改变预览或成片参数时支持。",
        "依赖 Bokeh UI、虚化算法、深度/分割和参数记忆。",
        "调整各档位并拍摄，检查预览、成片、默认值、记忆和边缘质量。",
        node_id="kb.toolbar.bokeh", parent_id="kb.toolbar", node_type="交互",
        app_binding="BokehMode; Bokeh UI nodes", fl_projection="独立行",
        fl_dimensions="项目 / 摄像头", fl_condition="输出摄像头或可调范围不同即展开。",
    ),
    row(
        "视频", "功能", "录制控制 / Recording Controls", "视频暂停与恢复 / Video Pause & Resume",
        "视频录制中暂停写入并在恢复后继续同一文件与时间轴。",
        "录制 UI 暴露 pause/resume 且编码封装链路支持同文件继续时支持。",
        "依赖录制状态机、编码器、音频、时间戳和 UI。",
        "录制中多次暂停恢复，检查文件连续性、音画同步、时长与异常恢复。",
        node_id="kb.video.pause_resume", parent_id="kb.capture", node_type="交互",
        app_binding="UiEventProxy.onVideoPause; CameraVideoMode", fl_projection="独立行",
        fl_dimensions="项目 / 规格", fl_condition="项目禁用或特定规格/HDR 组合受限时展开。",
    ),
    row(
        "视频", "功能", "录制控制 / Recording Controls", "视频静音录制 / Video Mute",
        "控制视频录制是否写入环境声音轨。",
        "视频设置提供静音开关，且录制链路按该值启停音频轨时支持。",
        "依赖音频权限、录音器、编码封装和设置状态。",
        "分别开启和关闭静音录制，检查文件音轨、播放、记忆和异常恢复。",
        node_id="kb.video.mute", parent_id="kb.settings.video", node_type="设置",
        app_binding="SettingKeys.KEY_VIDEO_MUTE; CameraVideoMode", fl_projection="独立行",
        fl_dimensions="项目", fl_condition="设置入口、默认值或政策存在项目差异时展开。",
    ),
    row(
        "通用", "Settings", "General settings", "Default gallery / 默认相册",
        "选择 Camera 缩略图和查看动作默认打开的相册应用。",
        "项目支持默认相册切换，且存在可选相册应用时支持。",
        "依赖系统包解析、相册 Intent、设置 UI 和产品门控。",
        "切换默认相册后点击缩略图，确认目标应用、回退和卸载场景。",
        node_id="kb.settings.general.default_gallery", parent_id="kb.settings.general", node_type="设置",
        app_binding="SettingKeys.KEY_DEFAULT_GALLERY; ProductConfig.isSupportDefaultGallerySwitch",
        config_gate="ProductConfig.isSupportDefaultGallerySwitch", fl_projection="独立行",
        fl_dimensions="项目", fl_condition="产品是否开放该设置或默认相册策略不同即展开。",
    ),
    row(
        "通用", "Settings", "General settings", "Storage location / 存储位置",
        "选择照片和视频写入手机存储或项目允许的其他存储位置。",
        "设置项存在且可选存储位置数量大于一时支持。",
        "依赖 StoragePathManager、可用卷、权限、容量与失败回退。",
        "切换每个可见位置拍照和录像，检查文件路径、低空间和拔出回退。",
        node_id="kb.settings.general.storage", parent_id="kb.settings.general", node_type="设置",
        app_binding="SettingKeys.KEY_CAMERA_SAVE_POS; StoragePathManager", fl_projection="独立行",
        fl_dimensions="项目", fl_condition="可用存储位置或默认路径不同即展开。",
    ),
    row(
        "通用", "Settings", "Photo settings", "Fallback macro control / 自动微距设置",
        "控制照片模式是否允许根据物距自动切换到微距链路；不等同于独立微距模式。",
        "项目为 Fallback 宏方案且设置项可见时支持。",
        "依赖微距摄像头、距离/清晰度判断、切镜策略、设置与暂态开关。",
        "切换设置后在近距离场景验证自动切镜、暂态开关和状态记忆。",
        node_id="kb.settings.photo.fallback_macro", parent_id="kb.settings.photo", node_type="设置",
        app_binding="SettingKeys.KEY_FALLBACK_MACRO_CONTROL; NcfPhotoMode",
        config_gate="Fallback macro ProductConfig", fl_projection="独立行",
        fl_dimensions="项目 / 摄像头", fl_condition="仅 Fallback 宏项目展开，并明确实际微距摄像头。",
    ),
    row(
        "通用", "Settings", "General settings", "重置相机设置 / Reset Camera Settings",
        "将相机设置、模式状态和需要清除的记忆项恢复到项目默认值。",
        "Settings 提供重置入口并定义完整重置范围时支持。",
        "依赖 SettingContext、默认值表、Preset/模式状态和确认 UI。",
        "修改各组设置和模式状态后执行重置，逐项核对默认值及不应清除的数据。",
        node_id="kb.settings.reset", parent_id="kb.settings", node_type="设置",
        app_binding="SettingKeys.KEY_RESET_SETTING; Settings UI", fl_projection="独立行",
        fl_dimensions="项目", fl_condition="重置范围或项目默认值不同即展开。",
    ),
]


STRUCTURAL_CHILD_ROWS = [
    row("照片 / 人像 / 视频 / 夜景 / 高像素 / 专业", "功能", "AE/AF", "Touch AE/AF",
        "点击预览位置同时驱动该区域的自动对焦和自动曝光。", "模式允许触控测光，且输出摄像头支持 AF 时判断 AF；固定焦摄像头只判断 Touch AE。", "依赖触控坐标映射、AE、AF 马达/固定焦策略和对焦框 UI。", "逐摄像头点击近远、明暗区域，核对焦点、曝光和 UI。",
        node_id="kb.focus.touch_ae_af", parent_id="kb.focus.auto", node_type="交互", app_binding="UiEventProxy single tap; CameraUIContext AE/AF", fl_projection="条件展开", fl_dimensions="模式 / 摄像头", fl_condition="固定焦或模式禁用 Touch AF 时展开。"),
    row("照片 / 人像 / 视频 / 夜景 / 高像素 / 专业", "功能", "AE/AF", "Face AE/AF",
        "以检测到的人脸作为测光和对焦优先区域。", "当前模式消费人脸框驱动 AE/AF 时支持；固定焦摄像头只有 Face AE。", "依赖人脸检测、AE、AF 与多人优先级。", "覆盖单人、多人、逆光和进出画，检查收敛与主体优先。",
        node_id="kb.focus.face_ae_af", parent_id="kb.focus.auto", node_type="能力", app_binding="face detection result; AE/AF strategy", fl_projection="条件展开", fl_dimensions="模式 / 摄像头", fl_condition="Face AE/AF 消费策略或固定焦差异导致验收不同即展开。"),
    row("照片 / 人像 / 视频 / 夜景 / 高像素 / 专业", "功能", "AE/AF", "Touch AE/AF Lock",
        "长按预览锁定当前曝光与对焦，直至用户解除或上下文变化。", "模式提供长按锁定且 AE/AF 状态机实际保持时支持。", "依赖长按手势、AE/AWB/AF Lock、状态提示和重置策略。", "长按后改变距离与亮度，检查锁定、解除及切模式恢复。",
        node_id="kb.focus.lock", parent_id="kb.focus.auto", node_type="交互", app_binding="UiEventProxy long press focus; AE/AF lock state", fl_projection="条件展开", fl_dimensions="项目 / 模式 / 摄像头", fl_condition="锁定范围、固定焦或重置规则不同即展开。"),
    row("照片 / 人像 / 视频 / 夜景 / 高像素 / 专业", "功能", "AE/AF", "CAF / 连续自动对焦",
        "预览和录制过程中持续跟随距离或主体变化进行自动对焦。", "输出摄像头具有 AF 且模式启用连续对焦策略时支持。", "依赖 AF 马达、CAF 算法、主体/运动检测和模式策略。", "让主体连续远近移动，检查跟焦速度、稳定性和抽动。",
        node_id="kb.focus.caf", parent_id="kb.focus.auto", node_type="能力", app_binding="camera AF mode / continuous focus strategy", fl_projection="条件展开", fl_dimensions="模式 / 摄像头 / 规格", fl_condition="固定焦、视频规格或模式 AF 策略不同即展开。"),
    row("照片 / 人像 / 视频 / 夜景 / 高像素 / 专业", "功能", "AE/AF", "EV 曝光补偿",
        "在自动曝光基准上施加用户曝光补偿。", "模式暴露 EV 控制且 HAL compensation range 非零时支持。", "依赖 AE compensation range/step、滑杆 UI 和状态记忆。", "验证最小、0、最大 EV 的预览、Capture Result 与成片。",
        node_id="kb.focus.ev", parent_id="kb.focus.auto", node_type="规格", app_binding="AE compensation range; exposure UI", fl_projection="条件展开", fl_dimensions="项目 / 模式 / 摄像头 / 规格", fl_condition="范围、步进、入口或记忆不同即展开。"),
    row(ALL_CAPTURE, "功能", "Zoom", "变焦交互 / Zoom Gestures",
        "点击倍率点、滑动变焦条和双指缩放三种用户交互。", "项目显示对应控件或手势且可连续改变 zoom ratio 时支持。", "依赖 zoom UI、gesture、ratio controller 与无障碍策略。", "逐模式验证点击、滑动和双指三种入口的一致性。",
        node_id="kb.zoom.gestures", parent_id="kb.zoom.control", node_type="交互", app_binding="zoom UI/controller; pinch gesture", fl_projection="随父节点", fl_dimensions="模式", fl_condition="默认随 Zoom 父行；只有项目删减某种交互或验收独立时展开。"),
    row(ALL_CAPTURE, "功能", "Zoom", "变焦倍率范围 / Zoom Range",
        "定义每个模式与输出摄像头可见的最小、最大倍率和默认光学点。", "从 camera capability、mode camera list 和 zoom configuration 逐组合取得真实范围。", "依赖 Sensor crop、镜头倍率、ISZ、数字变焦和模式限制。", "逐模式和摄像头核对最小/最大/默认点、成片元数据和越界限制。",
        node_id="kb.zoom.range", parent_id="kb.zoom.control", node_type="规格", app_binding="zoom range config; mode camera capability", fl_projection="规格展开", fl_dimensions="项目 / 模式 / 摄像头 / 规格", fl_condition="倍率范围是摄像头关键差异，按模式×摄像头固定展开。"),
    row(ALL_CAPTURE, "功能", "Zoom", "镜头切换策略 / Lens Switching Strategy",
        "描述跨物理镜头倍率点时使用 SAT 平滑切换、硬切还是锁定当前镜头数码变焦。", "按模式、规格、光照、录制状态和锁定镜头设置判断实际策略。", "依赖 SAT 标定、镜头可用性、zoom controller、录制链路和低照策略。", "跨每个镜头点双向变焦，检查 FOV、曝光、色彩、抖动和录制连续性。",
        node_id="kb.zoom.switch_strategy", parent_id="kb.zoom.control", node_type="能力", app_binding="zoom controller; LockLensZoomController; SAT config", fl_projection="条件展开", fl_dimensions="项目 / 模式 / 摄像头 / 规格", fl_condition="SAT/硬切/锁镜策略不同会直接改变验收结论，必须展开。"),
    row("专业", "功能", "专业参数 / Expert Parameters", "ISO 范围 / ISO Range",
        "专业模式每颗摄像头可手动选择的感光度范围与档位。", "读取 Sensor sensitivity range、HAL 限制和产品裁剪。", "依赖 Sensor、HAL manual sensor control 和参数 UI。", "逐摄像头验证最小/最大/中间档的 Capture Result 与成片。",
        node_id="kb.mode.expert.iso", parent_id="kb.mode.expert.parameter_ranges", node_type="规格", app_binding="CameraManualMode ISO setting", fl_projection="规格展开", fl_dimensions="项目 / 摄像头 / 规格", fl_condition="每颗 Sensor 边界不同，固定展开。"),
    row("专业", "功能", "专业参数 / Expert Parameters", "快门范围 / Shutter Range",
        "专业模式手动曝光时间范围与档位。", "读取 exposure time range，并结合防抖、暗电流和产品限制裁剪。", "依赖 Sensor/HAL manual exposure、OIS 和 UI。", "逐摄像头验证最短、最长和中间档曝光时间。",
        node_id="kb.mode.expert.shutter", parent_id="kb.mode.expert.parameter_ranges", node_type="规格", app_binding="CameraManualMode shutter setting", fl_projection="规格展开", fl_dimensions="项目 / 摄像头 / 规格", fl_condition="每颗 Sensor 边界不同，固定展开。"),
    row("专业", "功能", "专业参数 / Expert Parameters", "白平衡范围 / WB Range",
        "专业模式 AWB 与手动色温范围、档位和锁定行为。", "项目提供手动色温控制且 HAL/算法可应用时支持。", "依赖 AWB、manual color temperature、UI 和 preset state。", "逐摄像头覆盖最低/最高色温与 AWB，核对预览和成片。",
        node_id="kb.mode.expert.wb", parent_id="kb.mode.expert.parameter_ranges", node_type="规格", app_binding="CameraManualMode WB setting", fl_projection="条件展开", fl_dimensions="项目 / 摄像头 / 规格", fl_condition="范围或手动 WB 支持不同即展开。"),
    row("专业", "功能", "专业参数 / Expert Parameters", "手动对焦范围 / Manual Focus Range",
        "专业模式从近焦到无穷远的手动对焦控制。", "摄像头具备 AF 马达且 HAL 支持 lens focus distance 时支持；固定焦摄像头不支持。", "依赖 AF actuator、minimum focus distance、focus UI。", "逐摄像头验证近焦、远焦、无穷远和峰值/放大辅助。",
        node_id="kb.mode.expert.focus", parent_id="kb.mode.expert.parameter_ranges", node_type="规格", app_binding="CameraManualMode manual focus setting", fl_projection="规格展开", fl_dimensions="项目 / 摄像头 / 规格", fl_condition="固定焦与最近对焦距离是关键摄像头差异，固定展开。"),
    row("专业", "功能", "专业参数 / Expert Parameters", "RAW / DNG 输出",
        "专业模式保存 Bayer RAW/DNG，并可与 JPEG 同时输出。", "当前摄像头支持 RAW capability、对应 stream combination 与 DNG 写入时支持。", "依赖 RAW Sensor capability、capture session、DNG creator、存储和耗时。", "逐摄像头拍摄 RAW/JPEG，核对 DNG 元数据、可打开性、配对和保存耗时。",
        node_id="kb.mode.expert.raw", parent_id="kb.mode.expert", node_type="能力", app_binding="CameraManualMode RAW capture; DNG pipeline", fl_projection="条件展开", fl_dimensions="项目 / 摄像头 / 规格", fl_condition="RAW capability 和输出组合逐摄像头不同，支持时展开。"),
    row("专业", "功能", "专业辅助 / Expert Assist", "直方图 / Histogram",
        "在专业模式实时显示画面亮度分布，辅助曝光判断。", "项目显示直方图 UI 且统计数据随预览实时更新时支持。", "依赖预览统计、histogram UI、性能和刷新策略。", "在黑白灰及高反差场景检查分布、刷新、显隐和性能。",
        node_id="kb.mode.expert.histogram", parent_id="kb.mode.expert", node_type="交互", app_binding="CameraManualMode histogram UI (code presence to confirm)", implementation_status="待确认", fl_projection="独立行", fl_dimensions="项目 / 摄像头", fl_condition="项目是否提供入口或部分摄像头/规格禁用时展开。"),
]


DIRECTORY_NODES = [
    ("kb.root", "", "Camera Knowledge Base"),
    ("kb.launch", "kb.root", "启动与入口 / Launch & Entry"),
    ("kb.preview", "kb.root", "预览与场景感知 / Preview & Scene"),
    ("kb.focus", "kb.root", "对焦与曝光 / Focus & Exposure"),
    ("kb.zoom", "kb.root", "变焦与镜头切换 / Zoom & Lens"),
    ("kb.transient", "kb.root", "暂态开关 / Transient Switches"),
    ("kb.capture", "kb.root", "拍摄与录制交互 / Capture & Recording"),
    ("kb.toolbar", "kb.root", "工具栏 / Toolbar"),
    ("kb.modes", "kb.root", "模式 / Modes"),
    ("kb.common", "kb.root", "通用能力 / Common"),
    ("kb.common.preset", "kb.common", "预设 / Preset"),
    ("kb.common.widget", "kb.common", "小组件 / Widget"),
    ("kb.settings", "kb.common", "设置 / Settings"),
    ("kb.settings.general", "kb.settings", "通用设置 / General Settings"),
    ("kb.settings.photo", "kb.settings", "照片设置 / Photo Settings"),
    ("kb.settings.video", "kb.settings", "视频设置 / Video Settings"),
    ("kb.settings.help", "kb.settings", "帮助与反馈 / Help & Support"),
    ("kb.system", "kb.root", "系统交互 / System Interactions"),
    ("kb.gallery", "kb.root", "相册联动 / Gallery Integration"),
    ("kb.algorithms", "kb.root", "算法能力 / Algorithms"),
]


NODE_ID_OVERRIDES = {
    "模式栏": "kb.modes.switcher",
    "快速模式切换 / Quick Mode Switch": "kb.modes.quick_switch",
    "前后翻转 / Front-Rear Camera Switch": "kb.capture.camera_switch",
    "人脸检测": "kb.preview.face_detection",
    "FRT / 人像清晰度提升": "kb.algorithms.frt",
    "美颜算法 / Beauty Algorithm": "kb.algorithms.beauty",
    "人像虚化 / Portrait Bokeh": "kb.algorithms.portrait_bokeh",
    "ASD / AI场景检测": "kb.preview.asd",
    "脏污检测": "kb.preview.dirt_detection",
    "自动对焦-自动曝光": "kb.focus.auto",
    "变焦": "kb.zoom.control",
    "Photo EIS": "kb.algorithms.photo_eis",
    "Video EIS": "kb.algorithms.video_eis",
    "Video HDR 算法": "kb.algorithms.video_hdr",
    "OIS": "kb.zoom.ois",
    "各项专业模式参数极值范围": "kb.mode.expert.parameter_ranges",
    "ISZ / In Sensor Zoom": "kb.zoom.isz",
    "超分 / Super Resolution（SR）": "kb.zoom.super_resolution",
    "AI Zoom 开关 / AI Zoom Switch": "kb.transient.ai_zoom",
    "自动微距控制": "kb.transient.auto_macro",
    "自动夜景开关 / Auto Night Switch": "kb.transient.auto_night",
    "Text Mode（文本模式）": "kb.transient.text",
    "风格 / Style": "kb.toolbar.style",
    "Filter": "kb.toolbar.style.filter.photo",
    "Tuning": "kb.toolbar.style.tuning.photo",
    "风格-滤镜 / Style-Filter": "kb.toolbar.style.filter.video",
    "风格-调色 / Style-Tuning": "kb.toolbar.style.tuning.video",
    "风格-调色盘 / Style-Tuning Palette": "kb.toolbar.style.palette.video",
    "Motion Photo": "kb.toolbar.motion_photo",
    "动态照片 - 无效信息截取": "kb.toolbar.motion_photo.trim",
    "动态照片-视频支持录制声音": "kb.toolbar.motion_photo.audio",
    "Motion Photo cover HDR": "kb.toolbar.motion_photo.cover_hdr",
    "动态照片插帧 / Motion Photo Frame Interpolation": "kb.algorithms.motion_photo_interpolation",
    "Preset": "kb.common.preset.capability",
    "Preset Widget": "kb.common.widget.preset",
    "录制中前后置切换 / Front-Rear Switch While Recording": "kb.capture.camera_switch_recording",
    "视频规格 / Video Specs": "kb.mode.video.specs",
    "慢动作规格 / Slow Motion Specs": "kb.mode.slow_motion.specs",
    "延时摄影规格 / Timelapse Specs": "kb.mode.timelapse.specs",
    "高像素输出规格 / High Resolution Specs": "kb.mode.high_resolution.specs",
    "录制中拍照 / Video Snapshot": "kb.capture.video_snapshot",
    "录制中拍摄动态照片 / Motion Photo While Recording": "kb.capture.motion_photo_while_recording",
}


PARENT_BY_LEVEL2 = {
    "模式栏 / Mode Switch": "kb.modes",
    "前后翻转 / Camera Switch": "kb.capture",
    "预览框": "kb.preview",
    "AE/AF": "kb.focus",
    "Zoom": "kb.zoom",
    "左侧暂态开关": "kb.transient",
    "右侧暂态开关": "kb.transient",
    "工具栏 / Toolbar": "kb.toolbar",
    "Toolbar": "kb.toolbar",
    "Preset": "kb.common.preset",
    "Widget": "kb.common.widget",
    "General settings": "kb.settings.general",
    "Photo settings": "kb.settings.photo",
    "Video settings": "kb.settings.video",
    "Help & Support": "kb.settings.help",
    "系统 / System": "kb.system",
    "实时算法 / Realtime Algorithm": "kb.algorithms",
    "后处理算法 / Post-processing Algorithm": "kb.algorithms",
    "录制中拍照 / Capture While Recording": "kb.capture",
    "录制控制 / Recording Controls": "kb.capture",
    "视频规格 / Video Specs": "kb.mode.video",
    "慢动作规格 / Slow Motion Specs": "kb.mode.slow_motion",
    "高像素规格 / High Resolution Specs": "kb.modes",
    "启动与入口 / Launch & Entry": "kb.launch",
}

PARENT_BY_NAME = {
    "ASD / AI场景检测": "kb.preview",
    "人脸畸变矫正": "kb.preview",
    "ISZ / In Sensor Zoom": "kb.zoom",
    "超分 / Super Resolution（SR）": "kb.zoom",
    "各项专业模式参数极值范围": "kb.mode.expert",
    "Filter": "kb.toolbar.style",
    "Tuning": "kb.toolbar.style",
    "风格-滤镜 / Style-Filter": "kb.toolbar.style",
    "风格-调色 / Style-Tuning": "kb.toolbar.style",
    "风格-调色盘 / Style-Tuning Palette": "kb.toolbar.style",
    "动态照片 - 无效信息截取": "kb.toolbar.motion_photo",
    "动态照片-视频支持录制声音": "kb.toolbar.motion_photo",
    "Motion Photo cover HDR": "kb.toolbar.motion_photo",
    "动态照片插帧 / Motion Photo Frame Interpolation": "kb.toolbar.motion_photo.cover_hdr",
    "延时摄影规格 / Timelapse Specs": "kb.mode.timelapse",
}


PROJECTION_OVERRIDES = {
    "模式栏": ("父节点汇总", "项目", "FL 用一行描述模式集合；各模式能力由模式子节点独立判断。"),
    "快速模式切换 / Quick Mode Switch": ("条件展开", "项目", "只有项目定义专门快捷手势、切换时延或状态继承验收时独立展开。"),
    "风格 / Style": ("父节点汇总", "项目 / 模式 / 摄像头 / 规格", "FL 只投影 Style 父行；Filter/Tuning/Palette 留在 KB 说明，除非其支持范围导致独立验收结论。"),
    "Preset": ("父节点汇总", "项目", "选择、保存、导入、分享等知识子能力默认汇总为一条 Preset FL 行。"),
    "Motion Photo": ("父节点汇总", "项目 / 摄像头", "Motion Photo 主能力投影一行；关键封装差异按子节点条件展开。"),
    "动态照片 - 无效信息截取": ("条件展开", "项目", "裁剪策略有独立需求或验收结论时展开。"),
    "动态照片-视频支持录制声音": ("条件展开", "项目 / 摄像头", "声音能力在项目或摄像头范围存在差异时展开。"),
    "Motion Photo cover HDR": ("条件展开", "项目 / 摄像头 / 规格", "封面 HDR 支持或显示链路存在差异时展开。"),
    "动态照片插帧 / Motion Photo Frame Interpolation": ("随父节点", "项目 / 摄像头", "算法只在导致 Motion Photo 支持/画质验收差异时独立展开。"),
    "自动对焦-自动曝光": ("父节点汇总", "项目 / 模式 / 摄像头", "FL 保留 AE/AF 父行；Touch、Face、Lock、CAF、EV 在支持或验收结论不同时条件展开。"),
    "变焦": ("条件展开", "项目 / 模式 / 摄像头 / 规格", "倍率范围、光学点、SAT/硬切或录制限制不同即展开。"),
    "各项专业模式参数极值范围": ("规格展开", "项目 / 摄像头 / 规格", "ISO、快门、WB、对焦等边界必须按输出摄像头展开。"),
    "视频规格 / Video Specs": ("规格展开", "项目 / 摄像头 / 规格", "始终按摄像头×分辨率×帧率×HDR/HLG 组合展开。"),
    "慢动作规格 / Slow Motion Specs": ("规格展开", "项目 / 摄像头 / 规格", "始终按摄像头×分辨率×采集帧率展开。"),
    "延时摄影规格 / Timelapse Specs": ("规格展开", "项目 / 摄像头 / 规格", "按摄像头×输出规格展开；倍速在支持范围不同或需单独验收时再拆。"),
    "高像素输出规格 / High Resolution Specs": ("规格展开", "项目 / 摄像头 / 规格", "始终按摄像头×输出像素档×质量路径展开。"),
    "Filter": ("随父节点", "项目 / 模式 / 摄像头", "照片滤镜默认随 Style 父行；与 Tuning 支持结论不同时提升为独立行。"),
    "Tuning": ("随父节点", "项目 / 模式 / 摄像头", "照片调色默认随 Style 父行；与 Filter 支持结论不同时提升为独立行。"),
    "风格-滤镜 / Style-Filter": ("条件展开", "项目 / 模式 / 摄像头 / 规格", "视频滤镜的摄像头或 1080P30 等规格限制与父行结论不同时展开。"),
    "风格-调色 / Style-Tuning": ("条件展开", "项目 / 模式 / 摄像头 / 规格", "视频调色的摄像头或规格限制与滤镜不同即展开。"),
    "风格-调色盘 / Style-Tuning Palette": ("随父节点", "项目 / 模式 / 摄像头 / 规格", "默认随视频 Tuning；Palette 有独立支持差异时才展开。"),
}


STATUS_OVERRIDES = {
    "快速模式切换 / Quick Mode Switch": "待确认",
    "锁定白平衡": "规划中",
    "录制中拍摄动态照片 / Motion Photo While Recording": "规划中",
}


APP_BINDING_OVERRIDES = {
    "模式栏": "ModeIndex; mode_arrays.xml; CustomSubModeFactory",
    "快速模式切换 / Quick Mode Switch": "CameraBottomFunctionUINode; UiEventProxy.onModeChanged",
    "前后翻转 / Front-Rear Camera Switch": "UiEventProxy camera switch; CameraUIContext",
    "人脸检测": "pipeline face detection nodes; CameraUIContext",
    "FRT / 人像清晰度提升": "PortraitRepair/FRT pipeline node",
    "美颜算法 / Beauty Algorithm": "Beauty pipeline node; algoLib BeautyShot V1/V2/V3",
    "人像虚化 / Portrait Bokeh": "Bokeh pipeline node; SingleCamBokeh/DualCamBokeh",
    "ASD / AI场景检测": "NcfPhotoMode scene detection strategy",
    "脏污检测": "preview dirt detection strategy; CameraUIContext prompt",
    "自动对焦-自动曝光": "UiEventProxy single/long press focus; CameraUIContext AE/AF",
    "变焦": "zoom controller; CameraUIContext; mode camera list",
    "Photo EIS": "ProductConfig photo stabilization gate; photo pipeline",
    "Video EIS": "video stabilization setting; video pipeline",
    "Video HDR 算法": "CameraVideoMode HDR state; HDR video pipeline",
    "OIS": "camera characteristics / HAL stabilization modes",
    "各项专业模式参数极值范围": "CameraManualMode; manual ISO/shutter/WB/focus settings",
    "AIGC SR": "SuperResolution pipeline node",
    "HDSR": "SuperResolution pipeline node",
    "运动抓拍": "NcfPhotoMode MotionCapture",
    "RAW HDR": "RawHdrCapture/STRawHDR pipeline nodes",
    "CFR / 紫边去除": "RemovePurpleEdge pipeline node",
    "ISZ / In Sensor Zoom": "sensor crop/ISZ configuration; zoom controller",
    "Hex Zoom": "zoom controller; SuperResolution pipeline",
    "视频夜景": "CameraVideoMode low-light strategy; Night pipeline",
    "人像 HDR": "BokehMode HDR strategy; portrait HDR pipeline",
    "超分 / Super Resolution（SR）": "SuperResolution pipeline node",
    "多帧降噪 / MFNR": "RawDeepDenoise pipeline node",
    "Ultra HDR": "SettingKeys.KEY_ULTRA_HDR; UltraHdr pipeline node",
    "人脸畸变矫正": "DistortionCorrection pipeline node",
    "LDC / 光学畸变矫正": "DistortionCorrection pipeline node",
    "自动微距控制": "SettingKeys.KEY_FALLBACK_MACRO_CONTROL; NcfPhotoMode",
    "AI Zoom 开关 / AI Zoom Switch": "NcfPhotoMode AI zoom strategy; transient switch UI",
    "自动夜景开关 / Auto Night Switch": "NcfPhotoMode auto-night strategy; transient switch UI",
    "Text Mode（文本模式）": "NcfPhotoMode NoteDetect; NoteDetect pipeline node",
    "Flash": "flash setting; camera flash capability; toolbar UI",
    "录影灯 / Recording Light": "SettingKeys.KEY_CAMERA_VIDEO_RED_LIGHT; recording state",
    "Timer": "SettingKeys.KEY_SELF_TIMER; shutter countdown UI",
    "HDR 开关 / HDR Switch": "photo HDR setting; NcfPhotoMode HDR strategy",
    "Exposure": "AE compensation setting; exposure toolbar UI",
    "风格 / Style": "SettingKeys style/tuning keys; PresetDataParser; style UI nodes",
    "Filter": "style/filter setting keys; LUT renderer; PresetDataParser",
    "Tuning": "style/tuning setting keys; tuning renderer; PresetDataParser",
    "风格-滤镜 / Style-Filter": "CameraVideoMode style/LUT pipeline",
    "风格-调色 / Style-Tuning": "CameraVideoMode tuning/LUT pipeline; PresetDataParser",
    "风格-调色盘 / Style-Tuning Palette": "CameraVideoMode palette/LUT pipeline",
    "Motion Photo": "motion photo setting; NcfPhotoMode motion-photo pipeline",
    "动态照片 - 无效信息截取": "motion-photo trim/packaging pipeline",
    "动态照片-视频支持录制声音": "motion-photo audio capture/packaging pipeline",
    "Motion Photo cover HDR": "motion-photo cover; UltraHdr pipeline",
    "动态照片插帧 / Motion Photo Frame Interpolation": "motion-photo interpolation pipeline",
    "Quality": "high-resolution setting; mode camera capability",
    "Grid": "grid setting; preview overlay UI",
    "Ratio": "SettingKeys.KEY_PICTURE_ASPECT_RATIO; preview/capture crop",
    "Watermark": "SettingKeys.KEY_CAMERA_SHUTTER_WATERMARK; Watermark pipeline node",
    "More settings": "toolbar navigation to Settings",
    "Glyph Mirror": "SettingKeys.KEY_GLYPH_MIRROR; glyph hardware controller",
    "Preset": "SettingKeys.KEY_PRESET_SETTING; PresetDataParser",
    "Preset Widget": "WidgetCameraActivity",
    "Save location": "SettingKeys.KEY_RECORD_LOCATION",
    "Shutter sound": "SettingKeys.KEY_CAMERA_SHUTTER_SOUND",
    "Mirror front camera": "SettingKeys.KEY_CAPTURE_MIRROR",
    "Level": "SettingKeys.KEY_LEVEL_METER",
    "Auto Tone": "NcfPhotoMode ASD/automatic tone strategy",
    "影像基调 / Image Tone": "SettingKeys.KEY_CAMERA_COLOR_CONTROL_MODE",
    "色彩模式 / Color Mode": "SettingKeys.KEY_CAMERA_COLOR_MODE",
    "Watermark settings": "SettingKeys.KEY_CAMERA_SHUTTER_WATERMARK; Watermark pipeline node",
    "Tap to take a photo": "SettingKeys.KEY_SHUTTER_TOUCH; UiEventProxy",
    "QR code scanner": "SettingKeys.KEY_QRCODE",
    "Press and hold shutter": "SettingKeys.KEY_HOLD_SHUTTER_KEY; UiEventProxy",
    "Ultra XDR": "SettingKeys.KEY_ULTRA_HDR; UltraHdr pipeline node",
    "Video encoding": "SettingKeys.KEY_VIDEO_ENCODER; CameraVideoMode",
    "Power saving recording": "SettingKeys.KEY_VIDEO_COVER_SETTING; CameraVideoMode",
    "Auto FPS": "SettingKeys.KEY_VIDEO_AUTO_FPS; CameraVideoMode",
    "视频防抖开关": "video stabilization setting; CameraVideoMode",
    "锁定镜头": "SettingKeys.KEY_VIDEO_LOCK_LENS; LockLensZoomController",
    "锁定白平衡": "No matching production SettingKey found on code baseline",
    "Tips and feedback": "Settings UI external intent",
    "超级夜景": "Night pipeline node; NcfPhotoMode auto-night strategy",
    "极夜": "Night pipeline extreme-low-light branch",
    "超级夜景+美颜": "Night pipeline + Beauty pipeline",
    "Remosaic": "sensor mode / remosaic pipeline configuration",
    "TF 50MP HDR/MMF": "high-resolution HDR/MMF pipeline",
    "录制中前后置切换 / Front-Rear Switch While Recording": "CameraVideoMode; UiEventProxy camera switch",
    "视频规格 / Video Specs": "CameraVideoMode; ProductConfig video size/fps capability",
    "慢动作规格 / Slow Motion Specs": "CameraSlowMotionMode; high-speed profiles",
    "延时摄影规格 / Timelapse Specs": "timelapse mode; size/speed settings",
    "高像素输出规格 / High Resolution Specs": "high-resolution mode; sensor output configuration",
    "录制中拍照 / Video Snapshot": "UiEventProxy video snapshot; CameraVideoMode",
    "录制中拍摄动态照片 / Motion Photo While Recording": "planned CameraVideoMode + motion-photo parallel pipeline",
}


def automatic_node_id(row_data: dict[str, str]) -> str:
    """Create a deterministic fallback; important public nodes use overrides."""
    raw = f"{row_data.get('一级分类', '')}|{row_data.get('二级分类', '')}|{row_data.get('名称', '')}"
    ascii_hint = re.sub(r"[^a-z0-9]+", ".", row_data.get("名称", "").lower()).strip(".")
    suffix = ascii_hint[:36] if ascii_hint else sha1(raw.encode("utf-8")).hexdigest()[:12]
    return f"kb.capability.{suffix}"


def default_projection(row_data: dict[str, str]) -> tuple[str, str, str]:
    if row_data["一级分类"] == "算法 / Algorithm":
        return (
            "条件展开",
            "项目 / 模式 / 摄像头 / 规格",
            "算法路径改变项目支持结论、摄像头范围、规格范围或形成独立验收结果时展开；纯实现细节留在 KB。",
        )
    if row_data["一级分类"] == "通用 / Common":
        return ("独立行", "项目", "设置入口、默认值、选项、记忆或产品政策存在差异时展开。")
    return (
        "独立行",
        "项目 / 模式 / 摄像头",
        "用户入口、行为、模式范围或输出摄像头支持存在差异时展开。",
    )


# Purpose fields answer product questions before implementation questions:
# What user problem exists, what value is delivered, what outcome is expected,
# and where the capability stops. Exact overrides cover high-impact concepts;
# the branch defaults keep every long-tail KB node complete and reviewable.
PURPOSE_OVERRIDES: dict[str, tuple[str, str, str, str]] = {
    "模式栏": (
        "用户面对不同拍摄任务时，需要快速找到与任务匹配的拍摄方式，而不是在一个模式中理解大量互斥参数。",
        "用清晰、稳定的入口在照片、视频、夜景、人像、专业等拍摄意图之间切换。",
        "降低模式寻找和切换成本，并保证进入任一模式后立即具备可拍摄状态。",
        "只定义模式的组织、可见性和切换，不代表每个模式内部的摄像头、算法或规格都支持。",
    ),
    "快速模式切换 / Quick Mode Switch": (
        "连续拍摄时，逐个滑动或等待完整模式重建可能错过瞬间。",
        "让用户以更少操作、更短等待时间切到目标模式，同时保留合理的拍摄状态。",
        "缩短模式切换时延，减少黑屏、卡顿和参数丢失造成的拍摄中断。",
        "不等同于前后摄像头翻转，也不自动承诺所有模式之间均可无缝切换。",
    ),
    "前后翻转 / Front-Rear Camera Switch": (
        "用户需要在拍摄自己和拍摄外部场景之间切换，但不希望退出当前拍摄模式。",
        "在当前模式中直接切换前后摄，并尽可能保持用户已选择的拍摄意图。",
        "让前后摄切换快速、可预期，切换后预览、焦段和参数处于有效状态。",
        "描述录制开始前的摄像头翻转；录制中的前后切换是另一个能力。",
    ),
    "人脸检测": (
        "相机如果不知道画面中的人脸位置，就难以稳定优化人物的对焦、曝光、肤色和人像效果。",
        "自动识别人脸并把位置、大小和置信度提供给 AE/AF、美颜、人像等能力。",
        "提升人物作为主体时的清晰度、亮度和后续算法稳定性。",
        "检测到人脸不等于自动美颜或虚化；它只提供人脸信息和必要的预览反馈。",
    ),
    "ASD / AI场景检测": (
        "同一套成像参数无法同时适合天空、绿植、舞台、食物等语义差异明显的场景。",
        "识别场景语义，让相机选择更匹配的调试或算法策略。",
        "在无需用户手动调参的前提下，提高特定场景的色彩、曝光和细节表现。",
        "不包含仅基于亮度或动态范围的普通场景判断，也不等于独立拍摄模式。",
    ),
    "脏污检测": (
        "镜头指纹或污渍会造成雾化、炫光和清晰度下降，用户通常拍完后才发现。",
        "在拍摄前提醒用户清洁镜头，避免不可逆的画质损失。",
        "降低因镜头脏污产生的废片率，同时控制误提醒和打扰频率。",
        "只负责检测和提示，不负责通过算法恢复被污渍遮挡的真实细节。",
    ),
    "自动对焦-自动曝光": (
        "用户需要主体清晰且亮度正确，但移动主体、逆光和构图变化会持续改变最佳焦点与曝光。",
        "让相机根据触控、人脸和场景自动确定焦点与曝光，并提供锁定或补偿能力。",
        "减少失焦、过曝和欠曝，使用户在多数场景下无需理解底层相机参数即可拍到可用画面。",
        "这是 AE/AF 父能力；Touch、Face、Lock、CAF 和 EV 的具体差异由子节点描述。",
    ),
    "Touch AE/AF": (
        "自动策略可能无法知道用户真正想拍画面中的哪一个主体。",
        "用户点击目标区域即可明确指定对焦和测光意图。",
        "让用户以一次点击纠正主体选择，并获得及时、可理解的视觉反馈。",
        "固定焦摄像头只能响应 Touch AE，不能因此标记为支持 Touch AF。",
    ),
    "Face AE/AF": (
        "人物位于逆光、画面边缘或多人场景时，普通中心测光和对焦可能忽略真正主体。",
        "优先保证人脸的曝光和清晰度，让人物在复杂光线中仍然可用。",
        "提高人物拍摄成功率，并为美颜、人像和人脸修复提供稳定输入。",
        "固定焦摄像头只有 Face AE；多人优先级由策略定义，不保证所有人脸完全相同。",
    ),
    "Touch AE/AF Lock": (
        "重新构图或光线变化时，自动 AE/AF 持续收敛会让用户已经确定的画面发生漂移。",
        "锁住用户确认的焦点和曝光，便于重新构图或保持录制画面一致。",
        "在用户主动解除前保持稳定，避免亮度抽动和焦点跳变。",
        "锁定范围和自动解除条件由模式定义，不代表永久锁定所有 3A 状态。",
    ),
    "CAF / 连续自动对焦": (
        "主体或设备持续移动时，单次对焦很快会失效。",
        "持续跟随距离变化更新焦点，使运动主体保持清晰。",
        "提高移动人物、宠物和视频录制中的连续清晰度，同时减少来回抽焦。",
        "固定焦摄像头不支持 CAF；跟焦不等于主体追踪或运动抓拍。",
    ),
    "EV 曝光补偿": (
        "自动曝光给出的平均亮度不一定符合用户对雪景、舞台或剪影的创作意图。",
        "允许用户在自动曝光基础上主动调亮或调暗画面。",
        "在保留自动曝光便利性的同时提供可控的创作偏好。",
        "EV 是相对补偿，不等同于专业模式的固定 ISO 或快门。",
    ),
    "变焦": (
        "用户无法总是靠近或远离主体，需要在同一拍摄位置改变构图和主体大小。",
        "通过光学镜头、Sensor crop 和数码处理覆盖从广角到长焦的构图范围。",
        "让用户在连续取景中快速得到目标构图，并尽量保持切镜前后的画质、曝光和色彩一致。",
        "变焦能力不等于所有倍率均为光学画质；倍率范围和切镜策略由子节点定义。",
    ),
    "变焦倍率范围 / Zoom Range": (
        "界面如果展示硬件或算法无法可靠输出的倍率，会造成画质骤降或不可用组合。",
        "明确每个模式、摄像头和规格真正可用的最小、最大倍率与关键倍率点。",
        "保证 UI、实际镜头路径、成片元数据和项目验收使用同一范围定义。",
        "倍率数字只描述可用范围，不代表范围内所有倍率具有相同画质。",
    ),
    "镜头切换策略 / Lens Switching Strategy": (
        "跨镜头变焦时，视场、曝光、色彩或画面位置突变会破坏连续取景和视频。",
        "在 SAT、硬切和锁定当前镜头之间选择合适路径，使跨镜头行为可预期。",
        "减少切镜跳变、黑帧和录制中断，并在画质与连续性之间取得项目定义的平衡。",
        "策略会受光照、规格和录制状态限制；支持多摄不等于所有场景都使用 SAT。",
    ),
    "OIS": (
        "手持抖动会在低照、长曝光和长焦场景中造成模糊。",
        "通过镜组或 Sensor 的物理位移抵消角度抖动，保留更多真实成像区域。",
        "提升低照照片清晰度和长焦预览稳定性，并为算法提供更稳定的输入。",
        "OIS 是摄像头硬件能力，不等于 EIS，也不能消除主体自身运动。",
    ),
    "Photo EIS": (
        "高倍率或弱光手持拍照时，预览抖动和帧间错位会降低构图与合成成功率。",
        "利用陀螺仪和裁切补偿稳定照片预览或拍照链路。",
        "提升手持构图稳定性和多帧成片清晰度。",
        "会消耗部分视场，不替代 OIS，也不能冻结运动主体。",
    ),
    "Video EIS": (
        "走动或手持录制会产生连续抖动，直接影响视频可观看性。",
        "通过陀螺仪、运动估计和动态裁切稳定视频画面。",
        "降低高频抖动和步行晃动，在清晰度、视场和稳定度之间满足规格目标。",
        "不同分辨率和帧率可能不支持；EIS 不等于云台级稳定。",
    ),
    "风格 / Style": (
        "默认成像无法覆盖所有用户的审美偏好，逐项调色又需要较高学习成本。",
        "通过滤镜、调色盘和参数调节快速形成可预览、可复用的视觉风格。",
        "让用户在拍摄前获得稳定的个性化效果，并可通过 Preset 保存和复用。",
        "Style 负责视觉表达，不改变拍摄模式本身；不同视频规格可能限制其可用范围。",
    ),
    "Motion Photo": (
        "单张照片只能保留一个瞬间，容易错过动作前后、表情变化和现场氛围。",
        "在静态封面之外保留快门前后的短视频片段，允许用户回看完整瞬间。",
        "提高人物、宠物和运动场景的可选帧与回忆价值，同时保持普通照片的分享入口。",
        "不等同于普通视频；声音、封面 HDR、片段长度和相册播放能力需分别确认。",
    ),
    "视频规格 / Video Specs": (
        "清晰度、流畅度、动态范围、功耗和文件大小无法由单一视频规格同时最优。",
        "让项目和用户在分辨率、帧率、HDR/HLG 与稳定能力之间选择。",
        "为每颗摄像头给出真实可录、可长期稳定并可正确播放的规格组合。",
        "项目支持某个规格不代表所有摄像头、HDR、EIS 或 Style 组合都支持。",
    ),
    "慢动作规格 / Slow Motion Specs": (
        "普通帧率无法清楚呈现快速动作的细节过程。",
        "以高采集帧率记录动作，再以较低播放速度呈现。",
        "在可接受的清晰度、曝光、掉帧和温升下获得稳定慢动作效果。",
        "高帧率会缩短单帧曝光并提高光照要求；标称规格必须由 Sensor 与 pipeline 共同支持。",
    ),
    "高像素输出规格 / High Resolution Specs": (
        "普通像素合并输出无法满足裁切、放大或大尺寸输出对细节的需求。",
        "提供 50MP、200MP 等高像素档，让用户在细节、动态范围、耗时和文件大小之间选择。",
        "确保每个像素档具有真实输出路径、可接受的画质收益和稳定保存能力。",
        "高像素档不等同于简单放大；不同档位可能使用 Remosaic、HDR 或 upscale。",
    ),
    "专业模式 / Expert Mode": (
        "自动相机为了成功率会持续改变参数，无法满足长曝光、固定色温或一致性创作。",
        "把 ISO、快门、白平衡、对焦和 RAW 等关键控制交给有经验的用户。",
        "提供可预测、可复现的手动拍摄结果，并明确每颗摄像头的真实参数边界。",
        "专业模式不承诺突破 Sensor/HAL 极限；参数可用范围必须逐摄像头定义。",
    ),
    "全景模式 / Panorama Mode": (
        "单张照片视场不足以容纳宽阔风景、建筑或多人合影。",
        "引导用户移动设备并拼接多帧，生成超出单镜头瞬时视场的宽幅照片。",
        "在易操作的引导下获得连续、少拼接缝且曝光一致的宽视场成片。",
        "不等同于超广角单张拍摄；运动物体、距离过近和移动不稳定会影响拼接。",
    ),
    "夜景模式 / Night Mode": (
        "弱光下单帧照片容易过暗、噪声高、细节少，延长曝光又容易手抖。",
        "通过低照曝光策略和多帧计算摄影提升亮度、噪声和细节。",
        "在手持条件下得到更明亮、清晰且不过度失真的夜景照片。",
        "不能恢复完全无光场景，也不能消除运动主体在长曝光中的拖影。",
    ),
    "美颜算法 / Beauty Algorithm": (
        "默认成像可能放大肤质瑕疵，但统一强处理又容易损失身份特征和真实质感。",
        "针对人脸做可控的肤质、肤色和局部特征优化。",
        "在保留真实肤色、纹理、毛发和个人特征的前提下提升人物观感。",
        "只处理满足检测置信度的人脸，不应改变背景结构或替代 FRT 清晰度修复。",
    ),
    "人像虚化 / Portrait Bokeh": (
        "普通手机小底成像难以获得自然浅景深，复杂背景会分散对人物主体的注意力。",
        "分离人物与背景并模拟景深虚化，突出主体。",
        "获得自然的景深层次、稳定的发丝边缘和接近光学虚化的背景表现。",
        "辅助摄像头参与 Depth 不等于它是输出摄像头；透明物体和复杂边缘存在算法上限。",
    ),
    "FRT / 人像清晰度提升": (
        "远距离、低照或压缩场景中的人脸细节容易损失，普通锐化又会产生伪影。",
        "在检测到人脸时针对性恢复眼睛、五官和纹理细节。",
        "提升人脸可辨识度和清晰感，同时保持身份特征自然。",
        "FRT 不是美颜，不负责改变肤色、脸型或隐藏瑕疵。",
    ),
    "Preset": (
        "复杂的模式、焦段、滤镜和曝光组合难以重复设置，也难以分享给其他用户。",
        "把一组拍摄设置保存为可识别、可复用和可分享的拍摄配方。",
        "缩短重复创作的准备时间，并保证恢复后的参数与原 Preset 意图一致。",
        "Preset 只保存允许持久化的配置，不保证跨项目、跨版本或不兼容硬件完全复现。",
    ),
    "Ultra HDR": (
        "普通 SDR JPEG 无法在高亮屏幕上同时呈现强高光和暗部层次。",
        "通过 gain map 等信息保存并显示更高动态范围的照片。",
        "在兼容设备和相册中获得更真实的亮度层次，同时保留 SDR 兼容显示。",
        "拍摄支持不等于所有查看器都能 HDR 显示；它也不等同于 HDR 场景检测开关。",
    ),
    "超级夜景": (
        "弱光场景中单帧曝光无法同时满足亮度、噪声和手持清晰度。",
        "对齐并融合多帧低照图像，改善暗部、噪声和细节。",
        "提升手持低照成片的可用率，同时控制鬼影、过曝灯牌和处理耗时。",
        "不能消除快速运动主体造成的所有错位，也不代表极夜分支必然启用。",
    ),
    "Remosaic": (
        "多像素合一 Sensor 的常规输出牺牲了标称全分辨率细节。",
        "重建完整 CFA 排列以输出原生高像素图像。",
        "在足够光照下提供真实的高分辨率细节收益，并控制摩尔纹、伪色和耗时。",
        "Remosaic 不等于对低分辨率图片做 upscale；是否启用取决于 Sensor mode 和 pipeline。",
    ),
}


BRANCH_PURPOSE: dict[str, tuple[str, str, str, str]] = {
    "launch": (
        "用户从不同系统入口进入相机时，权限、默认模式和可访问内容可能不一致。",
        "让相机从目标入口快速、正确且安全地进入可拍摄状态。",
        "减少启动等待和入口失败，并确保安全相机等上下文不泄露受限内容。",
        "只描述进入和退出上下文，不代表入口后的全部模式与摄像头均支持。",
    ),
    "preview": (
        "用户在按下快门前需要知道相机看到了什么、识别了什么以及是否存在画质风险。",
        "通过实时预览、检测和提示帮助用户在拍摄前修正构图或环境问题。",
        "提高所见即所得程度，降低拍完后才发现问题的废片率。",
        "预览反馈不等同于最终成片算法，预览与成片允许存在受控差异。",
    ),
    "focus": (
        "主体位置、距离和光线持续变化，容易造成失焦或曝光不符合意图。",
        "让用户或自动策略明确主体，并稳定控制清晰度与亮度。",
        "在最少操作下提高主体清晰、曝光正确的拍摄成功率。",
        "具体能力受固定焦、HAL 3A 和模式策略限制。",
    ),
    "zoom": (
        "用户需要在不改变站位的情况下调整构图，但多镜头和数码变焦会带来画质与连续性差异。",
        "提供可理解、可控制的倍率和镜头路径。",
        "覆盖项目目标焦段，同时降低切镜跳变和高倍率画质下降。",
        "可选择某倍率不代表它是光学倍率或具有相同画质。",
    ),
    "capture": (
        "拍摄和录制过程中，用户需要可靠地触发、暂停、切换或并行生成内容。",
        "让关键拍摄动作有明确入口、即时反馈且不破坏当前媒体文件。",
        "减少误操作、内容丢失、音画中断和状态不可恢复。",
        "是否支持取决于模式、摄像头、规格和并行 pipeline 能力。",
    ),
    "toolbar": (
        "高频拍摄参数如果藏在深层设置中，用户无法在取景时快速调整。",
        "把当前模式最常用的控制放在拍摄界面，允许即时预览和修改。",
        "缩短调节路径，并保证入口显隐、默认值、记忆和互斥行为可预测。",
        "工具栏入口不等同于底层算法本身，具体效果和规格限制由关联节点定义。",
    ),
    "modes": (
        "不同拍摄目标需要不同采集、交互和算法策略，单一自动模式无法覆盖全部需求。",
        "为明确的拍摄意图提供一组协调好的默认能力。",
        "让用户进入模式后无需重新搭建参数组合即可完成目标拍摄。",
        "模式存在不代表其中所有摄像头、工具栏和算法都支持。",
    ),
    "settings": (
        "用户偏好、隐私要求和使用环境不同，统一默认配置无法适合所有人。",
        "允许用户长期控制相机行为、默认值和系统集成方式。",
        "让设置结果可理解、可记忆、可重置，并在相关模式中一致生效。",
        "设置入口只控制产品行为，不自动证明底层硬件或算法具备能力。",
    ),
    "algorithms": (
        "受限于手机光学、Sensor、算力和拍摄环境，基础单帧成像无法稳定达到目标画质。",
        "利用检测、对齐、融合、重建或增强处理弥补物理成像限制。",
        "在明确场景中改善清晰度、噪声、动态范围、色彩或主体表现，并控制伪影与耗时。",
        "代码中存在算法模块不等于生产链路实际启用；只有改变产品或独立 IQ 结论时才进入 FL。",
    ),
    "common": (
        "跨模式的能力如果分别设置和管理，会增加重复操作和状态不一致。",
        "提供可跨模式复用的配置、内容和系统入口。",
        "降低重复设置成本，并保持跨模式、前后台和重启后的状态一致。",
        "跨模式复用不代表所有模式都接受相同参数。",
    ),
    "system": (
        "相机需要与系统、相册和硬件服务协作，单独完成拍摄链路不足以形成完整体验。",
        "连接系统入口、权限、存储、显示和内容消费链路。",
        "保证从启动、拍摄、保存到查看的端到端体验连续可靠。",
        "系统能力可能受地区、应用版本、硬件和默认应用政策限制。",
    ),
}


def purpose_branch(row_data: dict[str, str]) -> str:
    node_id = row_data.get("节点 ID", "")
    level1 = row_data.get("一级分类", "")
    if node_id.startswith("kb.launch"):
        return "launch"
    if node_id.startswith("kb.preview"):
        return "preview"
    if node_id.startswith("kb.focus"):
        return "focus"
    if node_id.startswith("kb.zoom"):
        return "zoom"
    if node_id.startswith(("kb.capture", "kb.video")):
        return "capture"
    if node_id.startswith("kb.toolbar"):
        return "toolbar"
    if node_id.startswith("kb.mode"):
        return "modes"
    if node_id.startswith("kb.settings"):
        return "settings"
    if node_id.startswith(("kb.common", "kb.gallery", "kb.system")):
        return "common" if node_id.startswith("kb.common") else "system"
    if node_id.startswith("kb.algorithms") or level1 == "算法 / Algorithm":
        return "algorithms"
    if row_data.get("二级分类") in {"Toolbar", "工具栏 / Toolbar"}:
        return "toolbar"
    if level1 == "通用 / Common":
        return "settings"
    return "system"


def purpose_fields(row_data: dict[str, str]) -> tuple[str, str, str, str]:
    if row_data["名称"] in PURPOSE_OVERRIDES:
        return PURPOSE_OVERRIDES[row_data["名称"]]
    branch = purpose_branch(row_data)
    problem, value, goal, boundary = BRANCH_PURPOSE[branch]
    name = row_data["名称"]
    return (
        problem,
        f"{value}“{name}”是该目标下的具体能力或控制点。",
        goal,
        boundary,
    )


def enrich(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    enriched: list[dict[str, str]] = []
    for item in rows:
        row_data = dict(item)
        row_data["节点 ID"] = row_data.get("节点 ID") or NODE_ID_OVERRIDES.get(row_data["名称"]) or automatic_node_id(row_data)
        row_data["父节点 ID"] = (
            row_data.get("父节点 ID")
            or PARENT_BY_NAME.get(row_data["名称"])
            or PARENT_BY_LEVEL2.get(row_data["二级分类"], "kb.root")
        )
        row_data["节点类型"] = row_data.get("节点类型") or (
            "算法" if row_data["一级分类"] == "算法 / Algorithm"
            else "设置" if row_data["一级分类"] == "通用 / Common"
            else "能力"
        )
        row_data["交互位置"] = row_data.get("交互位置") or row_data["二级分类"]
        projection, dimensions, condition = PROJECTION_OVERRIDES.get(row_data["名称"], default_projection(row_data))
        row_data["FL 投影"] = row_data.get("FL 投影") or projection
        row_data["FL 展开维度"] = row_data.get("FL 展开维度") or dimensions
        row_data["FL 展开条件"] = row_data.get("FL 展开条件") or condition
        row_data["实现状态"] = STATUS_OVERRIDES.get(row_data["名称"], row_data.get("实现状态") or "已实现")
        row_data["代码基线"] = row_data.get("代码基线") or CODE_BASELINE
        row_data["App 绑定"] = row_data.get("App 绑定") or APP_BINDING_OVERRIDES.get(
            row_data["名称"], "待补充具体 Mode / SettingKey / UI node / pipeline node"
        )
        row_data["配置门控"] = row_data.get("配置门控") or "按 ProductConfig、模式配置和硬件能力确认"
        row_data["摄像头范围"] = row_data.get("摄像头范围") or "按项目确认"
        row_data["规格范围"] = row_data.get("规格范围") or "按项目确认"
        problem, user_value, product_goal, capability_boundary = purpose_fields(row_data)
        base_description = row_data["说明"].strip()
        row_data["说明"] = (
            f"【能力定义】{base_description}\n"
            f"【解决的问题】{problem}\n"
            f"【用户价值】{user_value}\n"
            f"【产品目标】{product_goal}\n"
            f"【能力边界】{capability_boundary}"
        )
        enriched.append(row_data)

    directory_rows = []
    for node_id, parent_id, name in DIRECTORY_NODES:
        directory_rows.append({
            "模式": "不适用",
            "节点 ID": node_id,
            "父节点 ID": parent_id,
            "节点类型": "目录",
            "一级分类": "目录 / Taxonomy",
            "二级分类": "目录 / Taxonomy",
            "名称": name,
            "交互位置": name,
            "说明": (
                "【能力定义】用于组织 Camera 知识节点和生成 Feature Tree。\n"
                "【解决的问题】当知识节点数量较多时，需要稳定层级帮助用户定位能力和理解上下文。\n"
                "【用户价值】通过统一导航快速找到相关能力，并沿父子关系理解功能归属。\n"
                "【产品目标】保证 Tree 与 KB 使用同一套节点关系，避免维护两份分类产生漂移。\n"
                "【能力边界】目录只组织知识，不代表 Camera 产品功能，也不进入项目 FL。"
            ),
            "判断依据": "不直接判断支持。",
            "依赖": "无。",
            "验证方法": "校验子节点父引用和 Tree 生成结果。",
            "App 绑定": "",
            "配置门控": "",
            "实现状态": "分类节点",
            "FL 投影": "不进入 FL",
            "FL 展开维度": "",
            "FL 展开条件": "目录节点永不进入项目 FL。",
            "摄像头范围": "不适用",
            "规格范围": "不适用",
            "代码基线": CODE_BASELINE,
            "来源项目": SOURCE,
            "备注": "",
        })
    return [
        {field: row_data.get(field, "") for field in KB_FIELDS}
        for row_data in directory_rows + enriched
    ]


def audit(rows: list[dict[str, str]]) -> list[str]:
    lines = ["# KB Functions Algorithms v7 Audit", ""]
    names = Counter(r["名称"] for r in rows)
    duplicates = [name for name, count in names.items() if count > 1]
    node_ids = Counter(r["节点 ID"] for r in rows)
    duplicate_node_ids = [node_id for node_id, count in node_ids.items() if count > 1]
    known_node_ids = set(node_ids)
    orphan_rows = [
        r for r in rows
        if r.get("父节点 ID") and r["父节点 ID"] not in known_node_ids
    ]
    allowed_projections = {"不进入 FL", "独立行", "父节点汇总", "随父节点", "条件展开", "规格展开"}
    bad_projections = [r for r in rows if r.get("FL 投影") not in allowed_projections]
    missing_projection_rule = [
        r for r in rows
        if r.get("FL 投影") != "不进入 FL" and not r.get("FL 展开条件", "").strip()
    ]
    missing_app_binding = [
        r for r in rows
        if r.get("节点类型") != "目录"
        and (
            not r.get("App 绑定", "").strip()
            or r.get("App 绑定", "").startswith("待补充")
        )
    ]
    required_description_sections = [
        "【能力定义】",
        "【解决的问题】",
        "【用户价值】",
        "【产品目标】",
        "【能力边界】",
    ]
    incomplete_descriptions = [
        r for r in rows
        if any(section not in r.get("说明", "") for section in required_description_sections)
    ]
    bad_verify = [
        r for r in rows
        if r["验证方法"].strip() in {"✓", "✗", "✅", "❌"} or not r["验证方法"].strip()
    ]
    bad_source = [
        r for r in rows
        if "26111" in r.get("来源项目", "") or "26121" in r.get("来源项目", "")
        or "26111" in r.get("备注", "") or "26121" in r.get("备注", "")
    ]
    bad_terms = [
        r for r in rows
        if any(term in json.dumps(r, ensure_ascii=False) for term in ["Hyper Zoom", "虹软", "4x以上支持"])
    ]

    lines.append(f"- Rows: {len(rows)}")
    lines.append(f"- Duplicate names: {len(duplicates)}")
    lines.append(f"- Duplicate node IDs: {len(duplicate_node_ids)}")
    lines.append(f"- Orphan parent references: {len(orphan_rows)}")
    lines.append(f"- Invalid FL projections: {len(bad_projections)}")
    lines.append(f"- Missing FL projection rules: {len(missing_projection_rule)}")
    lines.append(f"- Missing App bindings: {len(missing_app_binding)}")
    lines.append(f"- Incomplete structured descriptions: {len(incomplete_descriptions)}")
    lines.append(f"- Invalid verification methods: {len(bad_verify)}")
    lines.append(f"- Bad source-project mentions: {len(bad_source)}")
    lines.append(f"- Bad legacy terms: {len(bad_terms)}")
    lines.append("")

    status_counts = Counter(r.get("实现状态", "") for r in rows)
    lines.append("## 实现状态")
    lines.append("")
    for status, count in sorted(status_counts.items()):
        lines.append(f"- {status or '空'}: {count}")

    non_confirmed = [
        r for r in rows
        if r.get("实现状态") in {"规划中", "待确认", "内部", "调试"}
    ]
    lines.append("")
    lines.append("## 非已实现节点")
    lines.append("")
    if non_confirmed:
        for r in non_confirmed:
            lines.append(f"- {r['名称']}: {r['实现状态']} / {r.get('App 绑定', '')}")
    else:
        lines.append("- None")

    todo_rows = [r for r in rows if "待确认" in r.get("备注", "")]
    lines.append("")
    lines.append("## 待确认项")
    lines.append("")
    if todo_rows:
        for r in todo_rows:
            lines.append(f"- {r['名称']}: {r['备注']}")
    else:
        lines.append("- None")

    if duplicates:
        lines.append("")
        lines.append("## Duplicate Names")
        lines.extend(f"- {name}" for name in duplicates)

    if duplicate_node_ids:
        lines.append("")
        lines.append("## Duplicate Node IDs")
        lines.extend(f"- {node_id}" for node_id in duplicate_node_ids)

    if orphan_rows:
        lines.append("")
        lines.append("## Orphan Parent References")
        lines.extend(f"- {r['节点 ID']} -> {r['父节点 ID']}" for r in orphan_rows)

    if bad_projections:
        lines.append("")
        lines.append("## Invalid FL Projections")
        lines.extend(f"- {r['名称']}: {r.get('FL 投影', '')}" for r in bad_projections)

    if missing_projection_rule:
        lines.append("")
        lines.append("## Missing FL Projection Rules")
        lines.extend(f"- {r['名称']}" for r in missing_projection_rule)

    if missing_app_binding:
        lines.append("")
        lines.append("## Missing App Bindings")
        lines.extend(f"- {r['名称']}" for r in missing_app_binding)

    if incomplete_descriptions:
        lines.append("")
        lines.append("## Incomplete Structured Descriptions")
        lines.extend(f"- {r['名称']}" for r in incomplete_descriptions)

    if bad_verify:
        lines.append("")
        lines.append("## Invalid Verification Methods")
        lines.extend(f"- {r['名称']}: {r['验证方法']}" for r in bad_verify)

    if bad_source:
        lines.append("")
        lines.append("## Bad Source Project Mentions")
        lines.extend(f"- {r['名称']}: {r.get('来源项目', '')} / {r.get('备注', '')}" for r in bad_source)

    if bad_terms:
        lines.append("")
        lines.append("## Bad Legacy Terms")
        lines.extend(f"- {r['名称']}" for r in bad_terms)

    return lines


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    normalized = normalize(ROWS + CODE_STRUCTURE_ROWS + STRUCTURAL_CHILD_ROWS)
    enriched = enrich(normalized)
    payload = json.dumps(enriched, ensure_ascii=False, indent=2) + "\n"
    OUT_CANONICAL.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    # v6 remains a compatibility alias while downstream scripts migrate to v7.
    OUT_COMPAT.write_text(payload, encoding="utf-8")
    audit_payload = "\n".join(audit(enriched)) + "\n"
    OUT_AUDIT.write_text(audit_payload, encoding="utf-8")
    OUT_COMPAT_AUDIT.write_text(
        "# v6 Compatibility Audit\n\n"
        "> `kb-functions-algorithms.v6.json` is a migration alias of v7. "
        "The canonical audit follows.\n\n"
        + audit_payload,
        encoding="utf-8",
    )
    print(f"wrote {OUT_CANONICAL} ({len(enriched)} rows)")
    print(f"wrote {OUT_JSON} ({len(enriched)} rows)")
    print(f"wrote {OUT_COMPAT} (compatibility alias)")
    print(f"wrote {OUT_AUDIT}")
    print(f"wrote {OUT_COMPAT_AUDIT} (compatibility notice)")

    # Feature Tree is a generated KB view, never a second source of truth.
    from build_feature_tree import main as build_feature_tree

    build_feature_tree()


if __name__ == "__main__":
    main()
