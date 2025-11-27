from universe.character import init_character, display_character

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
    return None

def create_character():
    """
    This function creates the main character (the player). It prompts the player to enter their first and
last names and assign a value from 1 to 10 to four qualities: courage, intelligence, loyalty, and
ambition. The values entered are grouped in an attributes dictionary, then given to the
init_character() function to create the complete character. Finally, the character's profile is
displayed on the screen.
    """
    init_character()
    return None

def receive_letter():
    """
    This function simulates receiving the Hogwarts acceptance letter. It displays the letter’s message
and gives the player two options: accept or decline. If the player declines, the game ends
immediately with a humorous message. If they accept, the adventure continues.
Grimoire hint: The exit() function immediately terminates program execution. Once called, no
further instructions are executed, and the program stops at that point. You can pass an exit code
to indicate the reason for termination: 0 for normal exit, or any other value to signal an error.
    """
    return None

def meet_hagrid(character):
    """
This function introduces the character Hagrid. It displays a short dialogue and asks the player if
they want to follow him. Regardless of the choice, Hagrid ends up leading the player to Diagon
Alley.
    """
    return None

def buy_cuplies(character):
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
    return None

def start_chapter_1():
    introduction()
    create_character()
    receive_letter()
    meet_hagrid()
    buy_cuplies()
    print("End of Chapter 1! Your adventure begins at Hogwarts...")

    return display_character()