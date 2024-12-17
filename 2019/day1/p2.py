# import math module
import math

# read from input.txt, strip each line of whitespace and append ints to `data`
with open("input.txt") as i:
    d = i.readlines()
data = [int(line.strip()) for line in d]

# iterates through a list of modules and finds necessary fuel to run that module
# then finds the fuel to run that fuel, and so on until it reaches close to 0
def find_fuel(modules):
    fuel_needed = 0
    for i in modules:
        counter = math.floor(i / 3 - 2)
        while counter > 0:
            fuel_needed += counter
            counter = math.floor(counter / 3 - 2)
    return fuel_needed

# answer for AoC/2019/day1/pt2
print(find_fuel(data))