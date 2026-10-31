"""Shared design system for the product PDFs: cream pages, handwritten accents, flat SVG art, callouts."""
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
AUTHOR = "Fabian Capre"
BRAND = "Early, Not Rushed"
DISCLAIMER = ("General information from one person's experience. Not educational, psychological, medical or legal advice. "
              "Rules and options vary by state, district and college; check the official sources where you live.")

def css(print_mode=False):
    cream = "#FFFFFF" if print_mode else "#FBF5EA"
    sand = "#F4F0E8" if print_mode else "#F1E6D3"
    return f"""
@font-face{{font-family:'Lora';src:url('file://{FONTS}/Lora.ttf');font-weight:400 700}}
@font-face{{font-family:'Nunito';src:url('file://{FONTS}/Nunito.ttf');font-weight:300 800}}
@font-face{{font-family:'Hand';src:url('file://{FONTS}/PatrickHand-Regular.ttf')}}
:root{{--cream:{cream};--sand:{sand};--ink:#2B2622;--muted:#6B625A;--terra:#C4572D;--sage:#5F8A6B;--navy:#1F3864;--gold:#E9B44C;--line:#D9CDB8;--paper:#FFFFFF}}
@page{{size:8.5in 11in;margin:0}}
*{{box-sizing:border-box}}html,body{{margin:0;padding:0}}
body{{font:11.3pt/1.6 'Nunito',sans-serif;color:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.page{{width:8.5in;height:11in;padding:.75in .8in .85in;background:var(--cream);position:relative;overflow:hidden;page-break-after:always}}
.page:last-child{{page-break-after:auto}}
.run{{position:absolute;top:.38in;left:.8in;right:.8in;display:flex;justify-content:space-between;font:11pt 'Hand';color:var(--muted)}}
.foot{{position:absolute;bottom:.35in;left:.8in;right:.8in;display:flex;justify-content:space-between;font-size:7.6pt;color:var(--muted)}}
h1{{font:700 26pt/1.15 'Lora',serif;margin:.1in 0 .08in;color:var(--ink);padding-right:1.35in}}
h2{{font:700 16.5pt/1.2 'Lora',serif;margin:.22in 0 .06in;color:var(--navy)}}
h3{{font:700 11.5pt 'Nunito',sans-serif;margin:.14in 0 .03in;color:var(--terra)}}
p{{margin:.06in 0}}ul,ol{{margin:.05in 0 .05in .22in;padding:0}}li{{margin:.03in 0}}
.kicker{{font:15pt 'Hand';color:var(--terra);margin:0}}
.sub{{color:var(--muted);font-size:11pt;margin:.02in 0 .12in}}
.rule{{height:3px;width:.7in;background:var(--terra);border-radius:2px;margin:.08in 0 .14in}}
.box{{border-radius:12px;padding:.16in .2in;margin:.16in 0;page-break-inside:avoid}}
.story{{background:var(--sand);border-left:5px solid var(--terra)}}
.worked{{background:#E6EFE6;border-left:5px solid var(--sage)}}
.didnt{{background:#F4E1DA;border-left:5px solid #B5523A}}
.try{{background:#E3E8F2;border-left:5px solid var(--navy)}}
.plain{{background:var(--paper);border:1.5px solid var(--line)}}
.box .t{{font:14pt 'Hand';margin:0 0 2px}}
.story .t{{color:var(--terra)}}.worked .t{{color:var(--sage)}}.didnt .t{{color:#B5523A}}.try .t{{color:var(--navy)}}
.two{{display:flex;gap:.18in}}.two>*{{flex:1}}.three{{display:flex;gap:.14in}}.three>*{{flex:1}}
table{{border-collapse:collapse;width:100%;margin:.08in 0}}th,td{{border:1.5px solid var(--line);padding:7px 9px;vertical-align:top;font-size:9.8pt;text-align:left;background:var(--paper)}}
th{{background:var(--sand);font-weight:700}}table.tall td{{height:.7in}}
.ln{{border-bottom:1.5px solid var(--line);height:.27in}}
.fld{{margin:.1in 0}}.fld b{{font-size:9.6pt}}
.cb{{display:inline-block;width:.15in;height:.15in;border:1.6px solid var(--navy);border-radius:4px;margin-right:.08in;vertical-align:-2px;background:var(--paper)}}
.circ{{display:inline-block;width:.13in;height:.13in;border:1.6px solid var(--navy);border-radius:50%;margin:0 .05in 0 .15in;vertical-align:-2px;background:var(--paper)}}
.q{{display:flex;gap:.1in;padding:.065in 0;border-bottom:1px dashed var(--line);break-inside:avoid}}
.q .n{{font:700 12pt 'Lora';color:var(--terra);min-width:.28in}}.q .o{{font-size:9.4pt;color:var(--muted)}}
.fine{{font-size:8.2pt;color:var(--muted)}}
.quote{{font:italic 400 13.5pt/1.4 'Lora',serif;color:var(--navy);border-left:4px solid var(--gold);padding:.04in 0 .04in .16in;margin:.14in 0}}
.cover{{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:.9in}}
.cover h1{{font-size:38pt;margin:.1in 0;padding-right:0}}.cover .tag{{font:18pt 'Hand';color:var(--terra)}}
.cover .by{{font-size:12pt;color:var(--muted);margin-top:.22in}}
.pill{{display:inline-block;background:var(--navy);color:#fff;border-radius:999px;padding:.05in .2in;font-size:9.5pt;margin-top:.15in;letter-spacing:.04em}}
.hl{{background:linear-gradient(transparent 62%,rgba(233,180,76,.55) 62%)}}
@media print{{.page{{page-break-after:always}}}}
"""

# ---------- flat SVG art (all original) ----------
def svg(w, h, body, vb=None):
    vw, vh = vb if vb else (w, h)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {vw} {vh}">{body}</svg>'
T, N, S, G, K = "#C4572D", "#1F3864", "#5F8A6B", "#E9B44C", "#2B2622"

def art_stairs(W=520, H=300):
    w, h = 520, 300
    steps = [("3rd grade", "left school"), ("Age 13", "high school"), ("Age 15", "associate"), ("Age 17", "bachelor's")]
    b = ""
    for i, (a, l) in enumerate(steps):
        x = 20 + i * 120; y = h - 60 - i * 55
        b += f'<rect x="{x}" y="{y}" width="115" height="{h-y-20}" rx="8" fill="{["#E9D8BE","#EAC9B5","#C9DCCB","#C7D2E8"][i]}" stroke="{K}" stroke-width="2.5"/>'
        b += f'<text x="{x+57}" y="{y+28}" font-family="Hand" font-size="22" fill="{T}" text-anchor="middle">{a}</text><text x="{x+57}" y="{y+50}" font-family="Nunito" font-size="12.5" fill="{K}" text-anchor="middle">{l}</text>'
    x3 = 20 + 3 * 120 + 57; y3 = h - 60 - 3 * 55
    b += f'<circle cx="{x3}" cy="{y3-50}" r="16" fill="#F2C9A0" stroke="{K}" stroke-width="2.5"/><path d="M{x3} {y3-34} V{y3-8} M{x3} {y3-28} l-20 -12 M{x3} {y3-28} l20 -12" stroke="{K}" stroke-width="3" fill="none" stroke-linecap="round"/>'
    return svg(W, H, b, vb=(520, 300))

def art_wheel(size=300):
    cx = cy = size / 2; r = size / 2 - 30
    def pt(ang, rr): a = math.radians(-90 + ang); return cx + rr * math.cos(a), cy + rr * math.sin(a)
    a1, a2 = 135, 210; x1, y1 = pt(a1, r); x2, y2 = pt(a2, r)
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{K}" stroke-width="3"/>'
    b += f'<path d="M{cx} {cy} L{x1} {y1} A{r} {r} 0 0 1 {x2} {y2} Z" fill="{T}" opacity=".85" stroke="{K}" stroke-width="2.5"/>'
    for ang, lab in ((0, "12am"), (90, "6am"), (135, "9am"), (180, "12pm"), (210, "2pm"), (270, "6pm")):
        x, y = pt(ang, r + 18); b += f'<text x="{x}" y="{y+5}" font-family="Hand" font-size="17" fill="{K}" text-anchor="middle">{lab}</text>'
    mx, my = pt(172, r * .55); b += f'<text x="{mx}" y="{my}" font-family="Hand" font-size="18" fill="#fff" text-anchor="middle">school</text>'
    return svg(size, size, b)

def art_compass(size=160):
    c = size / 2
    b = f'<circle cx="{c}" cy="{c}" r="{c-8}" fill="#fff" stroke="{K}" stroke-width="3"/><circle cx="{c}" cy="{c}" r="{c-24}" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="3 5"/>'
    b += f'<path d="M{c} {c-52} L{c+14} {c} L{c} {c+52} L{c-14} {c} Z" fill="{T}" stroke="{K}" stroke-width="2.5"/><circle cx="{c}" cy="{c}" r="6" fill="{K}"/>'
    return svg(size, size, b)

def art_sprout(size=140):
    b = f'<path d="M{size/2} {size-14} C{size/2} {size/2+20} {size/2} {size/2} {size/2} {size/2-12}" stroke="{S}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    b += f'<path d="M{size/2} {size/2} C{size/2-40} {size/2-8} {size/2-52} {size/2-44} {size/2-52} {size/2-44} C{size/2-14} {size/2-50} {size/2-4} {size/2-24} {size/2} {size/2}Z" fill="{S}" stroke="{K}" stroke-width="2.5"/>'
    b += f'<path d="M{size/2} {size/2-20} C{size/2+40} {size/2-28} {size/2+52} {size/2-60} {size/2+52} {size/2-60} C{size/2+14} {size/2-66} {size/2+4} {size/2-42} {size/2} {size/2-20}Z" fill="#7DB188" stroke="{K}" stroke-width="2.5"/>'
    b += f'<ellipse cx="{size/2}" cy="{size-10}" rx="34" ry="8" fill="#B98E5C" stroke="{K}" stroke-width="2.5"/>'
    return svg(size, size, b)

def art_book(w=150, h=110):
    b = f'<path d="M10 20 Q{w/2-8} 8 {w/2} 24 V{h-14} Q{w/2-8} {h-26} 10 {h-12} Z" fill="#fff" stroke="{K}" stroke-width="3"/><path d="M{w-10} 20 Q{w/2+8} 8 {w/2} 24 V{h-14} Q{w/2+8} {h-26} {w-10} {h-12} Z" fill="#F7E7CB" stroke="{K}" stroke-width="3"/>'
    for i in range(3): b += f'<path d="M24 {40+i*16} H{w/2-14}" stroke="{N}" stroke-width="2.5" opacity=".4"/><path d="M{w/2+14} {40+i*16} H{w-24}" stroke="{T}" stroke-width="2.5" opacity=".5"/>'
    return svg(w, h, b)

def art_bubbles(W=240, H=110):
    w, h = 240, 110
    b = f'<rect x="6" y="6" width="150" height="62" rx="20" fill="#fff" stroke="{K}" stroke-width="3"/><path d="M40 68 L30 94 L64 68" fill="#fff" stroke="{K}" stroke-width="3"/>'
    b += f'<text x="81" y="43" font-family="Hand" font-size="19" fill="{T}" text-anchor="middle">what works?</text>'
    b += f'<rect x="96" y="36" width="138" height="58" rx="20" fill="{T}" opacity=".9" stroke="{K}" stroke-width="3"/><text x="165" y="72" font-family="Hand" font-size="19" fill="#fff" text-anchor="middle">what doesn\'t?</text>'
    return svg(W, H, b, vb=(240, 110))

def art_stars(w=120, h=40):
    return svg(w, h, "".join(f'<path d="M{20+i*40} 6 l5 11 12 1 -9 8 3 12 -11 -6 -11 6 3 -12 -9 -8 12 -1z" fill="{G}" stroke="{K}" stroke-width="2"/>' for i in range(3)))

def wave(color="#E9D8BE"):
    return f'<svg style="position:absolute;left:0;bottom:0;width:8.5in;height:1.3in" viewBox="0 0 850 130" preserveAspectRatio="none"><path d="M0 60 Q150 10 300 55 T600 50 T850 40 V130 H0 Z" fill="{color}" opacity=".7"/><path d="M0 85 Q200 45 380 85 T850 75 V130 H0 Z" fill="{color}"/></svg>'

# ---------- components ----------
def page(inner, title="", n=None, run=True, art=""):
    r = f'<div class="run"><span>{BRAND}</span><span>{title}</span></div>' if run else ""
    f = f'<div class="foot"><span>© 2026 {AUTHOR}. Personal use only.</span><span>@@N@@</span></div>' if run else ""
    c = f'<div style="position:absolute;top:.62in;right:.8in;opacity:.95">{art}</div>' if art else ""
    return f'<section class="page">{r}{c}{inner}{f}</section>'
def cover(title, tag, sub, art, extra="", pill=""):
    p = f'<div class="pill">{pill}</div>' if pill else ""
    return f'<section class="page cover">{wave()}<div style="position:relative">{art}<div class="tag">{tag}</div><h1>{title}</h1><div class="sub" style="max-width:5.4in">{sub}</div>{p}<div class="by">by {AUTHOR}</div>{extra}</div></section>'
def box(kind, title, body): return f'<div class="box {kind}"><p class="t">{title}</p>{body}</div>'
def head(kicker, title, sub=""): return f'<p class="kicker">{kicker}</p><h1>{title}</h1><div class="rule"></div>' + (f'<div class="sub">{sub}</div>' if sub else "")
def lines(n): return '<div class="ln"></div>' * n
def field(label, n=2): return f'<div class="fld"><b>{label}</b>{lines(n)}</div>'
def table(headers, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in headers); tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><tr>{th}</tr>{tr}</table>'
def checks(items): return "".join(f'<div class="q"><span class="cb"></span><span>{i}</span></div>' for i in items)
def questions(qs, opts=("Yes", "Not sure", "No"), start=1):
    out = ""
    for i, q in enumerate(qs, start):
        o = "".join(f'<span class="circ"></span>{x}' for x in opts)
        out += f'<div class="q"><span class="n">{i}</span><div>{q}<div class="o">{o}</div></div></div>'
    return out
def about_author():
    return (box("story", "About the author", f"<p><b>{AUTHOR}</b> left in-person school in 3rd grade and was homeschooled from then on. He completed high school through FLVS Flex in 2021 at 13, earned his associate degree in political science from Palm Beach State College in 2023 at 15, and his bachelor's degree in political science from Florida Atlantic University in 2025 at 17. He is now working on a master's degree.</p>"
            "<p>He is not a licensed teacher, counselor or lawyer. He shares what worked for him, what was hard, and what he would do differently.</p>"))
def build_html(pages, print_mode=False, title="Product"):
    out = []; n = 0
    for pg in pages:
        n += 1
        out.append(pg.replace("@@N@@", str(n), 1))
    return f"<!doctype html><meta charset='utf-8'><title>{title}</title><style>{css(print_mode)}</style>" + "".join(out)
