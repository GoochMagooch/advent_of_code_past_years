import re
with open('input.txt') as input:
    data = input.readlines()

for i in range(len(data)):
    data[i] = data[i].replace("zero", "0")
    data[i] = data[i].replace("one", "1")
    data[i] = data[i].replace("two", "2")
    data[i] = data[i].replace("three", "3")
    data[i] = data[i].replace("four", "4")
    data[i] = data[i].replace("five", "5")
    data[i] = data[i].replace("six", "6")
    data[i] = data[i].replace("seven", "7")
    data[i] = data[i].replace("eight", "8")
    data[i] = data[i].replace("nine", "9")

data_ints = []
for item in data:
    data_ints.append(re.sub("[^0-9]", "", item))
print(data_ints)

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