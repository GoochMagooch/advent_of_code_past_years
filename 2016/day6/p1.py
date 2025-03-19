import csv

with open('input.csv', newline='') as x:
    data = csv.reader(x)
print(data)