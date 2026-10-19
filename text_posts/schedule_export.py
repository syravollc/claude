#!/usr/bin/env python3
"""Make scheduler-ready CSVs from the text posts. Does NOT post anywhere.
  python3 schedule_export.py 2026-11-02          (start date, a Monday works best)
Writes: schedule_singles.csv (one row per post) and schedule_threads.csv (one row per thread part).
Posting days: Mon / Tue / Thu / Fri at 10:00 local time. Edit DAYS/TIME below to change.
Upload to a free scheduler that accepts CSV (check Buffer, Metricool, etc. for the exact format) or copy rows in by hand.
Always review each post first. Check each platform's rules on automation and AI labels."""
import csv, datetime as dt, os, sys, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import build_threads as bt
DAYS = [0, 1, 3, 4]; TIME = "10:00"
start = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today()
start -= dt.timedelta(days=start.weekday())
with open(os.path.join(HERE, "schedule_singles.csv"), "w", newline="") as f1, open(os.path.join(HERE, "schedule_threads.csv"), "w", newline="") as f2:
    w1 = csv.writer(f1); w2 = csv.writer(f2)
    w1.writerow(["week", "post", "date", "time", "text", "chars", "notes"]); w2.writerow(["week", "post", "date", "time", "part", "text", "chars"])
    for wk in sorted(bt.W):
        for i, p in enumerate(bt.W[wk][2]):
            d = start + dt.timedelta(weeks=wk - 1, days=DAYS[i]); single = bt.SINGLES[wk][i]
            w1.writerow([wk, i + 1, d.isoformat(), TIME, single, len(single), p.get("note", "")])
            for k, part in enumerate(bt.thread(p), 1): w2.writerow([wk, i + 1, d.isoformat(), TIME, k, part, len(part)])
print("wrote schedule_singles.csv and schedule_threads.csv starting week of", start)
