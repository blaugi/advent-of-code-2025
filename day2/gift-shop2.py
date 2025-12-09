with open("input.txt", "r") as file:
    ranges = file.read()

ranges = [(id_ranges.split("-")) for id_ranges in ranges.split(',')]
invalid_ids = []

for id_range in ranges:
    element = int(id_range[0])
    end = int(id_range[1])

    while element <= end:

        chunk_size =  len(str(element)) // 2
        while chunk_size > 0:
            if len(str(element)) % chunk_size == 0:
                str_element = str(element)
                
                parts = [str_element[0+i:chunk_size+i] for i in range(0, len(str_element), chunk_size)]

                for pair in zip(*parts):
                    if len(set(pair)) != 1:
                        break
                else:
                    invalid_ids.append(element)
                    break

            chunk_size -=1
                
        element += 1

print(sum(invalid_ids))