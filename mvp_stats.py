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

stats = []

# Creating file with "w+" so that we can read and write to it
# and it also truncates file every time
holder_file = open("D:\\NBA\\nba_stats\\prettify_holder.txt", "w+")

holder_links = soup.find_all("td")
holder_soup = BeautifulSoup(str(holder_links))

holder_file.write(holder_soup.prettify().decode("utf-8"))

flag = False
counter = 0

for line in holder_file:
    print counter
    counter = counter + 1
    print "hello"
    if (flag == True):
        stats.append(int(line))

    if "<td align=\"right\">" in line:
        flag = True
        print line
    else:
        flag = False

holder_file.close()

print stats
'''
for link in links:
    if "players" in str(link):
        print link
        mvp_name.append(str(link))


with open('stats/mvp_names.json', 'w') as outfile:
    json.dump(mvp_name, outfile)
'''



# <div class="table_container" id="div_mvp"> 83 lines