import os

from day5.part1.solution import (
    Publisher,
    get_seed_numbers,
)

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    almanac = Publisher.publish_almanac(input_text)

    locations = []
    for seed in get_seed_numbers(input_text):
        locations.append(almanac.get_seed_location(seed))

    # Answer: 389056265
    print(min(locations))
