import os
import actions as ac

print "\ncurrent directory:", os.listdir('.'), "\n"

draftcount = 0
draft_name = ''


for draft in os.listdir("output/automated-drafts"):
    if draft.startswith("autodraft"):
        # print draft
        draftcount += 1

draft_name = "output/automated-drafts/autodraft" + str(draftcount) + ".txt"

def ghostwrite(inspiration):
    with open(draft_name, "w") as latest_draft:
        latest_draft.write(inspiration)
        print "wrote " + draft_name


vein = open("assets/thesis-source-material.txt")

# transfused = ac.rearrange_lines(vein)
transfused = ac.garble(vein, 1)

ghostwrite(transfused)

print transfused
