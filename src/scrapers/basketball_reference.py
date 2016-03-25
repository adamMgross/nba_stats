import requests
from bs4 import BeautifulSoup
import json


'''
Takes in the type of stat that you are interested in
and the very first year for which the rankings are
available.
Dumps all the rankings extracted into json files for
later use.
'''

def dump_stats(type_of_stat, year):

    url = "http://www.basketball-reference.com/awards/awards_" + str(year) + ".html"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    first_division = soup.find_all("div", {"id":type_of_stat})
    soup = BeautifulSoup(str(first_division), "html.parser")
    links = soup.find_all("a")

    player_link = []

    players = []

    stats = []

    holder_links = soup.find_all("td")

    for link in links:
        if "players" in str(link):
            player_link.append(str(link))

    for player in player_link:
        players.append(player[player.index('html">')+6:player.index('</a')])

    num_of_players = len(players)

    # Every 18th statistic is the rank
    shift_amount_stats = 18

    for line in holder_links:
        if "<td align=\"right\">" in str(line):
            stats.append(str(line))

    for i in range(num_of_players):
        stats[i] = stats[i * shift_amount_stats]

    for i in range(num_of_players):
        if "T" in stats[i]:
            stats[i] = stats[i][stats[i].index('right">')+7:stats[i].index('T')]
        else:
            stats[i] = stats[i][stats[i].index('right">')+7:stats[i].index('</td')]


    stats_map = create_map_of_players_and_stats(players, stats)

    dir = '../../stats/Basketball_reference_stats/' + type_of_stat + '/' + str(year) + '_' + type_of_stat + '.json'

    with open(dir, 'w') as outfile:
        json.dump(stats_map, outfile)



'''
Takes in a list of players and their rankings in order
and then creates a map of the data
'''

def create_map_of_players_and_stats(players, stats):

    stats_map = {}
    counter = 0

    for player in players:
       stats_map[player] = stats[counter]
       counter += 1

    return stats_map