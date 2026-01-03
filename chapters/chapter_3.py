import random
from utils.input_utils import load_file, ask_text
from universe.house import update_house_points, display_winning_house
from universe.character import display_character, add_item

def learn_spells(character, file_path="data/spells.json"):
    print("You begin your magic lessons at Hogwarts...")
    spells = load_file(file_path)

    utility = []
    defensive = []
    offensive = []

    i = 0
    while i < len(spells):
        sp = spells[i]
        if sp["type"] == "Utility":
            utility.append(sp)
        elif sp["type"] == "Defensive":
            defensive.append(sp)
        elif sp["type"] == "Offensive":
            offensive.append(sp)
        i += 1

    learned = []


    learned.append(defensive[randint(0, len(defensive) - 1)])
    learned.append(offensive[randint(0, len(offensive) - 1)])

    picked = 0
    while picked < 3:
        sp = utility[randint(0, len(utility) - 1)]
        if sp not in learned:
            learned.append(sp)
            picked += 1


    i = 0
    while i < len(learned):
        sp = learned[i]
        add_item(character, "Spells", sp["name"])
        print("You have just learned:", sp["name"], "(" + sp["type"] + ")")
        input("Press Enter to continue...")
        i += 1

    i = 0
    while i < len(learned):
        sp = learned[i]
        add_item(character, "Spells", sp["name"])
        print("You have just learned:", sp["name"], "(" + sp["type"] + ")")
        input("Press Enter to continue...")
        i += 1

    print("You have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    i = 0
    while i < len(character["Spells"]):
        print("-", character["Spells"][i])
        i += 1
    input()


def magic_quiz(character, file_path="data/magic_quiz.json"):
    quiz = load_file(file_path)

    print("Welcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")
    input()

    asked = []
    correct = 0

    count = 0
    while len(asked) < 4:
        i = random.randint(0, len(quiz) - 1)
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
