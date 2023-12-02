import os

from solution import get_first_and_last_numbers

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

        # Answer: 55816
        print(sum(get_first_and_last_numbers(line) for line in input_text.splitlines()))
