import sys
with open('input.txt') as x:
    data_first = x.read().split(',')

data = []
for i in data_first:
    data.append(int(i))

position = 1
lowest_fuel = sys.maxsize
lowest_position = 0
fuel_step = 1
    
for i in range(len(data)):
    fuel = 0
    for j in data:
        difference = 0
        if j >= position:
            difference = j - position
        else:
            difference = position - j
        fuel += difference
    if fuel < lowest_fuel:
        lowest_fuel = fuel
        lowest_position = position
    position += 1
print(lowest_fuel)
print(lowest_position)