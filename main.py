from utils import input_utils
###TEST fct INPUT UTILS
print(input_utils.ask_text("Enter your character's name: "))
print(input_utils.ask_number("Enter a number (0–10): ", 0))
print(input_utils.ask_choice("Do you want to continue?", ["Yes", "No"]))
