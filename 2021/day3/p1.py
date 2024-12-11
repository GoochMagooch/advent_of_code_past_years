with open("input.txt") as input:
    data = input.readlines()

rows = []
for line in data:
    lines = []
    for i in line.strip():
        lines.append(int(i))
    rows.append(lines)

final_bin = []
for i in range(len(rows[0])):
    zero_bit = 0
    one_bit = 0
    for j in range(len(rows)):
        if rows[j][i] == 0:
            zero_bit += 1
        else:
            one_bit += 1
    if one_bit > zero_bit:
        final_bin.append(1)
    else:
        final_bin.append(0)

gamma = ''
for i in final_bin:
    gamma += str(i)
print(gamma)