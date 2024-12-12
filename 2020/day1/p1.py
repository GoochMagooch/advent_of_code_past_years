with open("input.txt") as input:
    data = input.readlines()

lines = []
for line in data:
    lines.append(int(line.strip()))

ans = 0
for i in lines:
    iterator = []
    iterator.append(i)
    for j in lines:
        j_iterator = []
        if j + iterator[0] == 2020:
            ans = j * i

print(ans)