with open('input.txt') as x:
    y = x.readlines()

data = [i.strip() for i in y]
print(data)