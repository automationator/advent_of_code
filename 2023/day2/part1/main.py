import os

from day2.part1.solution import (
    get_game_id,
    is_game_possible,
)

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        games = f.read().splitlines()

    # Answer: 2105
    print(sum(get_game_id(game) for game in games if is_game_possible(game)))
