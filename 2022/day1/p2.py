with open("input.txt") as input:
    data = input.readlines()

data_lines = []
lines = []
for line in data:
    lines.append(line)
    if line == "\n":
        data_lines.append(lines)
        lines = []

new_data_lines = []
for i in data_lines:
    new_lines = []
    for j in i:
        new_lines.append(j.strip())
    new_data_lines.append(new_lines)

sums = []
for line in new_data_lines:
    sum = 0
    for element in line:
        if element.isdigit():
            sum += int(element)
        sums.append(sum)
lines_sorted = sorted(sums)

final_sum = 0
for i in range(1, 6, 2):
    final_sum += lines_sorted[-i]
print(final_sum)
