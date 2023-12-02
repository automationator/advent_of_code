import os

from day2.part2.solution import get_game_power

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        games = f.read().splitlines()

    # Answer: 72422
    print(sum(get_game_power(game) for game in games))
