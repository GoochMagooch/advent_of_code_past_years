with open("input.txt") as i:
    data = i.read()

# converts original list into list of ints
data_split = data.split(',')
data_ints = [int(i) for i in data_split]

''' 
iterates through a list of ints
if list[i] == 1 then add list[i + 1] and list[i + 2] then replace list[i + 3] with the sum
if list[i] == 2 then multiply list[i + 1] by list[i + 2] and replace list[i + 3] with the product
end program if list[i] = 99
'''
for i in range(0, len(data_ints), 4):
    if data_ints[i] == 1:
        first = data_ints[data_ints[i + 1]]
        second = data_ints[data_ints[i + 2]]
        sum_position = i + 3
        sum = first + second
        data_ints[data_ints[sum_position]] = sum
    if data_ints[i] == 2:
        first = data_ints[data_ints[i + 1]]
        second = data_ints[data_ints[i + 2]]
        prod_position = i + 3
        product = first * second
        data_ints[data_ints[prod_position]] = product
    if data_ints[i] == 99:
        break

# answer to AoC/2019/day2/pt1
print(data_ints[0])