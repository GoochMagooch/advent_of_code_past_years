import re
with open('input.txt') as input:
    data = input.readlines()

data_ints = []
for item in data:
    data_ints.append(re.sub("[^0-9]", "", item))

ints = []
for i in data_ints:
    fl = []
    fl.append(i[0])
    fl.append(i[-1])
    ints.append(int(''.join(fl)))

sum = 0
for i in ints:
    sum += i
print(sum)