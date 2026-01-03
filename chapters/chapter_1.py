from utils.input_utils import ask_text, ask_number, ask_choice, load_file
from universe.character import init_character, display_character, modify_money, add_item


def introduction():
    print("Welcome to Chapter 1 – Arrival in the magical world")
    input()


def create_character():
    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")

    print("Choose your attributes:")
    courage = ask_number("Courage level (1-10): ", 1, 10)
    intelligence = ask_number("Intelligence level (1-10): ", 1, 10)
    loyalty = ask_number("Loyalty level (1-10): ", 1, 10)
    ambition = ask_number("Ambition level (1-10): ", 1, 10)

    attributes = {
        "courage": courage,
        "intelligence": intelligence,
        "loyalty": loyalty,
        "ambition": ambition
    }

    character = init_character(last_name, first_name, attributes)
    display_character(character)
    return character


def receive_letter():
    print("An owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    input()
    print("Dear Student,")
    print("We are pleased to inform you that you have been accepted to Hogwarts School of Witchcraft and Wizardry!")
    input()

    choice = ask_choice(
        "Do you accept this invitation and go to Hogwarts?",
        ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."]
    )

    if choice == "No, I'd rather stay with Uncle Vernon...":
        print("You tear up the letter, and Uncle Vernon cheers:")
        print("EXCELLENT! Finally, someone NORMAL in this house!")
        print("The magical world will never know you existed... Game over.")
        exit(0)


def meet_hagrid(character):
    print("Hagrid: 'Hello " + character["First Name"] + "! I'm here to help you with your shopping on Diagon Alley.'")
    input()
    choice = ask_choice("Do you want to follow Hagrid?", ["Yes", "No"])
    if choice == "No":
        print("Hagrid gently insists and takes you along anyway!")
    input()


def buy_supplies(character):
    inv = load_file("data/inventory.json")

    print("Welcome to Diagon Alley!")
    print("Catalog of available items:")

    for k in inv:
        print(str(k) + ". " + str(inv[k][0]) + " - " + str(inv[k][1]) + " Galleons")

    required = ["Magic Wand", "Wizard Robe", "Potions Book"]

    while len(required) > 0:
        print("You have " + str(character["Money"]) + " Galleons.")
        print("Remaining required items: " + ", ".join(required))

        num = ask_number("Enter the number of the item to buy: ", 1, len(inv))
        key = str(num)

        item_name = inv[key][0]
        price = inv[key][1]

        if item_name in character["Inventory"]:
            print("You already bought this item.")
            continue

        if character["Money"] < price:
            print("Not enough money. Game over.")
            exit(0)

        modify_money(character, -price)
        add_item(character, "Inventory", item_name)
        print("You bought: " + item_name + " (-" + str(price) + " Galleons).")

        i = 0
        while i < len(required):
            if required[i] == item_name:
                required.pop(i)
                break
            i += 1

    print("All required items have been purchased!")
    print("It's time to choose your Hogwarts pet!")
    print("You have " + str(character["Money"]) + " Galleons.")
    print("1. Owl - 20 galleons")
    print("2. Cat - 15 galleons")
    print("3. Rat - 10 galleons")
    print("4. Toad - 5 galleons")

    pet = ask_choice("Which pet do you want?", ["Owl", "Cat", "Rat", "Toad"])

    pet_price = 0
    if pet == "Owl":
        pet_price = 20
    elif pet == "Cat":
        pet_price = 15
    elif pet == "Rat":
        pet_price = 10
    else:
        pet_price = 5

    if character["Money"] < pet_price:
        print("Not enough money for this pet. Game over.")
        exit(0)

    modify_money(character, -pet_price)
    add_item(character, "Inventory", pet)
    print("You chose: " + pet + " (-" + str(pet_price) + " Galleons).")

    display_character(character)


def start_chapter_1():
    introduction()
    character = create_character()
    receive_letter()
    meet_hagrid(character)
    buy_supplies(character)
    print("End of Chapter 1! Your adventure begins at Hogwarts...")
    input()
    return character