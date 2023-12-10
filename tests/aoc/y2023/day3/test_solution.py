# https://adventofcode.com/2023/day/3

from aoc.y2023.day3.solution import (
    part1,
    part2,
)

input_text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def test_part1():
    assert part1(input_text) == 4361

def test_part2():
    assert part2(input_text) == 467835