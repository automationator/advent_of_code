# https://adventofcode.com/2023/day/7

from aoc.y2023.day7.solution import (
    part1,
    part2,
)

input_text = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def test_part1():
    assert part1(input_text) == 6440

def test_part2():
    assert part2(input_text) == 5905