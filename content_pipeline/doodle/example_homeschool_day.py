#!/usr/bin/env python3
"""Chalk-doodle explainer example (original artwork and script).
  python3 example_homeschool_day.py out.mp4 [--voice]      (--voice needs `pip install edge-tts` + internet)
Animation is a function of scene progress, so it stretches to match the narration length automatically."""
import asyncio, math, os, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine import *
FF = os.environ.get("FFMPEG", "ffmpeg")
SCENES = [  # (estimated seconds, narration, caption lines)
    (6.5, "What does a homeschool day actually look like? For me, it started at nine.", ["What does a homeschool day", "actually look like?"]),
    (8.0, "There are twenty-four hours in a day. My school day was about five of them: nine to around two.", ["24 hours in a day.", "My school day: about 5 of them."]),
    (10.0, "The rest of the day was free for other school activities, and things I was interested in. Like a trip to the park.", ["The rest was free for activities", "and things I was interested in."]),
    (6.0, "But free time doesn't plan itself. I had to learn to plan it.", ["Free time doesn't plan itself."]),
    (5.5, "If you'd like a simple weekly planner, it's in my bio.", ["Want a simple weekly planner?", "It's in my bio."])]
def caption(b, lines, p):
    for i, ln in enumerate(lines): b.write(ln, 540, 1745 + i * 52, 46, seg(p, .02 + .05 * i, .2 + .05 * i), color=DIM)
def clockdoodle(b, cx, cy, r, p, hour_hand_deg=270):
    b.circle(cx, cy, r, seg(p, 0, .6)); a = math.radians(hour_hand_deg)
    b.line(cx, cy, cx + r * .55 * math.cos(a), cy + r * .55 * math.sin(a), seg(p, .6, .8), width=8); b.line(cx, cy, cx, cy - r * .78, seg(p, .7, .9), width=6)
def s1(b, p, t):
    b.write("A homeschool day", 540, 360, 118, seg(p, 0, .3), bold=True)
    b.curve(260, 400, 540, 430, 820, 395, seg(p, .3, .45), color=ORANGE, width=8)
    b.figure(400, 1560, 1.55, seg(p, .1, .5), "wave" if p > .5 else "stand", t)
    clockdoodle(b, 800, 900, 120, seg(p, .55, .85)); b.write("9:00", 800, 1120, 84, seg(p, .85, 1), color=ORANGE, bold=True)
def s2(b, p, t):
    cx, cy, r = 540, 880, 300
    b.write("24 hours", 540, 370, 112, seg(p, 0, .15), bold=True)
    b.circle(cx, cy, r, seg(p, .08, .3))
    a1, a2 = math.radians(45), math.radians(120)
    for a in (a1, a2): b.line(cx, cy, cx + r * math.cos(a), cy + r * math.sin(a), seg(p, .3, .42))
    b.write("midnight", cx, cy - r - 24, 40, seg(p, .35, .45), color=DIM)
    for ang, lab in ((45, "9am"), (120, "2pm")):
        a = math.radians(ang); b.write(lab, cx + (r + 70) * math.cos(a), cy + (r + 70) * math.sin(a) + 14, 52, seg(p, .42, .52))
    h = seg(p, .5, .72)
    if h > 0:
        wedge = skia.Path(); wedge.moveTo(cx, cy)
        for i in range(0, 31): a = a1 + (a2 - a1) * i / 30; wedge.lineTo(cx + r * math.cos(a), cy + r * math.sin(a))
        wedge.close(); b.c.save(); b.c.clipPath(wedge, doAntiAlias=True); n = 18
        for k in range(int(n * h) + 1): x0 = cx - r + k * 36; b.line(x0, cy + r, x0 + 2 * r, cy - r, seg(h * n - k, 0, 1), color=ORANGE, width=5)
        b.c.restore()
    b.arrow(640, 1340, 580, 1090, seg(p, .65, .85)); b.write("school: 9 to ~2", 640, 1405, 58, seg(p, .72, .88), color=ORANGE, bold=True)
    b.write("the rest of my day", 250, 1300, 46, seg(p, .85, 1), color=DIM)
    b.figure(930, 1640, 0.9, seg(p, .2, .6), "point", t, flip=-1)
def s3(b, p, t):
    b.write("The rest: free", 540, 360, 112, seg(p, 0, .15), bold=True)
    # book
    x, y = 330, 700; q = seg(p, .15, .35); b.rect(x - 90, y - 70, 180, 140, q); b.line(x, y - 70, x, y + 70, seg(q, .6, 1)); b.write("ideas I was curious about", x, y + 140, 40, seg(p, .3, .4), color=DIM)
    # palette
    x, y = 750, 700; q = seg(p, .3, .5); b.circle(x, y, 80, q); [b.circle(x + dx, y + dy, 12, seg(q, .6, 1), color=ORANGE, width=6) for dx, dy in ((-30, -20), (10, -35), (35, 5), (-10, 30))]; b.write("activities", x, y + 140, 40, seg(p, .45, .55), color=DIM)
    # tree / park
    x, y = 330, 1190; q = seg(p, .45, .7); b.line(x, y + 80, x, y - 10, seg(q, 0, .4)); b.circle(x, y - 60, 70, seg(q, .3, 1)); b.line(x - 120, y + 80, x + 120, y + 80, seg(q, 0, .5)); b.write("a trip to the park", x, y + 150, 40, seg(p, .65, .75), color=DIM)
    # sun
    x, y = 750, 1190; q = seg(p, .6, .85); b.circle(x, y, 55, q, color=ORANGE)
    for i in range(8): a = i * math.pi / 4; b.line(x + 80 * math.cos(a), y + 80 * math.sin(a), x + 115 * math.cos(a), y + 115 * math.sin(a), seg(q, .5, 1), color=ORANGE, width=6)
    b.write("fresh air", x, y + 150, 40, seg(p, .8, .9), color=DIM)
def s4(b, p, t):
    b.write("Free time needs a plan", 540, 340, 100, seg(p, 0, .25), bold=True)
    x0, y0, cw, ch = 190, 560, 175, 160
    for r in range(3):
        for c in range(4): b.rect(x0 + c * cw, y0 + r * ch, cw - 14, ch - 14, seg(p, .1 + .035 * (r * 4 + c), .2 + .035 * (r * 4 + c)))
    for i, (r, c) in enumerate(((0, 1), (1, 0), (1, 2), (2, 3), (0, 3))):
        q = seg(p, .55 + .08 * i, .65 + .08 * i); cx, cy = x0 + c * cw + 80, y0 + r * ch + 70
        b.line(cx - 28, cy, cx - 8, cy + 24, seg(q, 0, .5), color=ORANGE, width=9); b.line(cx - 8, cy + 24, cx + 34, cy - 30, seg(q, .5, 1), color=ORANGE, width=9)
    b.figure(300, 1640, 1.15, seg(p, .15, .5), "think", t)
    b.write("?", 480, 1290, 90, seg(p, .5, .6), color=ORANGE, bold=True)
def s5(b, p, t):
    b.write("Weekly planner", 540, 340, 110, seg(p, 0, .2), bold=True)
    b.rect(260, 520, 560, 760, seg(p, .1, .35))
    for i in range(6):
        y = 640 + i * 100; q = seg(p, .3 + .07 * i, .4 + .07 * i); b.rect(300, y - 28, 44, 44, q); b.line(370, y + 12, 780, y + 12, q, width=5, color=DIM)
        b.line(306, y - 4, 320, y + 10, seg(q, .5, .8), color=ORANGE, width=8); b.line(320, y + 10, 344, y - 30, seg(q, .7, 1), color=ORANGE, width=8)
    b.write("link in bio", 540, 1450, 80, seg(p, .7, .9), color=ORANGE, bold=True); b.circle(540, 1425, 250, seg(p, .85, 1), color=ORANGE, width=6)
    b.figure(190, 1660, 1.0, seg(p, .2, .55), "wave", t)
FUN = [s1, s2, s3, s4, s5]
def voice(durs_out, tmp):
    import edge_tts
    paths = []
    for i, (_, narr, _) in enumerate(SCENES):
        mp3 = os.path.join(tmp, f"v{i}.mp3"); asyncio.run(edge_tts.Communicate(narr, "en-US-AriaNeural").save(mp3)); paths.append(mp3)
        r = subprocess.run([FF, "-i", mp3], capture_output=True, text=True); import re; m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
        durs_out.append(int(m[2]) * 60 + float(m[3]) + .5)
    return paths
if __name__ == "__main__":
    out = sys.argv[1]; tmp = tempfile.mkdtemp(); durs = [s[0] for s in SCENES]; vpaths = None
    if "--voice" in sys.argv:
        durs = []; vpaths = voice(durs, tmp)
    total = sum(durs); bounds = [sum(durs[:i]) for i in range(len(durs) + 1)]; b = Board(); active = []
    ffcmd = [FF, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"]
    wav = os.path.join(tmp, "chalk.wav")
    frames = int(total * FPS); tmpv = os.path.join(tmp, "video.mp4")
    pv = subprocess.Popen(ffcmd + ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", tmpv], stdin=subprocess.PIPE)
    for n in range(frames):
        t = n / FPS; i = max(k for k in range(len(durs)) if bounds[k] <= t or k == 0); p = (t - bounds[i]) / durs[i]
        b.begin(t); FUN[i](b, clamp(p), t); caption(b, SCENES[i][2], clamp(p)); active.append(1 if b.active else 0)
        pv.stdin.write(b.frame_bytes())
    pv.stdin.close(); pv.wait(); chalk_audio(active, wav)
    inputs = [FF, "-y", "-loglevel", "error", "-i", tmpv, "-i", wav]
    if vpaths:
        lst = os.path.join(tmp, "v.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in vpaths)); joined = os.path.join(tmp, "voice.mp3")
        # pad each clip to its scene length, then concat
        padded = []
        for k, pth in enumerate(vpaths):
            pp = os.path.join(tmp, f"vp{k}.wav"); subprocess.run([FF, "-y", "-loglevel", "error", "-i", pth, "-af", f"apad=whole_dur={durs[k]}", "-ar", "44100", "-ac", "1", pp], check=True); padded.append(pp)
        open(lst, "w").write("".join(f"file '{p}'\n" for p in padded)); subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, joined], check=True)
        subprocess.run(inputs + ["-i", joined, "-filter_complex", "[1:a]volume=0.6[a1];[a1][2:a]amix=inputs=2:duration=first:normalize=0[a]", "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", out], check=True)
    else:
        subprocess.run(inputs + ["-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-shortest", out], check=True)
    print("wrote", out, f"({total:.1f}s)")
