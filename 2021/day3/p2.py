with open("example.txt") as input:
    data = input.readlines()

rows = [line.strip() for line in data]

'''
ones = []
counter = 0
for i in rows:
    temp_lst = []
    if int(i[counter]) == 1:
        temp_lst.append(int(i))
    else:
        continue
    if len(temp_lst) == 1:
        ones.append(temp_lst)
        break
    counter += 1
print(ones)
'''

def find_ones(lst):
    ones = [-1, -2]
    while len(ones) > 1:
        counter = 0
        for i in lst:
            if lst[counter] == 1:
                ones.append(f"{counter}: {lst[i]}")
            else:
                continue
        counter += 1
        for item in ones:
            if int(item[counter - 1][0]) < counter:
                ones.remove(ones[item])
        if len(ones) == 1:
            ones.append(ones)
        return ones
print(find_ones(rows))

'''
int_lst = []
for i in rows:
    temp_lst = []
    for j in i:
        temp_lst.append(int(j))
    int_lst.append(temp_lst)
print(int_lst)
'''

'''
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