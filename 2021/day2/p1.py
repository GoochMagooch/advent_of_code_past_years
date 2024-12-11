with open("input.txt") as input:
    data = input.readlines()

depth = 0
horizon = 0
digits = []
for line in data:
    if "down" in line:
        for i in line:
            if i.isdigit():
                depth += int(i)
    elif "up" in line:
        for i in line:
            if i.isdigit():
                depth -= int(i)
    elif "forward" in line:
        for i in line:
            if i.isdigit():
                horizon += int(i)

print("Depth: " + str(depth))
print("Horizon: " + str(horizon))
print(depth * horizon)