with open('test.txt') as x:
    data = x.readlines()

data_lines = [line.strip() for line in data]

def find_multiples(lst):
    unique = []
    dup_two = 0
    dup_three = 0

    # creates list of unique elements from lst
    for i in lst:
        temp = []
        for j in i:
            if not j in temp:
                temp.append(j)
        unique.append(temp)

    # counts how many elements in unique are in lst
    # and their frequency
    for i in range(len(unique)):
        for j in range(len(unique[i])):
            count = 0
            for k in range(len(lst[i])):
                if unique[i][j] == lst[i][k]:
                    count += 1
                else:
                    continue
            if count == 2:
                dup_two += 1
            elif count == 3:
                dup_three += 1
            else:
                continue
    print(dup_two * dup_three)

find_multiples(data_lines)