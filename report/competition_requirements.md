# 自主选题初级组材料索引

本作品采用单块 AC880 开发板，器件为 AMD Zynq-7020（xc7z020clg484-2），硬件工具为 Vivado 2025.2。神经网络在板载 ARM 处理系统执行，PL 负责视频与外设链路。

本索引依据参赛队提供的 fpgachina26-amd-master.zip 中 tracks/open-topic/GUIDE.md 与根目录 TRACK_GUIDE_2026.md 的自主选题要求整理，不套用其他赛道的主机、容器或器件条件。

## 目录与要求对照

| 指南要求 | 对应文件与用途 |
| --- | --- |
| 项目简介与复现步骤 | ../readme.md、../docs/reproduce.md |
| 完整设计源码 | ../hardware/current/sources、../board_runtime/app、../ac880_fall |
| 可复现构建脚本 | ../hardware/current/scripts/build.tcl、../ac880_fall/scripts/build_semantic_runtime.py |
| 仿真或验证结果 | ../sim/results、../ac880_fall/tests、../hardware/current/simulation |
| 综合、实现、时钟与资源 | ../build/reports、../build/readme.md |
| 上板工程与运行脚本 | ../board_runtime、../board/results |
| 实测与参考结果对照 | ../data/validation、optimization_comparison.md |
| 通用技能包 | ../skill/readme.md、../skill/overlay_bundle_check.py、../skill/dma_debug.md |
| 设计报告 | technical_report.pdf、../docs/technical_report.md |
| 提示词、回答与自我纠错 | llm_collaboration.md；保留真实交互节选及对应验证 |
| 开源与再分发说明 | ../license.txt、../license_scope.md、../third_party_notices.md |

推荐目录不是强制结构。本工程将板端运行文件、训练源码和硬件分开存放，避免同一程序重复维护。文件名采用英文小写；readme.md 是指南 README.md 的同等入口，GitHub 可直接显示。仓库名称按参赛队指定使用 FPGA_project。

## 验证依据

- 96 项 Python 回归与 JavaScript 视频队列检查见 sim/results。
- SW0 逻辑 XSim 自检、规范化目录后的 Vivado 重建与 BD 校验日志随包保留。
- 综合和实现报告对应实测配置；重建入口检查不冒充又一次完整实现。
- bit/hwh、模型、NCNN 库与板端静态文件共 50 项由 manifest 配对校验。
- 视频参数探索和开发数据回归保留原始结果及条件，见 optimization_comparison.md；不将开发数据结果写成独立人员准确率。

## 使用与复现边界

配套运行文件可部署到匹配的 AC880 PYNQ/Linux 系统，系统依赖及接线见 docs/reproduce.md。系统镜像、原始训练数据和云端凭据不包含在仓库。当前材料没有精确到镜像构建号的在线环境快照，不能承诺任意新系统无需适配。

第三方 RTL、模型、字体和库保留原有许可与来源。MIT 仅覆盖参赛队原创且有权授权的内容；第三方完整再分发权利仍须按其条件核对，不能由原创 MIT 替代。

代码归档与公开仓库可验证文件一致性。完整的两档物理开关反复切换、独立人员现场评测及硬件时序签核属于实物验收范围，现有软件测试和手机回放不替代这些验收。

## 报名页面的独立材料

正式页面另需演示视频、签署的承诺授权书和规定实物照片。它们不作为源码混入仓库。视频需 MP4 / H.264、时长不超过 3 分钟、体积不超过 300 MB；代码上传项按页面要求使用 RAR、体积不超过 200 MB。技术文档为 PDF、体积不超过 50 MB。最终作品材料需避开学校、指导教师等身份信息。

根指南另要求进入决赛的自主选题队伍使用官方 PPT 模板准备一页英文海报并 A4 彩色打印；当前中文海报用于作品介绍，不能替代该决赛现场要求。
