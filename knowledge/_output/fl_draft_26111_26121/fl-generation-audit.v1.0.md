# 26111 / 26121 FL Draft Audit

This is a distribution draft, not final acceptance sign-off.

## 26111

- Rows: 224
- Status: {'待确认': 99, '已确认': 125}
- Modes: {'照片': 53, '人像': 15, '运动': 3, '视频': 32, '夜景': 24, '慢动作': 15, '全景': 3, '专业': 13, '前后双录': 12, '高像素': 18, '延时摄影': 10, '通用': 26}
- Rows needing fill/review: 104
- Duplicate keys: 0

### Review Queue

| 模式 | 一级分类 | 二级分类 | 名称 | owner | reason |
|---|---|---|---|---|---|
| 照片 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Filter | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Glyph Mirror | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Grid | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | More settings | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Motion Photo | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Motion Photo cover HDR | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Ratio | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Watermark | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 右侧暂态开关 | Text Mode（文本模式） | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 右侧暂态开关 | 自动夜景 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 左侧暂态开关 | 自动微距控制 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | 二维码识别 | Product | REQ26111-KB-004 / update / dispute=medium / PRD 要求只识别一个最大/稳定二维码，识别成功后变焦条区域出现跳转按键。 |
| 照片 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | 识别框视觉动效 | Product | REQ26111-KB-002 / update / dispute=medium / PM correction 2026-07-07: 宠物框不做；该候选只保留识别框视觉动效更新。 |
| 照片 | 功能 | 预览框 | 运动场景引导 | Product | REQ26111-KB-027 / add / dispute=medium / 不改变普通照片轻量运动抓拍，不在前置/视频/人像/夜景/Action 展示。 |
| 照片 | 功能 | 预览框 | 镜头脏污检测 / AI 去油污 / 提示引导 | Product | REQ26111-KB-026 / add / dispute=medium / PRD 030 4.2/4.3 写明检测、AI修复与提示升级；PM correction: 支持照片和人像模式。 |
| 照片 | 算法 | 取帧策略 | PZL | SE | 算法来源行，需 SE 按项目实测确认。 / 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 算法 | 后处理算法 | AI Zoom / AIGC SR | SE | 算法来源行，需 SE 按项目实测确认。 |
| 照片 | 算法 | 后处理算法 | 人脸畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 算法 | 后处理算法 | 超级夜景 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 算法 | 后处理算法 | 人脸畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 算法 | 后处理算法 | 多帧降噪 / MFNR | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 算法 | 后处理算法 | 超级夜景+美颜 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 运动 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 运动 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 运动 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | Mode Switch | 录像中拍照（VSS） | Product | REQ26111-KB-022 / add_exception / dispute=medium / 1080P/4K 均输出 9MP；MFNR、取帧偏差、滤镜保留为 P1/待测。 |
| 视频 | 功能 | Toolbar | 视频曝光调节 / 视频白平衡调节 | Product | REQ26111-KB-019 / add / dispute=medium / 与锁定白平衡关系待确认；退出相机后自动归零。 |
| 视频 | 功能 | Video Specs | 1080P 30FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 1080P 30FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 1080P 60FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 1080P 60FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 30FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 30FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 60FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 60FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 风格-滤镜 / Style-Filter | 风格-滤镜 / Style-Filter | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 风格-调色 / Style-Tuning | 风格-调色 / Style-Tuning | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 风格-调色盘 / Style-Tuning Palette | 风格-调色盘 / Style-Tuning Palette | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 算法 | 实时算法 | HLG / HDR 规格 | SE | 算法来源行，需 SE 按项目实测确认。 |
| 夜景 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 取帧策略 | PZL | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 人脸畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 光学畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 多帧降噪 / MFNR | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 极夜 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 超分 / Super Resolution（SR） | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 超级夜景 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 超级夜景+美颜 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 实时算法 | Photo EIS | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 慢动作 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 在对应模式点按/长按预览画面，确认对焦、测光、锁定、曝光补偿和人脸优先策略符合规格。 |
| 慢动作 | 功能 | Slow Motion Specs | 1080P 120FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 1080P 240FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 1080P 30FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 720P 120FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 720P 240FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 720P 480FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 慢动作 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 慢动作 | 功能 | 预览框 | 人脸检测 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 慢动作 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 全景 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 全景 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 全景 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | Toolbar | 各项专业模式参数极值范围 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 算法 | 取帧策略 | PZL | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 算法 | 后处理算法 | 光学畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 算法 | 实时算法 | Photo EIS | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 风格-滤镜 / Style-Filter | 风格-滤镜 / Style-Filter | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 风格-调色 / Style-Tuning | 风格-调色 / Style-Tuning | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 风格-调色盘 / Style-Tuning Palette | 风格-调色盘 / Style-Tuning Palette | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 延时摄影 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 延时摄影 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 延时摄影 | 功能 | 预览框 | 人脸检测 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 延时摄影 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 通用 | Settings | Video settings | 锁定镜头 | Product | REQ26111-KB-017 / add / dispute=medium / 嵌入 Base 只有一条需求记录，定义清晰。 |
| 通用 | 功能 | Toolbar | 工具栏热区呼出 | Product | REQ26111-KB-005 / review / dispute=high / 需避免把快门区域默认控件误展开进 FL。 |
| 通用 | 功能 | 预览框 | AI Preset 预览引导入口 / 场景推荐 | Product | REQ26111-KB-013 / add / dispute=medium / PRD 016: 相机预览页 AI Preset 按键；R1 为场景推荐，R2 推荐风格待定。PM correction: 预览作为引导入口。 |

## 26121

- Rows: 236
- Status: {'待确认': 103, '已确认': 133}
- Modes: {'照片': 55, '人像': 15, '运动': 3, '视频': 32, '夜景': 35, '慢动作': 15, '全景': 3, '专业': 13, '前后双录': 12, '高像素': 17, '延时摄影': 10, '通用': 26}
- Rows needing fill/review: 105
- Duplicate keys: 0

### Review Queue

| 模式 | 一级分类 | 二级分类 | 名称 | owner | reason |
|---|---|---|---|---|---|
| 照片 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Filter | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Glyph Mirror | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | More settings | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Motion Photo | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Ratio | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Toolbar | Watermark | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 右侧暂态开关 | Text Mode（文本模式） | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 右侧暂态开关 | 自动夜景 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 左侧暂态开关 | 自动微距控制 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | 二维码识别 | Product | REQ26111-KB-004 / update / dispute=medium / PRD 要求只识别一个最大/稳定二维码，识别成功后变焦条区域出现跳转按键。 |
| 照片 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 功能 | 预览框 | 识别框视觉动效 | Product | REQ26111-KB-002 / update / dispute=medium / PM correction 2026-07-07: 宠物框不做；该候选只保留识别框视觉动效更新。 |
| 照片 | 功能 | 预览框 | 运动场景引导 | Product | REQ26111-KB-027 / add / dispute=medium / 不改变普通照片轻量运动抓拍，不在前置/视频/人像/夜景/Action 展示。 |
| 照片 | 功能 | 预览框 | 镜头脏污检测 / AI 去油污 / 提示引导 | Product | REQ26111-KB-026 / add / dispute=medium / PRD 030 4.2/4.3 写明检测、AI修复与提示升级；PM correction: 支持照片和人像模式。 |
| 照片 | 算法 | 取帧策略 | PZL | SE | 算法来源行，需 SE 按项目实测确认。 / 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 算法 | 后处理算法 | AI Zoom / AIGC SR | SE | 算法来源行，需 SE 按项目实测确认。 |
| 照片 | 算法 | 后处理算法 | 人脸畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 照片 | 算法 | 后处理算法 | 超级夜景 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 功能 | 预览框 | 镜头脏污检测 / AI 去油污 / 提示引导 | Product | REQ26111-KB-026 / add / dispute=medium / PRD 030 4.2/4.3 写明检测、AI修复与提示升级；PM correction: 支持照片和人像模式。 |
| 人像 | 算法 | 后处理算法 | 人脸畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 算法 | 后处理算法 | 多帧降噪 / MFNR | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 人像 | 算法 | 后处理算法 | 超级夜景+美颜 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 运动 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 运动 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 运动 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | Mode Switch | 录像中拍照（VSS） | Product | REQ26111-KB-022 / add_exception / dispute=medium / 1080P/4K 均输出 9MP；MFNR、取帧偏差、滤镜保留为 P1/待测。 |
| 视频 | 功能 | Toolbar | Log 视频 | Product | 按 PM 口径：Log 放在视频 Toolbar；支持规格范围仍需根据项目 PRD/平台能力补齐。 |
| 视频 | 功能 | Toolbar | 视频曝光调节 / 视频白平衡调节 | Product | REQ26111-KB-019 / add / dispute=medium / 与锁定白平衡关系待确认；退出相机后自动归零。 |
| 视频 | 功能 | Video Specs | 1080P 30FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 1080P 30FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 1080P 60FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 1080P 60FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 30FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 30FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 60FPS | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Video Specs | 4K 60FPS HLG | SE | 初步按 26111.yaml、P0 功能列表、前置 4K PRD 和算法源表整理；TBD 项需 SE 确认。 |
| 视频 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 风格-滤镜 / Style-Filter | 风格-滤镜 / Style-Filter | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 风格-调色 / Style-Tuning | 风格-调色 / Style-Tuning | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 功能 | 风格-调色盘 / Style-Tuning Palette | 风格-调色盘 / Style-Tuning Palette | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 视频 | 算法 | 实时算法 | HLG / HDR 规格 | SE | 算法来源行，需 SE 按项目实测确认。 |
| 夜景 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | Zoom | 变焦 / Zoom | Product | 在对应模式点击默认变焦点并拖动变焦条，确认倍率范围、镜头切换、画质和稳定性符合项目规格。 |
| 夜景 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 取帧策略 | PZL | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 人脸畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 光学畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 多帧降噪 / MFNR | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 极夜 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 超分 / Super Resolution（SR） | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 超级夜景 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 后处理算法 | 超级夜景+美颜 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 夜景 | 算法 | 实时算法 | Photo EIS | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 慢动作 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 在对应模式点按/长按预览画面，确认对焦、测光、锁定、曝光补偿和人脸优先策略符合规格。 |
| 慢动作 | 功能 | Slow Motion Specs | 1080P 120FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 1080P 240FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 1080P 30FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 720P 120FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 720P 240FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Slow Motion Specs | 720P 480FPS | SE | 按 Product 口径展开为慢动作具体规格；每个项目通常只支持部分规格，需 SE/SQA 填写最终支持列。 |
| 慢动作 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 慢动作 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 慢动作 | 功能 | 预览框 | 人脸检测 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 慢动作 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 全景 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 全景 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 全景 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | AE/AF | 自动对焦-自动曝光 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | Toolbar | 各项专业模式参数极值范围 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | 预览框 | 人脸检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 算法 | 取帧策略 | PZL | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 算法 | 后处理算法 | 光学畸变矫正 | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 专业 | 算法 | 实时算法 | Photo EIS | SE | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 风格-滤镜 / Style-Filter | 风格-滤镜 / Style-Filter | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 风格-调色 / Style-Tuning | 风格-调色 / Style-Tuning | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 前后双录 | 功能 | 风格-调色盘 / Style-Tuning Palette | 风格-调色盘 / Style-Tuning Palette | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 延时摄影 | 功能 | Zoom | 变焦 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 延时摄影 | 功能 | 预览框 | ASD / AI场景检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 延时摄影 | 功能 | 预览框 | 人脸检测 | Product | 在对应触发场景确认预览框、提示或识别结果出现/消失时机正确，点击后的跳转或拍摄行为符合规格。 |
| 延时摄影 | 功能 | 预览框 | 脏污检测 | Product | 由 KB mode scope 展开；需按项目硬件/算法配置确认支持状态。 |
| 通用 | Settings | Video settings | 锁定镜头 | Product | REQ26111-KB-017 / add / dispute=medium / 嵌入 Base 只有一条需求记录，定义清晰。 |
| 通用 | 功能 | Toolbar | 工具栏热区呼出 | Product | REQ26111-KB-005 / review / dispute=high / 需避免把快门区域默认控件误展开进 FL。 |
| 通用 | 功能 | 预览框 | AI Preset 预览引导入口 / 场景推荐 | Product | REQ26111-KB-013 / add / dispute=medium / PRD 016: 相机预览页 AI Preset 按键；R1 为场景推荐，R2 推荐风格待定。PM correction: 预览作为引导入口。 |

