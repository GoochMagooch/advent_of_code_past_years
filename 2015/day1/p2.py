with open("input.txt") as y:
    x = y.read().strip()

data = []
for i in x:
    data.append(i)

index = 0
counter = 0
for i in data:
    if i == '(':
        counter += 1
        index += 1
    elif i == ')':
        counter -= 1
        index += 1
    if counter == -1:
        print(index)
        break
