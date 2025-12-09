from utils import input_utils
###TEST fct INPUT UTILS
"""
print(input_utils.ask_text("Enter your character's name: "))
print(input_utils.ask_number("Enter a number (0–10): ", 0))
print(input_utils.ask_choice("Do you want to continue?", ["Yes", "No"]))
"""
###Test assign house
from universe.house import assign_house

character = {
    "attributes": {
        "courage": 8,
        "intelligence": 7,
        "loyalty": 6,
        "ambition": 5
    }
}

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
 ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends",
 "Analyze the problem"],
 ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
 )
]
print(assign_house(character,questions))
