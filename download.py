import all_league
import p_of_week_month
import json


all_nba_stats = all_league.get_stats('http://www.basketball-reference.com/awards/all_league.html')
all_defense_stats = all_league.get_stats('http://www.basketball-reference.com/awards/all_defense.html')
all_rookie_stats = all_league.get_stats('http://www.basketball-reference.com/awards/all_rookie.html')
pow_stats = p_of_week_month.get_stats_week()
pom_stats = p_of_week_month.get_stats_month()

with open('stats/all_defense_stats.json', 'w') as outfile:
    json.dump(all_defense_stats, outfile)
with open('stats/all_nba_stats.json', 'w') as outfile:
    json.dump(all_nba_stats, outfile)
with open('stats/all_rookie_stats.json', 'w') as outfile:
    json.dump(all_rookie_stats, outfile)
with open('stats/players_of_the_week.json', 'w') as outfile:
    json.dump(pow_stats, outfile)
with open('stats/players_of_the_month.json', 'w') as outfile:
    json.dump(pom_stats, outfile)
