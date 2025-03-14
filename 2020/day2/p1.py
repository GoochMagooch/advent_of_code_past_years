with open('test.txt') as x:
    data = x.readlines()

data_stripped = [line.strip() for line in data]

def isolate_ranges(lst):
    temp_ranges = []
    for i in range(len(lst)):
        range_lst = []
        for j in range(3):
            range_lst.append(lst[i][j])
        temp_ranges.append(range_lst)

    ranges = []
    for i in temp_ranges:
        i.remove('-')
    for i in temp_ranges:
        temp = []
        for j in i:
            temp.append(int(j))
        ranges.append(temp)
    return ranges
range_lst = isolate_ranges(data_stripped)

# removes spaces from each password
data_strings = []
for i in data_stripped:
    data_string = ''
    for j in i:
        data_string += j
    data_strings.append(data_string.replace(' ', ''))
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