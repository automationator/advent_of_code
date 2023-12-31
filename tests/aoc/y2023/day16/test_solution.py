# https://adventofcode.com/2023/day/16

from aoc.y2023.day16.solution import part1, part2

input_text = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""


def test_part1():
    assert part1(input_text) == 46


def test_part2():
    assert part2(input_text) == 51
