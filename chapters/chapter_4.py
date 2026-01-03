from random import randint
from utils.input_utils import load_file
from universe.house import update_house_points, display_winning_house


def create_team(house, team_data, is_player=False, player=None):
    players = team_data[house]["players"]
    captain = team_data[house]["captain"]

    team = {
        "name": house,
        "captain": captain,
        "score": 0,
        "goals_scored": 0,
        "goals_blocked": 0,
        "caught_snitch": False,
        "players": players
    }

    if is_player and player is not None:
        pname = player["First Name"] + " " + player["Last Name"]
        seeker_name = pname + " (Seeker)"

        new_players = []

        i = 0
        while i < len(players):
            p = players[i]
            if "(Seeker)" in p:
                new_players.append(seeker_name)
            else:
                new_players.append(p)
            i += 1

        team["players"] = new_players

    return team


def attempt_goal(attacking_team, defending_team):
    chance_goal = randint(1, 10)

    if chance_goal >= 6:
        idx = randint(0, len(attacking_team["players"]) - 1)
        scorer = attacking_team["players"][idx]
        attacking_team["score"] = attacking_team["score"] + 10
        attacking_team["goals_scored"] = attacking_team["goals_scored"] + 1
        print(scorer + " scores a goal for " + attacking_team["name"] + "! (+10 points)")
    else:
        defending_team["goals_blocked"] = defending_team["goals_blocked"] + 1
        print(defending_team["name"] + " blocks the attack!")


def golden_snitch_appears():
    return randint(1, 6) == 6


def catch_golden_snitch(e1, e2):
    winner = e1
    if randint(0, 1) == 1:
        winner = e2

    winner["score"] = winner["score"] + 150
    winner["caught_snitch"] = True
    print("The Golden Snitch has been caught by " + winner["name"] + "! (+150 points)")
    return winner


def display_score(e1, e2):
    print("Current score:")
    print("→ " + e1["name"] + ": " + str(e1["score"]) + " points")
    print("→ " + e2["name"] + ": " + str(e2["score"]) + " points")


def display_team(team):
    print(team["name"] + " team (Captain: " + team["captain"] + "):")
    i = 0
    while i < len(team["players"]):
        print("- " + str(team["players"][i]))
        i += 1


def quidditch_match(character, houses_points):
    team_data = load_file("data/teams_quidditch.json")

    player_house = character["House"]
    all_houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    opponent_house = player_house
    while opponent_house == player_house:
        opponent_house = all_houses[randint(0, 3)]

    e1 = create_team(player_house, team_data, True, character)
    e2 = create_team(opponent_house, team_data, False, None)

    if len(e1["players"]) == 0 or len(e2["players"]) == 0:
        print("Error: one of the teams has no players.")
        exit(1)

    print("Chapter 4 — Quidditch Final!")
    print("Quidditch Match: " + e1["name"] + " vs " + e2["name"] + "!")
    display_team(e1)
    display_team(e2)
    input()

    turn = 1
    while turn <= 20:
        print("━━━ Turn " + str(turn) + " ━━━")

        attempt_goal(e1, e2)
        attempt_goal(e2, e1)
        display_score(e1, e2)

        if golden_snitch_appears():
            catch_golden_snitch(e1, e2)
            print("End of the match!")
            display_score(e1, e2)
            break

        input("Press Enter to continue")
        turn = turn + 1

    if e1["score"] > e2["score"]:
        print("Victory for " + e1["name"] + "!")
        update_house_points(houses_points, e1["name"], 500)
    elif e2["score"] > e1["score"]:
        print("Victory for " + e2["name"] + "!")
        update_house_points(houses_points, e2["name"], 500)
    else:
        print("It's a tie!")

    display_winning_house(houses_points)


def start_chapter_4_quidditch(character, houses_points):
    quidditch_match(character, houses_points)
    print("End of Chapter 4!")
    input()
    return character
