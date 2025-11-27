def ask_text(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("Enter valid input")
        else:
            return text

name = ask_text("Enter your character's name: ")

def ask_number(message, min_val, max_val):
    while True:
        number = int(input(message).strip())
        if number < min_val or number > max_val:
            print(f"Please enter a number between {min_val} and {max_val}.")
        else:
            return number

choice_number = ask_number("Courage level (0-10): ",0,10)

def ask_choice(message,options):
    while True:
        print(message)
        for i in range(len(options)):
            print(i+1,"." ,options[i])
        choice = int(input("Your choice:"))
        if choice in range(1,len(options)+1):
            return choice
        else:
            print("Please enter a valid choice.")

choice_option = ask_choice("Do you want to continue?", ["Yes", "No"])
