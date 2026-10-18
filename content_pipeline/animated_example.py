#!/usr/bin/env python3
"""Example: a fully code-drawn animated explainer (free tools only: Python + Pillow + ffmpeg).
Renders the 'A homeschool day: 9 to 2' storyboard with real animation (moving clock, walking character,
filling calendar). Usage: python3 animated_example.py out.mp4 [--frame N frame.png]
Silent by design here; add a voiceover with edge-tts on your own computer (see README)."""
import math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
W, H, FPS = 1080, 1920, 30
FF = os.environ.get("FFMPEG", "ffmpeg")
CREAM, NAVY, TERRA, GREEN, GOLD, SKY, INK = "#FBF5EA", "#1F3864", "#C4572D", "#2B5D4B", "#F2B544", "#CFE8F7", "#2B2622"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
_f = {}
def font(s):
    if s not in _f: _f[s] = ImageFont.truetype(FONT, s)
    return _f[s]
def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3
def lerp(a, b, x): return a + (b - a) * x
def hexrgb(h): return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
def mix(c1, c2, x): a, b = hexrgb(c1), hexrgb(c2); return tuple(int(lerp(p, q, x)) for p, q in zip(a, b))
def text(d, xy, s, size, color, anchor="mm", alpha=1.0, bg=CREAM):
    d.text(xy, s, font=font(size), fill=mix(bg, color, alpha) if isinstance(color, str) else color, anchor=anchor)
def wrap(d, s, size, width):
    out, cur = [], ""
    for w in s.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font(size)) <= width: cur = t
        else: out.append(cur); cur = w
    return out + ([cur] if cur else [])

def clock(d, cx, cy, r, hour, minute=0):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="white", outline=NAVY, width=int(r * .07))
    for i in range(12):
        a = math.radians(i * 30); d.line((cx + r * .82 * math.sin(a), cy - r * .82 * math.cos(a), cx + r * .93 * math.sin(a), cy - r * .93 * math.cos(a)), fill=NAVY, width=int(r * .04))
    ah = math.radians((hour % 12) * 30 + minute * .5); am = math.radians(minute * 6)
    d.line((cx, cy, cx + r * .5 * math.sin(ah), cy - r * .5 * math.cos(ah)), fill=NAVY, width=int(r * .08))
    d.line((cx, cy, cx + r * .75 * math.sin(am), cy - r * .75 * math.cos(am)), fill=TERRA, width=int(r * .05))
    d.ellipse((cx - r * .06, cy - r * .06, cx + r * .06, cy + r * .06), fill=NAVY)

def person(d, x, y, s, t, mode="stand", shirt=TERRA):
    sw = math.sin(t * 8) * (0.5 if mode == "walk" else 0)
    d.line((x, y - 60 * s, x - 22 * s + sw * 40 * s, y + 60 * s), fill=NAVY, width=int(16 * s))  # legs
    d.line((x, y - 60 * s, x + 22 * s - sw * 40 * s, y + 60 * s), fill=NAVY, width=int(16 * s))
    d.rounded_rectangle((x - 34 * s, y - 150 * s, x + 34 * s, y - 40 * s), int(18 * s), fill=shirt)  # torso
    d.line((x - 30 * s, y - 130 * s, x - 55 * s - sw * 30 * s, y - 70 * s), fill="#E8B58C", width=int(13 * s))  # arms
    d.line((x + 30 * s, y - 130 * s, x + 55 * s + sw * 30 * s, y - 70 * s), fill="#E8B58C", width=int(13 * s))
    d.ellipse((x - 32 * s, y - 220 * s, x + 32 * s, y - 156 * s), fill="#E8B58C")  # head
    d.pieslice((x - 34 * s, y - 226 * s, x + 34 * s, y - 170 * s), 180, 360, fill=INK)  # hair

def seated(d, x, y, s):
    d.rounded_rectangle((x - 34 * s, y - 150 * s, x + 34 * s, y - 20 * s), int(18 * s), fill=TERRA)
    d.line((x, y - 30 * s, x + 90 * s, y - 30 * s), fill=NAVY, width=int(16 * s)); d.line((x + 90 * s, y - 30 * s, x + 90 * s, y + 60 * s), fill=NAVY, width=int(16 * s))
    d.line((x + 20 * s, y - 120 * s, x + 95 * s, y - 80 * s), fill="#E8B58C", width=int(13 * s))
    d.ellipse((x - 32 * s, y - 220 * s, x + 32 * s, y - 156 * s), fill="#E8B58C"); d.pieslice((x - 34 * s, y - 226 * s, x + 34 * s, y - 170 * s), 180, 360, fill=INK)

def title(d, s, t, y=420, color=NAVY, bg=CREAM, size=104):
    p = ease(t / .6); lines = wrap(d, s, size, W - 160)
    for i, ln in enumerate(lines): text(d, (W // 2, y + i * (size + 14) + (1 - p) * 60), ln, size, color, alpha=p, bg=bg)

def scene1(d, t):  # clock at 9, desk and laptop
    title(d, "Start: 9:00", t)
    clock(d, 790, 760, 150 + math.sin(t * 3) * 3, 9)
    d.rectangle((120, 1230, 960, 1260), fill="#B07C4F"); d.rectangle((160, 1260, 200, 1500), fill="#B07C4F"); d.rectangle((880, 1260, 920, 1500), fill="#B07C4F")
    d.rounded_rectangle((420, 1090, 700, 1230), 12, fill=NAVY); d.rounded_rectangle((435, 1103, 685, 1217), 6, fill=mix(SKY, "#FFFFFF", .5)); d.polygon([(400, 1230), (720, 1230), (740, 1245), (380, 1245)], fill="#8890A0")
    seated(d, 260, 1230, 1.5)
    for i in range(3): d.rectangle((460, 1125 + i * 28, 460 + int(lerp(40, 190, ease((t - i * .4) / 1.2))), 1135 + i * 28), fill=TERRA)
def scene2(d, t, dur):  # hands sweep 9 -> 2
    p = ease(t / 4.2); hr = lerp(9, 14, p)
    title(d, "Done: around 2:00", t, y=300, size=92)
    clock(d, W // 2, 820, 230, hr)
    h = int(hr) % 12 or 12; m = int((hr % 1) * 60); text(d, (W // 2, 1120), f"{h}:{m:02d}", 90, NAVY)
    for i, item in enumerate(["Lectures", "Assignments", "Review", "Done!"]):
        a = ease((t - 1 - i * 1.0) / .4); y = 1230 + i * 66
        d.rounded_rectangle((250, y - 26, 290, y + 14), 8, outline=NAVY, width=5)
        if a > 0: d.line((256, y - 6, 268, y + 8), fill=GREEN, width=8); d.line((268, y + 8, 288, y - 22), fill=GREEN, width=8)
        text(d, (330, y - 6), item, 44, INK, anchor="lm", alpha=.35 + .65 * a)
def scene3(d, t):  # park, walking, floating icons
    d.rectangle((0, 0, W, 1250), fill=SKY); d.ellipse((780, 250, 960, 430), fill=GOLD); d.rectangle((0, 1250, W, H), fill="#7DBF7A"); d.polygon([(0, 1500), (W, 1380), (W, 1480), (0, 1640)], fill="#E7D6A7")
    for x in (180, 880): d.rectangle((x - 22, 1000, x + 22, 1250), fill="#7A5230"); d.ellipse((x - 120, 760, x + 120, 1040), fill="#3E8E54")
    title(d, "Free time", t, y=330, size=120, bg=SKY)
    person(d, lerp(120, 960, (t / 8) % 1.0), 1230, 1.9, t, "walk")
    for i, (lab, col) in enumerate([("BOOK", TERRA), ("ART", GOLD), ("PARK", GREEN)]):
        x = 270 + i * 270; y = 700 + math.sin(t * 2 + i) * 22; a = ease((t - .6 - i * .5) / .5)
        d.rounded_rectangle((x - 80, y - 60, x + 80, y + 60), 24, fill=mix(SKY, col, a)); text(d, (x, y), lab, 42, "#FFFFFF", alpha=a, bg=col)
def scene4(d, t):  # calendar fills
    title(d, "Plan the free time", t, y=300, size=84)
    x0, y0, cw, ch = 130, 520, 160, 200
    for c, day in enumerate(["M", "T", "W", "T", "F"]): text(d, (x0 + c * cw + cw // 2, y0 - 40), day, 44, NAVY)
    cols = [TERRA, GOLD, GREEN, NAVY, "#7B5EA7"]; n = 0
    for r in range(4):
        for c in range(5):
            x, y = x0 + c * cw, y0 + r * ch; d.rounded_rectangle((x + 4, y + 4, x + cw - 4, y + ch - 4), 16, fill="white", outline="#CFC6B8", width=3)
            if r >= 1 and (c + r) % 2 == 0:
                a = ease((t - .8 - n * .28) / .35); n += 1
                if a > 0: s = 1 - .5 * (1 - a); d.rounded_rectangle((x + 4 + (1 - s) * cw / 2, y + 4 + (1 - s) * ch / 2, x + cw - 4 - (1 - s) * cw / 2, y + ch - 4 - (1 - s) * ch / 2), 16, fill=cols[(c + r) % 5])
    text(d, (W // 2, 1480), "Blank space becomes a plan", 54, INK, alpha=ease((t - 3.5) / .5))
def scene5(d, t):  # planner page + CTA
    title(d, "Weekly planner", t, y=300, size=100)
    d.rounded_rectangle((250, 520, 830, 1300), 28, fill="white", outline=NAVY, width=6); d.rectangle((250, 520, 830, 600), fill=NAVY)
    text(d, (540, 560), "This week", 44, "#FFFFFF", bg=NAVY)
    for i in range(6):
        y = 660 + i * 100; d.line((300, y + 40, 780, y + 40), fill="#D9D2C5", width=3)
        a = ease((t - .5 - i * .35) / .3)
        d.rounded_rectangle((300, y - 8, 338, y + 30), 8, outline=NAVY, width=4)
        if a > 0: d.line((306, y + 10, 316, y + 22), fill=GREEN, width=7); d.line((316, y + 22, 334, y - 2), fill=GREEN, width=7)
    pulse = 1 + math.sin(t * 5) * .03; w = 300 * pulse
    d.rounded_rectangle((W // 2 - w, 1420, W // 2 + w, 1540), 60, fill=TERRA); text(d, (W // 2, 1480), "Link in bio", 56, "#FFFFFF", bg=TERRA)
SCENES = [(5, scene1, "My school day started at nine."),
          (7, scene2, "By around two, I was done."),
          (8, scene3, "The rest of the day was free for other school activities and things I was interested in."),
          (6, scene4, "That sounds easy. It takes a plan to use it well."),
          (5, scene5, "Want a simple weekly planner? Link in bio.")]
BGS = [CREAM, CREAM, SKY, CREAM, CREAM]
def frame(gt):
    t0 = 0
    for i, (dur, fn, cap) in enumerate(SCENES):
        if gt < t0 + dur or i == len(SCENES) - 1: break
        t0 += dur
    t = gt - t0
    im = Image.new("RGB", (W, H), BGS[i]); d = ImageDraw.Draw(im)
    if i == 0: text(d, (W // 2, 150), "A HOMESCHOOL DAY: 9 TO 2", 48, TERRA, alpha=ease(t / .5))
    fn(d, t, dur) if fn is scene2 else fn(d, t)
    lines = wrap(d, cap, 46, W - 260); top = H - 300 - len(lines) * 60 - 20; a = ease(t / .5)
    d.rounded_rectangle((60, top, W - 60, H - 250), 30, fill=mix(BGS[i], NAVY, .92 * a))
    for k, ln in enumerate(lines): text(d, (W // 2, top + 50 + k * 60), ln, 46, "#FFFFFF", alpha=a, bg=NAVY)
    d.rectangle((100, H - 160, W - 100, H - 146), fill="#D9D2C5"); d.rectangle((100, H - 160, 100 + (W - 200) * gt / 31, H - 146), fill=TERRA)
    return im
if __name__ == "__main__":
    if "--frame" in sys.argv:
        n = int(sys.argv[sys.argv.index("--frame") + 1]); frame(n / FPS).save(sys.argv[sys.argv.index("--frame") + 2]); sys.exit()
    out = sys.argv[1]
    p = subprocess.Popen([FF, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                          "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", "31", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-c:a", "aac", "-shortest", out], stdin=subprocess.PIPE)
    for n in range(31 * FPS): p.stdin.write(frame(n / FPS).tobytes())
    p.stdin.close(); p.wait(); print("wrote", out)
