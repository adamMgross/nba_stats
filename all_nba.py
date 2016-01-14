from bs4 import BeautifulSoup
import urllib2

def split_list(size_of_splits, original):
    to_return = []
    counter = 0
    for item in original:
        if counter == 0:
            to_return.append([])
        to_return[len(to_return)-1].append(item)
        counter += 1
        if counter == size_of_splits:
            counter = 0
    return to_return

def get_stats():

    w = urllib2.urlopen('http://www.basketball-reference.com/awards/all_league.html')

    soup = BeautifulSoup(w, 'html.parser')

    x = soup.findAll('td')
    y = split_list(8, x)
    final = []
    for elem in y:
        final.append([])
        for shit in elem:
            shit = str(shit)
            if 'html' in shit:
                final[len(final)-1].append(shit[shit.index('html')+6:shit.index('</a')])
            else:
                final[len(final)-1].append(shit[13:16])

    return final


