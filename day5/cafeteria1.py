
with open("example.txt", "r") as file:
    database= [line.rstrip() for line in file.readlines()]


ranges = [ranges.split("-") for ranges in database[:database.index('')]]
ids= database[database.index('') + 1:]


print(ranges)
print(ids)