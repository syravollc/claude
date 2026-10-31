"""Etsy listing images (4:3, 2000x1500) from the product pages. Run after the product HTML files exist."""
import os, subprocess, json, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ETSY = os.path.join(HERE, "etsy"); FONTS = os.path.join(HERE, "fonts")
PW = os.environ.get("PW_PATH") or subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip() + "/playwright"
env = dict(os.environ, PW_PATH=PW)
P = {
 "planner": dict(cap=['Year at a Glance', 'Weekly Planner', 'Monthly Check-In', 'Reset Plan'], file="planner", title="The Family Planner", tag="a planner that bends to your child", pages="7", badge="PRINTABLE PDF", price="$6-12",
   inc=["Year at a Glance", "Weekly Planner", "Monthly Check-In (learner + parent)", "Records Tracker", "College Questions Checklist", "Reset Plan", "Cream and print-friendly versions"], prev=[1, 2, 3, 6]),
 "readiness": dict(cap=['The 10-Question Check', 'Pace, options and results', 'Conversation Guide', 'Slow-Down Signals'], file="readiness", title="The Readiness Bundle", tag="is this the right fit, and how will we know?", pages="8", badge="PRINTABLE PDF", price="$6-12",
   inc=["10-Question Readiness Check", "What your answers suggest", "Parent + learner Conversation Guide", "Monthly Check-In", "Slow-Down Signals", "Cream and print-friendly versions"], prev=[2, 3, 4, 6]),
 "early_college": dict(cap=['How I did it', 'Ready for college?', 'Questions for the college', 'Start small'], file="early_college", title="The Early College Questions Checklist", tag="ask before you commit", pages="7", badge="PRINTABLE PDF", price="$6-12",
   inc=["My route (associate at 15, bachelor's at 17)", "Is your child ready for college classes?", "9 questions to ask the college", "A start-small plan", "College tracker + records checklist", "Cream and print-friendly versions"], prev=[1, 2, 3, 4]),
 "starter": dict(cap=['My first year', "What worked and what didn't", 'Plan your days', 'Find community'], file="starter", title="The First-Year Starter Pack", tag="your first year, a little easier", pages="13", badge="PRINTABLE PDF", price="$12-19",
   inc=["My first year, honestly", "What worked / what didn't", "Plan your days + community tracker", "The feedback talk", "Five first-year principles", "Planner pages: year, week, month, reset", "Cream and print-friendly versions"], prev=[2, 3, 4, 5]),
 "guide": dict(cap=['Why this guide exists', 'My story, honestly', 'Mapping the route', 'Early college'], file="guide", title="Early, Not Rushed: The Guide", tag="a guide to flexible and accelerated homeschooling", pages="28", badge="PDF GUIDE", price="$19-25",
   inc=["11 chapters from the student's side", "Ready or pushed? Readiness vs pressure", "Mapping the route, avoiding gaps", "Records, transcripts and early college", "Social life and being young on campus", "Tools and worksheets in every chapter"], prev=[3, 4, 10, 16]),
}
CSS = f"""@font-face{{font-family:'Lora';src:url('file://{FONTS}/Lora.ttf');font-weight:400 700}}
@font-face{{font-family:'Nunito';src:url('file://{FONTS}/Nunito.ttf');font-weight:300 800}}
@font-face{{font-family:'Hand';src:url('file://{FONTS}/PatrickHand-Regular.ttf')}}
*{{box-sizing:border-box;margin:0;padding:0}}body{{width:1000px;height:750px;background:#FBF5EA;font-family:'Nunito',sans-serif;color:#2B2622;position:relative;overflow:hidden}}
.terra{{color:#C4572D}}.hand{{font-family:'Hand'}}.serif{{font-family:'Lora',serif}}
.pg{{position:absolute;border-radius:10px;box-shadow:0 10px 30px rgba(60,40,20,.28);border:1px solid #D9CDB8;background:#fff;overflow:hidden}}
.pg img{{width:100%;display:block}}
.badge{{display:inline-block;background:#1F3864;color:#fff;border-radius:999px;padding:8px 22px;font-size:20px;letter-spacing:.06em}}
.wave{{position:absolute;left:0;bottom:0;width:1000px;height:120px}}
h1{{font-family:'Lora',serif;font-weight:700;line-height:1.1}}
"""
WAVE = '<svg class="wave" viewBox="0 0 1000 120" preserveAspectRatio="none"><path d="M0 60 Q180 10 350 55 T700 50 T1000 40 V120 H0Z" fill="#E9D8BE" opacity=".7"/><path d="M0 85 Q230 45 440 85 T1000 75 V120 H0Z" fill="#E9D8BE"/></svg>'
def wrap(body): return f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{body}"
def imgs(key, idxs): return [os.path.join(ETSY, key, "pages", f"{key}-{i:02d}.png") for i in idxs]
def image1(m, key):
    a = imgs(key, [0] + m["prev"][:2])
    return wrap(f'{WAVE}<div style="position:absolute;left:60px;top:90px;width:430px"><div class="hand terra" style="font-size:32px">{m["tag"]}</div><h1 style="font-size:56px;margin:10px 0 24px">{m["title"]}</h1><span class="badge" style="font-size:16px;padding:8px 18px">{m["badge"]} · INSTANT DOWNLOAD</span><p style="margin-top:22px;font-size:20px;color:#6B625A">{m["pages"]} pages · by Fabian Capre</p><p style="margin-top:6px;font-size:18px;color:#6B625A">By a former homeschooler: high school at 13, bachelor\'s at 17</p></div>'
        f'<div class="pg" style="left:600px;top:70px;width:290px;transform:rotate(7deg)"><img src="file://{a[2]}"></div><div class="pg" style="left:560px;top:140px;width:290px;transform:rotate(-5deg)"><img src="file://{a[1]}"></div><div class="pg" style="left:640px;top:200px;width:300px;transform:rotate(2deg)"><img src="file://{a[0]}"></div>')
def image2(m, key):
    li = "".join(f'<li style="margin:12px 0;display:flex;gap:14px;align-items:flex-start"><span style="color:#C4572D;font-size:28px;line-height:1">✓</span><span>{x}</span></li>' for x in m["inc"])
    return wrap(f'{WAVE}<div style="position:absolute;left:70px;top:60px;right:70px"><div class="hand terra" style="font-size:34px">what\'s inside</div><h1 style="font-size:50px;margin:6px 0 22px">{m["title"]}</h1><ul style="list-style:none;font-size:28px;line-height:1.3;max-width:620px">{li}</ul></div><div class="pg" style="left:700px;top:230px;width:230px;transform:rotate(5deg)"><img src="file://{imgs(key,[0])[0]}"></div>')
def image3(m, key):
    ims = imgs(key, m["prev"][:3]); out = ""
    for i, p in enumerate(ims):
        out += f'<div class="pg" style="left:{35+i*315}px;top:150px;width:290px"><img src="file://{p}"></div><div class="hand" style="position:absolute;left:{35+i*315}px;top:545px;width:290px;text-align:center;font-size:26px;color:#1F3864">{m["cap"][i]}</div>'
    return wrap(f'{WAVE}<div style="position:absolute;left:40px;top:36px"><div class="hand terra" style="font-size:32px">a peek inside</div><h1 style="font-size:44px">Real pages, clean and simple</h1></div>{out}<div style="position:absolute;left:40px;bottom:70px;font-size:20px;color:#6B625A">Screen version on cream paper · print version on white to save ink</div>')
def image4(m, key):
    steps = [("1", "Buy it", "Checkout on Etsy."), ("2", "Download", "Your files are in Purchases on Etsy (no shipping, nothing arrives in the mail)."), ("3", "Use it", "Open on any device, or print as many copies as you need for your own family.")]
    cards = "".join(f'<div style="flex:1;background:#fff;border:2px solid #D9CDB8;border-radius:18px;padding:28px 24px"><div class="serif terra" style="font-size:52px;font-weight:700">{n}</div><div class="hand" style="font-size:34px;color:#1F3864;margin:4px 0 8px">{t}</div><div style="font-size:21px;color:#6B625A;line-height:1.35">{d}</div></div>' for n, t, d in steps)
    return wrap(f'{WAVE}<div style="position:absolute;left:60px;top:60px;right:60px"><div class="hand terra" style="font-size:34px">how it works</div><h1 style="font-size:50px;margin:6px 0 34px">Instant digital download</h1><div style="display:flex;gap:22px">{cards}</div><p style="margin-top:30px;font-size:21px;color:#6B625A">Digital product: PDF, US Letter (8.5 x 11 in). No physical item will be shipped. For personal use only.</p></div>')
def image5(m, key):
    return wrap(f'{WAVE}<div style="position:absolute;left:70px;top:60px;width:560px"><div class="hand terra" style="font-size:34px">from someone who lived it</div><h1 style="font-size:46px;margin:6px 0 20px">Built from a real homeschool journey</h1><p style="font-size:24px;line-height:1.45">I left in-person school in 3rd grade, finished high school at 13, earned my associate degree at 15 and my bachelor\'s at 17. This is what worked, what didn\'t, and what I\'d do differently.</p><p style="margin-top:22px;font-size:26px;font-weight:700;color:#1F3864">Fabian Capre</p><p style="margin-top:20px;font-size:17px;color:#6B625A">Not educational, psychological, medical or legal advice. Every child is different.</p></div><div class="pg" style="left:690px;top:120px;width:250px;transform:rotate(4deg)"><img src="file://{imgs(key,[0])[0]}"></div>')
def shot(html_path, out_png):
    js = f"""const {{ chromium }} = require('{PW}');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1000,height:750}},deviceScaleFactor:2}});await p.goto('file://{html_path}');await p.waitForTimeout(400);await p.screenshot({{path:'{out_png}'}});await b.close();}})();"""
    tmp = os.path.join(ETSY, "_s.js"); open(tmp, "w").write(js); subprocess.run(["node", tmp], check=True)
if __name__ == "__main__":
    for key, m in P.items():
        os.makedirs(os.path.join(ETSY, key, "pages"), exist_ok=True)
        subprocess.run(["node", os.path.join(HERE, "shot.js"), os.path.join(HERE, m["file"] + ".html"), os.path.join(ETSY, key, "pages"), key, "1.3"], check=True, env=env)
        for n, fn in enumerate([image1, image2, image3, image4, image5], 1):
            hp = os.path.join(ETSY, key, f"_img{n}.html"); open(hp, "w").write(fn(m, key)); shot(hp, os.path.join(ETSY, key, f"{key}_listing_{n}.png")); os.remove(hp)
        print("done", key)
    os.remove(os.path.join(ETSY, "_s.js"))
