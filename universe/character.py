def init_character(last_name, first_name, attributes):
    return {
        "Last Name": last_name,
        "First Name": first_name,
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }


def display_character(character):
    print("Character profile:")
    for key in character:
        value = character[key]

        if key == "Attributes":
            print("Attributes:")
            for att in value:
                name = att[0].upper() + att[1:]
                print("- " + name + ": " + str(value[att]))

        elif key == "Inventory" or key == "Spells":
            if len(value) == 0:
                print(key + ": ")
            else:
                parts = []
                i = 0
                while i < len(value):
                    parts.append(str(value[i]))
                    i += 1
                print(key + ": " + ", ".join(parts))

        else:
            print(key + ": " + str(value))

    print()


def modify_money(character, amount):
    character["Money"] = character["Money"] + amount


def add_item(character, key, item):
    character[key].append(item)
