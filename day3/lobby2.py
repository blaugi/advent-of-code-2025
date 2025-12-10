import re

with open("input.txt", "r") as file:
    banks = file.readlines()

banks_jolts = []
for bank in banks:
    batteries = list(enumerate([int(battery) for battery in re.findall(r"\d", bank)]))

    current_joltage = ""
    numbers_left = 11
    last_id = -1
    while numbers_left >= 0:
        big_boi = 0
        for idx, battery in batteries[last_id +  1: -numbers_left or None]: #not include start and include the last
            if battery > big_boi:
                big_boi, last_id = battery, idx

        current_joltage += str(big_boi)

        numbers_left -= 1

    banks_jolts.append(int(current_joltage))



print(sum(banks_jolts))