import os
import pprint
import json
import subprocess

pprint.pprint

def safe_ins_all_nba(player, award_str, award_type, award_dict):
    team = award_str.split('-')[2]
    award_year = "-".join(award_str.split('-')[:2])
    struct = {player: 
                    {award_type: 
                        {team: [award_year]} 
                    }
             }
    if player not in award_dict:
        award_dict[player] = struct[player]
    elif award_type not in award_dict[player]:
        award_dict[player][award_type] = struct[player][award_type]
    elif team not in award_dict[player][award_type]:
        award_dict[player][award_type][team] = struct[player][award_type][team]
    else:
        award_dict[player][award_type][team].append(struct[player][award_type][team][0])


def log(message, pref=None):
    print("LOGGER: " + pref)
    pprint.pprint(message, indent=4)
    print('------------------------------------')

stats_fp = os.getcwd() + "/stats/" 
files = os.listdir(stats_fp)
json_queue = []
for f in files:
    if 'json' in f:
        json_queue.append(f)
log(json_queue, pref='created json json_queue')

player_all_league_awards = {}
for f in json_queue:
    if 'all' in f and 'stats' in f:
        with open(stats_fp + f, 'r') as json_stats:
            data = json.load(json_stats)
            award_type = '_'.join(f.split('.')[0].split('_')[:2])
            for award_str in data:
                for player in data[award_str]:
                    safe_ins_all_nba(str(player), 
                            str(award_str), 
                            str(award_type),  
                            player_all_league_awards)

log(player_all_league_awards, 'parsed all league awards')
with open("aggregated_all_nba.json", 'w') as outfile:
    json.dump(player_all_league_awards, outfile)

tops = {}
mvp_names = json.load(open(os.getcwd() + '/top_emvps.json', 'r'))
for name in mvp_names:
    try:
        tops[name] = player_all_league_awards[name]
        tops[name]['eMVP score'] = mvp_names[name]
    except Exception:
        print 'player not in all league'

with open("top_players.json", 'w') as outfile:
    json.dump(tops, outfile)
