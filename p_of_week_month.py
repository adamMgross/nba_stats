from bs4 import BeautifulSoup
import urllib2

months = ['January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December']

def get_stats_week():
    raw = urllib2.urlopen('http://www.basketball-reference.com/awards/pow.html')
    soup = BeautifulSoup(raw, 'html.parser')

    x = soup.findAll('a')

    string_x = []
    for thing in x:
        string_x.append(str(thing))

    players = []
    for thing in string_x:
        for month in months:
            if month in thing:
                players.append(thing[thing.index('html">')+6:thing.index('</a')])
    count = {}

    for player in players:
        if player in count:
            count[player] += 1
        else:
            count[player] = 1

    return count

def get_stats_month():
    raw = urllib2.urlopen('http://www.basketball-reference.com/awards/pom.html')
    soup = BeautifulSoup(raw, 'html.parser')

    x = soup.findAll('a')

    string_x = []
    for thing in x:
        string_x.append(str(thing))

    players = []
    for thing in string_x:
        for month in months:
            if month in thing:
                players.append(thing[thing.index('html">')+6:thing.index('</a')])
    count = {}

    for player in players:
        if player in count:
            count[player] += 1
        else:
            count[player] = 1

    sorted_players = sorted(count, key=count.get)
    return count
