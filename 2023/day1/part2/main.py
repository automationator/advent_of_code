import os

from part1.solution import get_first_and_last_numbers
from part2.solution import convert_spelled_numbers_to_digits

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    # Answer: 54980
    print(
        sum(
            get_first_and_last_numbers(convert_spelled_numbers_to_digits(line))
            for line in input_text.splitlines()
        )
    )
