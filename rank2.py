"""Like-for-like leaderboards: same model, same input size, INT8-class precision, batch 1, NPU inference only.
Latency rows are converted to FPS (1000/ms, marked †). Efficiency columns use data/specs_*.csv + chip_specs.csv."""
import csv, glob, re, os, collections

def num(s):
    try: return float(s)
    except (TypeError, ValueError): return None

specs = {}
for f in ['data/specs_m.csv', 'data/specs_g.csv', 'data/specs_f.csv', 'data/specs_h.csv', 'data/specs_d.csv', 'data/specs_e.csv', 'data/specs_j.csv', 'data/specs_k.csv', 'data/specs_l.csv',
          'data/chip_specs.csv', 'data/specs_a.csv', 'data/specs_b.csv']:  # first non-empty value wins
    if not os.path.exists(f): continue
    for r in csv.DictReader(open(f)):
        cur = specs.setdefault((r['vendor'], r['chip']), dict(r))
        for k, v in r.items():
            if v and not cur.get(k): cur[k] = v

def norm_chip(c):
    c = re.sub(r'[®™]', '', c)
    c = re.sub(r' (For Galaxy )?Mobile$', '', c).replace(' For Galaxy', '')
    return c.strip()

def spec_for(vendor, chip):
    for k in ((vendor, chip), (vendor, chip + ' (Hexagon NPU)')):
        if k in specs: return specs[k]
    return {}

TARGETS = {  # label -> (model matcher, expected input edge)
    'YOLOv5s · 640×640': (lambda k: k == 'yolov5s', 640),
    'YOLOv8n · 640×640': (lambda k: k == 'yolov8n', 640),
    'ResNet50 · 224×224': (lambda k: k.startswith('resnet50'), 224),
    'MobileNetV2 · 224×224': (lambda k: k.startswith('mobilenetv2'), 224),
}
INT8_OK = re.compile(r'^(|int8|uint8|a8w8|w8a8|int8 \(int8\))$', re.I)

def edge(s):
    m = re.findall(r'\d+', s or '')
    return max(int(x) for x in m) if m else None

def batch_ok(r):
    txt = ' '.join([r['notes'], r['model'], r['runtime']]).lower()
    return all(int(b) == 1 for b in re.findall(r'batch[ =_:]*(\d+)', txt))

def klass(r):
    n = r['notes'].lower()
    for tag in ('community', 'forum', 'media'):
        if n.startswith(tag): return 'community'
    return 'official'

cand = collections.defaultdict(list)
for f in sorted(glob.glob('data/*.csv')):
    if 'spec' in f or f.endswith('community.csv') and False: continue
    for r in csv.DictReader(open(f)):
        if r['metric'] not in ('fps', 'latency_ms'): continue
        n = r['notes'].lower()
        if any(w in n for w in ('concurrent', 'end-to-end', 'pipeline', 'outlier', 'not npu-only')): continue
        if f.endswith('apple.csv'): continue
        k = re.sub(r'[^a-z0-9]', '', r['model'].lower())
        for label, (match, size) in TARGETS.items():
            if not match(k): continue
            e = edge(r['input_size'])
            if e is not None and e != size: continue
            if e is None and not r['input_size'] == '' : continue
            if not INT8_OK.match(r['precision'] or ''): continue
            if not batch_ok(r): continue
            try: v = float(r['value'])
            except ValueError: continue
            if v <= 0: continue
            derived = r['metric'] == 'latency_ms'
            chip = norm_chip(r['chip'])
            cand[label].append(dict(r, chip=chip, fps=1000 / v if derived else v, derived=derived,
                                    size_known=e is not None, cls=klass(r), file=f))

out = ['# 同口径排名(Like-for-like)\n',
       '条件:同一模型、同一输入尺寸、INT8 类精度(或来源未标精度)、批大小 1、仅 NPU 推理(不含端到端流水线)。',
       '同一芯片只保留最高值;官方/厂商数据与社区/论坛数据分列。† = 由延迟换算(1000/ms)。「尺寸未标」表示来源没有给输入尺寸。',
       'FPS/TOPS、FPS/(GB/s) 仅在规格表有数据时给出;空白=缺规格。各家测试软件栈与是否含前后处理仍有差异,请当作量级参考。\n']
for label, rows in cand.items():
    best = {}
    for r in rows:
        k = (r['vendor'], r['chip'], r['cls'])
        if k not in best or r['fps'] > best[k]['fps']: best[k] = r
    out += [f'## {label}\n', '| # | 厂商 | 芯片 | FPS | 类别 | NPU TOPS | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 备注 | 来源 |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for i, r in enumerate(sorted(best.values(), key=lambda r: -r['fps']), 1):
        s = spec_for(r['vendor'], r['chip'])
        t = num(s.get('npu_tops_int8')) or num(r['chip_tops'])
        b = num(s.get('mem_bandwidth_gbps'))
        flag = ('†' if r['derived'] else '') + ('' if r['size_known'] else ' 尺寸未标')
        out.append(f'| {i} | {r["vendor"]} | {r["chip"]} | {r["fps"]:.1f}{"†" if r["derived"] else ""} | {"官方" if r["cls"]=="official" else "社区"} | {t or ""} | {b or ""} | {round(r["fps"]/t,2) if t else ""} | {round(r["fps"]/b,2) if b else ""} | {r["precision"] or "精度未标"}{"; 尺寸未标" if not r["size_known"] else ""} | [link]({r["source_url"]}) |')
    out.append('')
open('RANKING_LIKE_FOR_LIKE.md', 'w').write('\n'.join(out))
print({k: len(v) for k, v in cand.items()})
