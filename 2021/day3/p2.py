with open("input.txt") as input:
    data = input.readlines()

rows = [line.strip() for line in data]

# if there are more 0's than 1's in this column then do this
# else do this

ox_lst = []
c02_lst = []
for i in range(len(rows)):
    if rows[i][0] == '1':
        ox_lst.append(rows[i])
    elif rows[i][0] == '0':
        c02_lst.append(rows[i])

# find the most common digit in each row
counter = 0
while len(ox_lst) > 1:
    ox_final = []
    for i in range(len(ox_lst)):
        if ox_lst[i][counter] == '1':
            ox_final.append(ox_lst[i])
    ox_lst = ox_final
    counter += 1
print(ox_lst)
# finds the least common digit in each row
counter = 0
while len(c02_lst) > 1:
    c02_final = []
    for i in range(len(c02_lst)):
        if c02_lst[i][counter] == '0':
            c02_final.append(c02_lst[i])
    c02_lst = c02_final
    counter += 1
print(c02_lst)

oxygen = ''
for i in ox_lst:
    oxygen += str(i)
c02 = ''
for i in c02_lst:
    c02 += str(i)


def binary_decoder(string_of_ints):
    lst = []
    for i in string_of_ints:
        lst.append(int(i))

    char = 1
    decimal = 0
    for i in range(len(lst)):
        if lst[-1] == 1:
            decimal += char
            char *= 2
            lst.pop()
        else:
            char *= 2
            lst.pop()
    return decimal

print(binary_decoder(oxygen))
print(binary_decoder(c02))
