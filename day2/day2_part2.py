import re


def main() -> int:
    return sum(games_power())


def all_games() -> list:
    with open("input.txt") as file:
        games = file.readlines()
    return games


def get_minimum_necesarry_cubes(games_list) -> list:
    games = []
    for game in games_list:
        hand = re.findall(r"(\d+) (\w+)", game)
        minimum_cubes = {"red": 0, "green": 0, "blue": 0}
        for number, color in hand:
            minimum_cubes[color] = (
                int(number)
                if minimum_cubes[color] < int(number)
                else minimum_cubes[color]
            )
        games.append(minimum_cubes)
    return games


def games_power():
    game_power = []
    games = get_minimum_necesarry_cubes(all_games())
    for game in games:
        power = game["red"] * game["green"] * game["blue"]
        game_power.append(power)
    return game_power


if __name__ == "__main__":
    print(main())
