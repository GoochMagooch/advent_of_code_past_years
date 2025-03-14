with open('test.txt') as x:
    data = x.readlines()

data_stripped = [line.strip() for line in data]

# removes spaces from each password
data_strings = []
for i in data_stripped:
    data_string = ''
    for j in i:
        data_string += j
    data_strings.append(data_string.replace(' ', ''))
# isolate ranges
uppers = []
lowers = []
for i in data_strings:
    op = i.index('-')
    op_upper = op + 1
    double_upper = 0
    if i[op:3].isdigit():
        uppers.append(int(i[op:3]))
        uppers.append(double_upper)
    else:
        uppers.append(i[op_upper:2])
    lowers.append(i[:op])
print(uppers)
print(lowers)
# isolates required character
char_requirement = []
for i in data_strings:
    char_requirement.append(i[3])
# stores passwords from data strings
password = []
for i in data_strings:
    password.append(i[5:])

valid_count = 0
for i in range(len(range_lst)):
    char_count = 0
    for j in range(len(password[i])):
        if char_requirement[i] == password[i][j]:
            char_count += 1
    if char_count >= range_lst[i][0] and char_count <= range_lst[i][1]:
        valid_count += 1
print(valid_count)