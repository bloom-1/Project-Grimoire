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
    if len(houses) == 1:
        return f"{...} house is the winner."
    for house in houses:
        if