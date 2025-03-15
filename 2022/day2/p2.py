with open("input.txt") as y:
    d = y.readlines()

data = [i.strip().replace(' ', '') for i in d]

p_one = []
p_two = []
for i in data:
    p_one.append(i[0])
    p_two.append(i[1])

def game(lst1, lst2):
    x = 1
    y = 2
    z = 3
    win = 6
    points = 0
    for i in range(len(lst1)):
        if lst1[i] == 'A' and lst2[i] == 'X':
                points += x + 3
        elif lst1[i] == 'B' and lst2[i] == 'Y':
                points += y + 3
        elif lst1[i] == 'C' and lst2[i] == 'Z':
                points += z + 3
        elif lst1[i] == 'A' and lst2[i] == 'Y':
            points += win + y
        elif lst1[i] == 'A' and lst2[i] == 'Z':
            points += z
        elif lst1[i] == 'B' and lst2[i] == 'X':
            points += x
        elif lst1[i] == 'B' and lst2[i] == 'Z':
            points += win + z
        elif lst1[i] == 'C' and lst2[i] == 'X':
            points += win + x
        elif lst1[i] == 'C' and lst2[i] == 'Y':
            points += y
    return points

answer = game(p_one, p_two)

print(f"Answer: {answer}")