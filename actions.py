import random, re, pattern.en as pat
from django.utils.encoding import smart_str, smart_unicode

let = r"[a-zA-Z]" #letters
con = r"[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]" #consonants
vow = r"[aeiouAEIOU]" #vowels
pun = r"[.,?!-]" #punctuation
two = r"\s+([a-zA-Z][a-zA-Z])\s+" #two-letter words
twoend = con + vow + pun + "|" + vow + con + pun #ending noises


def cleanstring(sample):
    # first = re.sub(u"(\u2018|\u2019)", "'", sample)
    # second = re.sub(u"(\u2026)", "...", first)
    final = re.sub(r"\[\s*.+\s*\]", "", sample)
    return final

def rearrange_lines(sample):
    plasma = list(sample)
    random.shuffle(plasma)
    transfusion = "".join(plasma)
    return transfusion

def garble(sample, sz):
    plasma = []
    transfusion = ""

    if sz == 1:
        cleaned = re.sub("[^a-zA-Z]", "", sample)
        plasma = list(cleaned)
        random.shuffle(plasma)
        transfusion = plasma

    elif sz == 2:
        sounds = r"[aeiouAEIOU][b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]|[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z][aeiouAEIOU]"
        for match in re.finditer(sounds, sample):
            plasma.append(match.group(0))
            # print match.group(0)
        random.shuffle(plasma)
        # print plasma
        transfusion = plasma

    elif sz == 3:
        sounds = vow + con + vow + "|" + con + vow + con + "|" + two + "|" + twoend
        sounds += "|" + vow + vow + con + "|" + con + vow + vow
        for match in re.finditer(sounds, sample):
            # print match.group(0)
            nugget = match.group(1) if match.group(1) is not None else match.group(0)
            plasma.append(nugget)
            # print nugget
        random.shuffle(plasma)
        # print plasma
        transfusion = plasma
    elif sz == 4:

        sounds = vow + con + vow + pun + "|" + con + vow + con + pun
        sounds += "|" + vow + vow + con + pun + "|" + con + vow + vow + pun

        for match in re.finditer(sounds, sample):
            plasma.append(match.group())
            # print match.group(0)

        sounds = let + let + let + let
        for match in re.finditer(sounds, sample):
            plasma.append(match.group())
            # print match.group(0)

        random.shuffle(plasma)
        # print plasma
        transfusion = plasma

    elif sz >= 5:
        sounds = let +"{"+ str(sz-1) +"}"+ pun
        sounds += "|" + let + "{"+ str(sz) +"}"

        for match in re.finditer(sounds, sample):
            plasma.append(match.group())
            # print match.group(0)

        random.shuffle(plasma)
        # print plasma
        transfusion = plasma


    return transfusion

def peetree(sample):
    plasma = []
    transfusion = ""

    happiness = cleanstring(sample)
    tree = pat.parsetree(happiness, replace={})
    for sentence in tree:
        plasma.append(unicode(sentence.string))
        # for verb in sentence.verbs:
            # transfusion.append(unicode(verb.string))
            # print verb.string
    random.shuffle(plasma)
    transfusion = "\n".join(plasma)
    return transfusion

def rumplestiltskin(one, two, howfarthrough, ramp=True):
    # print one, "\n", two
    spacing = 1
    tightness = 15

    start = int(howfarthrough * len(one))

    remainder = len(one) - start
    spacing = remainder / tightness

    keeptracker = start

    for nugget in two:
        if keeptracker < len(one):
            one.insert(keeptracker, nugget)
            keeptracker += spacing
            if ramp == True:
                if spacing > 1: spacing = int(round(remainder/tightness))
                # if spacing > 1: spacing -= 1
                if spacing == 0: spacing = 1
                remainder = len(one) - keeptracker
                print remainder, spacing
        else:
            one.append(nugget)
        keeptracker += 1

    print "------------"
    return one
