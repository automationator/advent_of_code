import os

from day5.part2.solution import (
    Publisher,
    get_seed_ranges,
    parallelize_get_lowest_seed_location,
    split_range,
)

with open(os.path.join(os.path.dirname(__file__), "..", "sample_input.txt")) as f:
    input_text = f.read()


def test_get_seed_ranges():
    assert get_seed_ranges(input_text) == [range(79, 79 + 14), range(55, 55 + 13)]


def test_get_lowest_seed_location():
    almanac = Publisher.publish_almanac(input_text)
    lowest_location = float("inf")
    for seed_range in get_seed_ranges(input_text):
        if (location := almanac.get_lowest_seed_location(seed_range)) < lowest_location:
            lowest_location = location
    assert lowest_location == 46


def test_parallelize_get_lowest_seed_location():
    assert parallelize_get_lowest_seed_location(input_text) == 46


def test_split_range():
    r = range(10)
    assert split_range(r, 2) == [range(0, 5), range(5, 10)]
    assert split_range(r, 3) == [range(0, 4), range(4, 7), range(7, 10)]
