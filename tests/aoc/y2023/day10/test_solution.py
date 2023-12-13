# https://adventofcode.com/2023/day/10

from aoc.y2023.day10.solution import (
    part1,
    part2,
)


def test_part1():
    input_text = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

    assert part1(input_text) == 4

    input_text = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

    assert part1(input_text) == 8


def test_part2():
    input_text = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

    assert part2(input_text) == 4

    input_text = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

    assert part2(input_text) == 8

    input_text = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

    assert part2(input_text) == 10
