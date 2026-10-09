#!/usr/bin/env python3
"""Collect tech news / crowdfunding / products / complaints / papers / blogs / vendor posts.
stdlib only. Usage: python3 -I collect.py [outdir]   -> items.jsonl + status.json"""
import json, sys, os, re, time, html, urllib.request, urllib.parse, datetime, email.utils
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out")
UA = "Mozilla/5.0 (compatible; trendwatch/1.0)"
os.makedirs(OUT, exist_ok=True)

def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def strip(s):
    s = re.sub(r"<[^>]+>", " ", html.unescape(s or ""))
    return re.sub(r"\s+", " ", s).strip()

def parse_date(s):
    if not s: return ""
    s = s.strip()
    try:
        return email.utils.parsedate_to_datetime(s).astimezone(datetime.timezone.utc).strftime("%Y-%m-%d")
    except Exception: pass
    m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
    return m.group(1) if m else ""

def local(tag): return tag.rsplit("}", 1)[-1]

def parse_feed(data):
    root = ET.fromstring(data)
    out = []
    for e in root.iter():
        if local(e.tag) not in ("item", "entry"): continue
        d = {}
        for c in e:
            t = local(c.tag)
            if t == "link":
                d.setdefault("link", c.get("href") or (c.text or "").strip())
            elif t in ("title", "pubDate", "published", "updated", "description", "summary", "content", "encoded"):
                d.setdefault(t, c.text or "")
        out.append({"title": strip(d.get("title")), "url": d.get("link", ""),
                    "date": parse_date(d.get("pubDate") or d.get("published") or d.get("updated")),
                    "text": strip(d.get("description") or d.get("summary") or d.get("encoded") or d.get("content"))[:600]})
    return out

def do_rss(src):
    cat, name, url = src
    items = parse_feed(get(url))
    return [dict(i, cat=cat, source=name) for i in items if i["title"]]

def do_arxiv(cat):
    q = urllib.parse.urlencode({"search_query": f"cat:{cat}", "sortBy": "submittedDate", "sortOrder": "descending", "max_results": 100})
    root = ET.fromstring(get("https://export.arxiv.org/api/query?" + q, 60))
    out = []
    for e in root:
        if local(e.tag) != "entry": continue
        g = lambda n: next((strip(c.text) for c in e if local(c.tag) == n), "")
        out.append({"cat": "paper", "source": "arXiv " + cat, "title": g("title"), "url": g("id"),
                    "date": parse_date(g("published")), "text": g("summary")[:600]})
    return out

def do_hf():
    j = json.loads(get("https://huggingface.co/api/daily_papers"))
    return [{"cat": "paper", "source": "HF Daily Papers", "title": strip(p["paper"]["title"]),
             "url": "https://huggingface.co/papers/" + p["paper"]["id"], "date": parse_date(p["paper"].get("publishedAt", "")),
             "text": strip(p["paper"].get("summary", ""))[:600], "score": p["paper"].get("upvotes", 0)} for p in j]

def do_hn_front():
    ids = json.loads(get("https://hacker-news.firebaseio.com/v0/topstories.json"))[:100]
    def one(i):
        try: return json.loads(get(f"https://hacker-news.firebaseio.com/v0/item/{i}.json", 15))
        except Exception: return None
    with ThreadPoolExecutor(10) as ex: its = [x for x in ex.map(one, ids) if x]
    return [{"cat": "forum", "source": "Hacker News front", "title": strip(x.get("title")), "url": x.get("url") or f"https://news.ycombinator.com/item?id={x['id']}",
             "date": datetime.datetime.fromtimestamp(x.get("time", 0), datetime.timezone.utc).strftime("%Y-%m-%d"),
             "text": "", "score": x.get("score", 0), "comments": x.get("descendants", 0)} for x in its if x.get("title")]

def do_hn_query(q):
    # last 90 days, sorted by points
    since = int(time.time()) - 90 * 86400
    u = "https://hn.algolia.com/api/v1/search?" + urllib.parse.urlencode({"query": q, "tags": "(story,ask_hn)", "numericFilters": f"created_at_i>{since}", "hitsPerPage": 30})
    j = json.loads(get(u))
    return [{"cat": "forum", "source": "HN search", "query": q, "title": strip(h.get("title")),
             "url": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
             "date": parse_date(h.get("created_at", "")), "text": strip(h.get("story_text") or "")[:600],
             "score": h.get("points") or 0, "comments": h.get("num_comments") or 0} for h in j.get("hits", []) if h.get("title")]

def main():
    cfg = json.load(open(os.path.join(HERE, "sources.json")))
    jobs = [(f"rss:{n}", lambda s=s: do_rss(s)) for s in cfg["rss"] for n in [s[1]]]
    jobs += [(f"arxiv:{c}", lambda c=c: do_arxiv(c)) for c in cfg["arxiv"]]
    jobs += [("hf:daily", do_hf), ("hn:front", do_hn_front)]
    jobs += [(f"hnq:{q}", lambda q=q: do_hn_query(q)) for q in cfg["hn_queries"]]
    status, items = {}, []
    def run(j):
        name, fn = j
        for attempt in range(2):
            try: return name, fn(), None
            except Exception as e: err = f"{type(e).__name__}: {str(e)[:80]}"
            time.sleep(1)
        return name, [], err
    with ThreadPoolExecutor(8) as ex:
        for name, r, err in ex.map(run, jobs):
            status[name] = {"n": len(r), "err": err}; items += r
    seen, uniq = set(), []
    for i in items:
        k = (i["url"] or i["title"]).split("#")[0]
        if k in seen: continue
        seen.add(k); uniq.append(i)
    with open(os.path.join(OUT, "items.jsonl"), "w") as f:
        for i in uniq: f.write(json.dumps(i, ensure_ascii=False) + "\n")
    json.dump(status, open(os.path.join(OUT, "status.json"), "w"), ensure_ascii=False, indent=1)
    ok = sum(1 for v in status.values() if not v["err"])
    print(f"{len(uniq)} unique items; {ok}/{len(status)} sources ok")
    for k, v in status.items():
        if v["err"]: print("  FAIL", k, v["err"])

if __name__ == "__main__": main()
