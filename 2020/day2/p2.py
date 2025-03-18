import csv

with open('input.csv') as x:
    # Create csv object
    data = csv.reader(x, delimiter=' ')
    # Lists to populate with delimited columns of csv
    lowers = []
    highers = []
    char_required = []
    password = []
    # Loops through csv object to populate lists
    for row in data:
        quota, letter, pw = row[0], row[1][0], row[2]
        i = quota.index('-')
        lowers.append(int(quota[:i]))
        highers.append(int(quota[i + 1:]))
        char_required.append(letter)
        password.append(pw)
    x.close()

def password_validator(range1_lst, range2_lst, char_lst, pw_lst):
    count = 0
    # 
    for i in range(len(pw_lst)):
        # 
        char = char_lst[i]
        low = range1_lst[i]
        high = range2_lst[i]
        for j in range(1):
            if not char in pw_lst[i]:
                break
            if pw_lst[i].index(char) == low - 1 and pw_lst[i].index(char) == high - 1:
                break
            elif pw_lst[i].index(char) == low - 1 or pw_lst[i].index(char) == high - 1:
                count += 1
    return count

print(password_validator(lowers, highers, char_required, password))