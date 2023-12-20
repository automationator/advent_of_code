# https://adventofcode.com/2023/day/13

from aoc.y2023.day13.solution import (
    part1,
    part2,
)

input_text = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_part1():
    # Vertical (4, 5)
    # Horizontal (3, 4)

    assert part1(input_text) == 405


def test_part2():
    # Horizontal (2, 3)
    # Horizontal (0, 1)

    assert part2(input_text) == 400
