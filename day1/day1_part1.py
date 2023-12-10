import re


def main() -> int:
    total = list()
    with open("input.txt", "r") as day0:
        for line in day0:
            digit = re.findall(r"[\d]", line)
            star = int(digit[0] + digit[-1])
            total.append(star)
    return sum(total)


if __name__ == "__main__":
    print(main())
