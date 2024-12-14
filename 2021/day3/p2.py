with open("example.txt") as input:
    data = input.readlines()

rows = []
for line in data:
    lines = []
    for i in line.strip():
        lines.append(int(i))
    rows.append(lines)
