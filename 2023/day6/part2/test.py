import os

from day6.part2.solution import (
    Race,
    get_race,
)

with open(os.path.join(os.path.dirname(__file__), "..", "sample_input.txt")) as f:
    input_text = f.read()


def test_get_race():
    assert get_race(input_text) == Race(71530, 940200)
