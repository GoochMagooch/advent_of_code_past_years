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
        j_iterator.append(j)
        for k in lines:
            if k + j_iterator[0] + iterator[0] == 2020:
                ans = k * j * i

print(ans)