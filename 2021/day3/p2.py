with open("example.txt") as input:
    data = input.readlines()

rows = [line.strip() for line in data]
while len(rows) > 1:
    ox_lst = []
    ones = []
    zeros = []
    # counter reinitializes on each while iteration
    counter = 0
    for i in range(len(rows[0])):
        for j in range(len(rows)):
            if rows[j][counter] == '1':
                ones.append(rows[i])
            elif rows[j][counter] == '0':
                zeros.append(rows[i])
    counter += 1        

    if len(ones) == len(zeros):
        ox_lst = ones
    elif len(ones) > len(zeros):
        ox_lst = ones
    elif len(ones) < len(zeros):
        ox_lst = zeros
        
    rows = ox_lst
ox_lst = rows
print(ox_lst)