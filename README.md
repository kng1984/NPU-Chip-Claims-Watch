# NPU Chip Claims Watch

从 GitHub 公开仓库收集各家 NPU 在不同芯片(不同算力)上运行各模型的性能数据。

## 数据

`data/<vendor>.csv`,统一字段:

`vendor,chip,chip_tops,model,task,input_size,precision,metric,value,unit,runtime,source_url,notes`

- 数值均摘自 `source_url` 指向的源页面,未做估算;批大小、核数、是否含前后处理等口径写在 `notes`。
- `chip_tops` 仅在源页面或官方规格明确时填写,多数为空;Hailo 的 26/13/40 TOPS 来自官方规格而非源页面。
- 不同厂商的测试口径(批大小、精度、是否含前后处理)不同,**跨厂商直接比较数值不可靠**。

| 文件 | 行数 | 来源 | 芯片 |
|---|---|---|---|
| rockchip.csv | 493 | airockchip/rknn_model_zoo, rknn-llm | RK3566/68, RK3562, RK3576, RK3588, RV1109/1126/1126B, RK1808 |
| sophgo.csv | 1810 | sophgo/sophon-demo | BM1684, BM1684X, BM1688, CV186X, CV84X6 |
| axera.csv | 205 | AXERA-TECH/ax-samples, ax-llm | AX615, AX620Q, AX630C, AX637, AX650 |
| horizon.csv | 136 | D-Robotics/rdk_model_zoo | RDK X5, RDK X3 |
| huawei_ascend.csv | 85 | Ascend/ModelZoo-PyTorch | Ascend 310P3, 310B1 |
| hailo.csv | 45 | hailo-ai/hailo_model_zoo | Hailo-8, 8L, 10H |
| qualcomm.csv / intel.csv / cambricon.csv | 0 | — | 见下 |

## 已知缺口

- **Qualcomm、Intel、寒武纪**:无数据(Qualcomm AI Hub / HuggingFace 不可达,GitHub 上无公开表格)。
- Rockchip:未收录音频模型 RTF、多模态表、RV1103/RV1106。
- Sophgo:无 CV18xx;SRM1-20/SC7-* 为源页面原始标签;批大小取自 bmodel 文件名,耗时是按批还是按图未明;LLM 首 token 延迟未收录。
- Axera:精度未标注;ax-llm 仅 1 次示例运行。
- Ascend:未标注精度,个别表格无单位(按 fps 假定,见 notes);无 910/910B 与 LLM 数据。
- 未覆盖 NXP eIQ、Google Coral、Amlogic、MediaTek。

## 排名

- `data/chip_specs.csv`:芯片规格(CPU、NPU TOPS、内存带宽)。目前只有 RK3588 和 AX650/AX8850 有来源数据,其余为空——规格站点(rock-chips.com、hailo.ai、qualcomm.com、intel.com、d-robotics.cc、docs.radxa.com、wikipedia 等)被网络策略拦截,未从记忆填充。
- `rank.py` → `RANKING.md`:按模型 × 精度排 FPS,并在有规格时给出 FPS/TOPS 与 FPS/(GB/s)。带宽效率榜现在基本为空,等规格补全后重新运行 `python3 -I rank.py` 即可。
- 注意:精度未标注的数据归在 `n/a` 组,可能混有不同批大小(如 Hailo 为批 8/批 1),排名为粗略参考。

## 补充数据(第二轮,仅来自 GitHub)

- `data/specs_a.csv`、`data/specs_b.csv`:从 GitHub 文档仓库收集的规格,`rank.py` 会与 `chip_specs.csv` 合并(先出现的非空值优先)。仍缺:所有芯片的制程/FP16 基本为空;带宽只有 RK3576(22)、RK3588(44)、AX650/AX8850(34.1)三个,均为按板卡/模组位宽×速率算出的理论峰值;Sophgo 的 BM1684/BM1684X/BM1688 TOPS 来自 sophon-tools 代码注释,可信度较弱;RV1126、RK3588 等未标精度的 NPU 算力放在 notes,未计入 INT8 列。
- `data/community.csv`、`qualcomm.csv`、`intel.csv`、`cambricon.csv`、`huawei_ascend_910.csv`:社区/第三方 GitHub 实测,**未与原页面逐条核对**,含近似值与区间,硬件口径不一,**不参与 `RANKING.md`**。
- 仍无法访问论坛与规格站点(知乎、Reddit、CNX、Radxa 论坛、厂商官网、Qualcomm AI Hub、HuggingFace),需在环境网络设置中放开后才能补齐。

## 第三轮(网络放开后)

- `data/web_qualcomm.csv`:Qualcomm AI Hub 在 HuggingFace 的官方模型卡(2557 行,延迟与 LLM tokens/s)。排名里把批 1、NPU 的视觉模型延迟换算成 FPS(带 † 标记),LLM 行不入排名。
- `data/web_intel.csv`:仅 2 行(Core Ultra 9 288V,MLPerf Client Llama-2-7B);OpenVINO 官方页没有 NPU 数值。
- `data/web_forum_en.csv`:Hailo 官方 model zoo(批 1)与 Coral 延迟。
- 规格新增 `specs_d.csv`(Sophgo/Axera/RDK)、`specs_e.csv`(Hailo/昇腾/寒武纪/骁龙/Intel)、`specs_f.csv`(带页面依据的更正,合并时优先)。已知冲突记录在各行 notes:AX650 的 INT8 算力(10.8 vs 18)、AX8850(24)与 AX650N 不是同一颗芯片、昇腾 310P3 为第三方整卡数据折半。
- 中文论坛(知乎/CSDN/Radxa 论坛)实测尚未收集:子 agent 的 WebFetch 无法解析域名、curl 被权限分类器拦截;Rockchip 规格(RK3562/RK3566/RV11xx 等)也因此未补。

## 第四轮:全志与此芯

- `data/allwinner.csv`(26 行):Radxa 文档中 T527 / A733(Vivante VIP9000)的 YOLO、RetinaFace、CLIP 推理 FPS,仅推理、不含前后处理。
- `data/cix.csv`(4 行):此芯 P1(CD8180)的社区实测——合成卷积模型 277 FPS(约 20.1 TOPS 实效)、BiSeNet 10.7 ms、4000×4000 矩阵乘 343 ms。NPU 为安谋科技"周易"IP;SDK 需申请,标准模型公开成绩很少。45 TOPS 为 CPU+GPU+NPU 合计,NPU 单独约 30(Radxa 文档称 28.8,未核实)。
- 新增规格 `specs_g.csv`(Cix P1、全志 V853/T527)、`specs_h.csv`(RK3566/68、RK3562、RV1109,来源 CNX;与 `specs_a` 的算力存在冲突,见 notes)。

## 第五轮:Coral、Apple

- `data/coral.csv`(38 行):coral.ai 官方基准,19 个模型在 Edge TPU(USB Accelerator / Dev Board)上的单张推理延迟,Edge TPU 标称 4 TOPS(页面所述)。
- `data/apple.csv`(33 行):Apple Core ML 模型库的推理时间(iPhone 13–16 Pro、iPad Pro、M1–M3 Max)。**计算单元为 "All",即 CPU/GPU/神经引擎由 Core ML 调度,不是纯 NPU**;含合并单元格的行被跳过,数据不完整。
- 未取得:AMD Ryzen AI(文档站无数值,GitHub 页为空)、Hailo 社区(页面需 JS)、Reddit(返回空页)、Jeff Geerling 博文(返回空页)、Radxa RKLLM/CNX 的 RK3588 LLM 页面(返回空页)。

## 第六轮:CSDN / 论坛 / 博客

- `data/web_forum_cn.csv`(10 行):PhotonVision(Orange Pi 5,RK3588 的 YOLOv5/v5u/v8/11 延迟)、CSDN 触觉智能(RK3576 与 RK3588 的 YOLOv5s,23.7 / 21.3 ms)、Radxa 多路 YOLOv8n 文档、地瓜论坛(RDK X5 YOLOv8n 11.4 ms,整链路仅 4–5 FPS)、TinyComputers 博客(含一条疑似离群的 RK3576 数据,已标注)。
- CSDN 其余文章要么是端到端摄像头帧率、要么是区间值(如 "13–16 FPS"、"100+ FPS")或缺少测试条件,未收录。Seeed 的 RK 基准页只是 Rockchip 官方表的转载,已在 `rockchip.csv` 中。
- 搜索未找到可引用的:算能 BM1684X/BM1688、爱芯 AX650N/AX630C、海思、昇腾 Orange Pi AIpro 的 CSDN 实测(AIpro 那篇似为 CPU 推理)。

## 同口径排名

- `rank2.py` → `RANKING_LIKE_FOR_LIKE.md`:YOLOv5s、YOLOv8n(640×640)、ResNet50、MobileNetV2(224×224),仅取 INT8 类精度(或未标精度)、批大小 1、仅 NPU 推理的数据;延迟换算为 FPS(†);官方与社区分列;规格表有数据时给出 FPS/TOPS 与 FPS/(GB/s)。
- 与 `RANKING.md`(宽口径)的区别:前者剔除了批大小>1、端到端流水线、多路并发和离群值。仍需注意:各家软件栈不同,Qualcomm/Apple 等手机 SoC 数据是厂商云端设备实测的纯 NPU 延迟,与开发板数据口径并不完全相同。

## 等效算力排名(`rank3.py` → `RANKING_EFFECTIVE.md`)

- **等效 TOPS** = 实测 FPS × 单次推理 GOPs ÷ 1000(GOPs 来自 `data/ref/model_ops.csv`,统一为 2×MAC);按芯片给出中位数、最低–最高区间,以及相对标称 INT8 算力的利用率。只用 INT8 类精度、批大小 1、仅 NPU 推理的数据;等效算力超过标称 1.3 倍的折算(模型错配)已剔除。
- 分类:CNN 总榜、Transformer 视觉模型(样本很少,目前仅 Qualcomm)、应用场景(目标检测 / 图像分类 / 分割 / 人脸 / 姿态)。
- **端侧大模型**:等效内存吞吐 = tokens/s × 参数量 × 位宽/8,与理论带宽对比得到带宽利用率;另有同尺寸(≈0.5B/1.5B/3–9B,4/8bit)tokens/s 榜。VLM(名称参数含视觉塔)、MoE、超出理论带宽的行已剔除。
- 新增数据:`web_transformer.csv`(Axera/Rockchip/Hailo/Sophgo 的 LLM/VLM/ViT 等)、`specs_i.csv`(带宽补全:RK3588 实际板级配置为 34.1/38.4 GB/s,与早先的 44 GB/s 冲突,排名取 34.1)。
- 局限:带宽仍缺大量芯片(RK3576 的 22 GB/s 未核实,Sophgo/Axera 多数、Hailo-10H、RDK、昇腾、Cix 等为空);Transformer 视觉与 OCR/语音类缺少对应的 GOPs,无法折算;Qualcomm 手机 SoC 的标称 INT8 TOPS 未公布,利用率为空。

## 补充(Transformer 视觉与 Hailo 全量)

- `data/ref/hailo_zoo_table.csv`:Hailo Model Zoo 官方表(Hailo-8/8L/10H,215 行:批 1/批 8 FPS、输入、参数量、OPS(G)),包含 DeiT / DaViT / CAS-ViT / FastViT 等 Transformer 类模型;`rank3.py` 直接用其自带 OPS 与批 1 FPS 折算等效算力(OPS 口径已用 Ultralytics 等交叉核对为 2×MAC)。
- `data/model_ops.csv` 与 `hailo_zoo_table.csv` 现位于 `data/ref/`(参考表,不参与 `rank.py` 的 glob)。
- `RANKING_EFFECTIVE.md` 改为按「重模型(≥5 GOPs)等效 TOPS 中位」排序,避免只测小模型的芯片被高估/低估;Transformer 视觉榜现包含 Axera(Swin-T/DeiT-T/ViT-B)与 Hailo(23 个 ViT 类模型)。

## 带宽补全(第二次)

- `data/specs_j.csv`:骁龙 8 Gen 3(76.8)/8 Elite(84.8)/X Elite(135 GB/s)来自 Wikipedia 的 SoC 表;RK3576 为 19.2 GB/s(Wikipedia,未见位宽与速率,未核实,与早先按板卡估的 22 冲突,现取 19.2);RK3566/68、RK1808、Hailo-10H、Lunar Lake 只有接口位宽/类型,无带宽。
- 修正:Cix P1 的带宽按 128-bit × 5500 MT/s 推算为 88 GB/s(CNX 文中写 100 GB/s 与自身位宽×速率不符)。
- 仍无带宽:Sophgo 全系、Axera 全系、地平线 RDK X3/X5、RK3562/RV1126/RV1109/RV1126B、全志 T527/A733、昇腾 310B/310P、Coral、Apple A18 Pro、Core Ultra 7 155H(厂商官网多被代理拦截,PDF 链接失效)。
