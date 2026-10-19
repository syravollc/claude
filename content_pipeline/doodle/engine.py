"""Chalk-doodle animation engine (free: Python + skia-python + numpy + ffmpeg).
Hand-wobbled lines that draw themselves on, handwritten text, stick figure, orange accents, chalk scratch sound.
Everything is a function of scene progress p in [0,1], so animation automatically stretches to the narration length."""
import math, os, random, subprocess, wave
import numpy as np, skia
W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
CHALK = skia.Color(244, 244, 240); ORANGE = skia.Color(255, 140, 60); DIM = skia.Color(190, 190, 186)
TF = skia.Typeface.MakeFromFile(os.path.join(HERE, "fonts", "PatrickHand-Regular.ttf"))
TFB = skia.Typeface.MakeFromFile(os.path.join(HERE, "fonts", "Kalam-Bold.ttf"))
def clamp(x): return max(0.0, min(1.0, x))
def seg(p, a, b): return clamp((p - a) / (b - a)) if b > a else float(p >= a)
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)

class Board:
    def __init__(self):
        self.surface = skia.Surface(W, H); self.c = self.surface.getCanvas(); self.seed = 1; self.active = False
        rng = np.random.default_rng(7); bg = np.full((H, W, 4), (12, 12, 13, 255), dtype=np.uint8)
        yy, xx = np.mgrid[0:H, 0:W]; vig = 1 - 0.35 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / 2
        bg[..., :3] = (bg[..., :3] * vig[..., None]).astype(np.uint8)
        for _ in range(900): x, y = rng.integers(0, W), rng.integers(0, H); bg[y:y + 2, x:x + 2, :3] = rng.integers(28, 55)
        self.bg = skia.Image.fromarray(bg, colorType=skia.kRGBA_8888_ColorType)
    def begin(self, t):
        self.seed = int(t * 10) + 1; self.active = False; self.c.drawImage(self.bg, 0, 0)
    def paint(self, color, width, seed_off=0, seglen=16, dev=2.4):
        p = skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=width, StrokeCap=skia.Paint.kRound_Cap, StrokeJoin=skia.Paint.kRound_Join, Color=color)
        p.setPathEffect(skia.DiscretePathEffect.Make(seglen, dev, self.seed * 7 + seed_off)); return p
    def stroke(self, path, prog=1.0, color=CHALK, width=7):
        if prog <= 0: return
        if prog < 1:
            self.active = True; pm = skia.PathMeasure(path, False); dst = skia.Path(); pm.getSegment(0, pm.getLength() * prog, dst, True); path = dst
        self.c.drawPath(path, self.paint(color, width)); self.c.drawPath(path, self.paint(color & 0xB0FFFFFF if False else skia.Color(color_r(color), color_g(color), color_b(color), 90), width * .55, seed_off=3))
    def line(self, x1, y1, x2, y2, prog=1.0, **k):
        p = skia.Path(); p.moveTo(x1, y1); p.lineTo(x2, y2); self.stroke(p, prog, **k)
    def curve(self, x1, y1, cx, cy, x2, y2, prog=1.0, **k):
        p = skia.Path(); p.moveTo(x1, y1); p.quadTo(cx, cy, x2, y2); self.stroke(p, prog, **k)
    def circle(self, cx, cy, r, prog=1.0, **k):
        p = skia.Path(); p.moveTo(cx, cy - r)
        for i in range(1, 49): a = -math.pi / 2 + i / 48 * 2 * math.pi * 1.03; p.lineTo(cx + r * math.cos(a), cy + r * math.sin(a) * (1 + .02 * math.sin(i / 7)))
        self.stroke(p, prog, **k)
    def rect(self, x, y, w, h, prog=1.0, **k):
        p = skia.Path(); p.moveTo(x, y); [p.lineTo(*pt) for pt in ((x + w, y), (x + w, y + h), (x, y + h), (x - 3, y - 3))]; self.stroke(p, prog, **k)
    def arrow(self, x1, y1, x2, y2, prog=1.0, color=ORANGE, width=8):
        self.line(x1, y1, x2, y2, seg(prog, 0, .8), color=color, width=width)
        if prog > .8:
            a = math.atan2(y2 - y1, x2 - x1); q = seg(prog, .8, 1)
            for s in (-1, 1): self.line(x2, y2, x2 - 42 * q * math.cos(a + s * .5), y2 - 42 * q * math.sin(a + s * .5), color=color, width=width)
    def write(self, s, cx, y, size, prog=1.0, color=CHALK, bold=False, align="center"):
        if prog <= 0: return
        f = skia.Font(TFB if bold else TF, size); w = f.measureText(s); x = cx - w / 2 if align == "center" else cx
        rnd = random.Random(self.seed); c = self.c; c.save()
        if prog < 1: self.active = True; c.clipRect(skia.Rect(x - 10, y - size * 1.1, x + w * ease(prog) + 4, y + size * .5))
        p = skia.Paint(AntiAlias=True, Color=color); c.drawString(s, x + rnd.uniform(-1.2, 1.2), y + rnd.uniform(-1.2, 1.2), f, p); c.restore()
    def figure(self, x, y, s, prog=1.0, pose="stand", t=0.0, flip=1):
        """Stick figure with a smile. y = feet. pose: stand | wave | point | think | shrug"""
        hip = (x, y - 150 * s); neck = (x, y - 270 * s); head = (x, y - 318 * s); r = 44 * s
        self.circle(*head, r, seg(prog, 0, .25), width=7)
        e = seg(prog, .2, .3)
        if e > 0:
            for dx in (-14, 14): self.line(x + dx * s * flip, head[1] - 8 * s, x + dx * s * flip, head[1] - 4 * s, width=9)
            self.curve(x - 20 * s, head[1] + 14 * s, x, head[1] + 34 * s, x + 20 * s, head[1] + 14 * s, width=5)
        self.line(*neck, *hip, seg(prog, .25, .45))
        sh = (x, y - 245 * s); w = math.sin(t * 7) * 0.35
        arms = {"stand": ((-0.5, 1.0), (0.5, 1.0)), "wave": ((-0.5, 1.0), (1.9 + w, 1.0)), "point": ((-0.5, 1.0), (1.35 * flip, 1.15)),
                "think": ((-0.5, 1.0), (2.5, .75)), "shrug": ((-1.7, .8), (1.7, .8))}[pose]
        for k, (ang, ln) in enumerate(arms):
            ang = ang * (flip if k == 1 and pose in ("stand", "wave", "think") else 1)
            ex, ey = sh[0] + math.sin(ang) * 105 * s * ln, sh[1] + math.cos(ang) * 105 * s * ln * (1 if abs(ang) < 1.57 else -1 if False else 1)
            if pose == "wave" and k == 1: ex, ey = sh[0] + math.sin(ang) * 120 * s, sh[1] - abs(math.cos(ang)) * 100 * s
            hx, hy = ex + math.sin(ang) * 55 * s * .6, ey + (55 * s * .6 if abs(ang) < 1.2 else -20 * s)
            self.curve(*sh, (sh[0] + ex) / 2, (sh[1] + ey) / 2 + 12 * s, hx, hy, seg(prog, .45, .7))
        sway = math.sin(t * 2.2) * 4 * s
        self.line(*hip, x - 55 * s + sway, y, seg(prog, .7, .85)); self.line(*hip, x + 55 * s + sway, y, seg(prog, .78, .93))
    def frame_bytes(self):
        return self.surface.makeImageSnapshot().tobytes()

def color_r(c): return (c >> 16) & 255
def color_g(c): return (c >> 8) & 255
def color_b(c): return c & 255

def chalk_audio(active_flags, out_wav):
    """Soft chalk-scratch noise, loud only while something is being drawn."""
    sr = 44100; n = int(len(active_flags) / FPS * sr); env = np.repeat(np.array(active_flags, dtype=float), int(sr / FPS))[:n]
    env = np.pad(env, (0, max(0, n - len(env))))
    k = np.ones(900) / 900; env = np.convolve(env, k, mode="same")
    rng = np.random.default_rng(3); noise = rng.standard_normal(n); hp = np.diff(noise, prepend=0); lp = np.convolve(hp, np.ones(3) / 3, mode="same")
    x = lp * env * 0.07
    with wave.open(out_wav, "wb") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr); wf.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())
