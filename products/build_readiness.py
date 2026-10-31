import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
QS1 = ["Does the learner say they're bored, stuck, or rushing through things in their current setup?",
       "Can the learner explain what kind of learning works for them (face-to-face instructor, online instructor, reading alone, hands-on)?",
       "Is the learner willing to give honest feedback on what is and isn't working, and to try changes?",
       "When something is hard, does the learner keep going, or burn out quickly? (Notice what happens; it isn't about blame.)",
       "Is at least one adult able to check in on progress regularly, even if they aren't teaching?"]
QS2 = ["Are you open to changing the plan when something isn't working, instead of repeating how you were taught?",
       "Do you have a plan for social life (clubs, activities, community, friends), not just for academics?",
       "Do you know the options near you (virtual school, online instructors, tutors, dual enrollment)?",
       "Can the learner slow down or take a break without feeling like they failed?",
       "Are you clear that finishing early is one possible outcome, not the goal for every child?"]
def pages():
    P = []
    P.append(cover("The Readiness Bundle", "is this the right fit, and how will we know?", "A 10-question readiness check, a conversation guide, a monthly check-in, and slow-down signals, all in one printable pack.", art_sprout(160), pill="PRINTABLE PDF · 8 PAGES"))
    P.append(page(head("read this first", "Fit before speed", "Why I made this, and how to use it.") +
        '<div class="two"><div>'
        "<p>When I was in third grade, in-person school wasn't working for me. It taught one way at one speed, and I couldn't adapt to it. My family pulled me out, and we built learning around me: I told my parents what worked and what didn't, and they listened.</p>"
        "<p>I finished high school at 13 through FLVS Flex, earned my associate degree at 15 and my bachelor's at 17. But I want to be clear: <span class='hl'>finishing early isn't the point. Fit is.</span></p>"
        "<p>These pages are the questions I wish my family had written down, so you can talk it through together.</p></div>"
        f"<div style='flex:0 0 2.6in'>{art_stairs(250, 160)}</div></div>" +
        box("plain", "How to use this pack", "<ol><li>Answer the Readiness Check <b>together</b>, circling one answer each.</li><li>Read what your answers suggest, then use the Conversation Guide.</li><li>Do the Monthly Check-In on the same day each month.</li><li>If you see slow-down signals, pause and talk (page 7).</li></ol>") +
        box("story", "From my experience", "<p>There's no score that tells you what to do. The value is in the conversation. Ask, listen, change one thing, and check again.</p>") +
        f'<p class="fine">{DISCLAIMER}</p>', "Read This First"))
    P.append(page(head("part 1", "The 10-Question Readiness Check", "Answer together. Circle one answer for each. There are no right or wrong answers.") +
        "<h3>About the learner</h3>" + questions(QS1[:4], start=1) + "<h3>About the family</h3>" + questions(QS1[4:5] + QS2[:2], start=5), "Readiness Check", art=art_compass(90)))
    P.append(page(head("part 1, continued", "Pace and options") + questions(QS2[2:], start=8) +
        head("what your answers suggest", "", "") .replace('<h1></h1>', '') +
        '<div class="three">' + box("worked", "Mostly Yes", "<p>You have a good base. Write down three things you want the learning to look like.</p>") +
        box("try", "A mix of Not sure", "<p>That's normal. Pick two questions to talk about this week.</p>") +
        box("didnt", "Several No", "<p>That tells you where to start, not whether to stop. Take it one step at a time.</p>") + '</div>' +
        box("story", "What I'd say", "<p>Early on, my answers to #3 and #7 would have been 'Not sure' and 'No.' My parents didn't know yet what social options existed, and I hadn't learned to say what wasn't working. Both got better once we started talking.</p>"), "Readiness Check"))
    P.append(page(head("part 2", "The Conversation Guide", "Two questions, a pencil, and ten honest minutes.") + f"<div style='text-align:center;margin:.05in 0'>{art_bubbles(190, 87)}</div>" +
        box("plain", "Ask the learner", "<ol><li><b>What's one thing that works for you in how you learn?</b></li><li><b>What's one thing that doesn't?</b></li></ol><p>Write the answers down. Don't argue. Just listen.</p>") +
        '<div class="two"><div>' + field("What works", 2) + field("What doesn't", 2) + '</div><div>' + field("The one thing we'll change", 2) + field("Check in again on", 1) + '</div></div>' +
        box("worked", "What worked for me", "<p>My parents asked for feedback, and then they actually changed things. Face to face with an instructor, online with one, or no lectures at all: there's no single right style, only what fits the learner.</p>") +
        box("didnt", "What didn't", "<p>Running homeschool exactly like in-person school, with the same linear lessons at the kitchen table. I've watched families do this, and it's easy to understand why. It's what we know. It's just not the point.</p>"), "Conversation Guide"))
    P.append(page(head("each month", "Monthly Check-In", "Same day each month. Relaxed. Month of ____________") +
        '<div class="two"><div class="box plain"><p class="t" style="color:var(--navy)">The learner fills in</p>' + field("The best part of last month", 2) + field("The hardest part", 2) + field("Something I'd change", 2) + '<p><b>Energy (1-5):</b> 1 &nbsp; 2 &nbsp; 3 &nbsp; 4 &nbsp; 5</p><p><b>I want to go:</b> faster / slower / the same</p></div>' +
        '<div class="box plain"><p class="t" style="color:var(--navy)">The parent fills in</p>' + field("I noticed they seemed", 2) + field("Something I'm worried about", 2) + field("Something I'll change on my side", 2) + '</div></div>' + field("Decision for next month, together", 3), "Monthly Check-In", art=art_stars()))
    P.append(page(head("know when to pause", "Slow-Down Signals", "One sign isn't a verdict. Several together are a reason to slow down and talk.") +
        '<div class="two"><div>' + box("didnt", "Signs to watch for", "<ul><li>Dread or tears around schoolwork that wasn't there before</li><li>Losing interest in things they used to love</li><li>Cutting out friends and activities to keep up</li><li>Perfectionism, or fear of making mistakes</li><li>Praise tied mostly to speed</li></ul>") + '</div><div>' +
        box("try", "Pause or continue?", "<p>Answer yes or no together:</p>" + checks(["The learner wants to continue at this speed", "They understand it, not just finish it", "They're sleeping, eating and seeing friends normally", "There's an adult they can talk to about stress", "There's room each week for something just fun"]) + "<p class='fine'>Mostly yes: continue. Mixed: change one thing and recheck in two weeks. Mostly no: slow down.</p>") + '</div></div>' +
        box("story", "From my experience", "<p>Starting hard is normal. My first year of online school was rough: no classroom structure, lots of free time I wasn't used to, and missing my friends. But I'm not a doctor or counselor, and if you're worried about a child's well-being, please talk to a qualified professional.</p>"), "Slow-Down Signals", art=art_compass(90)))
    P.append(page(head("what's next", "Keep going, gently", "A few simple habits that made the biggest difference for me.") +
        "<ol><li><b>Ask, then listen.</b> Feedback is the best data you have.</li><li><b>Change one thing at a time.</b> Then check again.</li><li><b>Plan the social side on purpose.</b> It didn't happen automatically for me; it took about a year to find activities.</li><li><b>Protect rest and free time,</b> and plan what to do with it.</li><li><b>Remember the goal is fit.</b> Early graduation is one door among many.</li></ol>" + about_author() +
        f'<p class="fine" style="margin-top:.2in">{DISCLAIMER}</p>', "Keep Going", art=art_sprout(100)))
    return P
if __name__ == "__main__":
    for mode in (False, True): open(os.path.join(HERE, f"readiness{'_print' if mode else ''}.html"), "w").write(build_html(pages(), mode, "The Readiness Bundle"))
