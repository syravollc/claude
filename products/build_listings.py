import os
HERE = os.path.dirname(os.path.abspath(__file__))
AUTH = "Fabian Capre"
ABOUT = ("ABOUT THE AUTHOR\nI'm Fabian. I left in-person school in 3rd grade and was homeschooled from then on. I finished high school through FLVS Flex at 13 (2021), earned my associate degree in political science at 15 (2023) and my bachelor's degree in political science at 17 (2025), and I'm now working on a master's. "
         "I'm not a licensed teacher, counselor or lawyer. I share what worked for me, what didn't, and what I'd do differently.")
HOW = ("HOW IT WORKS\n1. Buy it on Etsy.\n2. Download your files from your Etsy purchases (this is a digital item: nothing is shipped).\n3. Open it on any device, or print as many copies as you need for your own family.")
FILES = "WHAT YOU RECEIVE\n- 1 PDF, US Letter size (8.5 x 11 in), cream screen version\n- 1 PDF, print-friendly white version (saves ink){extra}"
HONEST = ("GOOD TO KNOW\n- This is general information from one person's experience. It is not educational, psychological, medical or legal advice, and it can't promise any outcome.\n"
          "- Rules about homeschooling, records and college differ by state and change. Always check the official source where you live.\n"
          "- Personal use only. Please don't resell, share or redistribute the files.\n"
          "- AI tools helped me draft and format parts of this product. The experiences are mine and I reviewed all of the content.\n"
          "- Colors may look different on different screens and printers.")
POLICY = "SHOP POLICIES\n[Add your refund and support policy here. Digital items usually can't be returned, so say what you'll do if a file won't open.]"
L = [
 dict(key="planner", name="The Family Planner", price="$6-12",
  title="Homeschool Planner Printable PDF, Family Weekly Planner and Monthly Check-In, Records Tracker, Instant Download",
  tags=["homeschool planner","homeschool printable","family planner pdf","weekly planner pdf","monthly check in","homeschool records","learning planner","printable planner","homeschool mom","homeschool teens","digital planner pdf","parent planner","school year planner"],
  desc=("A planner that bends to your child.\n\nSix printable pages to plan the year, the week and the month, and to adjust when something isn't working. Built from my own experience of being homeschooled from 3rd grade, with short notes on what worked for me and what didn't.\n\nWHAT'S INSIDE (7 pages)\n- Year at a Glance: learning style, pace, structure, social life and goals\n- Weekly Planner with a protected fun slot and a Friday review\n- Monthly Check-In with one side for the learner and one for the parent\n- Records Tracker for transcripts, course lists, activity logs and more\n- College Questions Checklist for early college\n- Reset Plan for when things feel stuck\n\n"),
  extra="", alt=["Cover of The Family Planner with a compass illustration","List of what is inside the planner","Preview of the Year at a Glance, Weekly Planner and Monthly Check-In pages","How the instant digital download works","About the author"]),
 dict(key="readiness", name="The Readiness Bundle", price="$6-12",
  title="Is My Child Ready? Homeschool Readiness Checklist Printable, Parent and Teen Conversation Guide, Instant PDF",
  tags=["readiness checklist","homeschool checklist","1st year homeschool","is my child ready","conversation guide","parent teen talk","homeschool support","printable checklist","homeschool printable","homeschool parents","monthly check in","homeschool help","learning styles"],
  desc=("Is this the right fit, and how will we know?\n\nA 10-question readiness check, a conversation guide, a monthly check-in and slow-down signals, all in one printable pack. These are the questions I wish my family had written down when I moved from in-person school to homeschooling.\n\nWHAT'S INSIDE (8 pages)\n- Fit before speed: why this exists and how to use it\n- The 10-Question Readiness Check (learner, family, pace and options)\n- What your answers suggest\n- The Conversation Guide: two questions, ten honest minutes\n- Monthly Check-In (learner and parent)\n- Slow-Down Signals and a pause-or-continue check\n\nThis is a conversation tool, not a test or a diagnosis. There is no score that tells you what to do.\n\n"),
  extra="", alt=["Cover of The Readiness Bundle with a sprout illustration","List of what is inside the bundle","Preview of the readiness check, results and conversation guide pages","How the instant digital download works","About the author"]),
 dict(key="early_college", name="The Early College Questions Checklist", price="$6-12",
  title="Early College Checklist Printable, Dual Enrollment Questions for Homeschool Teens, College Planning Worksheet PDF",
  tags=["early college","dual enrollment","college checklist","homeschool college","college questions","homeschool teen","college planning","high school planning","teen college prep","printable checklist","college tracker","homeschool printable","start college early"],
  desc=("Ask before you commit.\n\nWhat to ask a college, how to start small, and what I learned finishing an associate degree at 15 and a bachelor's at 17. Rules about age, placement tests, credits and enrollment vary by college and state and change over time, so this checklist helps you ask the right questions.\n\nWHAT'S INSIDE (7 pages)\n- How I did it: my route, what worked and what was hard\n- Is your child ready for college classes? 8 questions\n- 9 questions to ask the college, with space for answers\n- A start-small plan for the first term\n- A college tracker\n- Records checklist and next steps\n\n"),
  extra="", alt=["Cover of The Early College Questions Checklist with a staircase illustration","List of what is inside the checklist","Preview of the route, readiness and college questions pages","How the instant digital download works","About the author"]),
 dict(key="starter", name="The First-Year Starter Pack", price="$12-19",
  title="First Year Homeschool Starter Pack Printable, New Homeschooler Guide Plus Planner Pages, Instant Download PDF",
  tags=["1st year homeschool","new homeschooler","homeschool starter","homeschool printable","homeschool planner","homeschool guide","getting started","homeschool pdf","homeschool mom","homeschool support","online school guide","homeschool beginner","homeschool bundle"],
  desc=("Your first year, a little easier.\n\nA short guide, a planner, and the check-ins I wish my family had in our first year of online school and homeschooling. My first year was the hardest part, and this pack is a shortcut through what we learned the hard way.\n\nWHAT'S INSIDE (13 pages)\n- My first year, honestly\n- What worked and what didn't\n- Plan your days (with a free-time plan)\n- Find community on purpose (with a tracker)\n- The feedback talk: scripts for parents and students\n- Five first-year principles\n- Planner pages: Year at a Glance, Weekly Planner, Monthly Check-In, Reset Plan\n- A quick readiness check\n\n"),
  extra="", alt=["Cover of The First-Year Starter Pack with a sprout illustration","List of what is inside the starter pack","Preview of the first-year story, what worked and plan your days pages","How the instant digital download works","About the author"]),
 dict(key="guide", name="Early, Not Rushed: The Guide", price="$19-25",
  title="Homeschool Guide PDF, Early Graduation and Early College from a Student's Side, Parent and Teen eBook",
  tags=["homeschool guide","homeschool ebook","early graduation","accelerated learning","homeschool teens","homeschool parent","homeschool pdf","gifted homeschool","early college guide","homeschool support","learning styles","homeschool help","homeschool book"],
  desc=("What worked for me, what didn't, and how to build a path around your child. For parents and students.\n\nI finished high school at 13 and college at 17, but this guide isn't about speed. It's about fit: building learning around the child. You get my honest story plus the tools I wish my family had.\n\nWHAT'S INSIDE (28 pages)\n- My story, honestly, including the hard first year\n- Ready, or pushed? Readiness vs. pressure\n- When acceleration is the wrong move\n- Mapping the route and avoiding gaps in the foundations\n- Records, transcripts and early college\n- Social life, and being young on campus\n- A weekly rhythm, using AI and other tools wisely, and what to do when things go wrong\n- A tool or worksheet in every chapter\n\n"),
  extra="", alt=["Cover of Early, Not Rushed: The Guide with a staircase illustration","List of what is inside the guide","Preview of the introduction, chapter 1 and mapping the route pages","How the instant digital download works","About the author"]),
]
out = ["# Etsy listings (ready to paste)\n",
 "Check Etsy's current rules before you publish: listing requirements, image sizes, digital file limits, AI disclosure, and fees. I wrote this from third-party sources and haven't seen your Etsy account.\n",
 "**Image files:** `products/etsy/<product>/<product>_listing_1.png` to `_5.png` (2000 x 1500 px, 4:3). Upload in this order: 1 is the thumbnail. If Etsy offers alt text, use the lines below.\n",
 "**Digital files to upload:** the screen PDF and the `_PRINT` PDF for each product (the guide has screen only).\n",
 "**Price:** the ranges are guesses to test. Remember fixed fees take a bigger share of low prices.\n",
 "**AI disclosure:** Etsy has rules about AI-assisted items. Set the listing attributes accurately (for example who made it and whether AI was used) and read their current Creativity Standards.\n"]
for l in L:
    assert len(l["title"]) <= 140, (l["key"], len(l["title"]))
    assert len(l["tags"]) == 13 and all(len(t) <= 20 for t in l["tags"]), (l["key"], [t for t in l["tags"] if len(t) > 20])
    files = FILES.format(extra=("\n- " + l["name"] + " files only; no physical item is shipped"))
    desc = l["desc"] + files + "\n\n" + HOW + "\n\n" + HONEST + "\n\n" + ABOUT + "\n\n" + POLICY
    out.append(f"\n---\n\n## {l['name']}\n\n**Price to test:** {l['price']}\n\n**Title ({len(l['title'])} characters):**\n{l['title']}\n\n**13 tags (each 20 characters or fewer):**\n" + ", ".join(l["tags"]) + "\n\n**Suggested category:** Paper & Party Supplies > Paper > Planners / or Digital Prints (check Etsy's current category tree)\n\n**Image alt text:**\n" + "\n".join(f"{i+1}. {a}" for i, a in enumerate(l["alt"])) + f"\n\n**Description:**\n\n```\n{desc}\n```\n")
open(os.path.join(HERE, "etsy", "LISTINGS.md"), "w").write("\n".join(out))
print("ok", [len(l["title"]) for l in L])
