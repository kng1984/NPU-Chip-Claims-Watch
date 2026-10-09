# tech-trend

采集科技媒体、众筹、新品、吐槽、论文、博客、论坛、厂商动态,做主题热度/动量/痛点/供给缺口分析,输出 REPORT.md。纯标准库,无依赖。

```
python3 -I collect.py   # 读 sources.json,写 out/items.jsonl、out/status.json
python3 -I analyze.py   # 写 REPORT.md
```

- 数据源在 `sources.json`(RSS、arXiv 16 个分类、HF 每日论文、HN 首页与 26 个检索词)。
- Reddit、Kickstarter、Indiegogo、GitHub API 在当前网络环境被拦,众筹/吐槽样本偏少。
- 主题词表与痛点词表在 `analyze.py` 顶部,按需调整;结果是信号筛选,需人工核实。
