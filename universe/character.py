def init_character(last_name : str, first_name : str, attributes)->dict:
    d = {
"Last Name": last_name,
"First Name": first_name,
"Money": 100,
"Inventory": [],
"Spells": [],
"Attributes": attributes
}
    return d


def display_character(character):
    """
This function displays the player's character information: full name, amount of money available,
attributes, inventory contents, and spells mastered, as well as all new information that may be
added to the character throughout the game (other fields will be introduced later). It should be
used to help the player track their character's progress and possessions throughout the
adventure.
Grimoire hint: Consider iterating directly over the keys of a dictionary. If a key’s value is:
• a dictionary: iterate through its subkeys to display the nested information.
• a list: convert its elements to strings and join them using join().
• otherwise, simply display the value.
    """
    return None

def modify_money(character, amount):
    """
   This function receives a positive or negative integer (the amount parameter) and adds it to the
player's character's current amount of money.
Grimoire hint: Use this function to manage the player's financial transactions throughout the
game.
    """
    return None


def add_item(Character, key, item):
    """
    This function adds an item to the list corresponding to the field specified by the key parameter in
the character dictionary. The key can be either 'Inventory' or 'Spells'. The item, passed as a string,
is appended to the specified list.
Grimoire hint: Call this function whenever the player obtains or recovers a new item or spell
during their journey.
    """