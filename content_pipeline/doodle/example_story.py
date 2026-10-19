#!/usr/bin/env python3
"""Hook video: 'I finished high school at 13' (original script, uses only facts the author gave).
  python3 example_story.py out.mp4 [--voice] [--frame SECONDS out.png]"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import example_v2 as ev
from engine2 import *
SCENES = [(4.2, "I finished high school at thirteen.", ["I finished high school", "at 13."]),
          (8.5, "I left school in third grade. High school done at thirteen. Associate degree at fifteen. Bachelor's degree at seventeen.", ["3rd grade: left school  ·  13: high school", "15: associate  ·  17: bachelor's"]),
          (5.0, "But finishing early was never the goal.", ["But finishing early", "was never the goal."]),
          (6.0, "What mattered was fit: learning built around me, at my pace.", ["What mattered was fit:", "learning built around me."]),
          (4.5, "Follow for what worked, and what was hard.", ["Follow for what worked,", "and what was hard."])]
def gradcap(b, x, y, s, rot=0.0, color=CHALK, prog=1.0):
    b.push(x, y, 1, rot=rot); pth = skia.Path(); pth.moveTo(x - 80 * s, y); [pth.lineTo(*q) for q in ((x, y - 34 * s), (x + 80 * s, y), (x, y + 34 * s), (x - 80 * s, y))]; b.stroke(pth, prog, color=color)
    b.curve(x - 45 * s, y + 18 * s, x, y + 62 * s, x + 45 * s, y + 18 * s, seg(prog, .4, 1), color=color); b.line(x + 60 * s, y + 6 * s, x + 60 * s, y + 52 * s, seg(prog, .6, 1), color=ORANGE, width=6); b.pop()
def s1(b, p, t):
    b.cam(1 + .1 * p, 0, 0, 5 * (1 - seg(p, .3, .5)) * seg(p, .25, .3), t)
    ev.title(b, "Finished high school", p, 330, 100, 0, .18); b.push(540, 470, out_back(seg(p, .15, .35)) if p > .15 else .01); b.write("at 13.", 540, 480, 150, 1, color=ORANGE, bold=True); b.pop()
    fx = lerp(1300, 540, ease(seg(p, 0, .3))); pose = "run" if p < .3 else "cheer"
    b.figure2(fx, 1560, 1.7, t, pose, 1.0, flip=-1 if p < .3 else 1, talk=p > .3)
    q = seg(p, .35, 1.0)
    if q > 0: gradcap(b, 540 + 80 * math.sin(q * 3), 1100 - 520 * math.sin(math.pi * min(q * 1.1, 1)), 1.6, rot=720 * q)
    ev.spark(b, 540, 520, seg(p, .45, .85), t, 8, 40, 90)
    b.endcam()
def s2(b, p, t):
    b.cam(1, 0, 0, 0, t); ev.title(b, "My timeline", p, 300, 100, 0, .12)
    stairs = [(170, 1450, "3rd grade", "left school"), (380, 1310, "age 13", "high school"), (590, 1170, "age 15", "associate"), (800, 1030, "age 17", "bachelor's")]
    fprog = seg(p, .08, .92); idx = fprog * 3.0; i = min(int(idx), 2); f = idx - i
    x0, y0 = stairs[i][0] + 45, stairs[i][1]; x1, y1 = stairs[i + 1][0] + 45, stairs[i + 1][1]
    jf = seg(f, .45, 1.0); fx = lerp(x0, x1, ease(seg(f, .3, 1.0))); fy = lerp(y0, y1, ease(seg(f, .3, 1.0))) - math.sin(math.pi * jf) * 110 if f > .3 else y0
    if p > .92: fx, fy = stairs[3][0] + 45, stairs[3][1]
    for k, (sx, sy, a, lab) in enumerate(stairs):
        q = seg(p, .02 + .2 * k, .12 + .2 * k)
        if q > 0:
            b.push(sx + 90, sy, out_back(q)); b.rect(sx, sy, 190, 600 - sy + 100 if False else 70, seg(q, 0, .8)); b.line(sx, sy + 70, sx, 1620, seg(q, .3, 1), width=5, color=DIM); b.pop()
            b.write(a, sx + 95, sy + 52, 40, seg(q, .4, 1), color=ORANGE, bold=True); b.write(lab, sx + 95, sy + 128, 38, seg(q, .6, 1), color=DIM)
    pose = "cheer" if (f > .85 and p < .95) or p > .95 else ("walk" if f < .3 or True else "idle"); b.figure2(fx, fy, 1.05, t, pose if jf < .9 else "cheer", 1.0, talk=True)
    q = seg(p, .88, 1)
    if q > 0: gradcap(b, 845, 520 - 16 * math.sin(t * 6), 1.1, rot=-8, color=ORANGE, prog=q)
    b.endcam()
def s3(b, p, t):
    b.cam(1, 0, 0, 0, t); b.push(540, 700, out_back(seg(p, 0, .2)) if p > 0 else .01); b.write("finishing early", 540, 700, 112, 1, bold=True); b.pop()
    x1 = 540 - 100 - 300; q = seg(p, .35, .6)
    b.line(160, 600, 920, 780, seg(q, 0, .5), color=ORANGE, width=14); b.line(920, 600, 160, 780, seg(q, .5, 1), color=ORANGE, width=14)
    b.push(540, 1000, out_back(seg(p, .55, .75)) if p > .55 else .01); b.write("≠ the goal", 540, 1010, 100, 1, color=ORANGE, bold=True); b.pop()
    b.figure2(540, 1640, 1.2, t, "shrug", seg(p, 0, .2) + .0 if p < .2 else 1.0, talk=True)
    b.endcam()
def s4(b, p, t):
    b.cam(1 + .08 * p, 0, 0, 0, t); ev.title(b, "What mattered:", p, 300, 96, 0, .15)
    b.push(540, 460, out_back(seg(p, .15, .35)) if p > .15 else .01); b.write("FIT", 540, 520, 190, 1, color=ORANGE, bold=True); b.pop()
    cx, cy = 540, 1280; hc = b.figure2(cx, 1500, 1.25, t, "idle", seg(p, .1, .3), talk=p > .3)
    for k, (kind) in enumerate(("book", "clock", "palette", "idea")):
        q = seg(p, .3 + .08 * k, .45 + .08 * k)
        if q <= 0: continue
        a = t * 1.1 + k * math.pi / 2; ox, oy = cx + 330 * math.cos(a) * out_back(q), cy - 20 + 140 * math.sin(a) * out_back(q) - 40; b.push(ox, oy, out_back(q))
        if kind == "book": b.rect(ox - 50, oy - 38, 100, 76, 1); b.line(ox, oy - 38, ox, oy + 38, 1)
        elif kind == "clock": b.circle(ox, oy, 46, 1); b.line(ox, oy, ox, oy - 30, 1, width=6); b.line(ox, oy, ox + 20, oy + 8, 1, width=6)
        elif kind == "palette": b.circle(ox, oy, 46, 1); b.circle(ox - 14, oy - 8, 9, 1, color=ORANGE, width=6); b.circle(ox + 12, oy + 10, 9, 1, color=ORANGE, width=6)
        else:
            b.circle(ox, oy, 34, 1, color=ORANGE); [b.line(ox + 48 * math.cos(-math.pi / 2 + (j - 2) * .5), oy + 48 * math.sin(-math.pi / 2 + (j - 2) * .5), ox + 70 * math.cos(-math.pi / 2 + (j - 2) * .5), oy + 70 * math.sin(-math.pi / 2 + (j - 2) * .5), 1, color=ORANGE, width=6) for j in range(5)]
        b.pop()
    b.endcam()
def s5(b, p, t):
    b.cam(1.06 - .06 * p, 0, 0, 0, t); b.push(540, 600, out_back(seg(p, 0, .25)) if p > 0 else .01); b.write("Follow", 540, 600, 170, 1, color=ORANGE, bold=True); b.pop()
    ev.title(b, "for what worked", p, 790, 84, .15, .2); ev.title(b, "and what was hard", p, 900, 84, .3, .2)
    b.figure2(540, 1560, 1.5, t, "wave", seg(p, 0, .3) if p < .3 else 1.0, talk=True)
    q = seg(p, .45, .6); bw = math.sin(t * 9) * 12
    if q > 0: b.arrow(900, 1290 + bw, 820, 1420 + bw, 1)
    ev.spark(b, 200, 1000, seg(p, .5, .95), t); ev.spark(b, 880, 1000, seg(p, .55, 1), t + 2)
    b.endcam()
ev.SCENES = SCENES; ev.FUN = [s1, s2, s3, s4, s5]
if __name__ == "__main__": ev.main()
