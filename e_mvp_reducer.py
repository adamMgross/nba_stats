import json
import pprint
import os


COEFF = -5

def rating_function(x):
    x = float(x)
    if x <= 3:
        return COEFF*pow(float(x/10), 2) + 1
    else:
        return float(1/x)

def main():
    pp = pprint.PrettyPrinter(indent=4)
    player_emvp_scores = {}
    filepath = os.getcwd() + '/stats/Basketball_reference_stats/div_mvp/'
    tag = '_div_mvp.json'
    for i in range(1956, 2016):
        f = open(filepath + str(i) + tag, 'r')
        mvp_results = json.load(f)
        for player in mvp_results:
            if player not in player_emvp_scores:
                player_emvp_scores[player] = rating_function(mvp_results[player])
            else:
                player_emvp_scores[player] += rating_function(mvp_results[player])


    x = []
    for player in player_emvp_scores:
        x.append((player_emvp_scores[player], str(player)))

    y = sorted(x)

    for i in range(0,15):
            print str(i + 1) + ": " + y[len(y) -i -1][1] + " " + str(y[len(y) -i -1][0])


for i in range(0,7):
    COEFF += 0.5
    print "COEFFICIENT: " + str(COEFF) + "------------------------"
    main()
    print "-------------------------------"