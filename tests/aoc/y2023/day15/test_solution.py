# https://adventofcode.com/2023/day/15

from aoc.y2023.day15.solution import part1, part2

input_text = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def test_part1():
    assert part1(input_text) == 1320


def test_part2():
    assert part2(input_text) == 145
