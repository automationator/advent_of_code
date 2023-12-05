import os

from day4.part1.solution import count_points

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    points = 0
    for game in input_text.splitlines():
        points += count_points(game)

    # Answer: 21919
    print(points)
