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
for i in range(len(data_separated)):
    integers = ''
    for j in data_separated[i]:
        if j == data_separated[i][0]:
            operators.append(j)
        else:
            integers += j
    int_data.append(int(integers))

frequency = 0
frequency_lst = []
for i in range(len(operators)):
    if operators[i] == '+':
        frequency += int_data[i]
        frequency_lst.append(frequency)
    else:
        frequency -= int_data[i]
        frequency_lst.append(frequency)

frequency_two = frequency
for i in range(len(operators)):
    if operators[i] == '+':
        frequency_two += int_data[i]
        if frequency_two in frequency_lst:
            print(frequency_two)
            break
    else:
        frequency_two -= int_data[i]
        if frequency_two in frequency_lst:
            print(frequency_two)
            break