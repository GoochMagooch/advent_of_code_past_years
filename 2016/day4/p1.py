import csv
with open('input.csv', newline='') as x:
    data = csv.reader(x, delimiter='[')
    sector_str = []
    sector_id = []
    checksum = []
    for i in data:
        sector_str.append(i[0][:-3].replace('-', ''))
        sector_id.append(int(i[0][-3:]))
        checksum.append(i[1].replace(']', ''))

def find_checksum(sector_str_lst, id_lst, checksum_lst):
    sum = 0
    for i in range(len(sector_str_lst)):
        unique = ''     
        for j in range(len(sector_str_lst[i])):
            if not sector_str_lst[i][j] in unique and sector_str_lst[i][j] in checksum_lst[i]:
                unique += sector_str_lst[i][j]
        sorted_unique = ''.join(sorted(unique))
        if len(unique) == len(checksum[i]):
            if unique == checksum_lst[i] or sorted_unique == checksum_lst[i]:
                sum += 1
            else:
                continue
        else:
            continue
    return sum
print(find_checksum(sector_str, sector_id, checksum))