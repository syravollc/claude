#!/usr/bin/env python3
"""Livelier chalk-doodle example (original artwork and script). Usage: python3 example_v2.py out.mp4 [--voice] [--frame SECONDS out.png]"""
import asyncio, math, os, re, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from engine2 import *
FF = os.environ.get("FFMPEG", "ffmpeg")
SCENES = [(5.5, "What does a homeschool day actually look like? For me, it started at nine.", ["What does a homeschool day", "actually look like?"]),
          (7.0, "There are twenty-four hours in a day. My school day was about five of them: nine to around two.", ["24 hours in a day.", "My school day: about 5 of them."]),
          (8.5, "The rest of the day was free for other school activities, and things I was interested in. Like a trip to the park.", ["The rest was free for activities", "and things I was interested in."]),
          (5.5, "But free time doesn't plan itself. I had to learn to plan it.", ["Free time doesn't plan itself."]),
          (5.0, "If you'd like a simple weekly planner, it's in my bio.", ["Want a simple weekly planner?", "It's in my bio."])]
def caption(b, lines, p):
    for i, ln in enumerate(lines): b.write(ln, 540, 1745 + i * 52, 46, seg(p, .02 + .04 * i, .14 + .04 * i), color=DIM)
def title(b, s, p, y=330, size=112, a=0.0, c=.2):
    b.push(540, y, out_back(seg(p, a, a + .12)) * .25 + .75 if p > a else .75); b.write(s, 540, y, size, seg(p, a, a + c), bold=True); b.pop()
def spark(b, cx, cy, p, t, n=6, r1=26, r2=60):
    for i in range(n):
        a = i * 2 * math.pi / n + t * 1.5; q = seg(p, 0, .5) * (1 - seg(p, .75, 1)); b.line(cx + r1 * math.cos(a), cy + r1 * math.sin(a), cx + (r1 + (r2 - r1) * q) * math.cos(a), cy + (r1 + (r2 - r1) * q) * math.sin(a), 1, color=ORANGE, width=6) if q > 0 else None
def s1(b, p, t):
    b.cam(1 + .08 * p, 0, 40 * p, 0, t)
    fx = lerp(-200, 470, ease(seg(p, 0, .3))); pose = "run" if p < .3 else "wave"
    title(b, "A homeschool day", p, 330, 118, 0.08, .22); b.curve(250, 400, 540, 435, 830, 392, seg(p, .32, .45), color=ORANGE, width=8)
    spark(b, 880, 300, seg(p, .35, .7), t); spark(b, 190, 300, seg(p, .4, .75), t + 1)
    b.figure2(fx, 1560, 1.6, t, pose, 1.0, talk=p > .3)
    q = seg(p, .42, .6)
    if q > 0:
        b.push(810, 880, out_back(q)); b.circle(810, 880, 120, seg(q, 0, .7))
        h = lerp(rad(90), rad(270), ease(seg(p, .55, .85))); b.line(810, 880, 810 + 70 * math.cos(h - math.pi / 2 + math.pi), 880 + 70 * math.sin(h - math.pi / 2 + math.pi), 1, width=8)
        b.line(810, 880, 810, 880 - 92, seg(q, .6, 1), width=6); b.pop()
    b.push(810, 1100, out_back(seg(p, .8, .95)) if p > .8 else 0.01); b.write("9:00", 810, 1100, 90, 1, color=ORANGE, bold=True); b.pop()
    b.endcam()
def s2(b, p, t):
    cx, cy, r = 540, 880, 300; z = 1 + .12 * seg(p, .55, 1); b.cam(z, 60 * seg(p, .55, 1), 120 * seg(p, .55, 1), 0, t)
    title(b, "24 hours", p, 360, 116, 0, .15)
    q = seg(p, .05, .22); b.push(cx, cy, out_back(q) if q > 0 else .01); b.circle(cx, cy, r, seg(q, 0, .8)); b.pop()
    b.write("midnight", cx, cy - r - 24, 40, seg(p, .2, .28), color=DIM)
    hr = 14 * ease(seg(p, .22, .62)); ang = lambda h: math.radians(-90 + 360 * h / 24)
    if hr > 0:
        a1, a2 = ang(9), ang(hr) if hr > 9 else ang(9)
        if hr > 9:
            wedge = skia.Path(); wedge.moveTo(cx, cy)
            for i in range(0, 41): a = a1 + (a2 - a1) * i / 40; wedge.lineTo(cx + r * math.cos(a), cy + r * math.sin(a))
            wedge.close(); b.c.save(); b.c.clipPath(wedge, doAntiAlias=True)
            for k in range(26):
                x0 = cx - r + k * 26; b.line(x0, cy + r, x0 + 2 * r, cy - r, 1, color=ORANGE, width=5)
            b.c.restore(); b.line(cx, cy, cx + r * math.cos(a1), cy + r * math.sin(a1), 1)
        b.line(cx, cy, cx + r * .94 * math.cos(ang(hr)), cy + r * .94 * math.sin(ang(hr)), 1, color=ORANGE, width=11); b.circle(cx, cy, 14, 1, color=ORANGE, width=10)
    for h, lab in ((9, "9am"), (14, "2pm")):
        if hr >= h - .1:
            a = ang(h); k = out_back(seg(hr, h - .1, h + .4)); b.push(cx + (r + 75) * math.cos(a), cy + (r + 75) * math.sin(a)); b.write(lab, cx + (r + 75) * math.cos(a), cy + (r + 75) * math.sin(a) + 16, 56, 1, bold=True); b.pop()
    bw = math.sin(t * 9) * 8 * seg(p, .66, 1)
    b.arrow(660, 1370 + bw, 590, 1100 + bw, seg(p, .64, .76)); b.push(640, 1430, out_back(seg(p, .68, .8)) if p > .68 else .01); b.write("school: 9 to ~2", 640, 1430, 62, 1, color=ORANGE, bold=True); b.pop()
    fx = lerp(1350, 940, ease(seg(p, .25, .5))); b.figure2(fx, 1650, 1.05, t, "run" if p < .5 else "point", 1.0, flip=-1, talk=p > .5)
    b.endcam()
def s3(b, p, t):
    b.cam(1, 0, 0, 0, t); title(b, "The rest: free", p, 300, 108, 0, .12)
    gy = 1500; b.line(0, gy, W, gy, seg(p, 0, .1), width=6)
    fx = lerp(-120, 1220, seg(p, .04, .96)); b.figure2(fx, gy, 1.35, t, "walk", 1.0, talk=True)
    cy = 800; items = [(210, "ideas I was curious about"), (470, "activities"), (730, "a trip to the park"), (940, "fresh air")]
    def pp(i): return seg((fx - (items[i][0] - 190)) / 150.0, 0, 1)
    def drop(q): return (1 - bounce(q)) * -260
    x = items[0][0]; q = pp(0)
    if q > 0: b.push(x, cy, 1, dy=drop(q)); b.rect(x - 85, cy - 65, 170, 130, seg(q, 0, .5)); b.line(x, cy - 65, x, cy + 65, seg(q, .3, .7)); b.write("curious ideas", x, cy + 130, 40, seg(q, .5, 1), color=DIM); b.pop()
    x = items[1][0]; q = pp(1)
    if q > 0:
        b.push(x, cy, 1, dy=drop(q)); b.circle(x, cy, 75, seg(q, 0, .5))
        for k, (dx, dy) in enumerate(((-30, -20), (10, -34), (36, 6), (-8, 30))): b.circle(x + dx, cy + dy, 12, seg(q, .4 + .1 * k, 1), color=ORANGE, width=6)
        b.write("activities", x, cy + 130, 40, seg(q, .5, 1), color=DIM); b.pop()
    x = items[2][0]; q = pp(2)
    if q > 0:
        sw = math.sin(t * 3) * 7; b.push(x, cy, 1, dy=drop(q)); b.line(x, cy + 110, x, cy - 10, seg(q, 0, .4)); b.circle(x + sw, cy - 60, 80, seg(q, .2, .8)); b.write("the park", x, cy + 160, 40, seg(q, .5, 1), color=DIM); b.pop()
    x = items[3][0]; q = pp(3)
    if q > 0:
        b.push(x, cy, 1, dy=drop(q)); b.circle(x, cy, 52, seg(q, 0, .5), color=ORANGE)
        for i in range(8):
            a = i * math.pi / 4 + t * 1.2; b.line(x + 78 * math.cos(a), cy + 78 * math.sin(a), x + 112 * math.cos(a), cy + 112 * math.sin(a), seg(q, .3, .9), color=ORANGE, width=6)
        b.write("fresh air", x, cy + 160, 40, seg(q, .5, 1), color=DIM); b.pop()
    b.endcam()
def s4(b, p, t):
    shake = 6 * max(0, 1 - ((p * 5.5 - 0) % 1)) * seg(p, .62, .95)
    b.cam(1, 0, 0, shake, t); title(b, "Free time needs a plan", p, 320, 98, 0, .15)
    x0, y0, cw, ch = 190, 520, 175, 160; k = 0
    for r in range(3):
        for c in range(4):
            q = seg(p, .02 + .028 * k, .16 + .028 * k); k += 1
            if q > 0: cx, cy = x0 + c * cw + 80, y0 + r * ch + 70; b.push(cx, cy, out_back(q)); b.rect(x0 + c * cw, y0 + r * ch, cw - 14, ch - 14, seg(q, 0, .8)); b.pop()
    fx = lerp(-150, 310, ease(seg(p, .05, .35))); b.figure2(fx, 1600, 1.25, t, "walk" if p < .35 else "think", 1.0, talk=p > .3)
    q = seg(p, .38, .5)
    if q > 0: b.push(480, 1220, out_back(q)); b.write("?", 480 + math.sin(t * 6) * 6, 1250, 110, 1, color=ORANGE, bold=True); b.pop()
    q = seg(p, .52, .62)
    if q > 0:
        b.push(560, 1150, out_back(q)); b.circle(560, 1150, 48, seg(q, 0, .7), color=ORANGE)
        for i in range(7): a = -math.pi / 2 + (i - 3) * .45; b.line(560 + 70 * math.cos(a), 1150 + 70 * math.sin(a), 560 + 110 * math.cos(a), 1150 + 110 * math.sin(a), seg(q, .5, 1), color=ORANGE, width=6)
        b.pop()
    for i, (r, c) in enumerate(((0, 1), (1, 0), (1, 2), (2, 3), (0, 3), (2, 1))):
        q = seg(p, .62 + .06 * i, .7 + .06 * i)
        if q > 0:
            cx, cy = x0 + c * cw + 80, y0 + r * ch + 70; b.push(cx, cy, lerp(2.2, 1.0, ease(q)))
            b.line(cx - 28, cy, cx - 8, cy + 24, seg(q, 0, .5), color=ORANGE, width=10); b.line(cx - 8, cy + 24, cx + 34, cy - 30, seg(q, .5, 1), color=ORANGE, width=10); b.pop()
    b.endcam()
def s5(b, p, t):
    b.cam(1.08 - .08 * p, 0, 0, 0, t); title(b, "Weekly planner", p, 320, 108, 0, .15)
    up = (1 - out_back(seg(p, .05, .3))) * 600; b.push(540, 900, 1, dy=up); b.rect(260, 520, 560, 760, 1)
    for i in range(6):
        y = 640 + i * 100; q = seg(p, .25 + .07 * i, .35 + .07 * i); b.rect(300, y - 28, 44, 44, 1); b.line(370, y + 12, 780, y + 12, 1, width=5, color=DIM)
        if q > 0:
            b.push(322, y - 6, out_back(q) * 1.0); b.line(306, y - 4, 320, y + 10, seg(q, 0, .5), color=ORANGE, width=9); b.line(320, y + 10, 344, y - 30, seg(q, .5, 1), color=ORANGE, width=9); b.pop()
    b.pop()
    b.figure2(170, 1660, 1.15, t, "cheer", 1.0, talk=True)
    q = seg(p, .7, .85); pulse = 1 + math.sin(t * 8) * .04
    if q > 0:
        b.push(540, 1450, out_back(q) * pulse); b.write("link in bio", 540, 1460, 84, 1, color=ORANGE, bold=True); b.curve(300, 1500, 540, 1535, 780, 1498, seg(q, .3, 1), color=ORANGE, width=8); b.pop()
        bw = math.sin(t * 9) * 10; b.arrow(900, 1290 + bw, 820, 1380 + bw, 1)
    b.endcam()
FUN = [s1, s2, s3, s4, s5]
def voice(durs, tmp):
    import edge_tts
    out = []
    for i, (_, narr, _) in enumerate(SCENES):
        mp3 = os.path.join(tmp, f"v{i}.mp3"); asyncio.run(edge_tts.Communicate(narr, "en-US-AriaNeural").save(mp3)); out.append(mp3)
        m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", subprocess.run([FF, "-i", mp3], capture_output=True, text=True).stderr); durs.append(int(m[2]) * 60 + float(m[3]) + .5)
    return out
def render_frame(b, t, durs, bounds):
    i = max(k for k in range(len(durs)) if bounds[k] <= t or k == 0); p = clamp((t - bounds[i]) / durs[i])
    b.begin(t); b.dust(t); FUN[i](b, p, t)
    tr = .35 / durs[i]
    if p > 1 - tr and i < len(durs) - 1: b.erase((p - (1 - tr)) / tr)
    caption(b, SCENES[i][2], p)
if __name__ == "__main__":
    tmp = tempfile.mkdtemp(); durs = [s[0] for s in SCENES]; vp = None
    if "--voice" in sys.argv: durs = []; vp = voice(durs, tmp)
    bounds = [sum(durs[:i]) for i in range(len(durs) + 1)]; b = Board2()
    if "--frame" in sys.argv:
        k = sys.argv.index("--frame"); render_frame(b, float(sys.argv[k + 1]), durs, bounds); b.surface.makeImageSnapshot().save(sys.argv[k + 2], skia.kPNG); sys.exit()
    out = sys.argv[1]; total = sum(durs); wav = os.path.join(tmp, "chalk.wav"); tmpv = os.path.join(tmp, "video.mp4"); active = []
    pv = subprocess.Popen([FF, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", tmpv], stdin=subprocess.PIPE)
    for n in range(int(total * FPS)):
        render_frame(b, n / FPS, durs, bounds); active.append(1 if b.active else 0); pv.stdin.write(b.frame_bytes())
    pv.stdin.close(); pv.wait(); chalk_audio(active, wav); base = [FF, "-y", "-loglevel", "error", "-i", tmpv, "-i", wav]
    if vp:
        padded = []
        for k, pth in enumerate(vp):
            pp = os.path.join(tmp, f"vp{k}.wav"); subprocess.run([FF, "-y", "-loglevel", "error", "-i", pth, "-af", f"apad=whole_dur={durs[k]}", "-ar", "44100", "-ac", "1", pp], check=True); padded.append(pp)
        lst = os.path.join(tmp, "v.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in padded)); joined = os.path.join(tmp, "voice.wav")
        subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, joined], check=True)
        subprocess.run(base + ["-i", joined, "-filter_complex", "[1:a]volume=0.6[a1];[a1][2:a]amix=inputs=2:duration=first:normalize=0[a]", "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", out], check=True)
    else: subprocess.run(base + ["-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-shortest", out], check=True)
    print("wrote", out, f"({total:.1f}s)")
