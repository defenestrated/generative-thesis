import os, random

print "\ncurrent directory:", os.listdir('.'), "\n"

draftcount = 0
draft_name = ''

for draft in os.listdir("output/automated-drafts"):
    if draft.startswith("autodraft"):
        draftcount += 1

draft_name = "autodraft" + str(draftcount) + ".txt"




vein = open("assets/thesis-source-material.txt")
# print vein.read()

plasma = list(vein)
random.shuffle(plasma)
transfusion = ''.join(plasma)

latest_draft = open(draft_name, "w")
latest_draft.write(transfusion)
print "wrote " + draft_name
