def ask_text(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("Enter valid input")
        else:
            return text


def ask_number(message, min_val=None, max_val=None):
    while True:
        number = int(input(message).strip())
        if min_val is not None and max_val is not None and number < min_val or number > max_val:
            print(f"Please enter a number between {min_val} and {max_val}.")
        elif min_val is not None and number < min_val:
            print(f"Please enter a number bigger than {min_val}.")
        elif max_val is not None and number > max_val:
            print(f"Please enter a number smaller than {max_val}.")
        else:
            return number



def ask_choice(message,options):
    while True:
        print(message)
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        choice = ask_number("Your choice:",1,len(options))
        return options[choice - 1]
        """
        if choice in range(1,len(options)+1):
            return choice
        else:
            print("Please enter a valid choice.")
        """

import json
def load_file(file_path):
    with open('file_path','r', encoding='utf-8') as f:
        data = json.load(f)
    return data



