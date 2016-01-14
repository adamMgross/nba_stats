import all_nba
import p_of_week_month
from player import Player
import json


all_nba_stats = all_nba.get_stats()
pow_stats = p_of_week_month.get_stats_week()
print pow_stats
pom_stats = p_of_week_month.get_stats_month()
print pom_stats
with open('all_nba_stats.txt', 'w') as outfile:
    json.dump(all_nba_stats, outfile)
with open('players_of_the_week.txt', 'w') as outfile:
    json.dump(pow_stats, outfile)
with open('players_of_the_month.txt', 'w') as outfile:
    json.dump(pom_stats, outfile)
