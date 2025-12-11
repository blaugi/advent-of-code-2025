
with open("input.txt", "r") as file:
    database= [line.rstrip() for line in file.readlines()]

separating_index = database.index("")
fresh_ranges, ingredients = [list(map(int, s_range.split("-"))) for s_range in database[:separating_index]], [int(l) for l in database[separating_index+1:]]

#key here is any() since it likely early exits at the first found range
print(len([l for l in ingredients if any([(b[0] <= l and l <= b[1]) for b in fresh_ranges])]))
