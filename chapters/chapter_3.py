from utils.input_utils import load_file, ask_text
from random import randint
from universe.house import update_house_points, display_winning_house
from universe.character import display_character

def learn_spells(character, file_path="data/spells.json"):
    print("You begin your magic lessons at Hogwarts...")
    spells = load_file(file_path)

    utility = []
    defensive = []
    offensive = []

    for sp in spells:
        if sp["type"] == "Utility":
            utility.append(sp)
        elif sp["type"] == "Defensive":
            defensive.append(sp)
        elif sp["type"] == "Offensive":
            offensive.append(sp)

    learned = []

    i = randint(0, len(defensive) - 1)
    learned.append(defensive[i])

    i = randint(0, len(offensive) - 1)
    learned.append(offensive[i])

    picked = 0
    while picked < 3:
        i = randint(0, len(utility) - 1)
        if utility[i] not in learned:
            learned.append(utility[i])
            picked += 1

    if "Spells" not in character:
        character["Spells"] = []

    for sp in learned:
        character["Spells"].append(sp["name"])
        print("You have just learned:", sp["name"], "(", sp["type"], ")")
        input("Press Enter to continue...")

    print("You have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for name in character["Spells"]:
        print("-", name)


def magic_quiz(character, file_path="data/magic_quiz.json"):
    quiz = load_file(file_path)

    print("Welcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")
    input()

    asked = []
    correct = 0

    count = 0
    while count < 4:
        i = randint(0, len(quiz) - 1)
        if i in asked:
            continue
        asked.append(i)

        q = quiz[i]["question"]
        a = quiz[i]["answer"]

        user = ask_text(q + " ").strip()

        if user.lower() == a.lower():
            print("Correct answer! +25 points for your house.")
            correct += 1
        else:
            print("Wrong answer. The correct answer was:", a)

        input()
        count += 1

    points = correct * 25
    print("Quiz finished! You earned", points, "points.")
    return points


def start_chapter_3(character, houses):
    learn_spells(character, "data/spells.json")
    points = magic_quiz(character, "data/magic_quiz.json")

    house = character.get("house", None)
    if house is not None:
        update_house_points(houses, house, points)

    display_winning_house(houses)
    display_character(character)
    return character
