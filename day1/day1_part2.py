import re


def main() -> int:
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    total = []
    with open("input.txt") as stars:
        for star in stars:
            # "(?=(pattern))" includes overlapping matches, "(pattern)" does not
            digit = re.findall(
                r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))",
                star,
            )
            digit_first = number_map[digit[0]] if digit[0] in number_map else digit[0]
            digit_last = number_map[digit[-1]] if digit[-1] in number_map else digit[-1]
            total.append(int(digit_first + digit_last))
    return sum(total)


if __name__ == "__main__":
    print(main())
