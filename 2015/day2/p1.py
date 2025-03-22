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
    min_side = min(l[i] * w[i], w[i] * h[i], l[i] * h[i])

    side1 = 2 * l[i] * w[i]
    side2 = 2 * w[i] * h[i]
    side3 = 2 * h[i] * l[i]

    dimensions.append(side1 + side2 + side3 + min_side)

ans = 0
for i in dimensions:
    ans += i
print(ans)