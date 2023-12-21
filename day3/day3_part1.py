import re


def main():
    with open("input.txt") as file:
        lines = file.read().splitlines()
    return sum(find_parts(lines))


def is_symbol(char):
    return not char.isdigit() and char != "."


def find_parts(schematic):
    parts = []
    width = len(schematic[0])
    height = len(schematic)
    for row, line in enumerate(schematic):
        for number in re.finditer(r"\d+", line):
            start = number.start() - 1
            end = number.end()
            part_number = int(number.group())
            if start >= 0 and is_symbol(line[start]):
                parts.append(part_number)
            elif end < width and is_symbol(line[end]):
                parts.append(part_number)
            for i in range(start, end + 1):
                if i >= len(line):
                    continue  # to the next line
                if row >= 0 and is_symbol(schematic[row - 1][i]):
                    parts.append(part_number)
                elif row < height - 1 and is_symbol(schematic[row + 1][i]):
                    parts.append(part_number)
    return parts


if __name__ == "__main__":
    print(main())
