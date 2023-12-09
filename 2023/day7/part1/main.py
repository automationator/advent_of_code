import os

from day7.part1.solution import count_total_winnings

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    # Answer: 248422077
    print(count_total_winnings(input_text))