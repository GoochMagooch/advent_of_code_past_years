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
    lowest = min(data_ints[i])
    highest = max(data_ints[i])
    ans += highest - lowest
print(ans)