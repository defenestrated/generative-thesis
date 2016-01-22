#-*- coding: utf-8 -*-

import os, io
import actions as ac

print "---------------------------------------------"
# print "\ncurrent directory:", os.listdir('.'), "\n"

draftcount = 0
draft_name = ''

sourcefile = "assets/thesis-source-material.txt"
# sourcefile = "assets/source-test.txt"


for draft in os.listdir("output/automated-drafts"):
    if draft.startswith("autodraft"):
        # print draft
        draftcount += 1

draft_name = "output/automated-drafts/autodraft" + str(draftcount) + ".txt"

def ghostwrite(inspiration):
    if isinstance(inspiration, list):
        print "converting from list..."
        inspiration = " ".join(inspiration).encode("utf-8")
    with io.open(draft_name, "w", encoding="utf-8") as latest_draft:
        latest_draft.write(inspiration)
        print "wrote " + draft_name


with io.open(sourcefile, encoding="utf-8") as source:
    vein = source.read()

# transfused = ac.rearrange_lines(vein)
# transfused = ac.garble(vein, 1)
transfused = ac.garble(vein, 2)
# transfused = ac.peetree(vein)

# print transfused

ghostwrite(transfused)



print "---------------------------------------------"
