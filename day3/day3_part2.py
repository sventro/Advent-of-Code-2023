import re
import math
from dataclasses import dataclass


@dataclass(slots=True)
class Part:
    value: str
    row: int
    start: int
    end: int


def main():
    with open("input.txt") as file:
        lines = file.read().splitlines()
    return sum(gear_ratios(find_gears(parse_schematic(lines))))


def parse_schematic(schematic):
    stars: list[Part] = []
    parts: list[Part] = []
    for row, line in enumerate(schematic):
        for part in re.finditer(r"(\d+|\*)", line):
            if part.group() == "*":
                stars.append(Part(part.group(), row, part.start() - 1, part.end() + 1))
            else:
                parts.append(Part(part.group(), row, part.start(), part.end()))
    return stars, parts


def row_adjacent(star, part):
    return part.row == star.row - 1 or part.row == star.row or part.row == star.row + 1


def ranges_overlap(star, part):
    return range(max(star.start, part.start), min(star.end, part.end))


def find_gears(schematic):
    gears = []
    for star in schematic[0]:
        parts = list()
        for part in schematic[1]:
            if row_adjacent(part, star):
                if ranges_overlap(star, part):
                    #print(star, part)
                    parts.append((int(part.value)))
        #print(parts)
        if len(parts) == 2:
            gears.append(parts)
    #print(gears)
    return gears


def gear_ratios(gears):
    gear_ratios = []
    for gear in gears:
        gear_ratios.append(math.prod(gear))
    return gear_ratios


if __name__ == "__main__":
    print(main())
