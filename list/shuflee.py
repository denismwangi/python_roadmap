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

if 'bob' in players:
    print('yes')
else:
    print('no')

print(len(players))
players.append("jon")
print(players)
players.insert(1, "lucy")
print(players)
pep = players.pop()
print(pep)
print(players)
pep1 = players.clear()
print(players)
a = players[2:4] #numbers only
print(a)