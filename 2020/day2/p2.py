import csv

with open('test.csv') as x:
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

def password_validator(low_range_lst, high_range_lst, char_lst, pw_lst):
    count = 0
    for i in range(len(pw_lst)):
        low = low_range_lst[i] - 1
        high = high_range_lst[i] - 1
        char = char_lst[i]
        if not char in pw_lst[i] or len(pw_lst[i]) < high + 1:
            pass
        if pw_lst[i][low] == char and pw_lst[i][high] == char:
            pass
        elif pw_lst[i][low] == char or pw_lst[i][high] == char:
            count += 1
    return count

print(password_validator(lowers, highers, char_required, password))