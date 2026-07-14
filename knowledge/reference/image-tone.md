# 影像基调 / Image Tone

> 来源：[Camera 5.1 - 影像基调（Image Tone）— 自然 & 标准风格](https://nothing-tech.sg.larksuite.com/wiki/ZvxXwZHzEiRCj5koY98l4zKMgaf)，revision 46；最新产品口径更新于 2026-07-14。

## 唯一命名与位置

- 统一名称：`影像基调 / Image Tone`。
- FL 位置：`通用 / Common → 设置 / Settings → 照片设置 / Photo Settings`。
- 不在照片、人像、夜景、专业、高像素等具体模式中重复展开。
- PRD revision 46 中的“下拉工具栏入口”属于旧方案，已被最新产品决定覆盖。

## 功能定义

影像基调通过 ISP pipeline 的 AE & Tone、Color 和锐化参数调整照片的基础观感。提供两种选项：

- `自然 / Natural`：饱和度和对比度接近真实效果，保留高光、阴影和中间调层次。
- `标准 / Standard`：默认选项，饱和度和对比度略高，提供更鲜明的出片效果。

设置长期保持，仅影响后续拍摄，不修改已拍摄照片。首次开启相机时显示自然/标准选择提示。影像基调作用于 JPEG，不影响 RAW；滤镜和调色叠加在影像基调之上，Preset 可保存并恢复该配置。

## FL 验收口径

- 后置所有摄像头支持自然/标准两种基调；前置范围按项目最终配置确认。
- 检查默认值、首次提示、设置持久化、切换后的预览/成片效果和 JPEG 编码耗时。
- 检查与滤镜、调色、Preset、HDR/夜景多帧链路和 Ultra HDR 的叠加关系。
- 确认各具体模式的 Toolbar 中不存在重复的影像基调入口或 FL 行。
