with open("input.txt") as x:
    y = x.readlines()

data = [line.strip() for line in y]

data_separated = []
for i in data:
    temp = []
    for j in i:
        temp.append(j)
    data_separated.append(temp)

int_data = []
operators = []
for i in data_separated:
    counter = 0
    temp = []
    integers = ''
    for j in i:
        if counter == 0:
            operators.append(i[0])
            counter += 1
        else:
            integers += i[counter]
            counter += 1
    integers.join('')
    int_data.append(int(integers))
print(int_data)
print(operators)

index = 0
frequency = 0
for i in operators:
    if i == '+':
        frequency += int_data[index]
        index += 1
    else:
        frequency -= int_data[index]
        index += 1
print(frequency)