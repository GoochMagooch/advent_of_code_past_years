with open("test.txt") as y:
    d = y.readlines()

data = []
for i in d:
    data.append(i.strip().replace(' ', ''))
print(data)
