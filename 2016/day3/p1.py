import re

with open('input.txt', newline='') as x:
    data = x.readlines()

data_stripped = []
for i in data:
    data_stripped.append(i.strip())

data_split = []
for i in data_stripped:
    data_split.append(i.split(' '))

data_final = []
for i in data_split:
    temp = []
    for j in i:
        if len(j) > 0:
            temp.append(int(j))
    data_final.append(temp)
print(data_final)

def triangle_analyzer(lst_of_dimensions):
    count = 0
    for i in range(len(lst_of_dimensions)):
        if lst_of_dimensions[i][0] + lst_of_dimensions[i][1] > lst_of_dimensions[i][2]:
            count += 1
    return count

print(triangle_analyzer(data_final))