with open("input.txt") as x:
    y = x.readlines()

# series of data cleaning
d = [line.replace('\t', ' ') for line in y]
a = [i.strip() for i in d]
t = []
for i in a:
    t.append(i.split(' '))

# create list named 'data' to manipulate
data = []
for i in t:
    ints = []
    for item in i:
        ints.append(int(item))
    data.append(ints)

counter = 0
for lst in data:
    largest = 0
    smallest = float('inf')
    for i in lst:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    counter += largest - smallest
print(counter)
