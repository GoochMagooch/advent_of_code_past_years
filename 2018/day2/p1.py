with open('test.txt') as x:
    data = x.read()

data_lines = []
for i in data:
    data_lines.append(i.strip())
print(data_lines)