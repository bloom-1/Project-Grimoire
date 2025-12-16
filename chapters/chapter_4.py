def create_team(house, team_data, is_player=False, player=None):
    team = {'name' : house[0], 'score':0, 'has_scored' : 0,
            'has_stopped' : 0, 'caught_snitch' : False,
            'players' : team_data}
    np = {}
    if is_player == True :
        np[team_data[0]] = 'Seeker'
        for i in range(1,len(team_data)):
            np[team_data[i]] = pass
