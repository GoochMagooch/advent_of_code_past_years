with open("input.txt") as input:
    data = input.readlines()

depth = 0
aim = 0
horizon = 0
for line in data:
    if "down" in line:
        for i in line:
            if i.isdigit():
                aim += int(i)
    elif "up" in line:
        for i in line:
            if i.isdigit():
                aim -= int(i)
    elif "forward" in line:
        for i in line:
            if i.isdigit():
                horizon += int(i)
                depth += aim * int(i)

print(horizon * depth)