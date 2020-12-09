import random

# all the participants
members = [
    "robin",
    "holly",
    "pippa",
    "ella",
    "lily",
    "finn",
    "julian",
    "simon",
    "lucas",
]

# set some exclusions as to who is not allowed to pick each other
exclusions = {
    "robin": ["holly", "pippa"],
    "holly": ["robin", "pippa"],
    "pippa": ["robin", "holly"],
    "ella": ["lily", "finn"],
    "lily": ["ella", "finn"],
    "finn": ["ella", "finn"],
    "julian": ["simon", "lucas"],
    "simon": ["julian", "lucas"],
    "lucas": ["julian", "simon"],
}


def draw_names(members, exclusions):

    # all the participants names go into a hat
    hat = list(members)

    # clone the members as well
    candidates = list(members)

    # let's draw names!
    drawn_names = {}

    while len(candidates) > 0:

        candidate = random.choice(candidates)
        drawn_name = random.choice(hat)

        # if the only name left in the hat is the candidate, we restart
        if len(candidates) == 1 and len(hat) == 1 and candidates[0] == hat[0]:
            print(">> last candidate is the only name left in the hat")
            return {}

        # if the hat only contains exclusions for this candidate, we restart
        if candidate in exclusions and all(x in exclusions[candidate] for x in hat):
            print(">> only candidate exclusions left in hat")
            return {}

        # add the draw to the list if the draw is not the candidate and the draw is not excluded
        if drawn_name != candidate and (
            candidate in exclusions and drawn_name not in exclusions[candidate]
        ):
            hat.remove(drawn_name)
            candidates.remove(candidate)
            drawn_names[candidate] = drawn_name

    return drawn_names


# we might have to retry a few times under certain conditions
drawn_names = draw_names(members, exclusions)
while len(drawn_names) == 0:
    drawn_names = draw_names(members, exclusions)

# print the result
for candidate in drawn_names:
    print("{} drew {}".format(candidate, drawn_names[candidate]))
