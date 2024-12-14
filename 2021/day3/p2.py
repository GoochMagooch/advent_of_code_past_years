with open("example.txt") as input:
    data = input.readlines()

rows = []
for line in data:
    lines = []
    for i in line.strip():
        lines.append(int(i))
    rows.append(lines)

oxygen = 0

for i in range(1):
    one_bits = []
    zero_bits = []
    for j in range(len(rows)):
        if rows[j][i] == 1:
            one_bits.append(rows[j])
        else:
            zero_bits.append(rows[j])
    if len(one_bits) > len(zero_bits):
        for i in range(1):
            one_bits_two = []
            zero_bits_two = []
            for j in range(len(one_bits)):
                if one_bits[j][1] == 1:
                    one_bits_two.append(one_bits[j])
                else:
                    zero_bits_two.append(one_bits[j])
        if len(one_bits_two) > len(zero_bits_two):
            for i in range(1):
                one_bits_three = []
                zero_bits_three = []
                for j in range(len(one_bits_two)):
                    if one_bits_two[j][2] == 1:
                        one_bits_three.append(one_bits_two[j])
                    else:
                        zero_bits_three.append(one_bits_two[j])
        else:
            for i in range(1):
                one_bits_three = []
                zero_bits_three = []
                for j in range(len(zero_bits_two)):
                    if zero_bits_two[j][2] == 1:
                        one_bits_three.append(zero_bits_two[j])
                    else:
                        zero_bits_three.append(zero_bits_two[j])
            if len(one_bits_three) > len(zero_bits_three):
                for i in range(1):
                    one_bits_four = []
                    zero_bits_four = []
                    for j in range(len(one_bits_three)):
                        if one_bits_three[j][3] == 1:
                            one_bits_four.append(one_bits_three[j])
                        else:
                            zero_bits_four.append(one_bits_three[j])
                if len(one_bits_four) > len(zero_bits_four):
                    for i in range(1):
                        one_bits_five = []
                        zero_bits_five = []
                        for j in range(len(one_bits_four)):
                            if one_bits_four[j][4] == 1:
                                one_bits_five.append(one_bits_four[j])
                            else:
                                zero_bits_five.append(one_bits_four[j])
                    if one_bits_five[-1] == 1:
                        oxygen = one_bits_five[-1]
                else:
                    for i in range(1):
                        one_bits_five = []
                        zero_bits_five = []
                        for j in range(len(zero_bits_four)):
                            if zero_bits_four[j][4] == 1:
                                one_bits_five.append(zero_bits_four[j])
                            else:
                                zero_bits_five.append(zero_bits_four[j])
            else:
                for i in range(1):
                    one_bits_four = []
                    zero_bits_four = []
                    for j in range(len(zero_bits_three)):
                        if zero_bits_three[j][3] == 1:
                            one_bits_four.append(zero_bits_three[j])
                        else:
                            zero_bits_four.append(zero_bits_three[j])
                if len(one_bits_four) > len(zero_bits_four):
                    for i in range(1):
                        one_bits_five = []
                        zero_bits_five = []
                        for j in range(len(one_bits_four)):
                            if one_bits_four[j][4] == 1:
                                one_bits_five.append(one_bits_four[j])
                            else:
                                zero_bits_five.append(one_bits_four[j])
                else:
                    for i in range(1):
                        one_bits_five = []
                        zero_bits_five = []
                        for j in range(len(zero_bits_four)):
                            if zero_bits_four[j][4] == 1:
                                one_bits_five.append(zero_bits_four[j])
                            else:
                                zero_bits_five.append(zero_bits_four[j])