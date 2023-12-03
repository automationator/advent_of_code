import os

from day3.part2.solution import Schematic

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    schematic = Schematic(input_text)
    gear_ratios = schematic.get_gear_ratios()

    # Answer: 78915902
    print(sum(gear_ratios))
