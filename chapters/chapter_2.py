from utils.input_utils import ask_choice, load_file
from universe.house import assign_house


def meet_friends(character):
    print("Hi! I'm Ron Weasley. Mind if I sit with you?")
    choice = ask_choice("How do you respond?", ["Sure, have a seat!", "Sorry, I prefer to travel alone."])

    if choice == "Sure, have a seat!":
        character["Attributes"]["loyalty"] += 1
    else:
        character["Attributes"]["ambition"] += 1

    print("Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    choice = ask_choice("How do you respond?", ["Yes, I love learning new things!", "Uh… no, I prefer adventures over books."])

    if choice == "Yes, I love learning new things!":
        character["Attributes"]["intelligence"] += 1
    else:
        character["Attributes"]["courage"] += 1

    print("I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    choice = ask_choice("How do you respond?", ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."])

    if choice == "Shake his hand politely.":
        character["Attributes"]["ambition"] += 1
    elif choice == "Ignore him completely.":
        character["Attributes"]["loyalty"] += 1
    else:
        character["Attributes"]["courage"] += 1

    print("Your updated attributes:", character["Attributes"])


def welcome_message():
    print("Professor Dumbledore : Welcome to Hogwarts everyone!")


def sorting_ceremony(character):
    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]

    final_house = assign_house(character, questions)
    character["House"] = final_house
    print("The Sorting Hat exclaims:", final_house + "!!!")


def enter_common_room(character):
    house_info = load_file("data/houses.json")
    house = character["House"]

    print(house_info[house]["emoji"], house_info[house]["description"])
    print(house_info[house]["installation_message"])
    print("Your house colors:", ",".join(house_info[house]["colors"]))


def start_chapter_2(character):
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)
    return character
