import csv
with open('test.csv', newline='') as x:
    data = csv.reader(x, delimiter='[')
print(data)