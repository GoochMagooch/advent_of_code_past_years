with open("example.txt") as input:
    data = input.readlines()

rows = [line.strip() for line in data]
while len(rows) > 1:
    ox_lst = []
    ones = []
    zeros = []
    # counter reinitializes on each while iteration
    counter = 0
    for i in range(len(rows[0])):
        for j in range(len(rows)):
            if rows[j][counter] == '1':
                ones.append(rows[i])
            elif rows[j][counter] == '0':
                zeros.append(rows[i])
    counter += 1        

    if len(ones) == len(zeros):
        ox_lst = ones
    elif len(ones) > len(zeros):
        ox_lst = ones
    elif len(ones) < len(zeros):
        ox_lst = zeros
        
    rows = ox_lst
ox_lst = rows
print(ox_lst)

'''
rows_two = [line.strip() for line in data]
c02_lst = []
one = []
zero = []
counter = 0
while len(rows_two) > 1:
    for i in range(len(rows_two)):
        if rows_two[i][counter] == '1':
            one.append(rows_two[i])
        elif rows_two[i][counter] == '0':
            zero.append(rows_two[i])
    whle len(one) > 1 and len(zero) > 1:
        if len(one) == len(zero):
            c02_lst = zero
        elif len(one) > len(zero):
            c02_lst = zero
        elif len(one) < len(zero):
            c02_lst = one
        
    rows_two = c02_lst
    counter += 1
'''
'''
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
'''
