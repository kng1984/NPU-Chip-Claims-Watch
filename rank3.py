"""Effective-compute rankings: convert measured FPS to equivalent TOPS (FPS x GOPs/inference), group by CNN / Transformer /
application scenario, and for LLM decode compute bandwidth utilisation (tokens/s x weight bytes / peak bandwidth)."""
import csv, glob, re, os, statistics, collections

def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())
def num(s):
    try: return float(s)
    except (TypeError, ValueError): return None
def edge(s):
    m = re.findall(r'\d+', s or '')
    return max(int(x) for x in m) if m else None

# ---------- specs (first non-empty wins) ----------
specs = {}
for f in ['specs_i', 'specs_j', 'specs_g', 'specs_f', 'specs_h', 'specs_d', 'specs_e', 'chip_specs', 'specs_a', 'specs_b']:
    p = f'data/{f}.csv'
    if not os.path.exists(p): continue
    for r in csv.DictReader(open(p)):
        cur = specs.setdefault((r['vendor'], r['chip']), dict(r))
        for k, v in r.items():
            if v and not cur.get(k): cur[k] = v

def norm_chip(c):
    c = re.sub(r'[®™]', '', c)
    return re.sub(r' (For Galaxy )?Mobile$', '', c).replace(' For Galaxy', '').strip()
def spec_for(v, c):
    for k in ((v, c), (v, c + ' (Hexagon NPU)')):
        if k in specs: return specs[k]
    return {}

# ---------- model ops ----------
ops = collections.defaultdict(list)
OPS_ROWS = list(csv.DictReader(open('data/ref/model_ops.csv')))
ALIAS = {'swint': 'swint', 'deitt': 'deittiny', 'deits': 'deitsmall', 'deitb': 'deitbase', 'vitb': 'vitb16', 'fastvitt8': 'fastvitt8', 'yolov5s': 'yolov5shailoyolov5s', 'resnet50v27': 'resnet50', 'mobilenetv212': 'mobilenetv2', 'resnetv150': 'resnet50',
         'swintiny': 'swint', 'swinsmall': 'swins', 'swinbase': 'swinb', 'vit': 'vitb16', 'squeezenet11': 'squeezenet11',
         'resnet50hailoresnetv150': 'resnet50'}
for r in OPS_ROWS:
    if r['family'] == 'LLM' or not num(r['gops']): continue
    k = norm(re.sub(r'\(.*?\)', '', r['model'])) if not r['model'].startswith(('YOLOv5s (', 'YOLOv3 (')) else norm(r['model'])
    ops[k].append(r)
ops['yolov5s'] = [r for r in OPS_ROWS if r['model'] == 'YOLOv5s (Hailo yolov5s)']
ops['yolov3'] = [r for r in OPS_ROWS if r['model'].startswith('YOLOv3 (')]
ops['resnet50'] = [r for r in OPS_ROWS if r['model'] == 'ResNet50']

def match_ops(model, size):
    k = norm(re.sub(r'\(.*?\)', '', model)); k = ALIAS.get(k, k)
    if k in ('yolov5s', 'yolov3'): cands = ops[k]
    else: cands = ops.get(k) or ops.get(k.rstrip('u'), [])
    if not cands: return None
    if size is None: return cands[0] if len(cands) == 1 else None
    for c in cands:
        if edge(c['input']) == size: return c
    return None

def scenario(name, task, fam):
    n = norm(name)
    if fam in ('Transformer',) : return 'Transformer'
    if re.search(r'seg|deeplab|unet', n): return '分割'
    if 'pose' in n: return '姿态'
    if re.search(r'retina|scrfd|face', n): return '人脸'
    if re.search(r'yolo|ssd|ppyoloe', n): return '目标检测'
    return '图像分类'

INT8_OK = re.compile(r'^(|int8|uint8|a8w8|w8a8|int8 \(int8\))$', re.I)
def batch_ok(r):
    txt = ' '.join([r['notes'], r['model'], r['runtime']]).lower()
    return all(int(b) == 1 for b in re.findall(r'batch[ =_:]*(\d+)', txt))
def cls(r):
    return 'community' if r['notes'].lower().startswith(('community', 'forum', 'media')) else 'official'

# ---------- vision rows -> effective TOPS ----------
obs = []
dropped = []
for f in sorted(glob.glob('data/*.csv')):
    b = os.path.basename(f)
    if b.startswith('specs_') or b in ('chip_specs.csv', 'model_ops.csv', 'apple.csv'): continue
    for r in csv.DictReader(open(f)):
        if r['metric'] not in ('fps', 'latency_ms') or not INT8_OK.match(r['precision'] or '') or not batch_ok(r): continue
        n = r['notes'].lower()
        if any(w in n for w in ('concurrent', 'end-to-end', 'pipeline', 'outlier', 'not npu-only', 'synthetic')): continue
        if 'compute unit' in n and 'compute unit npu' not in n: continue
        if r['vendor'] == 'Hailo' and cls(r) == 'official': continue
        if r['vendor'] == 'Qualcomm' and norm(r['model']) in ('yolov7',): continue  # AI Hub variant unclear
        m = match_ops(r['model'], edge(r['input_size']))
        v = num(r['value'])
        if not m or not v or v <= 0: continue
        fps = 1000 / v if r['metric'] == 'latency_ms' else v
        eff = fps * float(m['gops']) / 1000
        chip = norm_chip(r['chip'])
        s = spec_for(r['vendor'], chip)
        peak = num(s.get('npu_tops_int8')) or num(r['chip_tops'])
        if peak and eff > 1.3 * peak:
            dropped.append((r['vendor'], chip, r['model'], round(eff, 1), peak)); continue  # implausible: model mismatch / op-count convention
        obs.append(dict(vendor=r['vendor'], chip=chip, model=m['model'], fam=m['family'], scen=scenario(m['model'], m['task'], m['family']),
                        fps=fps, eff=eff, gops=float(m['gops']), peak=peak, bw=num(s.get('mem_bandwidth_gbps')), cls=cls(r), url=r['source_url'], derived=r['metric'] == 'latency_ms'))


# ---------- Hailo: use the model-zoo table's own FPS (batch 1) and OPS ----------
HZ_URL = 'https://github.com/hailo-ai/hailo_model_zoo/tree/master/docs/public_models'
for r in csv.DictReader(open('data/ref/hailo_zoo_table.csv')):
    try: fps = float(r['fps_b1']); gops = float(r['ops_g'])
    except ValueError: continue
    name = r['network']
    fam = 'Transformer' if re.search(r'vit|deit|swin|davit|cas_vit', name) else 'CNN'
    sc = scenario(name, r['task'], fam) if fam == 'CNN' else 'Transformer'
    if r['task'] == 'classification' and fam == 'CNN': sc = '图像分类'
    s = spec_for('Hailo', r['chip'])
    peak = num(s.get('npu_tops_int8'))
    eff = fps * gops / 1000
    if peak and eff > 1.3 * peak: continue
    obs.append(dict(vendor='Hailo', chip=r['chip'], model=name, fam=fam, scen=sc, fps=fps, eff=eff, gops=gops, peak=peak, bw=None, cls='official',
                    url=f'{HZ_URL}/{r["chip"].replace("-", "").upper()}', derived=False))

def agg(rows, key=lambda o: (o['vendor'], o['chip'], o['cls'])):
    g = collections.defaultdict(dict)  # (chip) -> model -> best eff
    meta = {}
    for o in rows:
        k = key(o)
        if o['model'] not in g[k] or o['eff'] > g[k][o['model']]['eff']: g[k][o['model']] = o
        meta[k] = o
    res = []
    for k, ms in g.items():
        e = [x['eff'] for x in ms.values()]
        h = [x['eff'] for x in ms.values() if x['gops'] >= 5]  # compute-heavy models (>=5 GOPs) fill the array better
        o = meta[k]
        hm = statistics.median(h) if h else None
        res.append(dict(key=k, n=len(e), nh=len(h), lo=min(e), med=statistics.median(e), hmed=hm, hi=max(e), peak=o['peak'], bw=o['bw'],
                        util=(hm / o['peak']) if (hm and o['peak']) else None, models=sorted(ms)))
    return sorted(res, key=lambda r: -(r['hmed'] if r['hmed'] is not None else 0))

def fmt_table(res, min_n=1):
    L = ['| # | 厂商 | 芯片 | 类别 | 样本数(重模型) | 重模型等效 TOPS 中位 | 全部模型中位 | 区间(最低–最高) | 标称 TOPS | 利用率(重模型中位/标称) | 带宽 GB/s | 重模型等效TOPS/(GB/s) |', '|---|---|---|---|---|---|---|---|---|---|---|---|']
    i = 0
    for r in res:
        if r['n'] < min_n: continue
        i += 1
        v, c, k = r['key']
        hm = r['hmed']
        L.append(f'| {i} | {v} | {c} | {"官方" if k=="official" else "社区"} | {r["n"]}({r["nh"]}){"(样本少)" if r["nh"]<2 else ""} | {f"{hm:.2f}" if hm is not None else "—"} | {r["med"]:.2f} | {r["lo"]:.2f}–{r["hi"]:.2f} | {r["peak"] or ""} | {f"{r["util"]*100:.0f}%" if r["util"] else ""} | {r["bw"] or ""} | {f"{hm/r["bw"]:.3f}" if (hm and r["bw"]) else ""} |')
    return L

out = ['# 等效算力排名(按真实性能折算)\n',
       '等效 TOPS = 实测 FPS × 单次推理 GOPs(`data/ref/model_ops.csv`,GOPs=2×MACs) ÷ 1000。只用 INT8 类精度(或来源未标精度)、批大小 1、仅 NPU 推理的行;延迟按 1000/ms 换算。',
       '排名依据「重模型中位」:只取单次推理 ≥5 GOPs 的模型(小模型喂不满阵列,且各芯片测试的模型集合不同,直接取全部模型中位会偏向只测小模型的芯片)。利用率 = 重模型中位 ÷ 标称 INT8 TOPS(标称缺失则为空)。区间 = 该芯片所有模型的最低到最高。括号内为重模型数,<2 视为样本少。',
       '注意:各家 GOPs 口径(2×MAC)统一,但模型变体(如 YOLOv5s 的 Hailo 版与 Ultralytics 版)、算子是否在 NPU 上全部执行、是否含前后处理仍可能不同。\n']
out += ['## 一、CNN 总榜(检测+分类+分割+人脸+姿态)\n'] + fmt_table(agg([o for o in obs if o['fam'] == 'CNN'])) + ['']
tr = [o for o in obs if o['fam'] in ('Transformer', 'Hybrid')]
out += ['## 二、Transformer 视觉模型(Swin / ViT / DeiT / FastViT)\n'] + (fmt_table(agg(tr)) if tr else ['(无足够数据)']) + ['']
out += ['## 三、按应用场景\n']
for sc in ('目标检测', '图像分类', '分割', '人脸', '姿态'):
    rows = [o for o in obs if o['scen'] == sc and o['fam'] == 'CNN']
    if not rows: continue
    out += [f'### {sc}\n'] + fmt_table(agg(rows)) + ['']
out += ['<!--LLM-->']
open('RANKING_EFFECTIVE.md', 'w').write('\n'.join(out))
print(len(obs), 'matched obs;', len({(o['vendor'], o['chip']) for o in obs}), 'chips')
print(collections.Counter(o['fam'] for o in obs), collections.Counter(o['scen'] for o in obs))

# ---------- LLM decode: effective memory throughput ----------
def params_b(name):
    m = re.search(r'(?<![\d.])(\d+(?:\.\d+)?)([bm])(?![a-z])', name.lower())
    if not m: return None
    return float(m.group(1)) * (1 if m.group(2) == 'b' else 0.001)
def bits_of(p):
    p = (p or '').lower()
    m = re.match(r'^(?:w|int|q)(\d+)', p) or re.match(r'^(?:w)(\d+)', p)
    if m: return int(m.group(1))
    if re.match(r'^(fp16|f16|bf16|float16)', p): return 16
    return None
llm = []
for f in sorted(glob.glob('data/*.csv')):
    b = os.path.basename(f)
    if b.startswith('specs_') or b in ('chip_specs.csv', 'model_ops.csv'): continue
    for r in csv.DictReader(open(f)):
        if r['metric'] != 'tokens_per_s': continue
        n = r['notes'].lower()
        if 'ttft' in n.split(';')[0] and 'decode' not in n: continue
        if r['vendor'] == 'Qualcomm' and 'GENIE' not in r['runtime'].upper().replace('GENIEX_LLAMACPP', ''): continue
        if r['vendor'] == 'Sophgo' and r['chip'] in ('SRM1-20', 'SC7-HP75', 'SC7-224T'): continue
        if 'Dragonwing' in r['chip'] or r['chip'].startswith('Qualcomm® SA'): continue
        pb = params_b(r['model']); bits = bits_of(r['precision']); v = num(r['value'])
        if not pb or not bits or not v: continue
        chip = norm_chip(r['chip'])
        s = spec_for(r['vendor'], chip)
        gbs = v * pb * bits / 8  # GB/s of weight traffic (weights only, ignores KV cache / scales)
        bwv = num(s.get('mem_bandwidth_gbps'))
        if re.search(r'vl|internvl|smolvlm|janus|minicpm-?v|llava|ocr', r['model'].lower()):
            continue  # VLM: name's param count includes the vision tower, overstating LLM weights
        if re.search(r'moe|a\d+b', r['model'].lower()) or (bwv and gbs > 1.15 * bwv):
            dropped.append((r['vendor'], chip, r['model'][:30], round(gbs, 1), bwv or 'MoE')); continue  # MoE (active params < total) or > peak bandwidth
        llm.append(dict(vendor=r['vendor'], chip=chip, model=r['model'], pb=pb, bits=bits, tps=v, gbs=gbs, bw=num(s.get('mem_bandwidth_gbps')), cls=cls(r), url=r['source_url']))
best = {}
for o in llm:
    k = (o['vendor'], o['chip'], o['cls'], o['model'].split('(')[0].split('/')[0].strip().lower(), o['bits'])
    if k not in best or o['tps'] > best[k]['tps']: best[k] = o
byc = collections.defaultdict(list)
for o in best.values(): byc[(o['vendor'], o['chip'], o['cls'])].append(o)
rows = []
for k, v in byc.items():
    g = [x['gbs'] for x in v]; bw = v[0]['bw']
    rows.append((statistics.median(g), k, v, bw))
rows.sort(key=lambda x: -x[0])
L = ['## 四、端侧大模型(LLM/VLM decode)\n',
     '解码每个 token 要读一遍全部权重,因此 **等效内存吞吐 = tokens/s × 参数量 × 位宽/8**(GB/s,只算权重,不含 KV cache 与量化缩放,实际略高)。带宽利用率 = 等效吞吐 ÷ 理论峰值带宽。',
     '参数量取自模型名(如 1.5B)、位宽取自精度标注(w4a16→4);未标精度/参数的行已剔除;Qualcomm 仅取 GENIE(QAIRT) 运行时、不含 llama.cpp 与车规 Dragonwing/SA 系列;Sophgo 未映射到具体芯片的平台已剔除。\n',
     '| # | 厂商 | 芯片 | 类别 | 模型数 | 等效内存吞吐 中位 GB/s | 区间 | 理论带宽 GB/s | 带宽利用率(中位) | 代表模型(tokens/s) |', '|---|---|---|---|---|---|---|---|---|---|']
for i, (med, k, v, bw) in enumerate(rows, 1):
    gs = sorted(x['gbs'] for x in v)
    top = sorted(v, key=lambda x: -x['gbs'])[:2]
    ex = '; '.join(f'{x["model"].split("(")[0].strip()[:28]} {x["bits"]}bit {x["tps"]:.1f}' for x in top)
    L.append(f'| {i} | {k[0]} | {k[1]} | {"官方" if k[2]=="official" else "社区"} | {len(v)}{"(样本少)" if len(v)<3 else ""} | {med:.1f} | {gs[0]:.1f}–{gs[-1]:.1f} | {bw or ""} | {f"{med/bw*100:.0f}%" if bw else ""} | {ex} |')
L.append('')
# size buckets
L += ['### 同尺寸对比(tokens/s,取各芯片最高)\n']
for lo, hi, bits, lab in ((0.3, 1.0, 4, '≈0.5B · 4bit'), (0.3, 1.0, 8, '≈0.5B · 8bit'), (1.0, 2.0, 4, '≈1.5B · 4bit'), (1.0, 2.0, 8, '≈1.5B · 8bit'), (3.0, 9.0, 4, '3–9B · 4bit')):
    sel = [o for o in best.values() if lo <= o['pb'] <= hi and o['bits'] == bits]
    c = {}
    for o in sel:
        k = (o['vendor'], o['chip'], o['cls'])
        if k not in c or o['tps'] > c[k]['tps']: c[k] = o
    if len(c) < 2: continue
    L += [f'**{lab}**\n', '| # | 厂商 | 芯片 | 类别 | tokens/s | 模型 | 理论带宽 | 带宽利用率 |', '|---|---|---|---|---|---|---|---|']
    for i, (k, o) in enumerate(sorted(c.items(), key=lambda kv: -kv[1]['tps']), 1):
        L.append(f'| {i} | {k[0]} | {k[1]} | {"官方" if k[2]=="official" else "社区"} | {o["tps"]:.1f} | {o["model"].split("(")[0].strip()[:30]} | {o["bw"] or ""} | {f"{o["gbs"]/o["bw"]*100:.0f}%" if o["bw"] else ""} |')
    L.append('')
out_text = open('RANKING_EFFECTIVE.md').read().replace('<!--LLM-->', '\n'.join(L))
if dropped:
    out_text += '\n\n---\n已剔除的不合理折算(CNN: 等效算力>1.3×标称;LLM: MoE 或超过理论带宽 1.15 倍;VLM 因名称参数量含视觉塔已不计入 LLM 榜): ' + '; '.join(f'{d[0]} {d[1]} {d[2]} {d[3]}>{d[4]}' for d in dropped[:20]) + '\n'
open('RANKING_EFFECTIVE.md', 'w').write(out_text)
print(len(llm), 'llm rows;', len(rows), 'chips;', len(dropped), 'dropped')
