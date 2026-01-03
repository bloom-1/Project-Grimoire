import json


def ask_text(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("Enter valid input")
        else:
            return text


def _is_integer_string(s):
    if s == "":
        return False

    i = 0
    if s[0] == "-":
        if len(s) == 1:
            return False
        i = 1

    while i < len(s):
        c = s[i]
        if c < "0" or c > "9":
            return False
        i += 1
    return True


def _to_integer(s):
    sign = 1
    i = 0
    if s[0] == "-":
        sign = -1
        i = 1

    n = 0
    while i < len(s):
        n = n * 10 + (ord(s[i]) - ord("0"))
        i += 1
    return sign * n


def ask_number(message, min_val=None, max_val=None):
    while True:
        raw = input(message).strip()

        if not _is_integer_string(raw):
            print("Please enter a valid integer.")
            continue

        number = _to_integer(raw)

        if min_val is not None and max_val is not None and (number < min_val or number > max_val):
            print("Please enter a number between " + str(min_val) + " and " + str(max_val) + ".")
        elif min_val is not None and number < min_val:
            print("Please enter a number bigger than " + str(min_val) + ".")
        elif max_val is not None and number > max_val:
            print("Please enter a number smaller than " + str(max_val) + ".")
        else:
            return number


def ask_choice(message, options):
    print(message)
    i = 0
    while i < len(options):
        print(str(i + 1) + ". " + str(options[i]))
        i += 1
    choice_num = ask_number("Your choice: ", 1, len(options))
    return options[choice_num - 1]


def load_file(file_path):
    f = open(file_path, "r")
    data = json.load(f)
    f.close()
    return data
