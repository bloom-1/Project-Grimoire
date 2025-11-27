def update_house_points(houses, house_name, points):
    """
    The house_name parameter specifies which house’s score should be adjusted, and points is the
number of points to add (or subtract if negative). If the house exists, the function updates its score
and displays a message showing the change and the new total. If the house cannot be found, a
warning message is displayed. This function does not return a value but modifies the dictionary
passed as a parameter directly.
    """
    return None

def display_winning_house(houses):
    """
    This function displays the house with the highest score at a given moment. It receives a dictionary
of houses with the current scores as a parameter. If only one house is in the lead, it is displayed
as the winner. In the event of a tie, all the houses that are tied are listed.
    """

    if len(houses) == 1:
        return f"{...} house is the winner."
    for house in houses:
        ...
    return None

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