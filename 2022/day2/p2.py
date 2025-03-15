with open("input.txt") as y:
    d = y.readlines()

data = [i.strip().replace(' ', '') for i in d]

lst_one = []
lst_two = []
for i in data:
    lst_one.append(i[0])
    lst_two.append(i[1])

def game(lst):
    point = 1
    draw = 3
    win = 6
    points = 0
    for i in range(len(lst)):
        if lst[i] == 'X':
                points += point
        elif lst[i] == 'Y':
                points += point + draw
        else:
                points += point + win
    return points

answer = game(lst_two)

print(f"Answer: {answer}")