import json
import yaml

def load(filename):
    with open(filename) as data_file:
        return yaml.safe_load(data_file)
"""
def load_pom():
    with open('players_of_the_month.txt') as data_file:
        return yaml.safe_load(data_file)

def load_pow():
    with open('players_of_the_week.txt') as data_file:
        return yaml.safe_load(data_file)

def load_all_nba_stats():
    with open('all_nba_stats.txt') as data_file:
      return yaml.safe_load(data_file)

def gather_week_month_info(pom_stats, pow_stats):
    data = {}
    
    for player in pom_stats:
        data[abbreviate_name(player)] = {"Player of the Month Awards": pom_stats[player]}
    for player in pow_stats:
        if player in pow_stats:
            data[player]["Player of the Week Awards"] = pow_stats[player]
        else:
            data[player] = {"Player of the Week Awards": pow_stats[player]}  
        
    return data

def gather_all_nba_info(all_nba):
    data = {}
    for team in all_nba:
        team_num = str(team[2][0])
        for i in range(3,8):
            player = team[i]
            if player not in data:
                data[player] = {team_num : 1}
            else:
                if team_num not in data[player]:
                    data[player][team_num] = 1
                else:
                    data[player][team_num] += 1
    return data
"""

def abbreviate_name(full_name):
    first = full_name[0] + '. '
    last = full_name[full_name.index(' ')+1:]
    return first + last
    

