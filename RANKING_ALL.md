# 全芯片总榜(一张表)

把数据集中出现的所有芯片放进同一张表。**综合分** = 该芯片在可得指标上的「全体百分位」平均(0–100;三项指标:CNN 等效算力、Transformer 视觉等效算力、LLM 解码等效内存吞吐);无数据的指标留空,不计入平均。
**覆盖**(C/T/L)表示三项指标哪几项有数据。只有 1 项指标的芯片综合分仅作参考(手机 SoC 常因只测了云端纯 NPU 延迟而排名靠前,与开发板口径不完全相同)。
各列含义:标称 TOPS = 厂商 INT8 标称;CNN/Transformer 等效 TOPS = 重模型(≥5 GOPs)中位的 FPS×GOPs;利用率 = CNN 等效/标称;LLM 等效 GB/s = tokens/s×权重字节;带宽利用率 = LLM 等效 GB/s ÷ 理论带宽。官方数据优先,无官方数据才用社区数据。

| 综合排名 | 厂商 | 芯片 | 类型 | 标称 INT8 TOPS | 带宽 GB/s | CNN 等效 TOPS | CNN 利用率 | Transformer 等效 TOPS | LLM 等效 GB/s | LLM 带宽利用率 | 覆盖 C/T/L | 综合分 | 宽口径最佳等效 TOPS(任意批大小/精度,参考) | 数据状态 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Qualcomm | Snapdragon X2 Elite | 手机/PC SoC |  |  | 17.25 |  | 7.63 | 82.6 |  | CTL | 97 |  |  |
| 2 | Qualcomm | Snapdragon 8 Elite Gen 5 | 手机/PC SoC |  |  | 15.28 |  | 8.78 | 45.9 |  | CTL | 96 |  |  |
| 3 | Qualcomm | Snapdragon 8 Elite | 手机/PC SoC |  | 84.8 | 14.33 |  | 6.04 | 40.3 | 47% | CTL | 84 |  |  |
| 4 | Qualcomm | Snapdragon 8 Gen 3 | 手机/PC SoC |  | 76.8 | 11.65 |  | 5.01 |  |  | CT· | 82 |  |  |
| 5 | Qualcomm | Snapdragon X Elite | 手机/PC SoC | 45.0 | 135.0 | 8.09 | 18% | 3.25 | 42.4 | 31% | CTL | 75 |  |  |
| 6 | Sophgo | BM1684X | 边缘 SoC/加速卡 | 32.0 |  | 8.53 | 27% |  | 38.6 |  | C·L | 74 |  |  |
| 7 | Sophgo | CV84X6 | 边缘 SoC/加速卡 | 64.0 |  | 5.33 | 8% |  | 38.8 |  | C·L | 69 |  |  |
| 8 | Axera | AX650/AX8850 | 边缘 SoC/NPU | 24.0 | 34.1 | 6.76 | 28% | 4.87 | 14.4 | 42% | CTL | 64 | 14.49 (YOLOv6-S, 批?) |  |
| 9 | Sophgo | BM1688 | 边缘 SoC/加速卡 | 16.0 | 34.1 | 5.79 | 36% |  | 13.6 | 40% | C·L | 55 |  |  |
| 10 | Hailo | Hailo-10H | PCIe/M.2 加速器 | 20.0 |  | 4.57 | 23% | 1.00 |  |  | CT· | 54 | 10.41 (YOLOv8m, 批?) |  |
| 11 | Axera | AX637/AX8910 | 边缘 SoC/NPU |  |  | 2.07 |  | 2.48 |  |  | CT· | 53 | 4.80 (YOLOv6-S, 批?) |  |
| 12 | Sophgo | BM1684 | 边缘 SoC/加速卡 | 17.6 |  | 1.87 | 11% |  |  |  | C·· | 52 |  |  |
| 13 | Hailo | Hailo-8 | PCIe/M.2 加速器 | 26.0 |  | 5.87 | 23% | 0.61 |  |  | CT· | 50 | 14.04 (YOLOv8s, 批?) |  |
| 14 | D-Robotics (Horizon Robotics) | RDK X5 | 边缘 SoC/NPU |  |  | 1.16 |  |  |  |  | C·· | 45 | 3.19 (MobileNetV1 (Hailo), 批?) |  |
| 15 | Rockchip | RK3588 | 边缘 SoC/NPU | 6.0 | 38.4 | 0.95 | 16% |  | 23.8 | 62% | C·L | 44 | 1.65 (YOLOv6-S, 批1) |  |
| 16 | Sophgo | CV186X | 边缘 SoC/加速卡 | 7.2 | 34.1 | 3.11 | 43% |  | 10.2 | 30% | C·L | 43 |  |  |
| 17 | Hailo | Hailo-8L | PCIe/M.2 加速器 | 13.0 |  | 2.34 | 18% | 0.48 |  |  | CT· | 38 | 6.86 (YOLOv8m, 批?) |  |
| 18 | Rockchip | RK3576 | 边缘 SoC/NPU | 6.0 | 21.9 | 1.02 | 17% |  | 10.9 | 50% | C·L | 34 | 1.59 (YOLOv6-S, 批1) |  |
| 19 | Allwinner | A733 | 边缘 SoC/NPU |  | 19.2 | 0.88 |  |  |  |  | C·· | 31 | 1.86 (YOLOv3 (Hailo yolov3_416), 批?) |  |
| 20 | Axera | AX630C | 边缘 SoC/NPU | 3.2 |  | 1.46 | 46% | 0.97 | 6.0 |  | CTL | 30 | 3.30 (YOLOv6-S, 批?) |  |
| 21 | Axera | AX620Q | 边缘 SoC/NPU | 2.4 |  | 1.14 | 48% | 0.46 |  |  | CT· | 25 | 2.61 (YOLOv6-S, 批?) |  |
| 22 | Rockchip | RK1808 | 边缘 SoC/NPU | 3.0 | 6.4 | 0.55 | 18% |  |  |  | C·· | 24 | 1.09 (YOLOv6-S, 批1) |  |
| 23 | Rockchip | RK3562 | 边缘 SoC/NPU | 1.0 |  | 0.47 | 47% |  | 6.4 |  | C·L | 18 | 0.78 (YOLOv6-S, 批1) |  |
| 24 | Rockchip | RV1126 | 边缘 SoC/NPU |  |  | 0.37 |  |  |  |  | C·· | 17 | 0.74 (YOLOv6-S, 批1) |  |
| 25 | Axera | AX615 | 边缘 SoC/NPU |  |  | 0.84 |  | 0.33 |  |  | CT· | 14 | 2.09 (YOLOv6-S, 批?) |  |
| 26 | Rockchip | RK3566/RK3568 | 边缘 SoC/NPU | 0.8 |  | 0.37 | 46% |  |  |  | C·· | 14 | 0.69 (YOLOv6-S, 批1) |  |
| 27 | Allwinner | T527 | 边缘 SoC/NPU | 2.0 |  | 0.36 | 18% |  |  |  | C·· | 10 | 1.04 (YOLOv3 (Hailo yolov3_416), 批?) |  |
| 28 | Rockchip | RV1109 | 边缘 SoC/NPU | 1.0 |  | 0.25 | 25% |  |  |  | C·· | 7 | 0.49 (YOLOv6-S, 批1) |  |
| 29 | Google Coral | Coral Edge TPU (USB Accelerator) | PCIe/USB 加速器 |  |  | 0.20 |  |  |  |  | C·· | 3 |  |  |
| 30 | Google Coral | Coral Edge TPU (Dev Board) | PCIe/USB 加速器 |  |  | 0.17 |  |  |  |  | C·· | 0 |  |  |
| 31 | Rockchip | RV1126B | 边缘 SoC/NPU | 3.0 | 10.7 |  |  |  | 5.8 | 54% | ··L | 0 |  |  |
| — | Apple | A18 Pro / M-series (Core ML) | 手机/PC SoC |  |  |  |  |  |  |  | ··· |  |  | Core ML 延迟(FP16,计算单元=CPU/GPU/神经引擎调度),与纯 NPU 不可比 |
| — | Axera | AX650 | 边缘 SoC/NPU | 18.0 |  |  |  |  |  |  | ··· |  |  | 无可折算数据 |
| — | Cambricon | MLU590 | 服务器加速卡 |  |  |  |  |  |  |  | ··· |  |  | 仅算子微基准,无模型级成绩 |
| — | Cix | P1 (CD8180) | 边缘 SoC/NPU | 30.0 | 88.0 |  |  |  |  |  | ··· |  |  | 仅合成基准:卷积网络等效约 20–22 TOPS、矩阵乘约 3.5 TOPS(社区实测);BiSeNet 10.7 ms 缺 GOPs;无标准模型成绩 |
| — | D-Robotics (Horizon Robotics) | RDK X3 | 边缘 SoC/NPU | 5.0 |  |  |  |  |  |  | ··· |  |  | 无可折算数据 |
| — | Huawei Ascend | Ascend 310B1 | 边缘/服务器加速卡 | 20.0 | 51.2 |  |  |  |  |  | ··· |  | 0.89 (MobileNetV2, 批?) | 无可折算数据 |
| — | Huawei Ascend | Ascend 310P3 | 边缘/服务器加速卡 | 140.0 | 204.0 |  |  |  |  |  | ··· |  | 34.77 (ResNet50, 批?) | 成绩为 FP32 输入 om 模型,批大小多为未标/大批;仅有「宽口径」参考值,未计入综合分 |
| — | Huawei Ascend | Ascend 910B (TP4, 4 cards) | 边缘/服务器加速卡 |  |  |  |  |  |  |  | ··· |  |  | 仅多卡大模型服务实测 |
| — | Huawei Ascend | Ascend 910B4 | 边缘/服务器加速卡 |  |  |  |  |  |  |  | ··· |  |  | 仅大模型服务实测 |
| — | Intel | Core Ultra 5 125H NPU (Meteor Lake; ASUS Vivobook S16 OLED) | 手机/PC SoC |  |  |  |  |  |  |  | ··· |  |  | 社区零散数字,硬件口径不明 |
| — | Intel | Core Ultra 7 258V NPU (Lunar Lake) | 手机/PC SoC | 47.0 |  |  |  |  |  |  | ··· |  |  | 仅规格,无可折算成绩 |
| — | Intel | Core Ultra 9 288V NPU (Lunar Lake) | 手机/PC SoC |  |  |  |  |  |  |  | ··· |  |  | 仅 MLPerf Client Llama-2-7B 一条(未标位宽) |
| — | Qualcomm | Snapdragon X Plus X1P-42-100 (Hexagon NPU) | 手机/PC SoC | 45.0 | 135.0 |  |  |  |  |  | ··· |  |  | 仅社区零散数字 |

"—" 排名表示目前没有任何可折算的数据(例如缺批大小 1 的 INT8 记录、缺模型 GOPs、或只有 FP16/混合精度成绩)。该类芯片的原始成绩见各厂商 CSV。