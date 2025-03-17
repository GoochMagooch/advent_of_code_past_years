# Reads data from input.txt
with open('input.txt') as x:
    # Assigns range limits to 'range_one' and 'range_two' as integers
    range_one, range_two = map(int, x.read().split('-'))

# Iterates through range and creates a list of string ranges to iterate through
range_strings = []
for i in range(range_one, range_two + 1):
    range_strings.append(str(i))

# Iterates through range_strings and creates individual lists of ranges, as integers, separated
range_list = []
for i in range_strings:
    temp = []
    for j in i:
        temp.append(int(j))
    range_list.append(temp)
print(range_list)

# Checks if conditions are true for each password
ans = 0
for i in range_list:
    for i in i:
        pass