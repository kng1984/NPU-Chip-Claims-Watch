# 同口径排名(Like-for-like)

条件:同一模型、同一输入尺寸、INT8 类精度(或来源未标精度)、批大小 1、仅 NPU 推理(不含端到端流水线)。
同一芯片只保留最高值;官方/厂商数据与社区/论坛数据分列。† = 由延迟换算(1000/ms)。「尺寸未标」表示来源没有给输入尺寸。
FPS/TOPS、FPS/(GB/s) 仅在规格表有数据时给出;空白=缺规格。各家测试软件栈与是否含前后处理仍有差异,请当作量级参考。

## YOLOv5s · 640×640

| # | 厂商 | 芯片 | FPS | 类别 | NPU TOPS | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 备注 | 来源 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Hailo | Hailo-8 | 543.0 | 官方 | 26.0 |  | 20.88 |  | 精度未标 | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO8/HAILO8_object_detection.rst) |
| 2 | Axera | AX650/AX8850 | 384.6 | 官方 | 24.0 | 34.1 | 16.03 | 11.28 | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX650_AX8850.md) |
| 3 | Hailo | Hailo-10H | 296.0 | 官方 | 20.0 |  | 14.8 |  | 精度未标 | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO10H/HAILO10H_object_detection.rst) |
| 4 | Hailo | Hailo-8L | 243.0 | 官方 | 13.0 |  | 18.69 |  | 精度未标 | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO8L/HAILO8L_object_detection.rst) |
| 5 | Axera | AX637/AX8910 | 141.0 | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX637_AX8910.md) |
| 6 | Axera | AX630C | 78.7 | 官方 | 3.2 |  | 24.59 |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX630C.md) |
| 7 | Axera | AX620Q | 62.3 | 官方 | 2.4 |  | 25.95 |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX620Q.md) |
| 8 | Rockchip | RK3576 | 57.5 | 官方 | 6.0 | 19.2 | 9.58 | 2.99 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 9 | Axera | AX615 | 50.5 | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX615.md) |
| 10 | Allwinner | A733 | 49.8 | 官方 |  |  |  |  | UINT8 | [link](https://docs.radxa.com/en/cubie/a5e/app-dev/npu-dev/model-zoo/yolov5) |
| 11 | Rockchip | RK3588 | 48.4 | 官方 | 6.0 | 44.0 | 8.07 | 1.1 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 12 | Rockchip | RK3588 | 47.0† | 社区 | 6.0 | 44.0 | 7.84 | 1.07 | INT8 | [link](https://deepseek.csdn.net/6a31fb10662f9a54cb80288d.html) |
| 13 | Rockchip | RK3576 | 42.1† | 社区 | 6.0 | 19.2 | 7.02 | 2.19 | INT8 | [link](https://deepseek.csdn.net/6a31fb10662f9a54cb80288d.html) |
| 14 | Rockchip | RK1808 | 28.2 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 15 | Rockchip | RK3562 | 23.6 | 官方 | 1.0 |  | 23.6 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 16 | Allwinner | T527 | 20.0 | 官方 | 2.0 |  | 10.0 |  | UINT8 | [link](https://docs.radxa.com/en/cubie/a5e/app-dev/npu-dev/model-zoo/yolov5) |
| 17 | Rockchip | RV1126 | 20.0 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 18 | Rockchip | RK3566/RK3568 | 19.3 | 官方 | 0.8 |  | 24.12 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 19 | Rockchip | RV1109 | 13.6 | 官方 | 1.0 |  | 13.6 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## YOLOv8n · 640×640

| # | 厂商 | 芯片 | FPS | 类别 | NPU TOPS | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 备注 | 来源 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Hailo | Hailo-8 | 1036.0 | 官方 | 26.0 |  | 39.85 |  | 精度未标 | [link](https://github.com/hailo-ai/hailo_model_zoo/blob/master/docs/public_models/HAILO8/HAILO8_object_detection.rst) |
| 2 | Axera | AX650/AX8850 | 709.2 | 官方 | 24.0 | 34.1 | 29.55 | 20.8 | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX650_AX8850.md) |
| 3 | Hailo | Hailo-10H | 375.0 | 官方 | 20.0 |  | 18.75 |  | 精度未标 | [link](https://github.com/hailo-ai/hailo_model_zoo/blob/master/docs/public_models/HAILO10H/HAILO10H_object_detection.rst) |
| 4 | Axera | AX637/AX8910 | 212.1 | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX637_AX8910.md) |
| 5 | Hailo | Hailo-8L | 202.0 | 官方 | 13.0 |  | 15.54 |  | 精度未标 | [link](https://github.com/hailo-ai/hailo_model_zoo/blob/master/docs/public_models/HAILO8L/HAILO8L_object_detection.rst) |
| 6 | Hailo | Hailo-8L | 144.7 | 社区 | 13.0 |  | 11.13 |  | 精度未标 | [link](https://github.com/aaronk2001/yolov8-hailo-pi5) |
| 7 | Rockchip | RK3576 | 90.2 | 官方 | 6.0 | 19.2 | 15.03 | 4.7 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 8 | Allwinner | A733 | 79.4 | 官方 |  |  |  |  | UINT8 | [link](https://docs.radxa.com/en/cubie/a5e/app-dev/npu-dev/model-zoo/yolov8) |
| 9 | Rockchip | RK3588 | 73.5 | 官方 | 6.0 | 44.0 | 12.25 | 1.67 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 10 | Axera | AX615 | 65.2† | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX615.md) |
| 11 | Rockchip | RK1808 | 42.3 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 12 | Rockchip | RK3562 | 40.9 | 官方 | 1.0 |  | 40.9 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 13 | Rockchip | RV1126 | 35.4 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 14 | Rockchip | RK3566/RK3568 | 34.0 | 官方 | 0.8 |  | 42.5 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 15 | Allwinner | T527 | 32.3 | 官方 | 2.0 |  | 16.15 |  | UINT8 | [link](https://docs.radxa.com/en/cubie/a5e/app-dev/npu-dev/model-zoo/yolov8) |
| 16 | Rockchip | RV1109 | 24.0 | 官方 | 1.0 |  | 24.0 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## MobileNetV2 · 224×224

| # | 厂商 | 芯片 | FPS | 类别 | NPU TOPS | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 备注 | 来源 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon 8 Elite Gen 5 | 5376.3† | 官方 |  |  |  |  | w8a8 | [link](https://huggingface.co/qualcomm/MobileNet-v2) |
| 2 | Qualcomm | Snapdragon 8 Elite | 4717.0† | 官方 |  | 84.8 |  | 55.62 | w8a8 | [link](https://huggingface.co/qualcomm/MobileNet-v2) |
| 3 | Qualcomm | Snapdragon X2 Elite | 3649.6† | 官方 |  |  |  |  | w8a8 | [link](https://huggingface.co/qualcomm/MobileNet-v2) |
| 4 | Axera | AX650/AX8850 | 3546.1 | 官方 | 24.0 | 34.1 | 147.75 | 103.99 | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX650_AX8850.md) |
| 5 | Qualcomm | Snapdragon 8 Gen 3 | 3413.0† | 官方 |  | 76.8 |  | 44.44 | w8a8 | [link](https://huggingface.co/qualcomm/MobileNet-v2) |
| 6 | Qualcomm | Snapdragon X Elite | 2202.6† | 官方 | 45.0 | 135.0 | 48.95 | 16.32 | w8a8 | [link](https://huggingface.co/qualcomm/MobileNet-v2) |
| 7 | Axera | AX637/AX8910 | 1111.0 | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX637_AX8910.md) |
| 8 | Axera | AX630C | 1083.4† | 官方 | 3.2 |  | 338.57 |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX630C.md) |
| 9 | Axera | AX620Q | 816.3 | 官方 | 2.4 |  | 340.14 |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX620Q.md) |
| 10 | Rockchip | RK3576 | 467.0 | 官方 | 6.0 | 19.2 | 77.83 | 24.32 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 11 | Rockchip | RK3588 | 450.7 | 官方 | 6.0 | 44.0 | 75.12 | 10.24 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 12 | Google Coral | Coral Edge TPU (USB Accelerator) | 384.6† | 官方 | 4.0 |  | 96.15 |  | INT8 | [link](https://coral.ai/docs/edgetpu/benchmarks/) |
| 13 | Google Coral | Coral Edge TPU (Dev Board) | 384.6† | 官方 | 4.0 |  | 96.15 |  | INT8 | [link](https://coral.ai/docs/edgetpu/benchmarks/) |
| 14 | Axera | AX615 | 345.3† | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX615.md) |
| 15 | Rockchip | RV1126 | 322.3 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 16 | Rockchip | RK3562 | 281.3 | 官方 | 1.0 |  | 281.3 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 17 | Rockchip | RV1109 | 212.9 | 官方 | 1.0 |  | 212.9 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 18 | Rockchip | RK3566/RK3568 | 180.7 | 官方 | 0.8 |  | 225.87 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 19 | Rockchip | RK1808 | 170.3 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 20 | Google | Coral Edge TPU (USB Accelerator) | 54.9† | 社区 |  |  |  |  | 精度未标; 尺寸未标 | [link](https://github.com/aallan/benchmarking-ml-on-the-edge) |
| 21 | Google | Coral Edge TPU (Dev Board) | 47.8† | 社区 |  |  |  |  | 精度未标; 尺寸未标 | [link](https://github.com/aallan/benchmarking-ml-on-the-edge) |

## ResNet50 · 224×224

| # | 厂商 | 芯片 | FPS | 类别 | NPU TOPS | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 备注 | 来源 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon X2 Elite | 2445.0† | 官方 |  |  |  |  | w8a8 | [link](https://huggingface.co/qualcomm/ResNet50) |
| 2 | Qualcomm | Snapdragon 8 Elite Gen 5 | 2207.5† | 官方 |  |  |  |  | w8a8 | [link](https://huggingface.co/qualcomm/ResNet50) |
| 3 | Qualcomm | Snapdragon 8 Elite | 2096.4† | 官方 |  | 84.8 |  | 24.72 | w8a8 | [link](https://huggingface.co/qualcomm/ResNet50) |
| 4 | Qualcomm | Snapdragon 8 Gen 3 | 1709.4† | 官方 |  | 76.8 |  | 22.26 | w8a8 | [link](https://huggingface.co/qualcomm/ResNet50) |
| 5 | Qualcomm | Snapdragon X Elite | 1186.2† | 官方 | 45.0 | 135.0 | 26.36 | 8.79 | w8a8 | [link](https://huggingface.co/qualcomm/ResNet50) |
| 6 | Axera | AX650/AX8850 | 749.1 | 官方 | 24.0 | 34.1 | 31.21 | 21.97 | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX650_AX8850.md) |
| 7 | Axera | AX637/AX8910 | 292.0 | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX637_AX8910.md) |
| 8 | Axera | AX630C | 178.1† | 官方 | 3.2 |  | 55.64 |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX630C.md) |
| 9 | Axera | AX620Q | 132.1 | 官方 | 2.4 |  | 55.02 |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX620Q.md) |
| 10 | Rockchip | RK3588 | 110.1 | 官方 | 6.0 | 44.0 | 18.35 | 2.5 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 11 | Rockchip | RK3576 | 99.0 | 官方 | 6.0 | 19.2 | 16.5 | 5.16 | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 12 | Axera | AX615 | 86.1† | 官方 |  |  |  |  | 精度未标 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX615.md) |
| 13 | Rockchip | RK3562 | 54.9 | 官方 | 1.0 |  | 54.9 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 14 | Rockchip | RK3566/RK3568 | 37.9 | 官方 | 0.8 |  | 47.37 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 15 | Rockchip | RK1808 | 37.1 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 16 | Rockchip | RV1126 | 36.2 | 官方 |  |  |  |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 17 | Rockchip | RV1109 | 24.4 | 官方 | 1.0 |  | 24.4 |  | INT8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
