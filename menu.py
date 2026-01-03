from utils.input_utils import ask_choice
from chapters import chapter_1, chapter_2, chapter_3, chapter_4


def display_main_menu():
    print("1. Start Chapter 1 – Arrival in the magical world.")
    print("2. Exit the game.")


def launch_menu_choice():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    display_main_menu()

    choice = ask_choice("Choose an option:", ["Start Chapter 1", "Exit"])

    if choice == 2 or choice == "Exit":
        return

    character = chapter_1.start_chapter_1()
    chapter_2.start_chapter_2(character)
    chapter_3.start_chapter_3(character, houses)
    chapter_4.start_chapter_4_quidditch(character, houses)