import re
from dataclasses import dataclass


PARTS = r"(?!\.)(\d+|\D)"  # ignore "." find numbers of any length and non digits


@dataclass(slots=True)
class Part:
    value: str
    row: int
    start: int
    end: int


def main() -> int:
    with open("input.txt") as file:
        lines = file.read().splitlines()
    parts, symbols = parse_schematic(lines)
    return sum(find_parts(parts=parts, symbols=symbols))


def parse_schematic(schematic: list[str]) -> tuple[list[Part], list[Part]]:
    parts: list[Part] = []
    symbols: list[Part] = []
    for row, line in enumerate(schematic):
        for part in re.finditer(PARTS, line):
            if not part.group().isdigit():
                symbols.append(Part(part.group(), row, part.start(), part.end()))
            else:
                parts.append(Part(part.group(), row, part.start() - 1, part.end() + 1))
    return (parts, symbols)


def row_adjacent(part: Part, symbol: Part) -> bool:
    return (
        part.row - 1 == symbol.row
        or part.row == symbol.row
        or part.row + 1 == symbol.row
    )


def ranges_overlap(part: Part, symbol: Part) -> bool:
    return range(max(symbol.start, part.start), min(symbol.end, part.end))


def find_parts(parts: list[Part], symbols: list[Part]) -> list[int]:
    all_parts: list[int] = []
    for part in parts:
        for symbol in symbols:
            if row_adjacent(part, symbol):
                if ranges_overlap(part, symbol):
                    all_parts.append((int(part.value)))
    return all_parts


if __name__ == "__main__":
    print(main())
