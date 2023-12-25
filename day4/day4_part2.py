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
    for scratch_card in cards:
        matching_numbers = set(scratch_card.winning_numbers.split()) & set(
            scratch_card.numbers.split()
        )  # intersection of the card numbers and winning numbers
        if len(matching_numbers):
            duplicate_cards = cards[
                scratch_card.card : scratch_card.card + len(matching_numbers)
            ]
            cards.extend(duplicate_cards) 
    return cards


if __name__ == "__main__":
    print(main())
