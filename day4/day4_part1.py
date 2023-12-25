import re
from dataclasses import dataclass

CARDS = r"Card +(\d+): +((?:\d+ +){10})\| +((?:\d+ +|\d+){25})"


@dataclass(slots=True)
class Scratch_card:
    card: int
    winning_numbers: str
    numbers: str


def main() -> int:
    with open("input.txt") as file:
        card_pile = file.read().splitlines()
    return sum(check_cards(parse_cards(card_pile)))


def parse_cards(all_cards: list[str]):
    scratch_cards = []
    for cards in all_cards:
        for card in re.finditer(CARDS, cards):
            scratch_cards.append(
                Scratch_card(
                    card=int(card.group(1)),
                    winning_numbers=card.group(2),
                    numbers=card.group(3),
                )
            )
    return scratch_cards


def check_cards(cards: list[Scratch_card])->list[int]:
    all_points = []
    for scratch_card in cards:
        matching_numbers = set(scratch_card.winning_numbers.split()) & set(
            scratch_card.numbers.split()
        )
        if len(matching_numbers):
            points = 1 * pow(2, len(matching_numbers) - 1)
            all_points.append(points)
    return all_points


if __name__ == "__main__":
    print(main())
