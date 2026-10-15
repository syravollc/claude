#!/usr/bin/env python3
"""Auto-edit a talking-head recording into a vertical short. Runs on YOUR computer.

  python3 edit_video.py raw.mp4 out.mp4 [--srt captions.srt] [--min-silence 0.45] [--threshold -35]

What it does (all automatic):
  1. finds silences/pauses and cuts them (tight "jump-cut" pacing, keeps a small pad)
  2. crops/scales to 1080x1920 (9:16)
  3. normalises loudness
  4. burns captions if --srt is given, or auto-generates them when faster-whisper is installed
Needs ffmpeg on PATH (or set FFMPEG=/path/to/ffmpeg). Captions auto-generation: pip install faster-whisper.
It does not add music, B-roll or effects. Review the output before posting.
"""
import argparse, os, re, subprocess, sys, tempfile
FF = os.environ.get("FFMPEG", "ffmpeg")

def run(cmd, capture=False):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 and not capture: sys.exit("ffmpeg failed:\n" + r.stderr[-1500:])
    return r

def duration(path):
    r = run([FF, "-i", path], capture=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])

def keep_segments(path, thr, min_sil, pad):
    r = run([FF, "-i", path, "-af", f"silencedetect=noise={thr}dB:d={min_sil}", "-f", "null", "-"], capture=True)
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    total, segs, t = duration(path), [], 0.0
    for s, e in zip(starts, ends + [total] * (len(starts) - len(ends))):
        if s - t > 0.15: segs.append((max(0, t - 0), min(total, s + pad)))
        t = max(0, e - pad)
    if total - t > 0.15: segs.append((t, total))
    return segs or [(0, total)]

def cut(src, dst, segs):
    expr = "+".join(f"between(t,{a:.3f},{b:.3f})" for a, b in segs)
    vf = (f"select='{expr}',setpts=N/FRAME_RATE/TB,scale=1080:1920:force_original_aspect_ratio=increase,"
          f"crop=1080:1920,setsar=1")
    af = f"aselect='{expr}',asetpts=N/SR/TB,loudnorm=I=-16:TP=-1.5:LRA=11"
    run([FF, "-y", "-i", src, "-vf", vf, "-af", af, "-r", "30", "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "medium",
         "-crf", "20", "-c:a", "aac", "-b:a", "160k", dst])

def auto_srt(video, srt):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return False
    segs, _ = WhisperModel("small", compute_type="int8").transcribe(video)
    def ts(x): h, m, s = int(x // 3600), int(x % 3600 // 60), x % 60; return f"{h:02}:{m:02}:{s:06.3f}".replace(".", ",")
    with open(srt, "w") as f:
        for i, s in enumerate(segs, 1): f.write(f"{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n\n")
    return True

def burn(src, srt, dst):
    style = "FontName=Arial,FontSize=14,Bold=1,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,BorderStyle=1,Outline=2,Alignment=2,MarginV=180"
    safe = srt.replace("\\", "/").replace(":", "\\:")
    run([FF, "-y", "-i", src, "-vf", f"subtitles='{safe}':force_style='{style}'", "-pix_fmt", "yuv420p", "-c:a", "copy", dst])

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("src"); p.add_argument("dst")
    p.add_argument("--srt"); p.add_argument("--min-silence", type=float, default=0.45)
    p.add_argument("--threshold", type=float, default=-35); p.add_argument("--pad", type=float, default=0.08)
    a = p.parse_args()
    segs = keep_segments(a.src, a.threshold, a.min_silence, a.pad)
    kept = sum(b - x for x, b in segs); print(f"keeping {kept:.1f}s of {duration(a.src):.1f}s in {len(segs)} segments")
    tmp = tempfile.mkdtemp(); stage = os.path.join(tmp, "cut.mp4"); cut(a.src, stage, segs)
    srt = a.srt
    if not srt:
        srt = os.path.join(tmp, "auto.srt")
        if not auto_srt(stage, srt): srt = None; print("no captions (install faster-whisper or pass --srt)")
    if srt: burn(stage, srt, a.dst)
    else: os.replace(stage, a.dst)
    print("wrote", a.dst)
