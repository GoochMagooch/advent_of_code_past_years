with open('input.txt') as x:
    data_first = x.read().split(',')
print(data_first)

data = []
for i in data_first:
    data.append(int(i))
print(data)

