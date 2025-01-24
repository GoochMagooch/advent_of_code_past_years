with open("input.txt") as x:
    y = x.read().strip()

data = []
for i in y:
    data.append(i)

counter = 0
for i in data:
    if i == '(':
        counter += 1
    elif i == ')':
        counter -= 1

print(counter)
