import os

from day5.part2.solution import parallelize_get_lowest_seed_location

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    # Answer: 137516820
    print(parallelize_get_lowest_seed_location(input_text))
