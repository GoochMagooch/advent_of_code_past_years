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

# Find needed ribbon length for each present
ans = 0
for i in range(len(l)):
    p = 0
    max_side = max(l[i], w[i], h[i])

    # Find smallest perimeter for ribbon length
    if max_side == l[i]:
        p = (w[i] + w[i]) + (h[i] + h[i])
    elif max_side == w[i]:
        p = (l[i] + l[i]) + (h[i] + h[i])
    else:
        p = (l[i] + l[i]) + (w[i] + w[i])

    # Find extra ribbon needed for bow
    extra = l[i] * w[i] * h[i]

    # Total amount of ribbon needed
    ans += extra + p

print(ans)