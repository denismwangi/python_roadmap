from random import shuffle

players = ['joe', 'sue', 'sally','bob']

shuffle(players)
for p in players:
    print(p)

shuffle(players)
teams = []
for i in range(0, len(players), 2):
    teams.append([players[1], players[i+1]])
    print(teams)