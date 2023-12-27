import re
import math
from dataclasses import dataclass

GEARS = r"(\d+|\*)"  # find numbers of any length and  "*"


@dataclass(slots=True)
class Part:
    value: str
    row: int
    start: int
    end: int


def main() -> int:
    with open("input.txt") as file:
        lines = file.read().splitlines()
    stars, parts = parse_schematic(lines)
    gears = find_gears(stars, parts)
    return sum(calculate_gear_ratios(gears))


def parse_schematic(schematic: list[str]) -> tuple[list[Part], list[Part]]:
    stars: list[Part] = []
    parts: list[Part] = []
    for row, line in enumerate(schematic):
        for part in re.finditer(GEARS, line):
            if part.group() == "*":
                stars.append(Part(part.group(), row, part.start() - 1, part.end() + 1))
            else:
                parts.append(Part(part.group(), row, part.start(), part.end()))
    return stars, parts


def row_adjacent(star: Part, part: Part) -> bool:
    return part.row == star.row - 1 or part.row == star.row or part.row == star.row + 1


def ranges_overlap(star: Part, part: Part) -> bool:
    return range(max(star.start, part.start), min(star.end, part.end))


def find_gears(stars: list[Part], parts: list[Part]) -> list[list[int, int]]:
    gears = []
    for star in stars:
        parts = list()
        for part in parts:
            if row_adjacent(part, star):
                if ranges_overlap(star, part):
                    parts.append((int(part.value)))
        if len(parts) == 2:
            gears.append(parts)
    return gears


def calculate_gear_ratios(gears: list[list[int, int]]) -> list[int]:
    gear_ratios = []
    for gear in gears:
        gear_ratios.append(math.prod(gear))
    return gear_ratios


if __name__ == "__main__":
    print(main())
