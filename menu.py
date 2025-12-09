from universe.house import assign_house
from chapters import chapter_1, chapter_2, chapter_3, chapter_4, chapter_5_extension
def display_main_menu():
    print("1. Start Chapter 1 – Arrival in the magical world.")
    print("2. Exit the game.")


def launch_menu_choice():
    houses = {}
    choice = int(input(""))
    while choice != 1 or choice != 2:
        choice = int(input("Please choose a number between 1 and 2."))
    if choice == 2 :
        exit()
    else :
        chapter_1.start_chapter_1()
        chapter_2.welcome_message()
        chapter_3.