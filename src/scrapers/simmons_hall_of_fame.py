from bs4 import BeautifulSoup
import urllib2
import json

def split_to_clean_list(size_of_splits, original):
    to_return = []
    counter = 0
    for item in original:
        if counter != size_of_splits:
            if counter == 0:
                to_return.append([])
            to_return[len(to_return)-1].append(item)
            counter += 1
        if counter == size_of_splits:
            counter = 0
    return to_return

url = 'http://www.basketball-reference.com/awards/simmons_pyramid.html'
def get_stats(url):

    w = urllib2.urlopen(url)

    soup = BeautifulSoup(w, 'html.parser')

    x = soup.findAll('a')
    array_dump = x[34:130]
    for i in range(0, len(array_dump)):
        entry = str(array_dump[i])
        array_dump[i] = entry[entry.index('html')+6:entry.index('</a>')]
    
    array_dump.insert(0, 'This is to make each player\'s rank correspond with their index')
    return array_dump

data = get_stats(url)
with open('stats/simmons_hall_of_fame.json', 'w') as outfile:
    json.dump(data, outfile)
