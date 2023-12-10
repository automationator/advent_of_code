# https://adventofcode.com/2023/day/8

from aoc.y2023.day8.solution import (
    part1,
    part2,
)


def test_part1():
    input_text = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

    assert part1(input_text) == 6

def test_part2():
    input_text = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

    assert part2(input_text) == 6