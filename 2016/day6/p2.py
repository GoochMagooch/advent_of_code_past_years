import sys
with open('input.txt') as x:
    y = x.readlines()

data = []
for i in y:
    data.append(i.strip())

columns = []
for i in range(len(data[0])):
    temp = []
    for j in range(len(data)):
        temp.append(data[j][i])
    columns.append(temp)

unique_chars = []
for i in columns:
    temp = []
    for j in i:
        if not j in temp:
            temp.append(j)
    unique_chars.append(temp)

ans = ''
for i in range(len(unique_chars)):
    least_common = sys.maxsize
    char = ''
    for j in unique_chars[i]:
        temp_int = 0
        for k in range(len(columns[i])):
            if j == columns[i][k]:
                temp_int += 1
        if temp_int < least_common:
            least_common = temp_int
            char = j
    ans += char
print(ans)