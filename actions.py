import random, re

def rearrange_lines(sample):
    plasma = list(sample)
    random.shuffle(plasma)
    transfusion = "".join(plasma)
    return transfusion

def garble(sample, cluster_size):
    blood = sample.read()
    cleaned = re.sub("[^a-zA-Z]", "", blood)
    plasma = list(cleaned)
    random.shuffle(plasma);
    transfusion = " ".join(plasma)
    return transfusion
