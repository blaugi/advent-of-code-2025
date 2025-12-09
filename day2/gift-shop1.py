with open("example.txt", "r") as file:
    ranges = file.read()

ranges = [(id_ranges.split("-")) for id_ranges in ranges.split(',')]
invalid_ids = []

for id_range in ranges:
    element = int(id_range[0])
    end = int(id_range[1])

    while element <= end:
        if len(str(element)) % 2 == 0:
            str_element = str(element)
            i = len(str_element) // 2
            half_1, half_2 = str_element[:i], str_element[i:]

            for pair in zip(half_1, half_2):
                if pair[0] != pair[1]:
                    break
            else:
                invalid_ids.append(element)
        
        element += 1

print(sum(invalid_ids))