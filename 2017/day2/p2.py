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

print(data)

final_num = 0
for i in range(len(data)):
    placeholder = data[i]
    for item in placeholder:
        divisor = item
        counter = 0
        for j in range(len(placeholder)):
            num = divisor / placeholder[counter]
            if num.is_integer() and num > 1:
                final_num += num
            counter += 1
print(final_num)
