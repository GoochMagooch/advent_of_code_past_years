import sys
import csv
with open("input.csv") as y:
    x = csv.reader(y, delimiter='x')
    l = []
    w = []
    h = []
    for i in x:
        l.append(int(i[0]))
        w.append(int(i[1]))
        h.append(int(i[2]))

# 2*l*w + 2*w*h + 2*h*l
dimensions = []
for i in range(len(l)):
    count = 0
    min_side = sys.maxsize
    temp = []

    side1 = 2 * l[i] * w[i]
    count += 1
    temp.append(l[i])
    side2 = 2 * w[i] * h[i]
    count += 1
    temp.append(w[i])
    side3 = 2 * h[i] * l[i]
    count += 1
    temp.append(h[i])

    for i in range(count):
        if temp[i] < min_side:
            min_side = temp[i]
    dimensions.append(side1 + side2 + side3 + min_side)

ans = 0
for i in dimensions:
    ans += i
print(ans)