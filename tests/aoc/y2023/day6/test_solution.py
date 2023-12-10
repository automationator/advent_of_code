# https://adventofcode.com/2023/day/6

from aoc.y2023.day6.solution import (
    part1,
    part2,
)

input_text = """Time:      7  15   30
Distance:  9  40  200"""

def test_part1():
    assert part1(input_text) == 288

def test_part2():
    assert part2(input_text) == 71503