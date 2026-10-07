"""Rank chips per (model, precision) by FPS; add FPS/TOPS and FPS/(GB/s) when chip_specs.csv has the figures."""
import csv, glob, re, collections

specs = {(r['vendor'], r['chip']): r for r in csv.DictReader(open('data/chip_specs.csv'))}
def num(s):
    try: return float(s)
    except (TypeError, ValueError): return None

groups = collections.defaultdict(list)
for f in sorted(glob.glob('data/*.csv')):
    if f.endswith('chip_specs.csv') or 'specs_' in f or f.endswith('community.csv'): continue
    for r in csv.DictReader(open(f)):
        if r['metric'] != 'fps': continue
        key = (re.sub(r'[^a-z0-9]', '', r['model'].lower()), r['precision'] or 'n/a')
        groups[key].append(r)

out = ['# 排名（按模型 × 精度，FPS 降序）\n',
       '由 `rank.py` 生成。只比较 fps 指标；同一芯片同模型取最大值（批大小/输入尺寸可能不同，见源 CSV 的 notes）。',
       'FPS/TOPS、FPS/(GB/s) 仅在 `data/chip_specs.csv` 有对应规格时给出，空表示缺规格，**不是 0**。',
       '各厂商测试口径不同，跨厂商排名仅供参考。\n']
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
        s = specs.get((r['vendor'], r['chip']), {})
        t, b, v = num(s.get('npu_tops_int8')) or num(r['chip_tops']), num(s.get('mem_bandwidth_gbps')), float(r['value'])
        out.append(f'| {i} | {r["vendor"]} | {r["chip"]} | {v:g} | {t or ""} | {b or ""} | {round(v/t,2) if t else ""} | {round(v/b,2) if b else ""} | [link]({r["source_url"]}) |')
    out.append('')
open('RANKING.md', 'w').write('\n'.join(out))
print(n, 'groups')
