#!/usr/bin/env python3
"""Topic heat / momentum / pain-point / supply-gap analysis over out/items.jsonl -> REPORT.md"""
import json, re, os, sys, collections, datetime, math
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
items = [json.loads(l) for l in open(os.path.join(OUT, "items.jsonl"))]
today = datetime.date.fromisoformat(os.environ.get("TW_TODAY", datetime.date.today().isoformat()))
for i in items:
    i["_t"] = (i["title"] + " " + i.get("text", "")).lower()
    try: i["_age"] = (today - datetime.date.fromisoformat(i["date"])).days
    except Exception: i["_age"] = None

TOPICS = {  # name -> regex (lowercase)
 "端侧/边缘AI与NPU": r"\bnpu\b|edge ai|on-device|端侧|边缘计算|tinyml|neural engine|copilot\+|ai pc|ai phone|\bnpus?\b",
 "本地大模型推理": r"local llm|llama\.cpp|ollama|\bgguf\b|self-hosted (llm|ai)|本地部署|lm studio|vllm|inference (engine|server)",
 "LLM量化/压缩/蒸馏": r"quantiz|\bint4\b|\bfp4\b|\bfp8\b|pruning|distillation|蒸馏|量化|low-bit|bitnet",
 "推理加速/KV缓存/投机解码": r"speculative decoding|kv cache|paged ?attention|flash ?attention|continuous batching|prefill|decode|moe|mixture[- ]of[- ]experts|long[- ]context",
 "AI Agent与工具调用": r"\bagents?\b|agentic|mcp\b|tool use|function calling|computer use|智能体|coding agent|vibe coding",
 "多模态/视觉/视频生成": r"multimodal|vision[- ]language|\bvlm\b|diffusion|video generation|text-to-video|3d gaussian|nerf|world model",
 "具身智能/机器人": r"robot|embodied|humanoid|manipulation|机器人|具身|autonomous driving|自动驾驶|\bvla\b",
 "GPU/加速器与AI芯片": r"\bgpu\b|blackwell|rubin|\bhbm\d?e?\b|tpu|trainium|accelerator|ai chip|ai芯片|cuda|rocm|instinct|gaudi|cerebras|groq|tenstorrent|算力",
 "RISC-V/开源指令集": r"risc-v|riscv|rvv|\bvector extension|龙芯|loongarch|openhwgroup",
 "存储/内存/CXL/HBM": r"\bdram\b|\bnand\b|\bssd\b|cxl|ddr5|lpddr|hbm|memory wall|processing[- ]in[- ]memory|\bpim\b|内存涨价|存储",
 "先进制程/封装/Chiplet": r"chiplet|\b2nm\b|\b3nm\b|\b18a\b|advanced packaging|cowos|hybrid bonding|ucie|tsmc|glass substrate|制程|封装|foundry",
 "光互连/网络/数据中心": r"co-packaged|optical interconnect|silicon photonics|infiniband|ultra ethernet|nvlink|rdma|800g|1\.6t|data ?center|datacenter|数据中心|液冷|liquid cooling",
 "能效/散热/电源": r"power consumption|energy[- ]efficien|thermal|cooling|watt|battery|功耗|散热|能效|gan charger|solid[- ]state battery|固态电池",
 "单板机/嵌入式/IoT": r"raspberry pi|\bsbc\b|esp32|rp2040|rp2350|microcontroller|\bmcu\b|jetson|rk3588|orange pi|radxa|embedded|嵌入式|zephyr|rtos|home assistant|matter protocol",
 "FPGA/EDA/开源硬件": r"fpga|verilog|chisel|hls\b|eda\b|open[- ]source hardware|openroad|kicad|asic design|llm.{0,15}(rtl|verilog)",
 "操作系统/内核/Rust": r"linux kernel|\brust\b|\bebpf\b|wasm|webassembly|unikernel|rust for linux|systemd|鸿蒙|harmonyos|openharmony|android 1\d|windows 1\d|macos",
 "安全/隐私/供应链": r"vulnerabilit|\bcve-|zero[- ]day|ransomware|supply chain attack|side[- ]channel|spectre|confidential computing|\btee\b|post-quantum|passkey|encryption|漏洞|勒索",
 "数据库/数据基础设施": r"database|postgres|sqlite|duckdb|vector (db|database|search)|rag\b|lakehouse|clickhouse|数据库|向量库|stream processing",
 "云原生/运维/FinOps": r"kubernetes|\bk8s\b|serverless|observability|terraform|cloud cost|finops|edge compute|cloudflare workers|docker|devops",
 "XR/可穿戴/智能眼镜": r"smart glasses|ar glasses|vision pro|\bxr\b|\bvr\b|headset|smartwatch|wearable|meta ray-ban|智能眼镜|可穿戴|ring\b",
 "消费电子/掌机/PC": r"handheld|steam deck|rog ally|laptop|mini pc|e-ink|e ink|墨水屏|折叠屏|foldable|keyboard|monitor|oled|游戏本|迷你主机",
 "3D打印/创客/DIY": r"3d print|prusa|bambu|maker|diy|cnc|laser cutter|creality|创客",
 "量子/新型计算": r"quantum|neuromorphic|analog (ai|computing)|photonic comput|量子|类脑|存算一体|in-memory comput",
}
PAIN = r"overheat|throttl|\bbug|broken|crash|brick|recall|defect|fail(s|ed|ure)?\b|unreliable|flaky|noisy|loud fan|drain|laggy|\bslow\b|too expensive|overpriced|price hike|shortage|out of stock|vendor lock|lock-in|locked[- ]in|no (driver|support|documentation)|poor (support|docs|documentation)|undocumented|abandon|eol\b|end of life|enshittif|frustrat|annoy|\bhate\b|wish (there|i|someone)|why (is|does|can't|isn't)|doesn't work|not working|dumpster|scam|misleading|false advertis|fake|marketing|bait|吐槽|翻车|坑|缺货|涨价|发热|卡顿|难用|踩雷|召回|割韭菜|虚标|不兼容|没有文档|停产|鸡肋"
SUPPLY_CATS = {"crowdfunding", "newproduct"}
W = {"media": 1, "blog": 1, "vendor": 1.5, "paper": 0.7, "forum": 1, "complaint": 1.2, "newproduct": 1.5, "crowdfunding": 2}
pain_re = re.compile(PAIN); tre = {k: re.compile(v) for k, v in TOPICS.items()}

stat = {k: collections.defaultdict(float) for k in TOPICS}
ex = {k: {"pain": [], "supply": [], "hot": [], "paper": []} for k in TOPICS}
for it in items:
    pain = bool(pain_re.search(it["_t"])) and it["cat"] != "paper"
    eng = 1 + math.log1p(it.get("score", 0) + 2 * it.get("comments", 0))
    for k, r in tre.items():
        if not r.search(it["_t"]): continue
        s = stat[k]; c = it["cat"]
        s["n"] += 1; s["n_" + c] += 1; s["w"] += W[c]
        recent = it["_age"] is not None and it["_age"] <= 14
        older = it["_age"] is not None and 14 < it["_age"] <= 60
        if recent: s["recent"] += 1
        if older: s["older"] += 1
        if pain: s["pain"] += eng; s["pain_n"] += 1; ex[k]["pain"].append((eng, it))
        if c in SUPPLY_CATS: s["supply"] += 1; ex[k]["supply"].append((it["_age"] or 999, it))
        if c == "paper": ex[k]["paper"].append((it["_age"] or 999, it))
        if c in ("forum", "complaint") : ex[k]["hot"].append((eng * (1 + it.get("comments", 0) / 50), it))

total_recent = sum(1 for i in items if i["_age"] is not None and i["_age"] <= 14)
total_older = sum(1 for i in items if i["_age"] is not None and 14 < i["_age"] <= 60)
base = (total_recent / max(1, total_older)) if total_older else 1
rows = []
for k, s in stat.items():
    mom = ((s["recent"] + 1) / (s["older"] + 1)) / base   # momentum vs overall volume
    demand = s["w"] + 2 * s["pain"]
    gap = demand / (1 + 3 * s["supply"])
    rows.append(dict(topic=k, n=int(s["n"]), mom=mom, pain=s["pain"], pain_n=int(s["pain_n"]), supply=int(s["supply"]), gap=gap,
                     papers=int(s["n_paper"]), forum=int(s["n_forum"] + s["n_complaint"]), vendor=int(s["n_vendor"]), recent=int(s["recent"])))

def link(i, n=90):
    t = i["title"].replace("|", "/")[:n]
    return f"[{t}]({i['url']})" if i["url"] else t

# emerging terms: bigrams recent vs older
STOP = set("the a an of to in and for on with is are was be by from as at that this it its or how what why new your you we our can will not more via using use based into than about their these those have has had but all one two can't just get out up".split())
def toks(t): return [w for w in re.findall(r"[a-z][a-z0-9\-\.\+]{1,}", t) if w not in STOP]
def grams(sel):
    c = collections.Counter()
    for it in sel:
        seen = set(); w = toks(it["title"].lower())
        for a, b in zip(w, w[1:]):
            g = a + " " + b
            if g not in seen: seen.add(g); c[g] += 1
    return c
rec = grams([i for i in items if i["_age"] is not None and i["_age"] <= 10 and i["cat"] != "paper"])
old = grams([i for i in items if i["_age"] is not None and 10 < i["_age"] <= 70 and i["cat"] != "paper"])
emerg = sorted(((g, c, c / (old[g] + 1)) for g, c in rec.items() if c >= 4), key=lambda x: -x[2] * math.log(x[1]))[:25]

L = []
A = L.append
cnt = collections.Counter(i["cat"] for i in items)
ds = sorted(i["date"] for i in items if i["date"])
A(f"# 科技趋势与机会点报告\n\n生成日期 {today};样本 {len(items)} 条({'、'.join(f'{k} {v}' for k, v in cnt.most_common())});时间范围 {ds[0] if ds else '?'} ~ {ds[-1] if ds else '?'}。")
A("\n**方法与局限**:标题+摘要关键词匹配到 %d 个主题;动量=近14天占比/15~60天占比(已按总量归一);痛点=命中吐槽词的非论文条目按热度加权;供给=众筹+新品条目数;机会分=(加权热度+2×痛点)/(1+3×供给)。这是**信号筛选器而非结论**:关键词会误判,RSS 只覆盖最近几天到几周,Reddit/Kickstarter/Indiegogo/GitHub 被网络策略拦截,因此众筹与吐槽样本偏少,需人工核实后再下判断。\n" % len(TOPICS))

A("## 1. 主题热度与动量\n\n| 主题 | 条目 | 论文 | 论坛/吐槽 | 近14天 | 动量 | 痛点 | 供给(众筹+新品) |\n|---|--:|--:|--:|--:|--:|--:|--:|")
for r in sorted(rows, key=lambda r: -r["n"]):
    A(f"| {r['topic']} | {r['n']} | {r['papers']} | {r['forum']} | {r['recent']} | {r['mom']:.2f} | {r['pain_n']} | {r['supply']} |")
A("\n动量>1.3 视为升温,<0.8 视为降温(样本小时波动大)。")
up = [r for r in rows if r["mom"] > 1.3 and r["n"] >= 15]; down = [r for r in rows if r["mom"] < 0.8 and r["n"] >= 15]
A("\n- 升温:" + (";".join(f"{r['topic']}({r['mom']:.2f})" for r in sorted(up, key=lambda r: -r["mom"])) or "无"))
A("- 降温:" + (";".join(f"{r['topic']}({r['mom']:.2f})" for r in sorted(down, key=lambda r: r["mom"])) or "无"))

A("\n## 2. 新兴词组(近10天 vs 此前,标题二元组)\n")
A("、".join(f"`{g}`×{c}" for g, c, _ in emerg))

A("\n## 3. 机会点候选(需求大、供给少)\n\n按机会分排序,每项附代表性痛点/论文/在售产品,供人工判断。\n")
for r in sorted(rows, key=lambda r: -r["gap"])[:8]:
    k = r["topic"]
    A(f"### {k}(机会分 {r['gap']:.1f};痛点 {r['pain_n']};供给 {r['supply']};论文 {r['papers']};动量 {r['mom']:.2f})")
    for label, key in (("痛点/吐槽", "pain"), ("论坛热点", "hot"), ("在售/众筹", "supply"), ("近期论文", "paper")):
        lst = ex[k][key]
        lst = sorted(lst, key=lambda x: -x[0])[:4] if key in ("pain", "hot") else sorted(lst, key=lambda x: x[0])[:3]
        if lst: A(f"- **{label}**:" + ";".join(f"{link(i)}({i['source']})" for _, i in lst))
    A("")

A("## 4. 众筹与新品信号\n")
cf = sorted([i for i in items if i["cat"] in SUPPLY_CATS], key=lambda i: (i["cat"] != "crowdfunding", i["_age"] if i["_age"] is not None else 999))
for i in cf[:30]: A(f"- [{i['cat']}] {i['date']} {link(i, 100)}({i['source']})")

A("\n## 5. 产品吐槽/痛点样本(热度排序)\n")
pains = sorted(((1 + math.log1p(i.get("score", 0) + 2 * i.get("comments", 0)), i) for i in items if i["cat"] in ("forum", "complaint", "media", "newproduct") and pain_re.search(i["_t"])), key=lambda x: -x[0])[:30]
for _, i in pains: A(f"- {i['date']} {link(i, 100)}({i['source']};👍{i.get('score', 0)} 💬{i.get('comments', 0)})")

A("\n## 6. 论文方向\n")
pc = collections.Counter(i["source"] for i in items if i["cat"] == "paper")
A("采样量:" + "、".join(f"{k.replace('arXiv ', '')} {v}" for k, v in pc.most_common()))
hf = sorted((i for i in items if i["source"] == "HF Daily Papers"), key=lambda i: -i.get("score", 0))[:12]
A("\n**HF 每日论文高赞:**")
for i in hf: A(f"- 👍{i.get('score', 0)} {link(i, 100)}")

A("\n## 7. 数据源健康度\n")
st = json.load(open(os.path.join(OUT, "status.json")))
A(f"成功 {sum(1 for v in st.values() if not v['err'])}/{len(st)};空返回:" + (", ".join(k for k, v in st.items() if not v['err'] and v['n'] == 0) or "无"))
open(os.path.join(HERE, "REPORT.md"), "w").write("\n".join(L) + "\n")
print("wrote REPORT.md", len(L), "lines")
