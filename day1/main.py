
def main():
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
    print(count)
if __name__ == "__main__":
    main()
