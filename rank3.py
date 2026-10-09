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
for f in ['specs_m', 'specs_i', 'specs_j', 'specs_k', 'specs_l', 'specs_g', 'specs_f', 'specs_h', 'specs_d', 'specs_e', 'chip_specs', 'specs_a', 'specs_b']:
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

INT8_OK = re.compile(r'^(|int8|uint8|a8w8|w8a8|int8 \(int8\)|quantized.*|not stated.*)$', re.I)
def batch_ok(r):
    txt = ' '.join([r['notes'], r['model'], r['runtime']]).lower()
    return all(int(b) == 1 for b in re.findall(r'batch[ =_:]*(\d+)', txt))
def cls(r):
    return 'community' if r['notes'].lower().startswith(('community', 'forum', 'media')) else 'official'


def sophgo_model(m):
    """Map a sophon-demo row 'Group / chip/file_precision_1b.bmodel' to (model name, assumed input edge)."""
    parts = [p.strip() for p in m.split(' / ')]
    grp = parts[0].lower(); f = parts[-1].split('/')[-1].lower()
    base = re.split(r'_(?:fp32|fp16|f16|f32|int8|bf16)', f)[0]
    base = re.sub(r'_v\d.*$', '', base)
    if grp == 'yolov5' and base.startswith('yolov5s'): return ('yolov5s', '640')
    if grp == 'yolov8_plus_det' and base.startswith('yolov8') and base[6] in 'nsm': return ('yolov8' + base[6], '640')
    if grp == 'yolov8_plus_seg' and base.startswith('yolov8') and base[6] in 'nsm': return ('yolov8' + base[6] + '-seg', '640')
    if grp == 'yolov8_pose' and base.startswith('yolov8') and base[6] in 'nsm': return ('yolov8' + base[6] + '-pose', '640')
    if grp == 'yolov10' and base.startswith('yolov10') and base[7] in 'ns': return ('yolov10' + base[7], '640')
    if grp == 'yolov7' and base.startswith('yolov7') and 'tiny' not in base: return ('yolov7', '640')
    if grp == 'yolox' and base in ('yolox_s', 'yolox_m'): return ('yolox-' + base[-1], '640')
    if grp == 'resnet' and base.startswith('resnet50'): return ('resnet50', '224')
    return None

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
        if r['vendor'] == 'Huawei Ascend' and not re.search(r'batch[ =_:]*1\b', (r['notes'] + ' ' + r['model']).lower()): continue  # batch not stated => likely max-throughput batch
        if r['vendor'] == 'Sophgo':
            if r['chip'] in ('SRM1-20', 'SC7-HP75', 'SC7-224T'): continue
            r = dict(r); mn = sophgo_model(r['model'])
            if not mn: continue
            r['model'] = mn[0]; r['input_size'] = r['input_size'] or mn[1]
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

# ================= master table: every chip in one list =================
def vnorm(v): return 'Google Coral' if v == 'Google' else v
allchips = set()
for f in sorted(glob.glob('data/*.csv')):
    b = os.path.basename(f)
    if b.startswith('specs_') or b == 'chip_specs.csv': continue
    for r in csv.DictReader(open(f)):
        if f.endswith('apple.csv'): continue
        c = norm_chip(r['chip'])
        if c in ('SRM1-20', 'SC7-HP75', 'SC7-224T') or c.startswith(('Qualcomm SA', 'Qualcomm® SA')) or 'Dragonwing' in c or c.startswith('Intel NPU (SoC') or c == 'MLU590-M9' or c.startswith('Snapdragon 8 Gen 1'): continue
        allchips.add((vnorm(r['vendor']), c))
allchips |= {('Apple', 'A18 Pro / M-series (Core ML)')}

def pick(res):  # (vendor, chip) -> best entry, official preferred
    d = {}
    for e in res:
        k = (vnorm(e['key'][0]), e['key'][1])
        if k not in d or (e['key'][2] == 'official' and d[k]['key'][2] != 'official'): d[k] = e
    return d
cnn_d = pick(agg([o for o in obs if o['fam'] == 'CNN']))
tr_d = pick(agg([o for o in obs if o['fam'] == 'Transformer']))
llm_d = {}
for med, k, v, bw in rows:
    kk = (vnorm(k[0]), k[1])
    if kk not in llm_d or (k[2] == 'official' and llm_d[kk][1] != 'official'): llm_d[kk] = (med, k[2], len(v), bw)


STATUS = {('Cix', 'P1 (CD8180)'): '仅合成基准:卷积网络等效约 20–22 TOPS、矩阵乘约 3.5 TOPS(社区实测);BiSeNet 10.7 ms 缺 GOPs;无标准模型成绩',
          ('Apple', 'A18 Pro / M-series (Core ML)'): 'Core ML 延迟(FP16,计算单元=CPU/GPU/神经引擎调度),与纯 NPU 不可比',
          ('Cambricon', 'MLU590'): '仅算子微基准,无模型级成绩', ('Intel', 'Core Ultra 9 288V NPU (Lunar Lake)'): '仅 MLPerf Client Llama-2-7B 一条(未标位宽)',
          ('Intel', 'Core Ultra 7 258V NPU (Lunar Lake)'): '仅规格,无可折算成绩', ('Intel', 'Core Ultra 5 125H NPU (Meteor Lake; ASUS Vivobook S16 OLED)'): '社区零散数字,硬件口径不明',
          ('Huawei Ascend', 'Ascend 910B (TP4, 4 cards)'): '仅多卡大模型服务实测', ('Huawei Ascend', 'Ascend 910B4'): '仅大模型服务实测',
          ('Huawei Ascend', 'Ascend 310P3'): '成绩为 FP32 输入 om 模型,批大小多为未标/大批;仅有「宽口径」参考值,未计入综合分',
          ('Qualcomm', 'Snapdragon X Plus X1P-42-100 (Hexagon NPU)'): '仅社区零散数字'}

KIND = {'Qualcomm': '手机/PC SoC', 'Apple': '手机/PC SoC', 'Intel': '手机/PC SoC', 'Hailo': 'PCIe/M.2 加速器', 'Google Coral': 'PCIe/USB 加速器',
        'Huawei Ascend': '边缘/服务器加速卡', 'Cambricon': '服务器加速卡', 'Sophgo': '边缘 SoC/加速卡'}
def pct(vals):
    srt = sorted(vals, reverse=True)
    n = len(srt)
    return lambda x: 100.0 if n == 1 else 100.0 * (n - 1 - srt.index(x)) / (n - 1)
p_cnn = pct([e['hmed'] if e['hmed'] is not None else e['med'] for e in cnn_d.values()])
p_tr = pct([e['hmed'] if e['hmed'] is not None else e['med'] for e in tr_d.values()])
p_llm = pct([v[0] for v in llm_d.values()])


# ---------- wide-scope fallback: any batch / any precision (fps rows only), best matched model ----------
wide = {}
for f in sorted(glob.glob('data/*.csv')):
    b = os.path.basename(f)
    if b.startswith('specs_') or b in ('chip_specs.csv', 'apple.csv'): continue
    for r in csv.DictReader(open(f)):
        if r['metric'] != 'fps': continue
        n = r['notes'].lower()
        if any(w in n for w in ('end-to-end', 'pipeline', 'concurrent', 'outlier', 'synthetic')): continue
        if r['vendor'] == 'Sophgo':
            mn = sophgo_model(r['model'])
            if not mn: continue
            r = dict(r, model=mn[0], input_size=r['input_size'] or mn[1])
        m = match_ops(r['model'], edge(r['input_size']))
        v = num(r['value'])
        if not m or not v: continue
        k = (vnorm(r['vendor']), norm_chip(r['chip']))
        eff = v * float(m['gops']) / 1000
        s = spec_for(*k); peak = num(s.get('npu_tops_int8'))
        if peak and eff > 1.3 * peak: continue
        if k not in wide or eff > wide[k][0]: wide[k] = (eff, m['model'], r['precision'] or '未标', re.findall(r'batch[ =_:]*(\d+)', n))

M = []
for (v, c) in sorted(allchips):
    s = spec_for(v, c) or spec_for(v, c.split(' (')[0])
    peak = num(s.get('npu_tops_int8')); bw = num(s.get('mem_bandwidth_gbps'))
    e1, e2, e3 = cnn_d.get((v, c)), tr_d.get((v, c)), llm_d.get((v, c))
    c1 = (e1['hmed'] if e1['hmed'] is not None else e1['med']) if e1 else None
    c2 = (e2['hmed'] if e2['hmed'] is not None else e2['med']) if e2 else None
    c3 = e3[0] if e3 else None
    sc = [p_cnn(c1) if c1 is not None else None, p_tr(c2) if c2 is not None else None, p_llm(c3) if c3 is not None else None]
    have = [x for x in sc if x is not None]
    M.append(dict(wide=wide.get((v, c)), v=v, c=c, kind=KIND.get(v, '边缘 SoC/NPU'), peak=peak, bw=bw, c1=c1, c2=c2, c3=c3, sc=sc,
                  score=(sum(have) / len(have)) if have else None, nm=len(have),
                  util=(c1 / peak if (c1 and peak) else None), bwu=(c3 / bw if (c3 and bw) else None)))
M.sort(key=lambda m: (-(m['score'] if m['score'] is not None else -1), m['v'], m['c']))
f2 = lambda x, d=1: '' if x is None else f'{x:.{d}f}'
T = ['# 全芯片总榜(一张表)\n',
     '把数据集中出现的所有芯片放进同一张表。**综合分** = 该芯片在可得指标上的「全体百分位」平均(0–100;三项指标:CNN 等效算力、Transformer 视觉等效算力、LLM 解码等效内存吞吐);无数据的指标留空,不计入平均。',
     '**覆盖**(C/T/L)表示三项指标哪几项有数据。只有 1 项指标的芯片综合分仅作参考(手机 SoC 常因只测了云端纯 NPU 延迟而排名靠前,与开发板口径不完全相同)。',
     '各列含义:标称 TOPS = 厂商 INT8 标称;CNN/Transformer 等效 TOPS = 重模型(≥5 GOPs)中位的 FPS×GOPs;利用率 = CNN 等效/标称;LLM 等效 GB/s = tokens/s×权重字节;带宽利用率 = LLM 等效 GB/s ÷ 理论带宽。官方数据优先,无官方数据才用社区数据。\n',
     '| 综合排名 | 厂商 | 芯片 | 类型 | 标称 INT8 TOPS | 带宽 GB/s | CNN 等效 TOPS | CNN 利用率 | Transformer 等效 TOPS | LLM 等效 GB/s | LLM 带宽利用率 | 覆盖 C/T/L | 综合分 | 宽口径最佳等效 TOPS(任意批大小/精度,参考) | 数据状态 |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|']
rk = 0
for m in M:
    if m['score'] is None: rank = '—'
    else:
        rk += 1; rank = str(rk)
    cov = ''.join(('C' if m['sc'][0] is not None else '·', 'T' if m['sc'][1] is not None else '·', 'L' if m['sc'][2] is not None else '·'))
    T.append(f'| {rank} | {m["v"]} | {m["c"]} | {m["kind"]} | {f2(m["peak"],1)} | {f2(m["bw"],1)} | {f2(m["c1"],2)} | {f"{m["util"]*100:.0f}%" if m["util"] else ""} | {f2(m["c2"],2)} | {f2(m["c3"],1)} | {f"{m["bwu"]*100:.0f}%" if m["bwu"] else ""} | {cov} | {f2(m["score"],0)} | {(f"{m['wide'][0]:.2f} ({m['wide'][1]}, 批{m['wide'][3][0] if m['wide'][3] else '?'})" if m['wide'] else '')} | {STATUS.get((m["v"], m["c"]), "无可折算数据" if m["score"] is None else "")} |')
T += ['', '"—" 排名表示目前没有任何可折算的数据(例如缺批大小 1 的 INT8 记录、缺模型 GOPs、或只有 FP16/混合精度成绩)。该类芯片的原始成绩见各厂商 CSV。']
open('RANKING_ALL.md', 'w').write('\n'.join(T))
print(len(M), 'chips in master;', sum(1 for m in M if m['score'] is not None), 'ranked')
