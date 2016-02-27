from bs4 import BeautifulSoup
import urllib2

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

def get_stats(url):

    w = urllib2.urlopen(url)

    soup = BeautifulSoup(w, 'html.parser')

    x = soup.findAll('td')
    y = split_to_clean_list(8, x)
    array_dump = []
    for elem in y:
        array_dump.append([])
        for shit in elem:
            shit = str(shit)
            if 'html' in shit:
                array_dump[len(array_dump)-1].append(shit[shit.index('html')+6:shit.index('</a')])
            else:
                array_dump[len(array_dump)-1].append(shit[13:16])

    final_dict = {}
    for entry in array_dump:
        year = entry[0]
        team = entry[2]
        identifier = year + '-' + team + 'team'
        players = entry[3:]
        final_dict [identifier] = players

    return final_dict

def organize_all_league_info(all_league):
    data = {}
    for team in all_league:
        team_num = str(team[2][0])
        for i in range(3,8):
            player = team[i]
            if player not in data:
                data[player] = {team_num : 1}
            else:
                if team_num not in data[player]:
                    data[player][team_num] = 1
                else:
                    data[player][team_num] += 1
    return data


