import universe.character
import json
from random import random, randint
from universe.house import update_house_points, display_winning_house
from universe.character import display_character
"""Chapter 3 – Classes and discovering Hogwarts:
• Learning basic spells: 1 defensive spell, 1 oXensive spell, 3 utility spells.
• Mini-games related to Snape's classes (logic, memory, spell recognition, etc.)."""

def learn_spells(character, file_path="../data/spells.json"):
    print("You begin your magic lessons at Hogwarts...")
    sp = None

    with open('spells.json', 'r') as f:
        s = json.load(f)

    for spell in s['']:
        pass

    req = {"Offensive spell": 0, "Defensive spell" : 0, "Utility spell" : 0}

    while req[0] != 1 and req[1] != 1 and req[2] != 3:
        choice = random(s)
        for r in req:
            if choice[2] == r :
                r += 1
        sk = []
        print(f"You have just learned the spell : {choice} ({choice[2]})")
        sk.append(choice)
        input("Press Enter to continue...")

    input()
    print("You have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for i in sk :
        print(i, end="/NL")



def magic_quiz(character, file_path="../data/magic_quiz.json"):
    print("Welcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")
    input()
    """
    choose a random question
    compare the answer given to the correct answer
    if they are the same print "Correct answer! +25 points for your house." and add 25 points to the house
    else print "Wrong answer. The correct answer was: Wingardium Leviosa"
    after the 4 questions, print out the number of points acquired 
    """
    pass


def start_chapter_3(character, houses):
    learn_spells(character,file_path="../data/spells.json")
    magic_quiz(character, file_path="../data/magic_quiz.json")
    update_house_points(houses, ...)
    display_winning_house(houses)
    display_character(character)