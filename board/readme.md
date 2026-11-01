# 上板文件与实测记录

成套运行文件位于 ../board_runtime，硬件为 AC880 / xc7z020clg484-2，摄像头 OV5640。程序以 PYNQ/Linux 和 ARMv7 NCNN 执行。

先执行 `python skill/overlay_bundle_check.py board_runtime`。断电接好设备后启动已验证系统，将整个 board_runtime 部署至 /home/xilinx/fall_gesture_trial，赋予 run.sh 可执行权限并执行。Linux 系统镜像未打包；需要匹配的 PYNQ 镜像、NumPy、OpenCV、Pillow 和用户权限。现有包不能替代系统镜像，也不保证任意 PYNQ 安装直接运行。

SW0 向下为摔倒，向上为手势。系统信息与完整步骤见 ../docs/reproduce.md。正常停止使用 ./run.sh stop。

results/ 保留实际部署回执：新程序在整板重新上电后正常启动，SW0=1、摄像头就绪，手势模式暂停摔倒推理，用户确认 HDMI 与网页无割裂。两档反复切换、热启动稳定性和独立人员精度尚未完成验收。回执不等于新的现场验收。
