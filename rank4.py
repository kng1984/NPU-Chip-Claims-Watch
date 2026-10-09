"""Common-suite leaderboard: every chip ranked on the SAME models (INT8-class, batch 1, NPU-only inference)."""
import io, contextlib, re, statistics, collections
with contextlib.redirect_stdout(io.StringIO()):
    exec(open('rank3.py').read())      # builds obs / specs / helpers (and regenerates the other rankings)

SUITE = {'YOLOv5s': 'YOLOv5s', 'YOLOv5s (Hailo yolov5s)': 'YOLOv5s', 'YOLOv8n': 'YOLOv8n', 'YOLOv8s': 'YOLOv8s',
         'ResNet50': 'ResNet50', 'MobileNetV2': 'MobileNetV2'}
HAILO = {'yolov5s⭐': 'YOLOv5s', 'yolov5s': 'YOLOv5s', 'yolov8n⭐': 'YOLOv8n', 'yolov8n': 'YOLOv8n', 'yolov8s⭐': 'YOLOv8s', 'yolov8s': 'YOLOv8s',
         'resnet_v1_50⭐': 'ResNet50', 'resnet_v1_50': 'ResNet50', 'mobilenet_v2_1.0': 'MobileNetV2'}
SUITE_ORDER = ['YOLOv5s', 'YOLOv8n', 'YOLOv8s', 'ResNet50', 'MobileNetV2']
best = {}  # (vendor, chip, model) -> (fps, class)
for o in obs:
    m = HAILO.get(o['model']) if o['vendor'] == 'Hailo' else SUITE.get(o['model'])
    if not m: continue
    k = (vnorm(o['vendor']), o['chip'], m)
    cand = (o['cls'] == 'official', o['fps'])
    if k not in best or cand > (best[k][1] == 'official', best[k][0]): best[k] = (o['fps'], o['cls'], o['derived'])
chips = sorted({(v, c) for v, c, m in best})
per_model = {m: sorted((best[(v, c, m)][0] for v, c in chips if (v, c, m) in best), reverse=True) for m in SUITE_ORDER}
def mp(m, x):
    arr = per_model[m]; n = len(arr)
    return 100.0 if n == 1 else 100.0 * (n - 1 - arr.index(x)) / (n - 1)
R = []
for v, c in chips:
    got = {m: best[(v, c, m)] for m in SUITE_ORDER if (v, c, m) in best}
    pcts = [mp(m, got[m][0]) for m in got if len(per_model[m]) >= 3]
    s = spec_for(v, c) or spec_for(v, c.split(' (')[0])
    peak = num(s.get('npu_tops_int8')); bw = num(s.get('mem_bandwidth_gbps'))
    ft = statistics.median([got[m][0] for m in got]) if False else None
    R.append(dict(v=v, c=c, got=got, score=(sum(pcts) / len(pcts)) if pcts else None, n=len(got), peak=peak, bw=bw))
R.sort(key=lambda r: (r['n'] < 2, -(r['score'] if r['score'] is not None else -1), -r['n'], r['v']))  # single-model chips last
L = ['# 同一套模型总榜(Common-suite)\n',
     '所有芯片在**同一批基准模型**上比较:YOLOv5s / YOLOv8n / YOLOv8s(640×640),ResNet50 / MobileNetV2(224×224);INT8 类精度(或来源未标)、批大小 1、仅 NPU 推理;延迟按 1000/ms 换算(†)。',
     '**排序**:测过 ≥2 个套件模型的芯片在前,只测过 1 个模型的芯片(综合分极易失真)排在后面并标「单模型」。Hailo 的 ResNet50 为 Hailo 自家变体 resnet_v1_50(6.98 GOPs,与 torchvision ResNet50 的 8.18 GOPs 不同)。\n'
     '**综合分** = 芯片在每个模型上的「FPS 百分位」(该模型有数据的芯片之间)的平均,0–100;只统计有数据的模型;**测过的模型数少于 2 个的芯片综合分仅作参考**。官方数据优先,无官方才用社区数据(标 ᶜ)。',
     '这张表不做 GOPs 折算,直接比同一模型的 FPS,因此不依赖 `model_ops.csv`;但各家 YOLOv5s 变体(如 Hailo 版 17.4 GOPs 与 Ultralytics 版)、输入尺寸和软件栈仍可能略有不同。\n',
     '| 名次 | 厂商 | 芯片 | 标称 INT8 TOPS | 带宽 GB/s | YOLOv5s | YOLOv8n | YOLOv8s | ResNet50 | MobileNetV2 | 测过模型数 | 综合分 | 每 TOPS 的 FPS(YOLOv5s 或 ResNet50) |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
def cell(g, m):
    if m not in g: return ''
    f, cl, d = g[m]
    return f'{f:.1f}{"†" if d else ""}{"ᶜ" if cl != "official" else ""}'
rk = 0
for r in R:
    if r['score'] is None: rank = '—'
    else: rk += 1; rank = str(rk) + ('(单模型)' if r['n'] < 2 else '')
    g = r['got']; per = ''
    for m in ('YOLOv5s', 'ResNet50'):
        if m in g and r['peak']: per = f'{g[m][0] / r["peak"]:.2f} ({m})'; break
    L.append(f'| {rank} | {r["v"]} | {r["c"]} | {f2(r["peak"],1)} | {f2(r["bw"],1)} | ' + ' | '.join(cell(g, m) for m in SUITE_ORDER) + f' | {r["n"]} | {f2(r["score"],0)} | {per} |')
L += ['', f'共 {len(R)} 颗芯片至少在一个套件模型上有数据。未出现的芯片(Cix P1、Apple、Intel、寒武纪、昇腾 910 等)见 `RANKING_ALL.md` 的「数据状态」。']
open('RANKING_COMMON_SUITE.md', 'w').write('\n'.join(L))
print(len(R), 'chips,', sum(1 for r in R if r['score'] is not None), 'scored')
