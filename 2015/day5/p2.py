with open('input.txt') as y:
    data = [i.strip() for i in y]

ans = 0
for i in range(len(data)):
    nice = True

    # Checks if string contains at least one set of repeating characters
    index = -1
    same_char_count = 0
    for j in range(len(data[i]) - 1):
        if data[i][index] == data[i][index - 1]:
            same_char_count += 1
        index -= 1
    if same_char_count == 0:
        nice = False
        continue
    
    # Checks if string does not contain 'ab', 'cd, 'pq', or 'xy'
    index = -1
    # for j in range(4):
    for k in range((len(data[i])) - 1):
        if data[i][index] == 'b' and data[i][index - 1] == 'a':
            nice = False
            break
        elif data[i][index] == 'd' and data[i][index - 1] == 'c':
            nice = False
            break
        elif data[i][index] == 'q' and data[i][index - 1] == 'p':
            nice = False
            break
        elif data[i][index] == 'y' and data[i][index - 1] == 'x':
            nice = False
            break
        else:
            index -= 1

    if nice == True:
        ans += 1

print(ans)