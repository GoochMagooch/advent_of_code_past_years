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

def password_validator(range1_lst, range2_lst, char_req_lst, pw_lst):
    low = 0
    high = 0
    for i in range(len(pw_lst)):
        char = char_req_lst[i]
        valid_pw = True
        char_count = 0
        if not char in pw_lst[i]:
            valid_pw = False
        else:
            for j in pw_lst[i]:
                if j == char:
                    char_count += 1
        if char_count >= low and char_count <= high:
            valid_pw
        else:
            valid_pw = False