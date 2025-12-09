def part1():
    count = 0
    position = 50
    with open("input.txt") as f:
        while line := f.readline():
            match line[0]:
                case "R":
                    position += int(line[1:])
                case "L":
                    position -= int(line[1:])

            while position < 0:
                position += 100
            while position > 99:
                position -= 100

            if position == 0:
                count += 1
    print(f"part 1 zeroes count: {count}")


def part2():
    count = 0
    position = 50
    with open("input.txt") as f:
        while line := f.readline():
            direction = line[0]
            value = int(line[1:])

            # remove cycles
            if value > 100:
                clicks, value = divmod(value, 100)
                count += clicks

            if direction == "R":
                if position + value >= 100:
                    count += 1
                position = (position + value) % 100
            else:
                if position and position - value <= 0: #check if position != 0 so as to not zero crossing when you are on 0 and move left
                    count += 1
                position = (position - value) % 100

    print(f"part 2 zeroes count: {count}")


if __name__ == "__main__":
    part1()
    part2()
