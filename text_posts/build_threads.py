# Builds threads_weeks_1_to_8.md from the video drafts (weeks 2-8 from build_drafts.py, week 1 below) plus hand-written single posts.
import sys, os, re, io, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content_pipeline", "drafts"))
with contextlib.redirect_stdout(io.StringIO()):
    import build_drafts as bd
W = dict(bd.W)
F = lambda hook, lines, note="": dict(t="face", hook=hook, lines=lines, note=note)
A = lambda hook, narr, note="": dict(t="anim", hook=hook, scenes=[(0, n, "", "") for n in narr], note=note)
W[1] = ("Start here", "Intro and core story", [
    F("Pulled out of school in 3rd grade. Here's why.", ["In third grade, I got pulled out of in-person school.", "It wasn't because I was a bad student.", "It was because the way school was taught didn't fit how I learn.", "Homeschooling let me work at my own pace and follow ideas I was curious about.", "And it taught me a lot about myself.", "I ended up graduating high school at thirteen.", "But finishing early isn't the only point.", "If you're a parent wondering whether this could work for your family, I'll be sharing what worked, what was hard, and what I'd do differently."]),
    A("School fit everyone the same. I wasn't the same.", ["In school, everyone learned the same way, at the same speed.", "I tried to adapt. It never really fit me.", "So my family built learning around me. I told my parents what worked and what didn't.", "That's the real power of homeschooling: it can bend to the child."]),
    F("\"But what about socialization?\"", ["If you're a homeschool parent, you've heard this question.", "Here's my honest answer.", "I was homeschooled, and I had just as much social life as other kids, maybe more.", "I was part of local high school clubs and organizations, and I was active in church groups.", "Socialization didn't happen by accident. It happened because we made room for it."], "Add one real example of a club or activity you did. Don't add anything you didn't do."),
    A("Homeschooling at a kitchen table can still feel like school.", ["I've seen families start homeschooling and run it just like in-person school.", "Same linear lessons. Same one-sided teaching. Just at home.", "But homeschooling can adapt: face to face with an instructor, online with one, or no lectures at all.", "Ask your child what's working and what isn't. Then change it."], "Describes a pattern only; no real family is identified.")])
SINGLES = {
 1: ["Pulled out of school in 3rd grade. Not because I was a bad student, but because the way it was taught didn't fit how I learn. Homeschooling let me work at my own pace. I finished high school at 13. But early graduation isn't the point. Fit is.",
     "In school, everyone learned the same way at the same speed. I tried to adapt and it never fit. So my family built learning around me: I told my parents what worked and what didn't, and we changed things. Homeschooling can bend to the child.",
     "If you're a homeschool parent you've heard \"what about socialization?\" My honest answer: I had as much social life as other kids, maybe more. Local high school clubs, community orgs, church groups. It didn't happen by accident. We made room for it.",
     "Homeschooling at a kitchen table can still feel like school: same linear lessons, new room. Try this: ask your child what works and what doesn't, then change one thing. Face to face, online, or no lectures at all. Fit the learner."],
 2: ["My first year of online school, I hated it. At school the classroom told me where to be all day. Online I had lecture times and assignments, then I was free. I wasn't used to that. If your kid is switching, the first year can feel strange. That's normal.",
     "My school day: start at 9, done around 2. The rest of the day was free for other school activities and things I was interested in. It takes a plan to use free time well. That was my biggest lesson.",
     "I was pulled out of school mid-year, so I never got to say goodbye to most of my friends. That was one of the hardest parts. If your child is changing schools, talk about the friends they'll miss. Plan the goodbyes and the hellos.",
     "Free time isn't a plan. Online school gave me lots of it and I didn't know what to do with it. What I needed was an outlook: this time is a gift, so plan for it. Talk about the free time before day one."],
 3: ["In my first year of homeschool I thought homeschool social life didn't exist. It did. My parents just didn't know yet what to sign me up for. It took about a year to find local activities. If you're in that first year and it feels empty, keep looking.",
     "Where to look for community: local clubs and orgs (check their rules), faith and community groups, classes and co-ops, volunteering, sports and arts. Pick one this month.",
     "I once told my parents I missed being in school and felt like I was missing a piece of my childhood. They didn't get defensive. They understood it was a process they were still learning too. If your child says something like that, listen first.",
     "Two questions that changed my education: What's one thing that works for you? What's one thing that doesn't? Write the answers down, change one thing, check in again in two weeks."],
 4: ["Ready or pushed? From outside they can look the same. The difference is what happens when it gets hard. A child who's ready can say so and the plan changes. A child who's pushed hides it. Ask them. Then listen.",
     "Readiness comes from the child's curiosity. Pressure comes from an outside goal. Protect rest and downtime either way.",
     "Signs to slow down and talk: dread around school, losing interest in things they love, cutting out friends to keep up. One sign isn't much; several together are a signal. If you're worried about their well-being, talk to a qualified professional.",
     "Once a month, sit down and ask: best part? hardest part? what would you change? faster, slower or the same? Write it down, change one thing. Ten minutes."],
 5: ["How I started college at 13: I took the PERT test, finished high school, and enrolled. It wasn't hard to get in because on paper I had what was required. I took most classes online but still did things on campus. This was my route. Check yours.",
     "Before college early, ask: age requirements? which credits transfer (get it in writing)? who's our contact? withdrawal policy? parent role for a minor? Rules differ by college.",
     "There's a shock moment when you tell classmates your age. Because of my path I matured quickly, which helped me fit in, but it wasn't always easy. If your child is young on campus, let them decide how and when to share.",
     "You don't have to start college with a full load. One class is a test of fit: how the workload, people and pace feel. Then decide together."],
 6: ["After my associate degree at 15, a university felt like a different ballpark. It took time but I found my footing. FAU's campus had a high school on it, so I made friends with a lot of high schoolers. Big jumps need time to adjust.",
     "At FAU I took in-person classes, my first time in a classroom in years. It took adaptation. If your child moves from online to in-person, give them time.",
     "College clubs were a big part of my experience. I was a regular member of groups like Konbit Kreyòl and the Black Student Union and made a lot of friends. If your child is young on campus, clubs are a great way to find your people.",
     "Keep records: transcripts, a course list, your diploma, an activity log. Back it up. Check your state's rules too."],
 7: ["In my second-to-last semester I did a Florida legislative internship. I spent the session in Tallahassee working with a state representative, living on my own for the first time. My age didn't get in the way. Homeschooling can open doors like that.",
     "Can my child graduate early? Maybe. But it's one door of many. Homeschooling can also mean more time for interests, going deeper, or a path built around the child. Start with fit, not speed.",
     "I'm one of three brothers. My other two brothers later followed the same process, so I went in blindly with my parents and paved the way. If you're the first in your family to try this, it's okay not to know everything yet.",
     "Speed up or slow down? Ask: does the learner want this? Do they understand it, not just finish it? Are they sleeping, eating and seeing friends normally? Mostly yes: continue. Mostly no: slow down."],
 8: ["If we were at your kitchen table, I'd say: build learning around your child. Ask for feedback and listen. Change things when they aren't working. And remember: finishing early is one outcome, not the goal.",
     "What \"the right way\" means to me: 1) build it around the child and how they learn, 2) ask for feedback and listen, 3) change things when they aren't working. Results vary, but that's my approach.",
     "I offer free 30-minute chats for families thinking through homeschooling. I'm not a teacher or counselor and I can't promise outcomes, but I can share what worked for me. Message me if you'd like one.",
     "Moving fast? Check for gaps. Pick a topic from a few months ago and ask your child to explain it like they're teaching you. No hints. If it's shaky, go back before going forward."]}
def chunks(sentences, limit=250):
    out, cur = [], ""
    for s in sentences:
        if cur and len(cur) + 1 + len(s) > limit: out.append(cur); cur = s
        else: cur = (cur + " " + s).strip()
    return out + ([cur] if cur else [])
def thread(p):
    sents = [l.strip() for l in p["lines"] if l.strip() != "[pause]"] if p["t"] == "face" else [sc[1] for sc in p["scenes"]]
    parts = [p["hook"]] + chunks(sents)
    parts.append("If this was useful, I put together a free 10-question readiness checklist for families. Happy to share it if you'd like.")
    return [f"{i+1}/{len(parts)} {t}" if len(parts) > 1 else t for i, t in enumerate(parts)]
out = ["# Text posts and threads: weeks 1-8 (status: DRAFT, review before posting)\n",
 "For each of the 32 posts: a **single post** (written to stay under about 280 characters; check each platform's limit) and a **thread** built from the video script.\n",
 "Rules: change anything that doesn't sound like you. No links unless the platform or group allows them. The last tweet of each thread offers the checklist, so only keep it where promotion is allowed. Say 'my experience', no guarantees, no private details about parents or brothers. Keep proof ready. Check group rules first (`group_rules_checklist.md`).\n"]
for wk in sorted(W):
    theme, sub, posts = W[wk]; out.append(f"\n---\n\n# Week {wk}: {theme}\n")
    for i, p in enumerate(posts):
        single = SINGLES[wk][i]; out.append(f"\n## Week {wk}, Post {i+1}: {p['hook']}\n**Single post** ({len(single)} characters):\n> {single}\n\n**Thread:**\n" + "\n\n".join(thread(p)) + "\n")
        if p.get("note"): out.append(f"**NOTE FOR YOU:** {p['note']}\n")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "threads_weeks_1_to_8.md"), "w").write("\n".join(out))
print(sum(len(W[w][2]) for w in W), "posts;", "max single length", max(len(s) for v in SINGLES.values() for s in v))
