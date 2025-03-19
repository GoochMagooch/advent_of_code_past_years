with open('test.txt') as y:
    x = y.readlines()

data = []
for i in x:
    data.append(i.strip())
print(data)