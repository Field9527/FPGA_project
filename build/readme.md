# 可复现硬件构建与报告

Windows / Vivado 2025.2：

```powershell
vivado -mode batch -source hardware/current/scripts/build.tcl -tclargs E:/Zynq_cache/temp/ac880_submission_build
```

默认重建并校验 Block Design，追加 bitstream 才执行综合、实现及 bit 生成。需新的空输出目录，IP 缓存位于 E:/Zynq_cache/vivado_ip。本包保留时钟 IP Tcl、BD、RTL 和 XDC；不包含 Vivado 安装、IP 缓存或项目生成目录。

reports/ 为现有实际运行的 SW0 配置构建报告。仅因目录名规范化而重新检查构建入口，未修改 RTL 功能；不能把这次入口检查当成又一次完整实现。

主要约束时钟：外部 50 MHz、AXI 100 MHz、HDMI 像素 74.25 MHz、串行器 371.25 MHz、摄像头参考输出 24 MHz。时序报告还将 camera_pclk 约束为 74.25 MHz；该约束值不是摄像头现场测频结果。
