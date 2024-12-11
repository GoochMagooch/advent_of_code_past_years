with open("input.txt") as input:
    data = input.readlines()

data_ints = []
for line in data:
    data_ints.append(int(line.strip()))

incr = 0
decr = 0

for i in range(1, len(data_ints)):
    if data_ints[i] > data_ints[i - 1]:
        incr += 1
    elif data_ints[i] < data_ints[i - 1]:
        decr += 1

print(incr)
print(decr)