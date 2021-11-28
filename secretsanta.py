import random
import itertools


def pick_names(families):
    exclusions = {}

    for family in families:
        for person in family:
            exclusions[person] = family

    everybody = list(itertools.chain.from_iterable(families))
    available = everybody.copy()
    random.shuffle(everybody)

    picks = {}

    for person in everybody:
        candidates = [p for p in everybody if p not in exclusions[person] and p in available]
        if len(candidates) == 0:
            return None
        # print(f"candidates for {person} are {candidates}")
        # print(f"available picks are {available}")
        picks[person] = random.choice(candidates)
        available.remove(picks[person])

    return picks


families = [
    ["robin", "holly", "pippa"],
    ["ella", "lily", "finn"],
    ["julian", "simon", "lucas", "vinn"],
]

picks = None
count = 0
while not picks:
    picks = pick_names(families)
    count = count + 1

for pick in picks:
    print(f"{pick} picked {picks[pick]}")

print(f"completed in {count} attempt(s)")
