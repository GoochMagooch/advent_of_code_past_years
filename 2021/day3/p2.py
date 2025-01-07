with open("input.txt") as input:
    data = input.readlines()

rows = []
for line in data:
    lines = []
    for i in line.strip():
        lines.append(int(i))
    rows.append(lines)

# calculates the number of 1's and 0's in each column of `rows`
# places those values in their respective categories of either 'gamma' or 'epsilon'
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
    if one_bit > zero_bit and one_bit == zero_bit:
        final_bin_gamma.append(1)
        final_bin_epsilon.append(0)
    else:
        final_bin_gamma.append(0)
        final_bin_epsilon.append(1)

# converts gamma and epsilon lists to strings of digits
gamma = ''
for i in final_bin_gamma:
    gamma += str(i)
epsilon = ''
for i in final_bin_epsilon:
    epsilon += str(i)

# converts strings of binary to the decimal value
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
        elif lst[-1] == 0:
            char *= 2
            lst.pop()
        else:
            print(f"{lst} is not a binary number")
    return decimal

power_consumption = binary_decoder(gamma) * binary_decoder(epsilon)
print(power_consumption)

ox_gen_rating = 0
c02_scrub_rating = 0
life_support = ox_gen_rating * c02_scrub_rating
print(life_support)

























