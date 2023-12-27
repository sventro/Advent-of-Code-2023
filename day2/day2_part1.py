import re

CUBES_MAX = {"red": 12, "green": 13, "blue": 14}


with open("input.txt") as file:
    all_games = file.readlines()


def valid_games(games_list: list[list[str]]) -> list[str]:
    for i, game in enumerate(games_list):
        hands = re.findall(r"(\d+) (\w+)", game)
        for number, color in hands:
            if int(number) > CUBES_MAX[color]:
                games_list[i] = ""
    return list(filter(None, games_list))


def get_game_ids(games) -> list[int]:
    game_ids = []
    for game in games:
        game_id = re.findall(r"(?:Game) (\d+)", game)[0]
        game_ids.append(int(game_id))
    return game_ids


if __name__ == "__main__":
    print(sum(get_game_ids(valid_games(all_games))))
