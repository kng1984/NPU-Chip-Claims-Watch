"""Rank chips per (model, precision) by FPS; add FPS/TOPS and FPS/(GB/s) when chip_specs.csv has the figures."""
import csv, glob, re, collections

specs = {}
for f in ['data/specs_g.csv', 'data/specs_f.csv', 'data/specs_h.csv', 'data/specs_d.csv', 'data/specs_e.csv', 'data/chip_specs.csv', 'data/specs_a.csv', 'data/specs_b.csv']:  # first non-empty value wins
    for r in csv.DictReader(open(f)):
        cur = specs.setdefault((r['vendor'], r['chip']), dict(r))
        for k, v in r.items():
            if v and not cur.get(k): cur[k] = v
def num(s):
    try: return float(s)
    except (TypeError, ValueError): return None

def norm_chip(c):
    c = re.sub(r'[®™]', '', c)
    c = re.sub(r' (For Galaxy )?Mobile$', '', c).replace(' For Galaxy', '')
    return c.strip()

groups = collections.defaultdict(list)
for r in csv.DictReader(open('data/web_qualcomm.csv')):  # derived FPS = 1000 / latency (batch 1, NPU, vision only)
    if r['metric'] != 'latency_ms' or 'compute unit NPU' not in r['notes'] or float(r['value']) <= 0: continue
    r = dict(r, metric='fps', value=str(1000 / float(r['value'])), chip=norm_chip(r['chip']),
             notes='derived: 1000/latency_ms; ' + r['notes'])
    groups[(re.sub(r'[^a-z0-9]', '', r['model'].lower()), r['precision'] or 'n/a')].append(r)

for f in sorted(glob.glob('data/*.csv')):
    if f.endswith('chip_specs.csv') or 'specs_' in f or f.endswith('community.csv') or 'web_' in f: continue
    for r in csv.DictReader(open(f)):
        if r['metric'] != 'fps': continue
        key = (re.sub(r'[^a-z0-9]', '', r['model'].lower()), r['precision'] or 'n/a')
        groups[key].append(r)

out = ['# 排名（按模型 × 精度，FPS 降序）\n',
       '由 `rank.py` 生成。只比较 fps 指标；同一芯片同模型取最大值（批大小/输入尺寸可能不同，见源 CSV 的 notes）。',
       'FPS/TOPS、FPS/(GB/s) 仅在 `data/chip_specs.csv` 有对应规格时给出，空表示缺规格，**不是 0**。',
       '各厂商测试口径不同，跨厂商排名仅供参考。† = 由延迟换算(1000/latency_ms，批大小1)，非厂商直接给出的 FPS。\n']
n = 0
for (m, p), rows in sorted(groups.items(), key=lambda a: -len({(r['vendor'], r['chip']) for r in a[1]})):
    best = {}
    for r in rows:
        k = (r['vendor'], r['chip'])
        if k not in best or float(r['value']) > float(best[k]['value']): best[k] = r
    if len(best) < 3: continue
    n += 1
    if n > 40: break
    out += [f'## {rows[0]["model"]} · {p}\n',
            '| # | 厂商 | 芯片 | FPS | NPU TOPS(INT8) | 带宽 GB/s | FPS/TOPS | FPS/(GB/s) | 来源 |', '|---|---|---|---|---|---|---|---|---|']
    for i, r in enumerate(sorted(best.values(), key=lambda r: -float(r['value'])), 1):
        s = specs.get((r['vendor'], r['chip'])) or specs.get((r['vendor'], r['chip'] + ' (Hexagon NPU)'), {})
        t, b, v = num(s.get('npu_tops_int8')) or num(r['chip_tops']), num(s.get('mem_bandwidth_gbps')), float(r['value'])
        out.append(f'| {i} | {r["vendor"]} | {r["chip"]} | {v:g}{"†" if r["notes"].startswith("derived") else ""} | {t or ""} | {b or ""} | {round(v/t,2) if t else ""} | {round(v/b,2) if b else ""} | [link]({r["source_url"]}) |')
    out.append('')
open('RANKING.md', 'w').write('\n'.join(out))
print(n, 'groups')
