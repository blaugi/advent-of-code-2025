with open("input.txt", "r") as file:
    database= [line.rstrip() for line in file.readlines()]

separating_index = database.index("")
fresh_ranges = [list(map(int, s_range.split("-"))) for s_range in database[:separating_index]]

fresh_ranges = sorted(fresh_ranges)
current_range = fresh_ranges[0]
solution = 0

for f_range in fresh_ranges[1:]:
    if f_range[1] <= current_range[1]:
        pass
    
    elif f_range[0] > current_range[1]:
        solution += 1 + (current_range[1] - current_range[0])
        current_range = f_range

    elif f_range[0] <= current_range[1]:
        current_range = [current_range[0], f_range[1]]

solution += 1 + (current_range[1] - current_range[0]) # add the remaining one

print(solution)

