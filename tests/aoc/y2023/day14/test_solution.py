# https://adventofcode.com/2023/day/14


from aoc.y2023.day14.solution import part1, part2

input_text = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def test_part1():
    assert part1(input_text) == 136


def test_part2():
    assert part2(input_text) == 64
