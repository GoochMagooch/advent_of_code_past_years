import re
with open("example.txt") as y:
    x = y.readlines()

data = []
for i in range(len(x)):
    data.append(x[i].replace(f'Game {i+1}: ', ''))

id_sum = 0
games = []
for i in data:
    games.append(i.split(';'))

games_stripped = []
for i in games:
    sublist = []
    games_stripped.append(sublist)
    for j in i:
        sublist.append(j.strip())
print(games_stripped)
