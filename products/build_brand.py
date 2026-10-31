import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "brand"); FONTS = os.path.join(HERE, "fonts")
PW = os.environ.get("PW_PATH") or subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip() + "/playwright"
CREAM, TERRA, NAVY, SAGE, GOLD, INK = "#FBF5EA", "#C4572D", "#1F3864", "#5F8A6B", "#E9B44C", "#2B2622"
FONTCSS = f"""@font-face{{font-family:'Lora';src:url('file://{FONTS}/Lora.ttf');font-weight:400 700}}
@font-face{{font-family:'Nunito';src:url('file://{FONTS}/Nunito.ttf');font-weight:300 800}}
@font-face{{font-family:'Hand';src:url('file://{FONTS}/PatrickHand-Regular.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}}"""
def icon(size=200, bg=True, ring=False):
    """A sprout under a warm sun: growth at its own pace. viewBox 200x200."""
    b = ""
    if bg: b += f'<rect x="4" y="4" width="192" height="192" rx="44" fill="{CREAM}" stroke="{INK}" stroke-width="5"/>'
    b += f'<circle cx="100" cy="82" r="48" fill="{GOLD}" opacity=".9" stroke="{INK}" stroke-width="4.5"/>'
    b += f'<path d="M100 150 C100 128 100 112 100 92" stroke="{INK}" stroke-width="13" fill="none" stroke-linecap="round"/><path d="M100 150 C100 128 100 112 100 92" stroke="{SAGE}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    b += f'<path d="M100 112 C70 112 54 90 54 90 C84 82 100 94 100 112Z" fill="{SAGE}" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>'
    b += f'<path d="M100 96 C128 96 146 72 146 72 C116 64 100 78 100 96Z" fill="#7DB188" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>'
    b += f'<path d="M58 156 Q100 132 142 156 Z" fill="#B98E5C" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>'
    b += f'<path d="M36 162 H164" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 200 200">{b}</svg>'
def wave(w, h, color="#E9D8BE"):
    return f'<svg style="position:absolute;left:0;bottom:0;width:{w}px;height:{h}px" viewBox="0 0 1000 120" preserveAspectRatio="none"><path d="M0 60 Q180 10 350 55 T700 50 T1000 40 V120 H0Z" fill="{color}" opacity=".7"/><path d="M0 85 Q230 45 440 85 T1000 75 V120 H0Z" fill="{color}"/></svg>'
def shot(name, w, h, body, scale=2, transparent=False, bg=CREAM):
    html = f"<!doctype html><meta charset=utf-8><style>{FONTCSS}body{{width:{w}px;height:{h}px;background:{'transparent' if transparent else bg};position:relative;overflow:hidden;font-family:'Nunito',sans-serif;color:{INK}}}</style>{body}"
    hp = os.path.join(OUT, f"_{name}.html"); open(hp, "w").write(html)
    js = f"const {{chromium}}=require('{PW}');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{w},height:{h}}},deviceScaleFactor:{scale}}});await p.goto('file://{hp}');await p.waitForTimeout(400);await p.screenshot({{path:'{os.path.join(OUT, name)}.png',omitBackground:{str(transparent).lower()}}});await b.close();}})();"
    jp = os.path.join(OUT, "_s.js"); open(jp, "w").write(js); subprocess.run(["node", jp], check=True); os.remove(hp)
def lockup_h(scale=1.0, dark=False):
    c = "#fff" if dark else NAVY
    return (f'<div style="display:flex;align-items:center;gap:{26*scale}px">{icon(int(150*scale))}<div><div style="font:700 {64*scale}px/1.05 Lora,serif;color:{c}">Early, Not Rushed</div>'
            f'<div style="font:{34*scale}px Hand;color:{TERRA};margin-top:{6*scale}px">learning that fits</div></div></div>')
if __name__ == "__main__":
    open(os.path.join(OUT, "logo_icon.svg"), "w").write(icon(1000))
    shot("logo_icon_1000", 500, 500, f'<div style="position:absolute;inset:50px">{icon(400)}</div>', scale=2)
    shot("logo_icon_transparent", 500, 500, f'<div style="position:absolute;inset:50px">{icon(400, bg=False)}</div>', scale=2, transparent=True)
    shot("logo_horizontal", 1100, 300, f'<div style="position:absolute;left:60px;top:70px">{lockup_h()}</div>', scale=2)
    shot("logo_stacked", 700, 700, f'<div style="text-align:center;padding-top:60px">{icon(280)}<div style="font:700 70px/1.05 Lora,serif;color:{NAVY};margin-top:30px">Early, Not Rushed</div><div style="font:42px Hand;color:{TERRA};margin-top:8px">learning that fits</div></div>', scale=2)
    # Etsy shop icon (square), social profile
    shot("etsy_shop_icon_500", 500, 500, f'<div style="position:absolute;inset:60px">{icon(380)}</div>', scale=1)
    shot("social_profile_1080", 540, 540, f'<div style="position:absolute;inset:70px">{icon(400)}</div>', scale=2)
    # Etsy banner 3360x840 (1680x420 css @2x); keep key content centered/safe
    shot("etsy_banner_3360x840", 1680, 420,
         f'{wave(1680, 130)}<div style="position:absolute;left:0;right:0;top:0;bottom:0;display:flex;align-items:center;justify-content:center;gap:90px"><div>{lockup_h(1.25)}</div><div style="max-width:420px;border-left:5px solid {GOLD};padding-left:28px"><div style="font:700 30px/1.2 Lora,serif;color:{INK}">Printable planners, checklists and guides</div><div style="font:26px Hand;color:{TERRA};margin-top:10px">from a former homeschooler</div></div></div>', scale=2)
    shot("etsy_mini_banner_1200x300", 1200, 300, f'{wave(1200, 90)}<div style="position:absolute;left:0;right:0;top:0;bottom:30px;display:flex;align-items:center;justify-content:center">{lockup_h(0.95)}</div>', scale=1)
    # social cover 1500x500
    shot("social_cover_1500x500", 1500, 500, f'{wave(1500, 120)}<div style="position:absolute;left:0;right:0;top:0;bottom:40px;display:flex;align-items:center;justify-content:center;gap:70px"><div>{lockup_h(1.15)}</div><div style="max-width:420px;font:700 28px/1.25 Lora,serif;color:{INK}">Finished high school at 13 and college at 17. Fit before speed.</div></div>', scale=1)
    os.remove(os.path.join(OUT, "_s.js")); print("ok")
