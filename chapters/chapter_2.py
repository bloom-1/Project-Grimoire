"""Chapter 2 – The journey to Hogwarts:
• Meeting Ron, Hermione, and Draco.
• House selection via direct choice or personality test (minimum of 3 questions).
• Settling into the common room.
The chapter_2.py module manages the second chapter of the adventure, "The Journey to
Hogwarts," """
from utils.input_utils import *
from universe.house import assign_house

def meet_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward...")
    input()
    print("A red-haired boy enters your compartment, looking friendly.")
    input()
    print("Hi ! I'm Ron Weasley. Mind if I sit with you?")
    ron_choice = ask_choice("How do you respond?",["Sure, have a seat!","Sorry, i prefer to travel alone."])
    if ron_choice == 1:
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        character["attributes"]["loyalty"] += 1
    elif ron_choice == 2:
        print("Oh... Ok")
        character["attributes"]["ambition"] += 1
    input()
    print("A girl enters next, already carrying a stack of books.")
    input()
    print("Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'")
    input()
    hermione_choice = ask_choice("How do you respond?",["Yes, I love learning new things!","Uh... no, I prefer adventures over books."])
    if hermione_choice == 1:
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        character["attributes"]["intelligence"] += 1
    elif hermione_choice == 2:
        character["attributes"]["courage"] += 1
    input()
    print("Then a blonde boy enters, looking arrogant.")
    input()
    print("I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think ?")
    draco_choice = ask_choice("How do you respond?",["Shake his hand politely","Ignore him completely.","Respond with arrogance."])
    if draco_choice == 1:
        character["attributes"]["ambition"] += 1
    elif draco_choice == 2:
        print("Draco frowns, annoyed. — You'll regret that!")
        character["attributes"]["loyalty"] += 1
    elif draco_choice == 3:
        character["attributes"]["courage"] += 1
    input()
    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    input()
    print("Your choices already say a lot about your personality!")
    input()
    print(f"Your updated attributes: {character['attributes']}")
def welcome_message():
    input()
    return "Professor Dumbledore : Welcome !"

def sorting_ceremony(character):
    input()
    print("The sorting ceremony begins in the Great Hall...")
    input()
    print("The sorting Hat observes")
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
    character["house"] = final_house
    print("Sorting Hat : Uhmmm... I see")
    input()
    print(f"The Sorting Hat exclaims: {final_house}!!!")
    input()
    print(f"You join the {final_house} students to loud cheers!")
    input()


def enter_common_room(character):
    input()
    print("You follow the prefects through the castle corridors...")
    input()
    house_info = load_file("houses.json")
    input()
