from universe.character import init_character, display_character
import json
"""
Chapter 1 – Arrival in the magical world:
• Player’s character creation: last name, first name, and starting attributes.
• Receipt of the letter from Hogwarts.
• Meeting with Hagrid.
• Purchase of supplies on Diagon Alley (budget and inventory management).

The chapter_1.py module represents the first chapter of the adventure: arrival in the magical
world. This module integrates a series of functions that sequentially handle character creation,
receiving the Hogwarts letter, meeting Hagrid, and purchasing supplies prior to the journey to
school.
"""



def introduction():
    """
    This function displays the introductory text for the chapter. It should welcome the player and
announce the beginning of the story.
    """
    return "Welcome to Chapter 1 – Arrival in the magical world"

def create_character():
    """
    This function creates the main character (the player). It prompts the player to enter their first and
last names and assign a value from 1 to 10 to four qualities: courage, intelligence, loyalty, and
ambition. The values entered are grouped in an attributes dictionary, then given to the
init_character() function to create the complete character. Finally, the character's profile is
displayed on the screen.
    """
    fn = input("Enter your character's last name: ")
    ln = input("Enter your character's first name: ")

    print("Choose your attributes:")
    courage = int(input("Courage level (1-10): "))
    while courage < 0 or courage > 10 :
        courage = int(input("Courage level (1-10): "))

    intelligence = int(input("Intelligence level (1-10): "))
    while intelligence < 0 or intelligence > 10 :
        intelligence = int(input("Intelligence level (1-10): "))

    loyalty = int(input("Loyalty level (1-10): "))
    while loyalty < 0 or loyalty < 10 :
        loyalty = int(input("Loyalty level (1-10): "))

    ambition = int(input("Ambition level (1-10): "))
    while ambition <0 or ambition > 10 :
        ambition = int(input("Ambition level (1-10): "))

    attributes = {
        "Courage" : courage,
        "Intelligence" : intelligence,
        "Loyalty" : loyalty,
        "Ambition" : ambition
    }

    return init_character(ln, fn, attributes)


def receive_letter():
    """
    This function simulates receiving the Hogwarts acceptance letter. It displays the letter’s message
and gives the player two options: accept or decline. If the player declines, the game ends
immediately with a humorous message. If they accept, the adventure continues.
Grimoire hint: The exit() function immediately terminates program execution. Once called, no
further instructions are executed, and the program stops at that point. You can pass an exit code
to indicate the reason for termination: 0 for normal exit, or any other value to signal an error.
    """
    print("An owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    input()
    print("“Dear Student,")
    input()
    print("We are pleased to inform you that you have been accepted to Hogwarts School of Witchcraft and Wizardry!”")
    input()
    print("Do you accept this invitation and go to Hogwarts?")
    input()
    print("1. Yes, of course!")
    input()
    print("2. No, I'd rather stay with Uncle Vernon...")
    input()
    choice = 0
    while choice <= 0 or choice >= 3 :
        choice = int(input("Your choice : "))
    if choice == 1 :
        pass
    else :
        print("You tear up the letter, and Uncle Vernon cheers:")
        input()
        print("“EXCELLENT! Finally, someone NORMAL in this house!”")
        input()
        print("The magical world will never know you existed... Game over.")
        exit()



def meet_hagrid(character):
    """
This function introduces the character Hagrid. It displays a short dialogue and asks the player if
they want to follow him. Regardless of the choice, Hagrid ends up leading the player to Diagon
Alley.
    """
    print("Hagrid: 'Hello Harry! I’m here to help you with your shopping on Diagon Alley.'")
    input()
    print("Do you want to follow Hagrid?")
    input()
    print("1. Yes")
    input()
    print("2. No")
    input()
    choice = 0
    while choice <= 0 or choice >= 3 :
        choice = int(input("Your choice : "))
    print("Hagrid gently insists and takes you along anyway!")



def buy_suplies(character):
    """
This function allows to buy the required school supplies on Diagon Alley. The complete catalog is
loaded from the data/inventory.json file. The player must buy the three essential items: Magic
wand, Wizard robe, and Potions book.
Once these purchases have been made, the player must choose a pet from among the authorized
species:
• Owl - 20 galleons
• Cat - 15 galleons
• Rat - 10 galleons
• Toad - 5 galleons
Please note: The budget is checked before each purchase. If the player does not have enough
money or forgets a mandatory item, they lose the game.
Finally, the function displays the character's final inventory.
    """

    with open('inventory.json', 'r') as f:
        inv = json.load(f)

    for cat in inv['catalog']:
        print(cat)

    input()
    print(f"You have {character[3][0]} Galleons.")
    req = ["Magic Wand", "Wizard Robe", "Potions Book"]
    print(f"Remaining required items : {req}")
    choice = int(input("Enter the number of item to buy : "))
    p = 0
    for cat in inv['catalog']:
        if cat[0] == choice :
            it = cat[1]
            for car in cat[2]:
                try :
                    p += int(car)
                except:
                    continue
            if character[3][0] >= p :
                character[3][0] -= p
            else:
                print("You don't have enough Galleons")

    for i in req:
        if i == it:
            req -= it

    print(f"You bought : {it} (-{p} Galleons")
    input()
    print(f"You have {character[3][0]} Galleons.")
    print(f"Remaining required items : {req}")
    choice = int(input("Enter the number of item to buy : "))
    p = 0
    for cat in inv['catalog']:
        if cat[0] == choice:
            it = cat[1]
            for car in cat[2]:
                try:
                    p += int(car)
                except:
                    continue
            character[3][0] -= p

    for i in req:
        if i == it:
            req -= it
    print(f"You bought : {it} (-{p} Galleons")


    for ani in inv['pets']:
        print(ani)

    return None

def start_chapter_1():
    introduction()
    create_character()
    receive_letter()
    meet_hagrid(create_character())
    buy_suplies(create_character())
    print("End of Chapter 1! Your adventure begins at Hogwarts...")

    return display_character()