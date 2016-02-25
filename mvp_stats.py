import requests
from bs4 import BeautifulSoup
import json

url="http://www.basketball-reference.com/awards/awards_2015.html"

r = requests.get(url)
soup = BeautifulSoup(r.content)
first_division = soup.find_all("div", {"id":"div_mvp"})
soup = BeautifulSoup(str(first_division))
links = soup.find_all("a")

mvp_name = []

for link in links:
    if "players" in str(link):
        print link
        mvp_name.append(str(link))


with open('stats/mvp_names.json', 'w') as outfile:
    json.dump(mvp_name, outfile)


# <div class="table_container" id="div_mvp">