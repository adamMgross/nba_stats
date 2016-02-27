import requests
from bs4 import BeautifulSoup
import json

url="http://www.basketball-reference.com/awards/awards_2015.html"

r = requests.get(url)
soup = BeautifulSoup(r.content)
first_division = soup.find_all("div", {"id":"div_mvp"})
soup = BeautifulSoup(str(first_division))
links = soup.find_all("a")

name = []

mvp_name = []

stats = []

holder_links = soup.find_all("td")
holder_soup = BeautifulSoup(str(holder_links))

for link in links:
    if "players" in str(link):
        name.append(str(link))

for name in name:
    mvp_name.append(name[name.index('html">')+6:name.index('</a')])

for line in holder_links:
    if "td align=\"right\">" in str(line):
        stats.append(str(line))

for i in range(len(mvp_name)):
    if "T" in stats[i]:
        stats[i] = stats[i][stats[i].index('right">')+7:stats[i].index("T")]
    else:
        stats[i] = stats[i][stats[i].index('right">')+7:stats[i].index('</td')]

for i in range(len(mvp_name)):
    stats[i] = stats[i * 18]

print stats
print mvp_name
with open('stats/mvp_names.json', 'w') as outfile:
    json.dump(mvp_name, outfile)