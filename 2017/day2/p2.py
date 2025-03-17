# Reads data from file line by line
with open('input.txt') as y:
    x = y.readlines()

# Populate list with lines of data with white space removed
data_stripped = []
for i in x:
    data_stripped.append(i.strip())

# Separate numbers by tabs and populate separate list with strings converted to integers
data = []
for i in data_stripped:
    data.append(i.split('\t'))
data_ints = []
for i in data:
    temp = []
    for j in i:
        temp.append(int(j))
    data_ints.append(temp)

# Increments integer with the difference of the highest and lowest integer in each list
ans = 0
for i in range(len(data_ints)):
    quotient = 0
    for j in range(len(data_ints[i])):
        current = data_ints[i][j]
        count = 0
        for k in range(len(data_ints[i])):
            if current % data_ints[i][count] == 0 and data_ints[i][count] != current:  
                quotient = current / data_ints[i][count]
                break
            else:
                count += 1
        if quotient > 0:
            ans += quotient
            break
print(ans)