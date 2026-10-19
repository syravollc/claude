"""Livelier chalk-doodle engine: jointed character (walk/run/wave/point/think/cheer), camera, pop-ins, eraser transitions, dust."""
import math, random
from engine import *

def lerp(a, b, x): return a + (b - a) * x
def out_back(x):
    x = clamp(x); c1 = 1.70158; c3 = c1 + 1; return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2
def bounce(x):
    x = clamp(x); n1, d1 = 7.5625, 2.75
    if x < 1 / d1: return n1 * x * x
    if x < 2 / d1: x -= 1.5 / d1; return n1 * x * x + .75
    if x < 2.5 / d1: x -= 2.25 / d1; return n1 * x * x + .9375
    x -= 2.625 / d1; return n1 * x * x + .984375
def rad(d): return math.radians(d)

def pose_angles(pose, t):
    z = dict(tl=4, sl=4, tr=-4, sr=-4, ul=8, fl=14, ur=-8, fr=-2, lean=0, tilt=0, bob=0, jump=0)
    br = math.sin(t * 2.4)
    if pose == "idle": z.update(ul=8 + 4 * br, ur=-8 - 4 * br, bob=2 * br)
    elif pose in ("walk", "run"):
        k = 1.0 if pose == "walk" else 1.5; ph = t * (9.5 if pose == "walk" else 13)
        tr_ = 32 * k * math.sin(ph); tl_ = -tr_
        z.update(tr=tr_, tl=tl_, sr=tr_ - 28 * k * (1 + math.sin(ph + 1.0)), sl=tl_ - 28 * k * (1 + math.sin(ph + 1.0 + math.pi)),
                 ur=-tr_ * .9, ul=-tl_ * .9, lean=6 * k, bob=7 * k * abs(math.sin(ph)))
        z["fr"] = z["ur"] + 25; z["fl"] = z["ul"] + 25
    elif pose == "wave": z.update(ur=125, fr=125 + 32 * math.sin(t * 11), ul=8 + 4 * br, bob=3 * br, tilt=4)
    elif pose == "point": z.update(ur=88, fr=88, ul=8 + 4 * br, bob=2 * br, lean=4)
    elif pose == "think": z.update(ur=34, fr=158, ul=8, tilt=-8 + 3 * br, bob=2 * br)
    elif pose == "cheer":
        j = abs(math.sin(t * 6.5)); z.update(ur=135 + 10 * math.sin(t * 13), ul=-135 - 10 * math.sin(t * 13 + 1), fr=150, fl=-150, tl=10, tr=-10, sl=10, sr=-10, jump=34 * j, tilt=3)
    elif pose == "shrug": z.update(ur=52, ul=-52, fr=108, fl=-108, tilt=6 * br)
    return z

class Board2(Board):
    def push(self, cx, cy, sx=1.0, sy=None, rot=0.0, dx=0.0, dy=0.0):
        c = self.c; c.save(); c.translate(cx + dx, cy + dy); c.rotate(rot); c.scale(sx, sx if sy is None else sy); c.translate(-cx, -cy)
    def pop(self): self.c.restore()
    def cam(self, zoom=1.0, px=0.0, py=0.0, shake=0.0, t=0.0):
        c = self.c; c.save(); sx = math.sin(t * 53) * shake; sy = math.cos(t * 47) * shake
        c.translate(W / 2 + sx, H / 2 + sy); c.scale(zoom, zoom); c.translate(-W / 2 - px, -H / 2 - py)
    def endcam(self): self.c.restore()
    def dust(self, t):
        p = skia.Paint(AntiAlias=True, Color=skia.Color(220, 220, 215, 55)); rng = random.Random(11)
        for k in range(46):
            x0, y0, sx, sy, r = rng.uniform(0, W), rng.uniform(0, H), rng.uniform(-14, 14), rng.uniform(-22, -6), rng.uniform(1.5, 3.6)
            self.c.drawCircle((x0 + sx * t) % W, (y0 + sy * t) % H, r, p)
    def erase(self, e):
        """Scribble-erase the board: bg image clipped through thick zig-zag strokes."""
        if e <= 0: return
        path = skia.Path(); n = 9; path.moveTo(-100, 120)
        for i in range(n): path.lineTo(W + 100 if i % 2 == 0 else -100, 120 + (i + .5) * (H - 120) / n)
        pm = skia.PathMeasure(path, False); dst = skia.Path(); pm.getSegment(0, pm.getLength() * clamp(e), dst, True)
        pa = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=260, StrokeCap=skia.Paint.kRound_Cap, StrokeJoin=skia.Paint.kRound_Join)
        outline = skia.Path(); pa.getFillPath(dst, outline); self.c.save(); self.c.clipPath(outline, doAntiAlias=True); self.c.drawImage(self.bg, 0, 0); self.c.restore()
        self.active = True
    def figure2(self, x, y, s, t, pose="idle", prog=1.0, flip=1, talk=False, color=CHALK):
        a = pose_angles(pose, t); f = flip; lean = rad(a["lean"]); r = 42 * s
        hipx, hipy = x, y - 148 * s - a["bob"] * s - a["jump"] * s
        def pt(px, py, ang, ln): return (px + f * ln * math.sin(rad(ang)), py + ln * math.cos(rad(ang)))
        def limb(p0, a1, l1, a2, l2, pr):
            j = pt(*p0, a1, l1); e = pt(*j, a2, l2); path = skia.Path(); path.moveTo(*p0); path.lineTo(*j); path.lineTo(*e); self.stroke(path, pr, color=color); return e
        foot_r = limb((hipx, hipy), a["tr"], 76 * s, a["sr"], 76 * s, seg(prog, 0, .3)); foot_l = limb((hipx, hipy), a["tl"], 76 * s, a["sl"], 76 * s, seg(prog, 0, .3))
        for fx, fy in (foot_r, foot_l):
            if prog > .3: self.line(fx, fy, fx + f * 24 * s, fy, color=color, width=7)
        neck = (hipx + f * 125 * s * math.sin(lean), hipy - 125 * s * math.cos(lean)); self.line(hipx, hipy, *neck, seg(prog, .25, .45), color=color)
        sh = (hipx + f * 110 * s * math.sin(lean), hipy - 110 * s * math.cos(lean)); pr = seg(prog, .4, .65)
        wr = limb(sh, a["ur"], 62 * s, a["fr"], 58 * s, pr); wl = limb(sh, a["ul"], 62 * s, a["fl"], 58 * s, pr)
        if pr >= 1:
            for wx, wy in (wr, wl): self.circle(wx, wy, 9 * s, 1, width=6, color=color)
        hc = (neck[0] + f * (r + 6 * s) * math.sin(lean + rad(a["tilt"])), neck[1] - (r + 6 * s) * math.cos(lean + rad(a["tilt"]))); hp = seg(prog, .6, .85)
        self.circle(*hc, r, hp, color=color)
        if prog > .85:
            blink = (t % 3.3) < .13; ex = f * 9 * s
            for dx in (-15 * s, 15 * s):
                if blink: self.line(hc[0] + dx + ex - 6 * s, hc[1] - 6 * s, hc[0] + dx + ex + 6 * s, hc[1] - 6 * s, width=5, color=color)
                else: self.line(hc[0] + dx + ex, hc[1] - 12 * s, hc[0] + dx + ex, hc[1] - 4 * s, width=10, color=color)
            my = hc[1] + 16 * s
            if talk:
                o = 4 + 13 * abs(math.sin(t * 13)) * s; p2 = skia.Path(); p2.addOval(skia.Rect(hc[0] + ex - 11 * s, my - o / 2, hc[0] + ex + 11 * s, my + o / 2)); self.c.drawPath(p2, self.paint(color, 5, seed_off=5))
            else: self.curve(hc[0] + ex - 18 * s, my - 2 * s, hc[0] + ex, my + 18 * s, hc[0] + ex + 18 * s, my - 2 * s, width=5, color=color)
        return hc
