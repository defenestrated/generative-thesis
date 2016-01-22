import random, re, pattern.en as pat
from django.utils.encoding import smart_str, smart_unicode


def cleanstring(sample):
    # first = re.sub(u"(\u2018|\u2019)", "'", sample)
    # second = re.sub(u"(\u2026)", "...", first)
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
        transfusion = " ".join(plasma)
    elif sz == 2:
        sounds = r"[aeiouAEIOU][b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]|[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z][aeiouAEIOU]"
        for match in re.finditer(sounds, sample):
            plasma.append(match.group(0))
            # print match.group(0)
        random.shuffle(plasma)
        # print plasma
        transfusion = " ".join(plasma)

    return transfusion

def peetree(sample):
    # happiness = cleanstring(sample)
    tree = pat.parsetree(sample, encoding='utf-8')
    transfusion = []
    for sentence in tree:
        for verb in sentence.verbs:
            transfusion.append(verb.string)
    return transfusion
