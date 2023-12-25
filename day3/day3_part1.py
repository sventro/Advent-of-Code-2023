import re
from dataclasses import dataclass


PARTS = r"(?!\.)(\d+|\D)"


@dataclass(slots=True)
class Part:
    value: str
    row: int
    start: int
    end: int


def main():
    with open("input.txt") as file:
        lines = file.read().splitlines()
    return sum(find_parts(parse_schematic(lines)))


def parse_schematic(schematic) -> tuple[list, list]:
    symbols: list[Part] = []
    parts: list[Part] = []
    for row, line in enumerate(schematic):
        for part in re.finditer(PARTS, line):
            if not part.group().isdigit():
                symbols.append(Part(part.group(), row, part.start(), part.end()))
            else:
                parts.append(Part(part.group(), row, part.start() - 1, part.end() + 1))
    return parts, symbols


def row_adjacent(part, symbol):
    return (
        part.row - 1 == symbol.row
        or part.row == symbol.row
        or part.row + 1 == symbol.row
    )


def ranges_overlap(part, symbol):
    return range(max(symbol.start, part.start), min(symbol.end, part.end))


def find_parts(schematic):
    all_parts = []
    for part in schematic[0]:
        for symbol in schematic[1]:
            if row_adjacent(part, symbol):
                if ranges_overlap(part, symbol):
                    all_parts.append((int(part.value)))
    return all_parts


if __name__ == "__main__":
    print(main())
