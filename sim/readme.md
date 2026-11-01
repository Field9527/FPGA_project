# 验证入口

在项目根目录设置 PYTHONPATH=ac880_fall/ml;board_runtime/app，执行 Python unittest discover ac880_fall/tests；先导入 cache_env，缓存放 E:/Zynq_cache。

JavaScript 视频队列：node ac880_fall/tests/test_video_stream.cjs。

SW0 RTL 自检：Vivado 2025.2 执行 hardware/current/scripts/simulate_switch.tcl，传入新的 E 盘输出目录。原始 TEST_PASS 日志位于 results/。

软件测试不代替识别准确率、时序签核或物理开关完整验收。results/software_tests.log 是本次整理后对导出源码重新运行的结果。
