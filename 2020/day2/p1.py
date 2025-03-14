with open('test.txt') as x:
    data = x.readlines()

data_stripped = [line.strip() for line in data]
print(data_stripped)