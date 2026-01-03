import random
from utils.input_utils import load_file
from universe.house import update_house_points, display_winning_house
from universe.character import display_character


def create_team(house, team_data, is_player=False, player=None):
    players = team_data[house]

    team = {
        "name": house, "score": 0, "goals_scored": 0, "goals_blocked": 0,
        "caught_snitch": False, "players": players
    }
    if is_player and player is not None:
        np = []
        pname = player["First Name"] + " " + player["Last Name"]
        np.append(pname + " (Seeker)")
        i = 0
        while i < len(players):
            if players[i] != pname and players[i] != (pname + " (Seeker)"):
                np.append(players[i])
            i += 1

        team["players"] = np

    return team


def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance_goal = random.randint(1, 10)

    if chance_goal >= 6:
        if player_is_seeker:
            s = attacking_team["players"][0]
        else:
            s = random.choice(attacking_team["players"])
        attacking_team["score"] = attacking_team["score"] + 10
        attacking_team["goals_scored"] = attacking_team["goals_scored"] + 1
        print(s + " scores a goal for " + attacking_team["name"] + "! (+10 points)")
    else:
        defending_team["goals_blocked"] = defending_team["goals_blocked"] + 1
        print(defending_team["name"] + " blocks the attack!")


def golden_snitch_appears():
    return random.randint(1, 6) == 6


def catch_golden_snitch(e1, e2):
    w = random.choice([e1, e2])
    w["score"] = w["score"] + 150
    w["caught_snitch"] = True
    print("The Golden Snitch is caught by " + w["name"] + "! (+150 points)")
    return w


def display_score(e1, e2):
    print("Current score:")
    print("→ " + e1["name"] + ": " + str(e1["score"]) + " points")
    print("→ " + e2["name"] + ": " + str(e2["score"]) + " points")


def display_team(house, team):
    print(house + " team:")
    i = 0
    while i < len(team["players"]):
        print("- " + str(team["players"][i]))
        i += 1


def quidditch_match(character, houses):
    team_data = load_file("data/teams_quidditch.json")

    player_house = character["House"]
    all_houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    opps = []
    i = 0
    while i < len(all_houses):
        if all_houses[i] != player_house:
            opps.append(all_houses[i])
        i += 1
    opps_house = random.choice(opps)

    e1 = create_team(player_house, team_data, True, character)
    e2 = create_team(opps_house, team_data, False, None)

    print("Quidditch Match: " + e1["name"] + " vs " + e2["name"] + "!")
    display_team(e1["name"], e1)
    display_team(e2["name"], e2)
    print("You are playing for " + e1["name"] + " as the Seeker")
    input()
    turn = 1
    while turn <= 20:
        print("━━━ Turn " + str(turn) + " ━━━")
        attempt_goal(e1, e2, True)
        attempt_goal(e2, e1, False)
        display_score(e1, e2)

        if golden_snitch_appears():
            w = catch_golden_snitch(e1, e2)
            display_score(e1, e2)
            return w

        input("Press Enter to continue")
        turn += 1
    display_score(e1, e2)

    if e1["score"] > e2["score"]:
        return e1
    if e2["score"] > e1["score"]:
        return e2
    return None


def start_chapter_4_quidditch(character, houses):
    w = quidditch_match(character, houses)

    if w is None:
        print("The match ends in a tie.")
    else:
        print("Winner of the match: " + w["name"])
        update_house_points(houses, w["name"], 500)

    display_winning_house(houses)
    display_character(character)
    return character