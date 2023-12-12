import re

with open("input.txt") as file:
    all_games = file.readlines()


def minimum_necesarry_cubes(games_list) -> list:
    games = []
    for game in games_list:
        hand = re.findall(r"(\d+) (\w+)", game)
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for number, color in hand:
            min_cubes[color] = (
                int(number) if min_cubes[color] < int(number) else min_cubes[color]
            )
        games.append(min_cubes)
    return games


def games_power(game_cubes):
    game_power = []
    games = game_cubes
    for game in games:
        game_power.append(game["red"] * game["green"] * game["blue"])
    return game_power


if __name__ == "__main__":
    print(sum(games_power(minimum_necesarry_cubes(all_games))))
