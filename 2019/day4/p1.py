# Reads data from input.txt and splits data by hyphen (-)
with open('input.txt') as x:
    data = x.read()
ranges = data.split('-')

# Assigns ranges to 'range_one' and 'range_two'
range_one = int(ranges[0])
range_two = int(ranges[1])

# 