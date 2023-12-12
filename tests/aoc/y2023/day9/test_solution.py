# https://adventofcode.com/2023/day/9

from aoc.y2023.day9.solution import (
    part1,
    part2,
)

input_text = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_part1():
    assert part1(input_text) == 114


def test_part2():
    assert part2(input_text) == 2
