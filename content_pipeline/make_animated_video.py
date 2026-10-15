#!/usr/bin/env python3
"""Turn an ANIMATED storyboard into a finished vertical video, automatically. Runs on YOUR computer.

  python3 make_animated_video.py drafts/weeks_02_to_08.md "Week 2, Post 2" out.mp4 [--voice en-US-AriaNeural]

Reads the scene lines (SCENE n (Ns) | NARRATION | VISUAL | ON-SCREEN TEXT), then for each scene:
  1. draws a 1080x1920 branded card with the on-screen text and narration captions
  2. adds slow zoom motion
  3. adds a voiceover if `pip install edge-tts` works and you are online (otherwise silent)
Then joins scenes, normalises loudness and writes an MP4.
Needs: ffmpeg on PATH (or FFMPEG=/path), Pillow (pip install pillow).
Honest limits: this makes clean kinetic-text explainer videos. It does NOT draw illustrated characters;
the VISUAL column is a note for you if you want to add illustrations in Canva/CapCut afterwards.
Review every video before posting. Synthetic voices may need an AI label on some platforms.
"""
import argparse, asyncio, os, re, subprocess, sys, tempfile, textwrap
from PIL import Image, ImageDraw, ImageFont
FF = os.environ.get("FFMPEG", "ffmpeg"); W, H = 1080, 1920
PALETTE = [("#1F3864", "#FFFFFF"), ("#7A2E12", "#FFFFFF"), ("#2B5D4B", "#FFFFFF"), ("#4A3B6B", "#FFFFFF"), ("#C4572D", "#FFFFFF")]
FONTS = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
         "C:/Windows/Fonts/arialbd.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"]

def font(size):
    for f in FONTS:
        if os.path.exists(f): return ImageFont.truetype(f, size)
    return ImageFont.load_default()

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg failed:\n" + r.stderr[-1200:])
    return r

def parse(path, heading):
    txt = open(path).read()
    m = re.search(r"^## " + re.escape(heading) + r": ANIMATED.*?(?=^## |\Z)", txt, re.S | re.M)
    if not m: sys.exit(f"No animated post found for heading '{heading}'")
    block = m.group(0); hook = re.search(r"\*\*HOOK TEXT:\*\* (.*)", block)
    scenes = []
    for ln in block.splitlines():
        s = re.match(r"SCENE (\d+) \((\d+)s\) \| NARRATION: (.*?) \| VISUAL: (.*?) \| ON-SCREEN TEXT: (.*)", ln)
        if s: scenes.append(dict(n=int(s[1]), secs=float(s[2]), narr=s[3], visual=s[4], text=s[5]))
    if not scenes: sys.exit("No SCENE lines found")
    return (hook[1] if hook else ""), scenes

def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + ([cur] if cur else [])

def card(i, total, sc, hook, path):
    bg, fg = PALETTE[i % len(PALETTE)]
    im = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(im)
    if i == 0 and hook:
        f = font(54); y = 190
        for ln in wrap(d, hook.upper(), f, W - 200): d.text((100, y), ln, font=f, fill="#FFD9C9"); y += 70
    f = font(92); lines = wrap(d, sc["text"], f, W - 200); y = H // 2 - len(lines) * 62
    for ln in lines: d.text((W // 2, y), ln, font=f, fill=fg, anchor="ma"); y += 124
    fc = font(46); cl = wrap(d, sc["narr"], fc, W - 260)
    top = H - 300 - len(cl) * 62 - 40; box = shade(bg, 0.55)
    d.rounded_rectangle((60, top, W - 60, H - 260), 30, fill=box)
    y = top + 28
    for ln in cl: d.text((W // 2, y), ln, font=fc, fill="#FFFFFF", anchor="ma"); y += 62
    d.rectangle((100, H - 160, W - 100, H - 146), fill=shade(bg, 0.75))
    d.rectangle((100, H - 160, 100 + (W - 200) * (i + 1) // total, H - 146), fill="#FFFFFF")
    im.save(path)

def shade(hexcol, k):
    r, g, b = (int(hexcol[j:j + 2], 16) for j in (1, 3, 5))
    return (int(r * k), int(g * k), int(b * k))

def tts(text, voice, out):
    try:
        import edge_tts
        asyncio.run(edge_tts.Communicate(text, voice).save(out))
        return os.path.getsize(out) > 1000
    except Exception as e:
        print("  (no voiceover:", type(e).__name__, ")"); return False

def dur(path):
    r = subprocess.run([FF, "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3]) if m else 0

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("md"); p.add_argument("heading"); p.add_argument("out")
    p.add_argument("--voice", default="en-US-AriaNeural"); a = p.parse_args()
    hook, scenes = parse(a.md, a.heading); tmp = tempfile.mkdtemp(); clips = []
    for i, sc in enumerate(scenes):
        png, mp3, mp4 = (os.path.join(tmp, f"s{i}.{x}") for x in ("png", "mp3", "mp4"))
        card(i, len(scenes), sc, hook, png)
        has_audio = tts(sc["narr"], a.voice, mp3); secs = sc["secs"]
        if has_audio: secs = max(secs, dur(mp3) + 0.4)
        frames = int(secs * 30)
        vf = f"zoompan=z='min(zoom+0.0006,1.08)':d={frames}:s={W}x{H}:fps=30,format=yuv420p"
        cmd = [FF, "-y", "-loop", "1", "-i", png]
        cmd += ["-i", mp3] if has_audio else ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]
        cmd += ["-vf", vf, "-t", f"{secs:.2f}", "-c:v", "libx264", "-c:a", "aac", "-shortest", "-pix_fmt", "yuv420p", mp4]
        run(cmd); clips.append(mp4); print(f"scene {sc['n']}: {secs:.1f}s {'with voice' if has_audio else 'silent'}")
    lst = os.path.join(tmp, "list.txt"); open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
    run([FF, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:v", "libx264",
         "-c:a", "aac", "-pix_fmt", "yuv420p", a.out]); print("wrote", a.out)
