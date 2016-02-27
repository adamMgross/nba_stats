import requests
from bs4 import BeautifulSoup
import json

url="http://www.basketball-reference.com/awards/awards_2015.html"

r = requests.get(url)
soup = BeautifulSoup(r.content)
first_division = soup.find_all("div", {"id":"div_mvp"})
soup = BeautifulSoup(str(first_division))
links = soup.find_all("a")

player = []

mvp_player = []

stats = []

holder_links = soup.find_all("td")
holder_soup = BeautifulSoup(str(holder_links))


for link in links:
    if "players" in str(link):
        player.append(str(link))

for player in player:
    mvp_player.append(player[player.index('html">')+6:player.index('</a')])

num_of_players = len(mvp_player)

for line in holder_links:
    if "<td align=\"right\">" in str(line):
        stats.append(str(line))

for i in range(num_of_players):
    stats[i] = stats[i * 18]

for i in range(num_of_players):
    if "T" in stats[i]:
        stats[i] = stats[i][stats[i].index('right">')+7:stats[i].index('T')]
    else:
        stats[i] = stats[i][stats[i].index('right">')+7:stats[i].index('</td')]


mvp_stats = {}
counter = 0
for player in mvp_player:
    mvp_stats[player] = stats[counter]
    counter += 1

with open('stats/mvp_names.json', 'w') as outfile:
    json.dump(mvp_stats, outfile)




# <div class="table_container" id="div_mvp"> 83 lines
>>>>>>> 4e83a26d835a9162093f33fdcc0e991518055e8f
