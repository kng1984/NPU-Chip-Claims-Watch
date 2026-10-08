# 排名（按模型 × 精度，FPS 降序）

由 `rank.py` 生成。只比较 fps 指标；同一芯片同模型取最大值（批大小/输入尺寸可能不同，见源 CSV 的 notes）。
FPS/TOPS、FPS/(GB/s) 仅在 `data/chip_specs.csv` 有对应规格时给出，空表示缺规格，**不是 0**。
各厂商测试口径不同，跨厂商排名仅供参考。† = 由延迟换算(1000/latency_ms，批大小1)，非厂商直接给出的 FPS。

## YOLOv5s · n/a

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Hailo | Hailo-8 | 543 | 26.0 |  | 20.88 |  | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO8/HAILO8_object_detection.rst) |
| 2 | Axera | AX650/AX8850 | 384.62 | 24.0 | 34.1 | 16.03 | 11.28 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX650_AX8850.md) |
| 3 | Hailo | Hailo-10H | 296 | 20.0 |  | 14.8 |  | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO10H/HAILO10H_object_detection.rst) |
| 4 | Hailo | Hailo-8L | 243 | 13.0 |  | 18.69 |  | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO8L/HAILO8L_object_detection.rst) |
| 5 | Axera | AX637/AX8910 | 141 |  |  |  |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX637_AX8910.md) |
| 6 | Axera | AX630C | 78.7 | 3.2 |  | 24.59 |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX630C.md) |
| 7 | Axera | AX620Q | 62.27 | 2.4 |  | 25.95 |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX620Q.md) |
| 8 | Axera | AX615 | 50.49 |  |  |  |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX615.md) |

## YOLOv8s · n/a

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Hailo | Hailo-8 | 491 | 26.0 |  | 18.88 |  | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO8/HAILO8_object_detection.rst) |
| 2 | Axera | AX650/AX8850 | 281.77 | 24.0 | 34.1 | 11.74 | 8.26 | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX650_AX8850.md) |
| 3 | Hailo | Hailo-10H | 252 | 20.0 |  | 12.6 |  | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO10H/HAILO10H_object_detection.rst) |
| 4 | Hailo | Hailo-8L | 208 | 13.0 |  | 16.0 |  | [link](https://raw.githubusercontent.com/hailo-ai/hailo_model_zoo/master/docs/public_models/HAILO8L/HAILO8L_object_detection.rst) |
| 5 | Axera | AX637/AX8910 | 88 |  |  |  |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX637_AX8910.md) |
| 6 | Axera | AX630C | 59.13 | 3.2 |  | 18.48 |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX630C.md) |
| 7 | Axera | AX620Q | 45.57 | 2.4 |  | 18.99 |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX620Q.md) |
| 8 | Axera | AX615 | 36.36 |  |  |  |  | [link](https://github.com/AXERA-TECH/ax-samples/blob/main/benchmark/Benchmark_AX615.md) |

## mobilenetv2-12 · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 467 | 6.0 | 22.0 | 77.83 | 21.23 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 450.7 | 6.0 | 44.0 | 75.12 | 10.24 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RV1126 | 322.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 281.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1109 | 212.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 180.7 | 1.0 |  | 180.7 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RK1808 | 170.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## resnet50-v2-7 · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 110.1 | 6.0 | 44.0 | 18.35 | 2.5 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3576 | 99 | 6.0 | 22.0 | 16.5 | 4.5 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 54.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3566/RK3568 | 37.9 | 1.0 |  | 37.9 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK1808 | 37.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 36.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 24.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov5s_relu · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 66.1 | 6.0 | 44.0 | 11.02 | 1.5 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3576 | 65 | 6.0 | 22.0 | 10.83 | 2.95 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 37.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 33.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 29.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 25.5 | 1.0 |  | 25.5 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 20.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov5n · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 112.7 | 6.0 | 22.0 | 18.78 | 5.12 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 82.5 | 6.0 | 44.0 | 13.75 | 1.88 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 61.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RV1126 | 53.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3562 | 47.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 39.7 | 1.0 |  | 39.7 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 36.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov5s · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 57.5 | 6.0 | 22.0 | 9.58 | 2.61 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 48.4 | 6.0 | 44.0 | 8.07 | 1.1 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 28.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 23.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 20 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 19.3 | 1.0 |  | 19.3 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 13.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov5m · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 23.7 | 6.0 | 22.0 | 3.95 | 1.08 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 20.9 | 6.0 | 44.0 | 3.48 | 0.47 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 13.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 10.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 8.6 | 1.0 |  | 8.6 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 8.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 5.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov6n · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 109.1 | 6.0 | 22.0 | 18.18 | 4.96 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 106.4 | 6.0 | 44.0 | 17.73 | 2.42 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 66.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RV1126 | 56.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3562 | 56.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 48.8 | 1.0 |  | 48.8 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 37.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov6s · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 36.4 | 6.0 | 44.0 | 6.07 | 0.83 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3576 | 35 | 6.0 | 22.0 | 5.83 | 1.59 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 24.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 17.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 16.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 15.2 | 1.0 |  | 15.2 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 10.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov6m · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 17.8 | 6.0 | 44.0 | 2.97 | 0.4 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3576 | 17.4 | 6.0 | 22.0 | 2.9 | 0.79 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 11.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 8.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 8.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 7.2 | 1.0 |  | 7.2 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 5.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov7-tiny · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 74.8 | 6.0 | 22.0 | 12.47 | 3.4 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 72.7 | 6.0 | 44.0 | 12.12 | 1.65 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 37.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 36.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 27.9 | 1.0 |  | 27.9 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 22.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 15.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov7 · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 13 | 6.0 | 22.0 | 2.17 | 0.59 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 11.4 | 6.0 | 44.0 | 1.9 | 0.26 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 7.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 5.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 4.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 4.6 | 1.0 |  | 4.6 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 3.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov8n · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 90.2 | 6.0 | 22.0 | 15.03 | 4.1 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 73.5 | 6.0 | 44.0 | 12.25 | 1.67 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 42.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 40.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 35.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 34 | 1.0 |  | 34.0 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 24 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov8s · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 40.8 | 6.0 | 22.0 | 6.8 | 1.85 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 38 | 6.0 | 44.0 | 6.33 | 0.86 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 19.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 18.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 15.1 | 1.0 |  | 15.1 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 13.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 8.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov8m · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 16.7 | 6.0 | 22.0 | 2.78 | 0.76 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 16.2 | 6.0 | 44.0 | 2.7 | 0.37 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 9.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 8.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 6.5 | 1.0 |  | 6.5 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 5.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 3.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov8n-obb · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 90.2 | 6.0 | 22.0 | 15.03 | 4.1 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 74 | 6.0 | 44.0 | 12.33 | 1.68 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 42.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 41.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 37.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 33.9 | 1.0 |  | 33.9 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 25.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolo11n · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 77.9 | 6.0 | 22.0 | 12.98 | 3.54 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 60 | 6.0 | 44.0 | 10.0 | 1.36 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 34 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3566/RK3568 | 20.6 | 1.0 |  | 20.6 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK1808 | 17.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 17 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 11.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolo11s · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 38.2 | 6.0 | 22.0 | 6.37 | 1.74 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 33 | 6.0 | 44.0 | 5.5 | 0.75 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 16.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3566/RK3568 | 10.2 | 1.0 |  | 10.2 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK1808 | 8.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 7.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolo11m · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 14.6 | 6.0 | 22.0 | 2.43 | 0.66 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 12.7 | 6.0 | 44.0 | 2.12 | 0.29 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 6.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK1808 | 5.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 4.6 | 1.0 |  | 4.6 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 2.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolox_s · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 41.5 | 6.0 | 22.0 | 6.92 | 1.89 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 37.1 | 6.0 | 44.0 | 6.18 | 0.84 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 23 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 18.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 15.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 15.2 | 1.0 |  | 15.2 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 10.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolox_m · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 17.6 | 6.0 | 22.0 | 2.93 | 0.8 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 16 | 6.0 | 44.0 | 2.67 | 0.36 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 10.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 8.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 6.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 6.6 | 1.0 |  | 6.6 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 4.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## ppyoloe_s · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 41.3 | 6.0 | 22.0 | 6.88 | 1.88 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 32.5 | 6.0 | 44.0 | 5.42 | 0.74 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 21.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 20 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 17.1 | 1.0 |  | 17.1 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 16.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 11.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## ppyoloe_m · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 17.8 | 6.0 | 22.0 | 2.97 | 0.81 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 15.8 | 6.0 | 44.0 | 2.63 | 0.36 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 9.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 9.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 7.8 | 1.0 |  | 7.8 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 7.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 5.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## deeplab-v3-plus-mobilenet-v2 · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 39.4 | 6.0 | 22.0 | 6.57 | 1.79 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 34 | 6.0 | 44.0 | 5.67 | 0.77 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 21.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RV1126 | 13 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 10.9 | 1.0 |  | 10.9 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1109 | 10.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RK1808 | 4.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov5n-seg · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 88.3 | 6.0 | 22.0 | 14.72 | 4.01 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 69.3 | 6.0 | 44.0 | 11.55 | 1.57 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 49.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RV1126 | 42.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3562 | 38.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 32.2 | 1.0 |  | 32.2 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 28.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov5s-seg · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 41.6 | 6.0 | 22.0 | 6.93 | 1.89 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 36.8 | 6.0 | 44.0 | 6.13 | 0.84 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 22.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 18.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 15 | 1.0 |  | 15.0 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 14 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 9.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov5m-seg · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 18 | 6.0 | 22.0 | 3.0 | 0.82 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 16.4 | 6.0 | 44.0 | 2.73 | 0.37 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 10.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 8.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 6.8 | 1.0 |  | 6.8 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 6.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 4.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov8n-seg · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 71.1 | 6.0 | 22.0 | 11.85 | 3.23 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 60.8 | 6.0 | 44.0 | 10.13 | 1.38 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 33 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK1808 | 32.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 27.8 | 1.0 |  | 27.8 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 27.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 18.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov8s-seg · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 30.8 | 6.0 | 22.0 | 5.13 | 1.4 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 28.9 | 6.0 | 44.0 | 4.82 | 0.66 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 14.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 14.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 11.7 | 1.0 |  | 11.7 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 9.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 6.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## yolov8m-seg · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 12.7 | 6.0 | 22.0 | 2.12 | 0.58 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 12.6 | 6.0 | 44.0 | 2.1 | 0.29 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK1808 | 6.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3562 | 6.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK3566/RK3568 | 5.2 | 1.0 |  | 5.2 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 4.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 3.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## ppseg_lite_1024x512 · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 35.7 | 6.0 | 44.0 | 5.95 | 0.81 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3576 | 33.6 | 6.0 | 22.0 | 5.6 | 1.53 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RV1126 | 27.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK1808 | 20.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1109 | 18.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3562 | 13.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RK3566/RK3568 | 5.9 | 1.0 |  | 5.9 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## RetinaFace_mobile320 · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 470.5 | 6.0 | 22.0 | 78.42 | 21.39 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3562 | 300.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3588 | 227.2 | 6.0 | 44.0 | 37.87 | 5.16 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RV1126 | 212.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK1808 | 198.5 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 156.4 | 1.0 |  | 156.4 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 144.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## RetinaFace_resnet50_320 · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 56.6 | 6.0 | 22.0 | 9.43 | 2.57 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 49.2 | 6.0 | 44.0 | 8.2 | 1.12 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 26.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK1808 | 24.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 20.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK3566/RK3568 | 18.7 | 1.0 |  | 18.7 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 14.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## ppocrv4_det · INT8

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 64.3 | 6.0 | 22.0 | 10.72 | 2.92 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 50.7 | 6.0 | 44.0 | 8.45 | 1.15 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 28 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3566/RK3568 | 22.1 | 1.0 |  | 22.1 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RV1126 | 16.1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RK1808 | 14.2 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 11 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## ppocrv4_rec · FP16

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3576 | 96.8 | 6.0 | 22.0 | 16.13 | 4.4 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3588 | 73.9 | 6.0 | 44.0 | 12.32 | 1.68 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 54.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3566/RK3568 | 19.5 | 1.0 |  | 19.5 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK1808 | 6.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 1.6 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 1 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## lite-transformer-encoder-16 · FP16

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 867.6 | 6.0 | 44.0 | 144.6 | 19.72 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3576 | 784.1 | 6.0 | 22.0 | 130.68 | 35.64 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 725.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3566/RK3568 | 337.5 | 1.0 |  | 337.5 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK1808 | 98.3 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 35.4 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 22.7 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## lite-transformer-decoder-16 · FP16

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 343.8 | 6.0 | 44.0 | 57.3 | 7.81 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 2 | Rockchip | RK3576 | 272.3 | 6.0 | 22.0 | 45.38 | 12.38 | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 3 | Rockchip | RK3562 | 252 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 4 | Rockchip | RK3566/RK3568 | 142.5 | 1.0 |  | 142.5 |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 5 | Rockchip | RK1808 | 109.9 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 6 | Rockchip | RV1126 | 65.8 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |
| 7 | Rockchip | RV1109 | 48 |  |  |  |  | [link](https://github.com/airockchip/rknn_model_zoo/blob/main/README.md) |

## ConvNext-Tiny · float

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon 8 Elite Gen 5 | 761.615† |  |  |  |  | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 2 | Qualcomm | Snapdragon X2 Elite | 751.88† |  |  |  |  | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 3 | Qualcomm | Snapdragon 8 Elite | 641.026† |  | 84.8 |  | 7.56 | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 4 | Qualcomm | Snapdragon 8 Gen 3 | 493.583† |  | 76.8 |  | 6.43 | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 5 | Qualcomm | Snapdragon X Elite | 375.375† | 45.0 | 135.0 | 8.34 | 2.78 | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |

## ConvNext-Tiny · w8a16

| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |
|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon X2 Elite | 1153.4† |  |  |  |  | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 2 | Qualcomm | Snapdragon 8 Elite Gen 5 | 1149.43† |  |  |  |  | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 3 | Qualcomm | Snapdragon 8 Elite | 925.069† |  | 84.8 |  | 10.91 | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 4 | Qualcomm | Snapdragon 8 Gen 3 | 650.195† |  | 76.8 |  | 8.47 | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
| 5 | Qualcomm | Snapdragon X Elite | 456.413† | 45.0 | 135.0 | 10.14 | 3.38 | [link](https://huggingface.co/qualcomm/ConvNext-Tiny) |
