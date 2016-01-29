#-*- coding: utf-8 -*-

import os, io
import actions as ac

print "---------------------------------------------"
# print "\ncurrent directory:", os.listdir('.'), "\n"

draftcount = 0
pigcount = 0
draft_name = ''
pig_name = ''

# sourcefile = "assets/thesis-source-material.txt"
sourcefile = "assets/source-test.txt"


for draft in os.listdir("output/automated-drafts"):
    if draft.startswith("autodraft"):
        # print draft
        draftcount += 1
    if draft.startswith("pigpile"):
        # print draft
        pigcount += 1

draft_name = "output/automated-drafts/autodraft" + str(draftcount) + ".txt"
pig_name = "output/automated-drafts/pigpile" + str(pigcount) + ".txt"

def ghostwrite(inspiration):
    if isinstance(inspiration, list):
        print "converting from list..."
        inspiration = unicode(" ".join(inspiration), "utf-8")
    elif isinstance(inspiration, str):
        print "incoming string, making unicode..."
        inspiration = unicode(inspiration, "utf-8")
    with io.open(draft_name, "w", encoding="utf-8") as latest_draft:
        latest_draft.write(inspiration)
        print "wrote " + draft_name

def pigpile(inspiration):
    if isinstance(inspiration, list):
        print "converting from list..."
        inspiration = " " + " ".join(inspiration).encode("utf-8")
    elif isinstance(inspiration, str):
        inspiration = unicode(inspiration, "utf-8")
    with io.open(pig_name, "a", encoding="utf-8") as latest_draft:
        latest_draft.write(inspiration)
        print "wrote " + pig_name


with io.open(sourcefile, encoding="utf-8") as source:
    vein = source.read()

# transfused = ac.rearrange_lines(vein)

transfused = ac.peetree(vein)
# for i in range(20):
    # transfused = ac.garble(vein, i+1)
    # transfused += " "
    # pigpile(transfused)
    # print transfused


one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
two = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
ac.leaver(one, two, 0.5, spacing=4)

# ghostwrite(transfused)
# os.system("open " + draft_name)

# transfused = ac.garble(vein, 6)



# pigpile(transfused)

# print transfused


print "---------------------------------------------"
