# https://adventofcode.com/2023/day/12

from aoc.y2023.day12.solution import part1, part2

input_text = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def test_part1():
    assert part1(input_text) == 21


def test_part2():
    assert part2(input_text) == 525152
