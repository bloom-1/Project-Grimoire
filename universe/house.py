from utils.input_utils import ask_choice


def update_house_points(houses, house_name, points):
    houses[house_name] = houses[house_name] + points
    print(house_name, "gains", points, "points. Total:", houses[house_name])


def display_winning_house(houses):
    best = None
    for h in houses:
        if best is None or houses[h] > best:
            best = houses[h]

    winners = []
    for h in houses:
        if houses[h] == best:
            winners.append(h)

    if len(winners) == 1:
        print("Winning house:", winners[0], "with", best, "points.")
    else:
        print("Tie between:", ", ".join(winners), "with", best, "points.")


def assign_house(character, questions):
    scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    att = character["Attributes"]

    scores["Gryffindor"] = scores["Gryffindor"] + att["courage"] * 2
    scores["Slytherin"] = scores["Slytherin"] + att["ambition"] * 2
    scores["Hufflepuff"] = scores["Hufflepuff"] + att["loyalty"] * 2
    scores["Ravenclaw"] = scores["Ravenclaw"] + att["intelligence"] * 2

    i = 0
    while i < len(questions):
        q, options, houses_for_options = questions[i]
        chosen = ask_choice(q, options)

        j = 0
        while j < len(options):
            if options[j] == chosen:
                scores[houses_for_options[j]] = scores[houses_for_options[j]] + 3
                break
            j += 1

        i += 1

    best_house = None
    best_score = None
    for h in scores:
        if best_score is None or scores[h] > best_score:
            best_score = scores[h]
            best_house = h

    return best_house
