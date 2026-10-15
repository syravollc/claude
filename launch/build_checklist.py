# Builds readiness_checklist.html (render to PDF with Chromium). Edit text here and rerun.
qs=[("About the learner",[
("Does the learner say they are bored, stuck, or rushing through things in their current setup?","Yes","Not sure","No"),
("Can the learner explain what kind of learning works for them (face-to-face instructor, online instructor, reading alone, hands-on)?","Yes","Not sure","No"),
("Is the learner willing to give honest feedback on what is and isn't working, and to try changes?","Yes","Not sure","No"),
("When something is hard, does the learner keep going or burn out quickly? (Note what happens, not who is to blame.)","Keeps going","Depends","Burns out")]),
("About the family",[
("Is at least one adult able to check in on progress regularly, even if they are not teaching?","Yes","Not sure","No"),
("Are you open to changing the plan when something isn't working, instead of repeating how you were taught?","Yes","Not sure","No"),
("Do you have a plan for social life (clubs, activities, community, friends), not just for academics?","Yes","Not sure","No")]),
("About pace and options",[
("Do you know the options near you (virtual school, online instructors, in-person tutors, dual enrollment)?","Yes","Not sure","No"),
("Can the learner slow down or take a break without feeling like they failed?","Yes","Not sure","No"),
("Are you clear that finishing early is one possible outcome, not the goal for every child?","Yes","Not sure","No")])]
n=0;body=""
for sec,items in qs:
    body+=f"<h3>{sec}</h3>"
    for q,a,b,c in items:
        n+=1
        body+=f'<div class="q"><span class="n">{n}</span><span class="t">{q}</span><span class="o"><i></i>{a} <i></i>{b} <i></i>{c}</span></div>'
css="""@page{size:Letter;margin:.6in}*{box-sizing:border-box}body{font:10.5pt/1.4 Arial,sans-serif;color:#222;margin:0}
.p{min-height:9.7in;page-break-after:always;position:relative}.p:last-child{page-break-after:auto}
h1{font:bold 22pt Georgia,serif;margin:0;color:#7a2e12}.sub{color:#555;margin:2px 0 8px}
.intro{background:#faf5ee;border-left:4px solid #c4572d;padding:8px 12px;margin:8px 0 10px;font-size:10pt}
h3{font-size:12pt;margin:12px 0 4px;color:#7a2e12;border-bottom:1px solid #ddd;padding-bottom:3px}
.q{display:grid;grid-template-columns:24px 1fr;gap:2px 8px;padding:6px 0;border-bottom:1px dotted #ccc}
.n{font-weight:bold;color:#c4572d}.o{grid-column:2;font-size:10pt;color:#333}
.o i{display:inline-block;width:11px;height:11px;border:1.5px solid #555;border-radius:50%;margin:0 4px 0 12px;vertical-align:-1px}.o i:first-child{margin-left:0}
.box{border:1px solid #c9bfb2;border-radius:8px;padding:10px 14px;margin:10px 0}.box h4{margin:0 0 4px;font-size:11pt;color:#7a2e12}
ul{margin:4px 0 4px 18px;padding:0}li{margin:3px 0}.ln{border-bottom:1px solid #999;height:24px}
.cta{background:#c4572d;color:#fff;border-radius:8px;padding:10px 14px;margin-top:12px}.cta a{color:#fff}
footer{position:absolute;bottom:0;left:0;right:0;font-size:8pt;color:#777;border-top:1px solid #ccc;padding-top:4px}"""
page1=f"""<div class=p><h1>The 10-Question Readiness Check</h1><div class=sub>For parents and students considering a flexible or accelerated homeschool path</div>
<div class=intro>By [NAME]. I left in-person school in 3rd grade, graduated high school at 13 through FLVS Flex, earned my associate degree at 15 and my bachelor's at 17. This is not a test or a diagnosis. These are questions I wish my family had written down so we could talk it through together.<br><b>Answer together. Circle one answer. There is no score that tells you what to do.</b></div>{body}
<footer>General information from one person's experience. Not educational, psychological, medical or legal advice. Rules vary by state and district.</footer></div>"""
page2=f"""<div class=p><h1>What your answers suggest</h1><div class=sub>Not a diagnosis. A starting point for a conversation.</div>
<div class=box><h4>Mostly "Yes"</h4>You have a good base. Next step: write down 3 things you want the learning experience to look like.</div>
<div class=box><h4>A mix of "Not sure"</h4>That's normal. Pick two questions to talk about this week.</div>
<div class=box><h4>Several "No"</h4>That tells you where to start, not whether to stop. Take it one step at a time.</div>
<h3>One-page conversation guide</h3>
<ul><li>Ask the learner: <b>"What is one thing that works for you in how you learn? What is one thing that doesn't?"</b></li><li>Write the answers down. Listen first.</li><li>Change one thing.</li><li>Check in again in two weeks.</li></ul>
<div class=box><h4>Our answers</h4><b>What works:</b><div class=ln></div><b>What doesn't:</b><div class=ln></div><b>The one thing we'll change:</b><div class=ln></div><b>Check in again on:</b><div class=ln></div></div>
<div class=box><h4>Remember</h4>Homeschooling doesn't have to copy school. It can bend to the child, face to face with an instructor, online with one, or without lectures at all. Ask for feedback, listen, and adjust. Finishing early is one possible outcome, not the goal for every child.</div>
<div class=cta><b>Want help thinking it through?</b> Book a 60-minute Acceleration Roadmap session: [BOOKING LINK] &nbsp;·&nbsp; Join the guide waitlist: [WAITLIST LINK]</div>
<footer>Not educational, psychological, medical or legal advice. For concerns about learning differences, mental health or legal requirements, talk to a qualified professional.</footer></div>"""
open("readiness_checklist.html","w").write(f"<!doctype html><meta charset=utf-8><title>The 10-Question Readiness Check</title><style>{css}</style>{page1}{page2}")
