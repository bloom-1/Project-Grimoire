def update_house_points(houses, house_name, points):
    """
    The house_name parameter specifies which house’s score should be adjusted, and points is the
number of points to add (or subtract if negative). If the house exists, the function updates its score
and displays a message showing the change and the new total. If the house cannot be found, a
warning message is displayed. This function does not return a value but modifies the dictionary
passed as a parameter directly.
    """
    if house_name in houses:
        houses[house_name] += points
        print(house_name, "gains", points, "points. Total:", houses[house_name])
    else:
        print("Unknown house:", house_name)



def display_winning_house(houses):
    """
    This function displays the house with the highest score at a given moment. It receives a dictionary
of houses with the current scores as a parameter. If only one house is in the lead, it is displayed
as the winner. In the event of a tie, all the houses that are tied are listed.
    """
    max_points = None

    for house_name in houses:
        points = houses[house_name]
        if max_points is None or points > max_points:
            max_points = points

    winners = []
    for house_name in houses:
        if houses[house_name] == max_points:
            winners.append(house_name)

    if len(winners) == 1:
        print("Winning house:", winners[0], "with", max_points, "points.")
    else:
        print("Tie between:", ", ".join(winners), "with", max_points, "points.")



from utils.input_utils import ask_choice
def assign_house(character, questions):
    """
    This function determines a player’s house by combining the character’s personal attributes with
their answers to the Sorting Hat’s personality test during the sorting ceremony. It takes the
following parameters:
• character: a dictionary representing the player’s character, including their attributes
(courage, intelligence, loyalty, ambition).
• questions: a list of tuples, each containing: (1) the question text, (2) a list of possible
choices, and (3) the corresponding houses for each answer.

The function calculates a score for each house: first by taking into account the player's character
attributes (each trait influences a specific house), then by adding points based on the answers to
the test.

Grimoire hint: The function’s logic follows these steps:
1. 2. 3. 4. Initialize a dictionary assigning a score of 0 to each house.
For each character attribute, retrieve its value (points) and multiply this value by 2 to
determine its influence on the corresponding house:
o Courage → courage points × 2 → add to Grybindor
o Ambition → ambition points × 2 → add to Slytherin
o Loyalty → loyalty points × 2 → add to Hublepub
o Intelligence → intelligence points × 2 → added to Ravenclaw
For each answer to the test, add 3 points to the house corresponding to the option chosen
by the player.
The house with the highest score becomes the player's final house, and the function
returns the name of that house.

!!!!! This function is used by sorting_ceremony(character) in the chapter_2 module to ensure that
the assignment runs smoothly. A complete example of execution is available in the dedicated
section. !!!!!
    """

    houses = {
        "Gryffindor" : 0,
    "Slytherin" : 0,
    "Hufflepuff" : 0,
    "Ravenclaw" : 0
    }

    att = character.get("attributes", {})

    courage = att.get("courage", 0)
    ambition = att.get("ambition", 0)
    loyalty = att.get("loyalty", 0)
    intelligence = att.get("intelligence", 0)

    houses["Gryffindor"] += courage * 2
    houses["Slytherin"] += ambition * 2
    houses["Hufflepuff"] += loyalty * 2
    houses["Ravenclaw"] += intelligence * 2

    for(question,choice,house_corresponding) in questions:
        sorting_choice = ask_choice(question, choice)
        house = house_corresponding[sorting_choice-1]
        houses[house] += 3


    highest_score = 0
    for house in houses:
        score = houses[house]
        if score > highest_score:
            highest_score = score
            final_house = house

    return final_house