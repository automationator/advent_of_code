# https://adventofcode.com/2023/day/1

from aoc.y2023.day1.solution import (
    part1,
    part2,
)


def test_part1():
    input_text = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    assert part1(input_text) == 142

def test_part2():
    input_text = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    assert part2(input_text) == 281