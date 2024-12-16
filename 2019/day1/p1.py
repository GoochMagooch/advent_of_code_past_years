# import math module
import math

# read from input.txt, strip each line of whitespace and append ints to `data`
with open("input.txt") as i:
    d = i.readlines()
data = [int(line.strip()) for line in d]

# iterates through a list of modules and calculates total fuel needed
def find_fuel(modules):
    fuel_needed = 0
    for i in modules:
        fuel_needed += math.floor(i / 3 - 2)
    return fuel_needed

# answer for AoC/2019/day1/pt1
print(find_fuel(data))