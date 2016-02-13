import requests
from bs4 import BeautifulSoup
import json
import re

url="http://www.basketball-reference.com/awards/awards_2015.html"

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
links = soup.find_all("a")
tester = "players"

name = []

for link in links:
    if "players" in str(link):
        print (link)
        name.append(str(link))

name.pop(0)

with open('stats/names.json', 'w') as outfile:
    json.dump(name, outfile)
