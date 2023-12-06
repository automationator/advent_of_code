import os

from day6.part1.solution import num_ways_to_win_multiplied

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    # Answer: 500346
    print(num_ways_to_win_multiplied(input_text))
