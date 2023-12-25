import re
import copy
from dataclasses import dataclass

CARDS = r"Card +(\d+): +((?:\d+ +){10})\| +((?:\d+ +|\d+){25})"
TEST_CARDS = r"Card +(\d+): +((?:\d+ +){5})\| +((?:\d+ +|\d+){8})"


@dataclass(slots=True)
class Scratch_card:
    card: int
    winning_numbers: str
    numbers: str


def main() -> int:
    test="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()
    with open("input.txt") as file:
        card_pile = file.read().splitlines()
    return len(check_winnings(parse_cards(card_pile)))


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


def check_winnings(cards: list[Scratch_card]):
    cards_copy = copy.deepcopy(cards)
    for scratch_card in cards_copy:
        
        matching_numbers = set(scratch_card.winning_numbers.split()) & set(
            scratch_card.numbers.split()
        )
        if len(matching_numbers):
            duplicate_cards = cards_copy[
                scratch_card.card : scratch_card.card + len(matching_numbers)]
            cards_copy.extend(duplicate_cards)
    return cards_copy


if __name__ == "__main__":
    print(main())
