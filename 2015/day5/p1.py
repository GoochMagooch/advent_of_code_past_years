with open('test.txt') as y:
    data = [i.strip() for i in y]

vowels = ['a', 'e', 'i', 'o', 'u']
nice = 0
for i in range(len(data)):
    count = 0
    '''
    # Counts vowels in each string
    vowel_count = 0
    for j in data[i]:
        if j in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        count += 1
    '''
    # Checks if string contains at least one set of repeating characters
    index = -1
    same_char_count = 0
    for j in range(len(data[i]) - 1):
        if data[i][index] == data[i][index - 1]:
            same_char_count += 1
        index -= 1
    if same_char_count > 0:
        count += 1

print(nice)