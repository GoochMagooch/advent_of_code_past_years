with open("test.txt") as x:
    y = x.readlines()

data = [line.strip() for line in y]

lst = []
for i in data:
    placeholder_lst = []
    for j in i:
        placeholder_lst.append()
