#!/usr/bin/env python3
"""Draft -> review -> approve -> export. Nothing here posts anywhere.

Commands:
  generate [--week N] [--dry-run]   create drafts in queue/ (status=draft)
  review                            list drafts with check results
  approve ID [ID...]                mark drafts approved (human decision)
  reject ID [ID...]
  export --start YYYY-MM-DD         write approved drafts to export/schedule.csv
                                    for bulk upload to a scheduling tool

Needs for real generation: ANTHROPIC_API_KEY and CONTENT_MODEL (a model id).
The model only receives story_facts.md as personal facts; it is told to invent none.
"""
import argparse, csv, datetime as dt, json, os, re, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
QUEUE = HERE / "queue"; EXPORT = HERE / "export"
PLATFORMS = ["short_video", "short_video", "carousel_or_post", "short_video"]  # 4 posts a week
BANNED = [r"guarantee", r"\bcure\b", r"graduate (by|at) 1\d.*(you|your child) (can|will)", r"\bproven\b",
          r"100%", r"doctor|diagnos|therapy|medication", r"get rich|passive income"]
DISCLOSURE = "Drafted with AI, reviewed and edited by me."

def facts():
    t = (HERE / "story_facts.md").read_text()
    if "[FILL]" in t:
        sys.exit("story_facts.md still has [FILL] items. Fill them with true facts first.")
    return t

def call_model(prompt, system):
    key, model = os.environ.get("ANTHROPIC_API_KEY"), os.environ.get("CONTENT_MODEL")
    if not key or not model:
        sys.exit("Set ANTHROPIC_API_KEY and CONTENT_MODEL, or use --dry-run.")
    body = json.dumps({"model": model, "max_tokens": 1200, "system": system,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
        "x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)["content"][0]["text"]

SYSTEM = ("You write warm, personal, relatable content for homeschool parents and students, in the first person "
          "as the author. Use ONLY the personal facts provided. Never invent personal details, statistics, quotes, "
          "testimonials, or results. No guarantees or promised outcomes. No medical or mental-health advice. "
          "If a fact you need is missing, write [NEEDS FACT: ...] instead of guessing.")

def make_prompt(topic, fmt, facts_text):
    shapes = {"short_video": "A 30-45 second short-video script: hook line, 3-4 beats, closing line, then a caption with 3 hashtags.",
              "carousel_or_post": "A text post or 6-slide carousel: slide-by-slide text, then a caption."}
    return (f"Personal facts (only source of personal details):\n{facts_text}\n\nTopic: {topic['title']} "
            f"(angle: {topic['angle']}).\nWrite: {shapes[fmt]}\nEnd with a gentle invitation to get the free "
            f"readiness checklist (link added later). Keep it honest, mention trade-offs where relevant.")

def checks(text):
    flags = [f"banned phrase: {p}" for p in BANNED if re.search(p, text, re.I)]
    if "[NEEDS FACT" in text: flags.append("needs a fact from you")
    return flags

def load(): return {p.stem: json.loads(p.read_text()) for p in sorted(QUEUE.glob("*.json"))}
def save(d): (QUEUE / f"{d['id']}.json").write_text(json.dumps(d, indent=2))

def generate(a):
    QUEUE.mkdir(exist_ok=True)
    topics = json.loads((HERE / "topics.json").read_text())["topics"]
    ft = "(dry run)" if a.dry_run else facts()
    start = (a.week - 1) * 4
    for i, fmt in enumerate(PLATFORMS):
        topic = topics[(start + i) % len(topics)]
        did = f"w{a.week:02d}_{i+1}_{topic['id']}"
        text = (f"[DRY RUN placeholder for: {topic['title']}]" if a.dry_run
                else call_model(make_prompt(topic, fmt, ft), SYSTEM))
        save({"id": did, "week": a.week, "topic": topic["title"], "format": fmt,
              "text": text + f"\n\n{DISCLOSURE}", "flags": checks(text), "status": "draft"})
        print("drafted", did)

def review(_):
    for d in load().values():
        print(f"{d['id']:22} {d['status']:9} flags={d['flags'] or '-'}")

def setstatus(ids, status):
    q = load()
    for i in ids:
        if i not in q: sys.exit(f"unknown id {i}")
        if status == "approved" and q[i]["flags"]:
            sys.exit(f"{i} has flags {q[i]['flags']}; edit the draft and clear 'flags' yourself to approve.")
        q[i]["status"] = status; save(q[i]); print(i, status)

def export(a):
    EXPORT.mkdir(exist_ok=True)
    day = dt.date.fromisoformat(a.start); rows = []
    for d in load().values():
        if d["status"] == "approved":
            rows.append({"date": day.isoformat(), "time": "17:00", "format": d["format"], "text": d["text"]})
            day += dt.timedelta(days=2)
    with open(EXPORT / "schedule.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "time", "format", "text"]); w.writeheader(); w.writerows(rows)
    print(f"wrote {len(rows)} approved items to export/schedule.csv")

if __name__ == "__main__":
    p = argparse.ArgumentParser(); s = p.add_subparsers(dest="cmd", required=True)
    g = s.add_parser("generate"); g.add_argument("--week", type=int, default=1); g.add_argument("--dry-run", action="store_true")
    s.add_parser("review")
    for n in ("approve", "reject"): x = s.add_parser(n); x.add_argument("ids", nargs="+")
    e = s.add_parser("export"); e.add_argument("--start", required=True)
    a = p.parse_args()
    {"generate": generate, "review": review, "approve": lambda a: setstatus(a.ids, "approved"),
     "reject": lambda a: setstatus(a.ids, "rejected"), "export": export}[a.cmd](a)
