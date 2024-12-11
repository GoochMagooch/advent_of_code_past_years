with open("input.txt") as input:
    data = input.readlines()

rows = []
for line in data:
    lines = []
    for i in line.strip():
        lines.append(int(i))
    rows.append(lines)

final_bin_gamma = []
final_bin_epsilon = []
for i in range(len(rows[0])):
    zero_bit = 0
    one_bit = 0
    for j in range(len(rows)):
        if rows[j][i] == 0:
            zero_bit += 1
        else:
            one_bit += 1
    if one_bit > zero_bit:
        final_bin_gamma.append(1)
        final_bin_epsilon.append(0)
    else:
        final_bin_gamma.append(0)
        final_bin_epsilon.append(1)


gamma = ''
for i in final_bin_gamma:
    gamma += str(i)
epsilon = ''
for i in final_bin_epsilon:
    epsilon += str(i)

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

print(binary_decoder(gamma))