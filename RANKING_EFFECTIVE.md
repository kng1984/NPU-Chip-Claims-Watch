# 等效算力排名(按真实性能折算)

等效 TOPS = 实测 FPS × 单次推理 GOPs(`data/model_ops.csv`,GOPs=2×MACs) ÷ 1000。只用 INT8 类精度(或来源未标精度)、批大小 1、仅 NPU 推理的行;延迟按 1000/ms 换算。
利用率 = 等效 TOPS 中位数 ÷ 标称 INT8 TOPS(标称算力缺失则为空)。区间 = 该芯片在所列模型上的最低到最高等效 TOPS。样本数 <3 的行请谨慎对待。
注意:各家 GOPs 口径(2×MAC)统一,但模型变体(如 YOLOv5s 的 Hailo 版与 Ultralytics 版)、算子是否在 NPU 上全部执行、是否含前后处理仍可能不同。

## 一、CNN 总榜(检测+分类+分割+人脸+姿态)

| # | 厂商 | 芯片 | 类别 | 样本数 | 等效 TOPS 中位 | 区间(最低–最高) | 标称 TOPS | 利用率(中位/标称) | 带宽 GB/s | 等效TOPS/(GB/s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon 8 Elite Gen 5 | 官方 | 7 | 12.49 | 2.62–22.22 |  |  |  |  |
| 2 | Qualcomm | Snapdragon X2 Elite | 官方 | 7 | 12.05 | 1.59–27.71 |  |  |  |  |
| 3 | Qualcomm | Snapdragon 8 Elite | 官方 | 7 | 11.51 | 2.24–21.28 |  |  | 84.8 | 0.136 |
| 4 | Hailo | Hailo-8 | 官方 | 9 | 9.47 | 1.52–14.04 | 26.0 | 36% |  |  |
| 5 | Qualcomm | Snapdragon 8 Gen 3 | 官方 | 7 | 9.32 | 1.81–17.73 |  |  | 76.8 | 0.121 |
| 6 | Axera | AX650/AX8850 | 官方 | 31 | 6.71 | 2.13–14.49 | 24.0 | 28% | 34.1 | 0.197 |
| 7 | Qualcomm | Snapdragon X Elite | 官方 | 7 | 6.47 | 0.82–13.64 | 45.0 | 14% | 135.0 | 0.048 |
| 8 | Hailo | Hailo-10H | 官方 | 5 | 5.16 | 1.16–10.41 | 20.0 | 26% |  |  |
| 9 | Hailo | Hailo-8L | 官方 | 8 | 2.34 | 0.82–6.86 | 13.0 | 18% |  |  |
| 10 | Axera | AX637/AX8910 | 官方 | 19 | 2.05 | 0.67–4.80 |  |  |  |  |
| 11 | Axera | AX630C | 官方 | 14 | 1.40 | 0.65–3.30 | 3.2 | 44% |  |  |
| 12 | Axera | AX620Q | 官方 | 11 | 1.08 | 0.49–2.61 | 2.4 | 45% |  |  |
| 13 | Hailo | Hailo-8 | 社区 | 2(样本少) | 1.02 | 0.42–1.63 | 26.0 | 4% |  |  |
| 14 | Rockchip | RK3576 | 官方 | 23 | 1.00 | 0.28–1.59 | 6.0 | 17% | 22.0 | 0.046 |
| 15 | Rockchip | RK3588 | 官方 | 23 | 0.90 | 0.27–1.65 | 6.0 | 15% | 34.1 | 0.026 |
| 16 | Allwinner | A733 | 官方 | 8 | 0.88 | 0.60–1.86 |  |  |  |  |
| 17 | Rockchip | RK3588 | 社区 | 1(样本少) | 0.82 | 0.82–0.82 | 6.0 | 14% | 34.1 | 0.024 |
| 18 | Axera | AX615 | 官方 | 11 | 0.80 | 0.21–2.09 |  |  |  |  |
| 19 | Hailo | Hailo-8L | 社区 | 5 | 0.78 | 0.25–1.60 | 13.0 | 6% |  |  |
| 20 | Rockchip | RK3576 | 社区 | 1(样本少) | 0.73 | 0.73–0.73 | 6.0 | 12% | 22.0 | 0.033 |
| 21 | Rockchip | RK1808 | 官方 | 20 | 0.53 | 0.10–1.09 |  |  |  |  |
| 22 | Rockchip | RK3562 | 官方 | 23 | 0.45 | 0.17–0.78 | 1.0 | 45% |  |  |
| 23 | Rockchip | RV1126 | 官方 | 20 | 0.36 | 0.11–0.74 |  |  |  |  |
| 24 | Allwinner | T527 | 官方 | 8 | 0.36 | 0.24–1.04 | 2.0 | 18% |  |  |
| 25 | Rockchip | RK3566/RK3568 | 官方 | 23 | 0.35 | 0.11–0.69 | 0.8 | 44% |  |  |
| 26 | Google Coral | Coral Edge TPU (USB Accelerator) | 官方 | 4 | 0.26 | 0.10–0.47 | 4.0 | 7% |  |  |
| 27 | Rockchip | RV1109 | 官方 | 20 | 0.25 | 0.08–0.49 | 1.0 | 25% |  |  |
| 28 | Google Coral | Coral Edge TPU (Dev Board) | 官方 | 4 | 0.24 | 0.09–0.47 | 4.0 | 6% |  |  |
| 29 | Google | Coral Edge TPU (USB Accelerator) | 社区 | 1(样本少) | 0.03 | 0.03–0.03 |  |  |  |  |
| 30 | Google | Coral Edge TPU (Dev Board) | 社区 | 1(样本少) | 0.03 | 0.03–0.03 |  |  |  |  |

## 二、Transformer 视觉模型(Swin / ViT / DeiT / FastViT)

| # | 厂商 | 芯片 | 类别 | 样本数 | 等效 TOPS 中位 | 区间(最低–最高) | 标称 TOPS | 利用率(中位/标称) | 带宽 GB/s | 等效TOPS/(GB/s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon 8 Elite Gen 5 | 官方 | 1(样本少) | 8.78 | 8.78–8.78 |  |  |  |  |
| 2 | Qualcomm | Snapdragon X2 Elite | 官方 | 1(样本少) | 7.63 | 7.63–7.63 |  |  |  |  |
| 3 | Qualcomm | Snapdragon 8 Elite | 官方 | 1(样本少) | 6.04 | 6.04–6.04 |  |  | 84.8 | 0.071 |
| 4 | Qualcomm | Snapdragon 8 Gen 3 | 官方 | 1(样本少) | 5.01 | 5.01–5.01 |  |  | 76.8 | 0.065 |
| 5 | Axera | AX650/AX8850 | 官方 | 1(样本少) | 3.60 | 3.60–3.60 | 24.0 | 15% | 34.1 | 0.106 |
| 6 | Qualcomm | Snapdragon X Elite | 官方 | 1(样本少) | 3.25 | 3.25–3.25 | 45.0 | 7% | 135.0 | 0.024 |
| 7 | Hailo | Hailo-8 | 官方 | 3 | 2.84 | 1.06–3.77 | 26.0 | 11% |  |  |
| 8 | Axera | AX637/AX8910 | 官方 | 1(样本少) | 1.83 | 1.83–1.83 |  |  |  |  |
| 9 | Axera | AX630C | 官方 | 1(样本少) | 0.62 | 0.62–0.62 | 3.2 | 19% |  |  |
| 10 | Axera | AX620Q | 官方 | 1(样本少) | 0.46 | 0.46–0.46 | 2.4 | 19% |  |  |
| 11 | Axera | AX615 | 官方 | 1(样本少) | 0.33 | 0.33–0.33 |  |  |  |  |

## 三、按应用场景

### 目标检测

| # | 厂商 | 芯片 | 类别 | 样本数 | 等效 TOPS 中位 | 区间(最低–最高) | 标称 TOPS | 利用率(中位/标称) | 带宽 GB/s | 等效TOPS/(GB/s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Hailo | Hailo-8 | 官方 | 6 | 9.95 | 2.54–14.04 | 26.0 | 38% |  |  |
| 2 | Axera | AX650/AX8850 | 官方 | 17 | 6.71 | 3.99–14.49 | 24.0 | 28% | 34.1 | 0.197 |
| 3 | Hailo | Hailo-10H | 官方 | 5 | 5.16 | 1.16–10.41 | 20.0 | 26% |  |  |
| 4 | Hailo | Hailo-8L | 官方 | 5 | 4.24 | 0.89–6.86 | 13.0 | 33% |  |  |
| 5 | Axera | AX637/AX8910 | 官方 | 9 | 2.10 | 1.35–4.80 |  |  |  |  |
| 6 | Axera | AX630C | 官方 | 8 | 1.53 | 1.10–3.30 | 3.2 | 48% |  |  |
| 7 | Axera | AX620Q | 官方 | 6 | 1.19 | 0.89–2.61 | 2.4 | 50% |  |  |
| 8 | Rockchip | RK3576 | 官方 | 17 | 1.03 | 0.51–1.59 | 6.0 | 17% | 22.0 | 0.047 |
| 9 | Hailo | Hailo-8 | 社区 | 2(样本少) | 1.02 | 0.42–1.63 | 26.0 | 4% |  |  |
| 10 | Rockchip | RK3588 | 官方 | 17 | 0.99 | 0.39–1.65 | 6.0 | 17% | 34.1 | 0.029 |
| 11 | Axera | AX615 | 官方 | 9 | 0.88 | 0.52–2.09 |  |  |  |  |
| 12 | Rockchip | RK3588 | 社区 | 1(样本少) | 0.82 | 0.82–0.82 | 6.0 | 14% | 34.1 | 0.024 |
| 13 | Hailo | Hailo-8L | 社区 | 5 | 0.78 | 0.25–1.60 | 13.0 | 6% |  |  |
| 14 | Allwinner | A733 | 官方 | 6 | 0.78 | 0.60–1.86 |  |  |  |  |
| 15 | Rockchip | RK3576 | 社区 | 1(样本少) | 0.73 | 0.73–0.73 | 6.0 | 12% | 22.0 | 0.033 |
| 16 | Rockchip | RK1808 | 官方 | 15 | 0.55 | 0.11–1.09 |  |  |  |  |
| 17 | Rockchip | RK3562 | 官方 | 17 | 0.49 | 0.22–0.78 | 1.0 | 49% |  |  |
| 18 | Rockchip | RK3566/RK3568 | 官方 | 17 | 0.39 | 0.13–0.69 | 0.8 | 48% |  |  |
| 19 | Rockchip | RV1126 | 官方 | 15 | 0.37 | 0.11–0.74 |  |  |  |  |
| 20 | Allwinner | T527 | 官方 | 6 | 0.32 | 0.24–1.04 | 2.0 | 16% |  |  |
| 21 | Rockchip | RV1109 | 官方 | 15 | 0.25 | 0.08–0.49 | 1.0 | 25% |  |  |

### 图像分类

| # | 厂商 | 芯片 | 类别 | 样本数 | 等效 TOPS 中位 | 区间(最低–最高) | 标称 TOPS | 利用率(中位/标称) | 带宽 GB/s | 等效TOPS/(GB/s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon 8 Elite Gen 5 | 官方 | 7 | 12.49 | 2.62–22.22 |  |  |  |  |
| 2 | Qualcomm | Snapdragon X2 Elite | 官方 | 7 | 12.05 | 1.59–27.71 |  |  |  |  |
| 3 | Qualcomm | Snapdragon 8 Elite | 官方 | 7 | 11.51 | 2.24–21.28 |  |  | 84.8 | 0.136 |
| 4 | Qualcomm | Snapdragon 8 Gen 3 | 官方 | 7 | 9.32 | 1.81–17.73 |  |  | 76.8 | 0.121 |
| 5 | Qualcomm | Snapdragon X Elite | 官方 | 7 | 6.47 | 0.82–13.64 | 45.0 | 14% | 135.0 | 0.048 |
| 6 | Axera | AX650/AX8850 | 官方 | 6 | 5.12 | 2.13–6.84 | 24.0 | 21% | 34.1 | 0.150 |
| 7 | Hailo | Hailo-8 | 官方 | 3 | 3.77 | 1.52–11.22 | 26.0 | 14% |  |  |
| 8 | Axera | AX637/AX8910 | 官方 | 2(样本少) | 1.53 | 0.67–2.39 |  |  |  |  |
| 9 | Axera | AX630C | 官方 | 6 | 1.35 | 0.65–1.62 | 3.2 | 42% |  |  |
| 10 | Hailo | Hailo-8L | 官方 | 3 | 1.13 | 0.82–2.92 | 13.0 | 9% |  |  |
| 11 | Axera | AX620Q | 官方 | 5 | 1.06 | 0.49–1.20 | 2.4 | 44% |  |  |
| 12 | Rockchip | RK3588 | 官方 | 2(样本少) | 0.59 | 0.27–0.90 | 6.0 | 10% | 34.1 | 0.017 |
| 13 | Rockchip | RK3576 | 官方 | 2(样本少) | 0.55 | 0.28–0.81 | 6.0 | 9% | 22.0 | 0.025 |
| 14 | Axera | AX615 | 官方 | 2(样本少) | 0.46 | 0.21–0.70 |  |  |  |  |
| 15 | Rockchip | RK3562 | 官方 | 2(样本少) | 0.31 | 0.17–0.45 | 1.0 | 31% |  |  |
| 16 | Google Coral | Coral Edge TPU (USB Accelerator) | 官方 | 4 | 0.26 | 0.10–0.47 | 4.0 | 7% |  |  |
| 17 | Rockchip | RV1126 | 官方 | 2(样本少) | 0.24 | 0.19–0.30 |  |  |  |  |
| 18 | Google Coral | Coral Edge TPU (Dev Board) | 官方 | 4 | 0.24 | 0.09–0.47 | 4.0 | 6% |  |  |
| 19 | Rockchip | RK3566/RK3568 | 官方 | 2(样本少) | 0.21 | 0.11–0.31 | 0.8 | 26% |  |  |
| 20 | Rockchip | RK1808 | 官方 | 2(样本少) | 0.20 | 0.10–0.30 |  |  |  |  |
| 21 | Rockchip | RV1109 | 官方 | 2(样本少) | 0.16 | 0.13–0.20 | 1.0 | 16% |  |  |
| 22 | Google | Coral Edge TPU (USB Accelerator) | 社区 | 1(样本少) | 0.03 | 0.03–0.03 |  |  |  |  |
| 23 | Google | Coral Edge TPU (Dev Board) | 社区 | 1(样本少) | 0.03 | 0.03–0.03 |  |  |  |  |

### 分割

| # | 厂商 | 芯片 | 类别 | 样本数 | 等效 TOPS 中位 | 区间(最低–最高) | 标称 TOPS | 利用率(中位/标称) | 带宽 GB/s | 等效TOPS/(GB/s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Axera | AX650/AX8850 | 官方 | 4 | 7.08 | 4.72–9.00 | 24.0 | 29% | 34.1 | 0.208 |
| 2 | Axera | AX637/AX8910 | 官方 | 4 | 2.15 | 1.66–2.72 |  |  |  |  |
| 3 | Rockchip | RK3576 | 官方 | 3 | 1.31 | 0.90–1.40 | 6.0 | 22% | 22.0 | 0.060 |
| 4 | Rockchip | RK3588 | 官方 | 3 | 1.23 | 0.77–1.39 | 6.0 | 21% | 34.1 | 0.036 |
| 5 | Allwinner | A733 | 官方 | 1(样本少) | 1.12 | 1.12–1.12 |  |  |  |  |
| 6 | Rockchip | RK1808 | 官方 | 3 | 0.62 | 0.41–0.76 |  |  |  |  |
| 7 | Rockchip | RK3562 | 官方 | 3 | 0.60 | 0.42–0.71 | 1.0 | 60% |  |  |
| 8 | Rockchip | RK3566/RK3568 | 官方 | 3 | 0.50 | 0.35–0.57 | 0.8 | 62% |  |  |
| 9 | Allwinner | T527 | 官方 | 1(样本少) | 0.48 | 0.48–0.48 | 2.0 | 24% |  |  |
| 10 | Rockchip | RV1126 | 官方 | 3 | 0.42 | 0.35–0.51 |  |  |  |  |
| 11 | Rockchip | RV1109 | 官方 | 3 | 0.28 | 0.23–0.34 | 1.0 | 28% |  |  |

### 姿态

| # | 厂商 | 芯片 | 类别 | 样本数 | 等效 TOPS 中位 | 区间(最低–最高) | 标称 TOPS | 利用率(中位/标称) | 带宽 GB/s | 等效TOPS/(GB/s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Axera | AX650/AX8850 | 官方 | 4 | 6.58 | 4.98–8.02 | 24.0 | 27% | 34.1 | 0.193 |
| 2 | Axera | AX637/AX8910 | 官方 | 4 | 1.97 | 1.65–2.47 |  |  |  |  |
| 3 | Allwinner | A733 | 官方 | 1(样本少) | 0.92 | 0.92–0.92 |  |  |  |  |
| 4 | Rockchip | RK3576 | 官方 | 1(样本少) | 0.61 | 0.61–0.61 | 6.0 | 10% | 22.0 | 0.028 |
| 5 | Rockchip | RK3588 | 官方 | 1(样本少) | 0.51 | 0.51–0.51 | 6.0 | 9% | 34.1 | 0.015 |
| 6 | Allwinner | T527 | 官方 | 1(样本少) | 0.43 | 0.43–0.43 | 2.0 | 21% |  |  |
| 7 | Rockchip | RK3562 | 官方 | 1(样本少) | 0.29 | 0.29–0.29 | 1.0 | 29% |  |  |
| 8 | Rockchip | RK3566/RK3568 | 官方 | 1(样本少) | 0.21 | 0.21–0.21 | 0.8 | 26% |  |  |

## 四、端侧大模型(LLM/VLM decode)

解码每个 token 要读一遍全部权重,因此 **等效内存吞吐 = tokens/s × 参数量 × 位宽/8**(GB/s,只算权重,不含 KV cache 与量化缩放,实际略高)。带宽利用率 = 等效吞吐 ÷ 理论峰值带宽。
参数量取自模型名(如 1.5B)、位宽取自精度标注(w4a16→4);未标精度/参数的行已剔除;Qualcomm 仅取 GENIE(QAIRT) 运行时、不含 llama.cpp 与车规 Dragonwing/SA 系列;Sophgo 未映射到具体芯片的平台已剔除。

| # | 厂商 | 芯片 | 类别 | 模型数 | 等效内存吞吐 中位 GB/s | 区间 | 理论带宽 GB/s | 带宽利用率(中位) | 代表模型(tokens/s) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon X2 Elite | 官方 | 16 | 82.6 | 6.7–131.3 |  |  | Llama-v3.2-3B-Instruct-SSD 4bit 87.5; Qwen3-8B 4bit 25.0 |
| 2 | Qualcomm | Snapdragon 8 Elite Gen 5 | 官方 | 14 | 45.9 | 17.9–82.8 |  |  | Llama-v3.2-3B-Instruct-SSD 4bit 55.2; Llama-v3-8B-Instruct 4bit 15.1 |
| 3 | Qualcomm | Snapdragon X Elite | 官方 | 15 | 42.4 | 6.7–80.4 | 135.0 | 31% | Llama-v3.2-3B-Instruct-SSD 4bit 53.6; Qwen3-8B 4bit 13.6 |
| 4 | Qualcomm | Snapdragon 8 Elite | 官方 | 14 | 40.3 | 17.5–69.2 | 84.8 | 47% | Llama-v3.2-3B-Instruct-SSD 4bit 46.1; Llama-v3-8B-Instruct 4bit 13.7 |
| 5 | Sophgo | CV84X6 | 官方 | 2(样本少) | 38.8 | 35.2–42.4 |  |  | Qwen / qwen3-4b-awq_w4f16_se 4bit 21.2; Qwen3_5 / qwen3.5-2b-int4-au 4bit 35.2 |
| 6 | Sophgo | BM1684X | 官方 | 15 | 38.6 | 23.9–51.8 |  |  | ChatGLM2 / chatglm2-6b_int8. 8bit 8.6; ChatGLM3 / chatglm3-6b_int8. 8bit 8.2 |
| 7 | Sophgo | BM1684X | 社区 | 1(样本少) | 38.3 | 38.3–38.3 |  |  | Llama3-8B 4bit 9.6 |
| 8 | Rockchip | RK3588 | 官方 | 19 | 23.8 | 19.7–30.5 | 34.1 | 70% | TeleChat2 3B 8bit 10.2; ChatGLM3 6B 8bit 5.0 |
| 9 | Axera | AX650/AX8850 | 官方 | 22 | 14.4 | 2.7–18.9 | 34.1 | 42% | DeepSeek-R1-Distill-Qwen-7B 8bit 2.7; Qwen2.5-7B-Instruct 8bit 2.6 |
| 10 | Sophgo | BM1688 | 官方 | 4 | 13.6 | 9.6–19.1 | 34.1 | 40% | Qwen / qwen1.5-1.8b_int4_seq 4bit 21.2; ChatGLM3 / chatglm3-6b_int4_ 4bit 5.1 |
| 11 | Rockchip | RK3576 | 官方 | 34 | 10.9 | 7.5–15.4 | 22.0 | 50% | TeleChat2 3B 8bit 5.1; ChatGLM3 6B 8bit 2.5 |
| 12 | Rockchip | RK3588 | 社区 | 1(样本少) | 10.8 | 10.8–10.8 | 34.1 | 32% | Qwen 1.5 0.5B 8bit 21.6 |
| 13 | Sophgo | CV186X | 官方 | 2(样本少) | 10.2 | 8.6–11.9 |  |  | Qwen / qwen1.5-1.8b_int4_seq 4bit 13.2; MiniCPM4 / minicpm4-0.5b-gpt 4bit 34.3 |
| 14 | Axera | AX650/AX8850 | 社区 | 1(样本少) | 7.7 | 7.7–7.7 | 34.1 | 23% | Qwen3-0.6B 8bit 12.9 |
| 15 | Rockchip | RK3562 | 官方 | 4 | 6.4 | 5.0–6.8 |  |  | Qwen2 0.5B 8bit 13.6; Qwen3 0.6B 8bit 10.9 |
| 16 | Axera | AX630C | 官方 | 1(样本少) | 6.0 | 6.0–6.0 |  |  | MiniCPM4-0.5B 8bit 12.0 |
| 17 | Rockchip | RV1126B | 官方 | 8 | 5.8 | 4.1–7.6 |  |  | MiniCPM4 0.5B 8bit 15.2; Qwen2 0.5B 8bit 13.6 |

### 同尺寸对比(tokens/s,取各芯片最高)

**≈0.5B · 4bit**

| # | 厂商 | 芯片 | 类别 | tokens/s | 模型 | 理论带宽 | 带宽利用率 |
|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon X2 Elite | 官方 | 135.7 | Qwen3-0.6B |  |  |
| 2 | Qualcomm | Snapdragon 8 Elite Gen 5 | 官方 | 132.8 | Qwen3-0.6B |  |  |
| 3 | Qualcomm | Snapdragon 8 Elite | 官方 | 125.0 | Qwen3-0.6B | 84.8 | 44% |
| 4 | Qualcomm | Snapdragon X Elite | 官方 | 89.9 | Qwen3-0.6B | 135.0 | 20% |
| 5 | Axera | AX650/AX8850 | 官方 | 44.0 | Qwen2.5-0.5B-Instruct | 34.1 | 32% |
| 6 | Sophgo | BM1688 | 官方 | 38.4 | MiniCPM4 / minicpm4-0.5b-gptq_ | 34.1 | 28% |
| 7 | Rockchip | RK3576 | 官方 | 34.6 | MiniCPM4 0.5B | 22.0 | 39% |
| 8 | Sophgo | CV186X | 官方 | 34.3 | MiniCPM4 / minicpm4-0.5b-gptq_ |  |  |
| 9 | Rockchip | RV1126B | 官方 | 23.2 | MiniCPM4 0.5B |  |  |

**≈0.5B · 8bit**

| # | 厂商 | 芯片 | 类别 | tokens/s | 模型 | 理论带宽 | 带宽利用率 |
|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 官方 | 45.3 | MiniCPM4 0.5B | 34.1 | 66% |
| 2 | Axera | AX650/AX8850 | 官方 | 36.0 | MiniCPM4-0.5B | 34.1 | 53% |
| 3 | Rockchip | RK3576 | 官方 | 23.3 | MiniCPM4 0.5B | 22.0 | 53% |
| 4 | Rockchip | RK3588 | 社区 | 21.6 | Qwen 1.5 0.5B | 34.1 | 32% |
| 5 | Rockchip | RV1126B | 官方 | 15.2 | MiniCPM4 0.5B |  |  |
| 6 | Rockchip | RK3562 | 官方 | 13.6 | Qwen2 0.5B |  |  |
| 7 | Axera | AX650/AX8850 | 社区 | 12.9 | Qwen3-0.6B | 34.1 | 23% |
| 8 | Axera | AX630C | 官方 | 12.0 | MiniCPM4-0.5B |  |  |

**≈1.5B · 4bit**

| # | 厂商 | 芯片 | 类别 | tokens/s | 模型 | 理论带宽 | 带宽利用率 |
|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon X2 Elite | 官方 | 90.6 | Llama-v3.2-1B-Instruct |  |  |
| 2 | Qualcomm | Snapdragon 8 Elite | 官方 | 67.2 | Llama-v3.2-1B-Instruct | 84.8 | 40% |
| 3 | Qualcomm | Snapdragon 8 Elite Gen 5 | 官方 | 65.2 | Llama-v3.2-1B-Instruct |  |  |
| 4 | Qualcomm | Snapdragon X Elite | 官方 | 43.5 | Llama-v3.2-1B-Instruct | 135.0 | 16% |
| 5 | Sophgo | BM1684X | 官方 | 41.1 | Qwen / qwen2.5-1.5b_int4_seq51 |  |  |
| 6 | Sophgo | CV84X6 | 官方 | 35.2 | Qwen3_5 / qwen3.5-2b-int4-auto |  |  |
| 7 | Sophgo | BM1688 | 官方 | 21.2 | Qwen / qwen1.5-1.8b_int4_seq51 | 34.1 | 56% |
| 8 | Rockchip | RK3576 | 官方 | 19.7 | TinyLLAMA 1.1B | 22.0 | 49% |
| 9 | Axera | AX650/AX8850 | 官方 | 19.0 | Qwen2.5-1.5B-Instruct | 34.1 | 42% |
| 10 | Sophgo | CV186X | 官方 | 13.2 | Qwen / qwen1.5-1.8b_int4_seq51 |  |  |

**≈1.5B · 8bit**

| # | 厂商 | 芯片 | 类别 | tokens/s | 模型 | 理论带宽 | 带宽利用率 |
|---|---|---|---|---|---|---|---|
| 1 | Rockchip | RK3588 | 官方 | 24.4 | TinyLLAMA 1.1B | 34.1 | 79% |
| 2 | Rockchip | RK3576 | 官方 | 12.2 | TinyLLAMA 1.1B | 22.0 | 61% |
| 3 | Axera | AX650/AX8850 | 官方 | 11.0 | Qwen2.5-1.5B-Instruct | 34.1 | 48% |

**3–9B · 4bit**

| # | 厂商 | 芯片 | 类别 | tokens/s | 模型 | 理论带宽 | 带宽利用率 |
|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon X2 Elite | 官方 | 87.5 | Llama-v3.2-3B-Instruct-SSD |  |  |
| 2 | Qualcomm | Snapdragon 8 Elite Gen 5 | 官方 | 55.2 | Llama-v3.2-3B-Instruct-SSD |  |  |
| 3 | Qualcomm | Snapdragon X Elite | 官方 | 53.6 | Llama-v3.2-3B-Instruct-SSD | 135.0 | 60% |
| 4 | Qualcomm | Snapdragon 8 Elite | 官方 | 46.1 | Llama-v3.2-3B-Instruct-SSD | 84.8 | 82% |
| 5 | Sophgo | CV84X6 | 官方 | 21.2 | Qwen / qwen3-4b-awq_w4f16_seq5 |  |  |
| 6 | Sophgo | BM1684X | 官方 | 14.2 | ChatGLM2 / chatglm2-6b_int4.bm |  |  |
| 7 | Axera | AX650/AX8850 | 官方 | 10.0 | Qwen2.5-3B-Instruct | 34.1 | 44% |
| 8 | Sophgo | BM1684X | 社区 | 9.6 | Llama3-8B |  |  |
| 9 | Rockchip | RK3576 | 官方 | 9.0 | TeleChat2 3B | 22.0 | 61% |
| 10 | Sophgo | BM1688 | 官方 | 5.1 | ChatGLM3 / chatglm3-6b_int4_2c | 34.1 | 45% |


---
已剔除的不合理折算(CNN: 等效算力>1.3×标称;LLM: MoE 或超过理论带宽 1.15 倍;VLM 因名称参数量含视觉塔已不计入 LLM 榜): Sophgo CV84X6 Qwen3_5 / qwen3.6-35b-a3b-int4 313.6>MoE; Sophgo CV84X6 Qwen3_5 / qwen3.6-35b-a3b-int4 313.2>MoE
