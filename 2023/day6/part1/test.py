import os

import pytest
from day6.part1.solution import (
    Race,
    get_number_of_ways_to_win,
    get_races,
    num_ways_to_win_multiplied,
)

with open(os.path.join(os.path.dirname(__file__), "..", "sample_input.txt")) as f:
    input_text = f.read()


def test_get_races():
    assert get_races(input_text) == [
        Race(7, 9),
        Race(15, 40),
        Race(30, 200),
    ]


@pytest.mark.parametrize(
    "race, expected",
    [
        (Race(7, 9), 4),
        (Race(15, 40), 8),
        (Race(30, 200), 9),
    ],
)
def test_get_number_of_ways_to_win(race, expected):
    assert get_number_of_ways_to_win(race) == expected


def test_num_ways_to_win_multiplied():
    assert num_ways_to_win_multiplied(input_text) == 288
