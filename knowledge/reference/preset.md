# Preset（预设）

## 概述

Preset 是滤镜 + Tuning + 相机参数的组合配置，一键切换拍摄风格。Nothing Camera 的差异化功能——竞品仅专业模式可用，Nothing 所有模式可用。

## 依赖

- 纯软件，无硬件限制
- 照片 + 人像 + 视频（1080P30fps）模式
- Tuning 依赖：部分 Preset 需要 Tuning 才能完整体验

## Preset 配置内容

| 类别 | 配置项 |
|------|--------|
| 基础 | 模式、镜头、焦段、曝光 |
| 效果 | 滤镜、Tuning (7参数)、人像虚化、光斑 |
| 附加 | 水印、闪光灯、倒计时、HDR、Auto Tone |
| 高级 | Motion Photo、画质 (50MP)、网格、比例、快门速度 |

## Default Presets（25131 继承自 25111 v3.3）

| 排序 | Preset | 模式 | 说明 |
|------|------|------|------|
| 1 | Cold Retro Future | Photo | 冷复古未来感，Tuning 机型专属 |
| 2 | Urban | Photo | 城市风格，高对比冷调 |
| 3 | Cine Amber | Video | **唯一视频 Preset**，电影琥珀色 |
| 4 | Cricket | Action | 印度独占，快门 ≤1/500 抓拍 |
| 5 | Sports | Action | ROW 地区抓拍 Preset |
| 5 | Amber | Photo | 经典琥珀胶片色 |
| 6 | Stretch | Photo | Jordan Hemingway 联名，深影高光 |
| 6 | B&W Film | Photo | 黑白胶片，50mm 视角 |
| 7 | Retro | Photo | 低饱和冷调，蓝灰色调 |
| 8 | Soft Focus | Portrait | **唯一人像 Preset**，F2.8 柔焦 |
| 9 | Lenticular | Photo | 玻璃折射特效 |
| 10 | Close Up | Macro | **微距 Preset**，3x 长焦细节 |

## 版本演进

| 版本 | 变化 |
|------|------|
| v1.0 (24111) | 5 个基础 Preset |
| v2.1 | +Lens 列，6 个 |
| v3.0 (25111) | +Cold Retro/Urban/Cine Amber，9 个 |
| v3.1 | 顺序与封面调整 |
| v3.2 | +Cricket（印度）|
| v3.3 | +Sports（ROW），Cricket→Sports 拆分 |

## 核心功能

### 快速保存
- 修改参数后底栏出现保存按钮
- 更新已有 / 存为新 Preset / 取消

### 卡片信息
- 显示作者、模式、焦段、滤镜缩写、曝光

### 导入/分享
- 支持用户导入 .cube LUT
- 分享卡片可带封面 + 配置信息

### 封面编辑
- 支持裁切 + 90° 旋转

## 竞品对比

| | Nothing | OPPO | 小米 | Sony |
|------|------|------|------|------|
| 覆盖模式 | 全部 | 仅专业 | 仅专业 | 全部 |
| 自定义调色 | ✅ 7参数 | ✅ | ✅ | ✅ |
| LUT 导入 | ✅ | ❌ | ✅ 手动 | ✅ 手动 |
| 一键分享 | ✅ | ❌ | ❌ | ❌ |
| 使用率 | 1.58% → 目标 2% | - | - | - |

## 埋点

| event | key | 说明 |
|------|------|------|
| preset_save | 1/2/3 | 点击保存 / 覆盖 / 存为新 |
| preset_control | 4/5 | 创建 / 添加封面 |
