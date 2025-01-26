with open("example.txt") as y:
    x = y.readlines()

data = []
for i in x:
    data.append(i.strip().replace('Game ', ''))
print(data)

id_sum = 0
