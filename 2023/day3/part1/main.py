import os

from day3.part1.solution import Schematic

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    schematic = Schematic(input_text)
    part_numbers = schematic.get_part_numbers()

    # Answer: 514969
    print(sum(part_numbers))
