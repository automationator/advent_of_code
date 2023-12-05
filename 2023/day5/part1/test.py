import os

import pytest
from day5.part1.solution import (
    Publisher,
    get_seed_numbers,
)

with open(os.path.join(os.path.dirname(__file__), "..", "sample_input.txt")) as f:
    input_text = f.read()


def test_get_seed_numbers():
    assert get_seed_numbers(input_text) == [79, 14, 55, 13]


@pytest.mark.parametrize(
    "seed, location",
    [
        (79, 82),
        (14, 43),
        (55, 86),
        (13, 35),
    ],
)
def test_get_seed_location(seed, location):
    almanac = Publisher.publish_almanac(input_text)
    assert almanac.get_seed_location(seed) == location
