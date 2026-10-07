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
