import re

CUBES_MAX = {"red": 12, "green": 13, "blue": 14}


def main() -> int:
    return sum(get_game_ids())


def all_games():
    with open("input.txt") as file:
        games = file.readlines()
    return games


def possible_games(games_list) -> list:
    for i, game in enumerate(games_list):
        hands = re.findall(r"(\d+) (\w+)", game)
        for number, color in hands:
            if int(number) > CUBES_MAX[color]:
                games_list[i] = ""
    return list(filter(None, games_list))


def get_game_ids() -> list:
    game_ids = []
    for game in possible_games(all_games()):
        game_id = re.findall(r"(?:Game) (\d+)", game)[0]
        game_ids.append(int(game_id))
    return game_ids


if __name__ == "__main__":
    print(main())
