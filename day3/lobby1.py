import re

with open("input.txt", "r") as file:
    banks = file.readlines()

banks_jolts = []
for bank in banks:
    batteries = re.findall(r"\d", bank)
    batteries = [int(battery) for battery in batteries]

    i = 0
    big_boi = (0, 0)
    for idx, battery in enumerate(batteries[:-1]):
        if battery > big_boi[1]:
            big_boi = idx, battery

    smaller_boi = 0
    for battery in batteries[big_boi[0] + 1:]:
        if battery > smaller_boi:
            smaller_boi = battery

    banks_jolts.append(int(str(big_boi[1]) + str(smaller_boi)))

print(sum(banks_jolts))