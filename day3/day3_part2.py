import re
import math
from dataclasses import dataclass

#not fully working yet need

@dataclass(slots=True)
class Part:
    value: str
    row: int
    start: int
    end: int


def main():
    with open("input.txt") as file:
        lines = file.read().splitlines()
    return gear_ratios(find_gears(parse_schematic(lines)))


def parse_schematic(schematic):
    stars: list[Part] = []
    parts: list[Part] = []
    for row, line in enumerate(schematic):
        for part in re.finditer(r"(\d+|\*)", line):
            if part.group() == "*":
                stars.append(Part(part.group(), row, part.start() - 1, part.end()))
            else:
                parts.append(Part(part.group(), row, part.start() - 1, part.end()))
    return stars, parts


def find_gears(schematic):
    gears = []
    for star in schematic[0]:
        parts = set()
        for part in schematic[1]:
            for i in range(star.start, star.end):
                if (
                    part.row == star.row
                    or part.row == star.row - 1
                    or part.row == star.row + 1
                ):
                    
                    if i in range(part.start, part.end):
                        parts.add(int(part.value))
        print(parts)
        if len(parts) == 2:
            gears.append(parts)
    return gears


def gear_ratios(gears):
    gear_ratios = []
    for gear in gears:
        gear_ratio = math.prod(gear)
        gear_ratios.append(gear_ratio)
    return gear_ratios


if __name__ == "__main__":
    print(sum(main()))
