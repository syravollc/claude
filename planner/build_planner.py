# Builds planner.html from simple helpers, then render with Chromium (see README in this folder).
def lines(n): return "".join('<div class="ln"></div>' for _ in range(n))
def box(label,n=3,h=None): return f'<div class="fld"><b>{label}</b>{lines(n)}</div>'
def table(headers,rows,cls=""):
    th="".join(f"<th>{h}</th>" for h in headers)
    tr="".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)
    return f'<table class="{cls}"><tr>{th}</tr>{tr}</table>'
disc="General planning tool from one family's experience. Not educational, legal, medical or psychological advice. Check your state's rules."
def page(title,sub,body): return f'<section><h1>{title}</h1><p class="sub">{sub}</p>{body}<footer>{disc}</footer></section>'
P=[]
P.append('<section class="cover"><h1>Early, Not Rushed</h1><h2>The Family Planner</h2><p>For parents and students building a learning path that fits.</p><p class="by">[NAME]</p><div class="how"><b>How to use this planner</b><ol><li>Fill in the Year-at-a-Glance together.</li><li>Copy the Weekly Planner each week (print several).</li><li>Do the Monthly Check-In on the same day each month.</li><li>Keep the Records Tracker updated every term.</li><li>Use the College Questions page before talking to any college.</li><li>Use the Reset Plan when things feel stuck.</li></ol><p>Print on regular paper. Pencil works best, because plans change, and that is the point.</p></div><footer>'+disc+'</footer></section>')
P.append(page("Year at a Glance","Where we are, where we might go, and what we will try. Review every term.",
 box("Learner's name or nickname (no personal details needed)",1)+
 table(["","Where we are now","What's working","What isn't","One thing we'll try"],
 [[r,"","","",""] for r in ["Learning style<br><small>(live instructor, online instructor, reading, hands-on)</small>","Pace","Daily structure","Social life","Goals<br><small>(not just graduation)</small>"]],"tall")+
 box("Route we are considering (stay + depth, subject acceleration, grade skip, early graduation, dual enrollment, online instructor, mix)",3)+
 box("What would tell us it's time to slow down?",2)+box("Next review date",1)))
rows=[[d,"","","",""] for d in ["Monday","Tuesday","Wednesday","Thursday","Friday","Weekend"]]
P.append(page("Weekly Planner","Week of ____________  ·  Energy this week (1-5): ____",
 table(["Day","Learning block 1<br><small>energy ★★★</small>","Learning block 2","Break / movement","Social or activity time"],rows,"tall")+
 box("Just for fun slot (protected)",1)+
 '<div class="fld"><b>Friday 5-minute review</b><div class="two"><div>What worked<div class="ln"></div><div class="ln"></div></div><div>What to change<div class="ln"></div><div class="ln"></div></div></div></div>'+
 '<p class="tip">Author\'s note: my own school day ran from about 9 to 2, which left the rest of the day free for other activities and things I was interested in. Plan what you will <i>do</i> with the free time, so it feels like a gift and not a gap.</p>'))
P.append(page("Monthly Check-In","Sit down together, relaxed. Month of ____________",
 '<div class="two"><div class="card"><h3>Learner fills this in</h3>'+box("Something I enjoyed this month",2)+box("Something that was hard",2)+box("Something I want to change",2)+
 '<p><b>My energy right now (1-5):</b> 1 &nbsp;2 &nbsp;3 &nbsp;4 &nbsp;5</p><p><b>I want to go:</b> faster &nbsp;/&nbsp; slower &nbsp;/&nbsp; the same</p></div>'+
 '<div class="card"><h3>Parent fills this in</h3>'+box("I noticed they seemed",2)+box("Something I'm worried about",2)+box("Something I'll change on my side",2)+
 '<p class="tip">Honest, not for judging. If you see ongoing dread, loss of interest, or changes in sleep or mood, slow down and talk to a qualified professional if you are worried.</p></div></div>'+
 box("Decision for next month (together)",3)))
P.append(page("Records Tracker","Keep these safe. Update every term.",
 table(["Item","Where it's stored","Last updated","Needed for"],[[x,"","",""] for x in ["Course list","Official transcripts","Diploma / graduation records","Activity log (clubs, groups, volunteering)","Work samples","Test results","Enrollment communication"]],"tall")+
 box("Notes: state or district rules to check",3)))
P.append(page("College Questions Checklist","Ask before committing. Write the answer, the date and who answered.",
 table(["Question","Answer","Date / who"],[[q,"",""] for q in ["Age and grade requirements? Any exceptions?","Which tests, transcripts or interviews are needed?","What does it cost? Any programs that help?","Which credits transfer, and where? (Get it in writing.)","In person, online, or hybrid?","Who is our contact? Is there a counselor or advisor?","Rules about parents being involved for a minor?","Effect on financial aid and future admissions?","Withdrawal policy if it isn't working?"]],"tall")))
P.append(page("Reset Plan","Use when everything feels stuck. A rough stretch is a signal to adjust, not a failure.",
 box("What's been hardest",2)+box("What we're pausing",2)+box("What we're keeping",2)+box("The one thing we'll change",2)+box("Who we'll talk to (trusted adult, mentor, professional)",2)+
 '<div class="fld"><b>Steps</b><ol><li>Stop adding new commitments for two weeks.</li><li>Have one honest conversation.</li><li>Protect sleep, play and friends.</li><li>Pick one thing to change.</li><li>Recheck in two weeks.</li><li>Decide together: continue, adjust or pause.</li></ol></div>'+
 box("Review date",1)+'<p class="tip">If your child seems consistently sad, anxious, withdrawn or unsafe, or you are worried about their health, please contact a doctor, counselor or other qualified professional.</p>'))
css="""@page{size:Letter;margin:.55in}*{box-sizing:border-box}body{font:11pt/1.4 Arial,Helvetica,sans-serif;color:#222;margin:0}
section{page-break-after:always;position:relative;min-height:9.7in}section:last-child{page-break-after:auto}
h1{font:bold 22pt Georgia,serif;margin:0 0 2px;border-bottom:2px solid #444;padding-bottom:4px}.sub{color:#555;margin:6px 0 12px;font-size:10.5pt}
h3{margin:0 0 6px;font-size:12pt}table{border-collapse:collapse;width:100%;margin:6px 0 12px}th,td{border:1px solid #888;padding:5px 6px;vertical-align:top;font-size:9.5pt;text-align:left}th{background:#eee}
table.tall td{height:.78in}table.tall td:first-child{width:1.35in;font-weight:bold}
.ln{border-bottom:1px solid #999;height:24px}.fld{margin:10px 0}.fld>b{font-size:10pt}
.two{display:flex;gap:14px}.two>*{flex:1}.card{border:1px solid #888;border-radius:8px;padding:10px}
.tip{font-size:9.5pt;color:#444;background:#f6f6f6;border-left:3px solid #888;padding:6px 10px;margin:10px 0}
footer{position:absolute;bottom:0;left:0;right:0;font-size:8pt;color:#777;border-top:1px solid #ccc;padding-top:4px}
.cover{text-align:center;padding-top:1.4in}.cover h1{font-size:36pt;border:0}.cover h2{font:20pt Georgia,serif;margin:0 0 20px}.by{font-size:13pt;margin:16px 0}
.how{text-align:left;max-width:5in;margin:30px auto;border:1px solid #888;border-radius:10px;padding:14px 22px}.how li{margin:4px 0}small{font-weight:normal}"""
open("planner.html","w").write(f"<!doctype html><meta charset=utf-8><title>Early, Not Rushed: Family Planner</title><style>{css}</style>"+"".join(P))
