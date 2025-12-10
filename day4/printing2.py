import itertools

with open("input.txt", "r") as file:
    grid= file.readlines()

rolls = []
for line in grid:
    line_roll= [[c,0] for c in line.rstrip() ]
    rolls.append(line_roll)

moves = [1, 0, -1]
neigh = list(itertools.product(moves,moves))
neigh.pop(4) # remove (0,0)

count  = 0
increased = True
while increased:

    for idy, line in enumerate(rolls):
        for idx, column in enumerate(line):
            if column[0] == '@':
                for n in neigh:
                    neigh_y = idy + n[0] if 0 <= idy + n[0] < len(rolls) else None
                    neigh_x = idx + n[1] if 0 <= idx + n[1] < len(line) else None
                    if not (neigh_x is None or neigh_y is None):
                        if rolls[neigh_y][neigh_x]: #if neighbour exists add a neighbour count
                            rolls[neigh_y][neigh_x][1] += 1
    increased = False
    for line in rolls:
        for column in line:
            if column[1] < 4 and column[0] =="@":
                increased = True
                count += 1
                column[0] = "x"
            column[1] = 0

print(count)