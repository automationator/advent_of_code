# https://adventofcode.com/2023/day/13

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from aoc import helpers


class Direction(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


@dataclass
class Mirror:
    """Stores the index of the row or column that is the mirror."""

    index: Optional[int] = None
    direction: Optional[Direction] = None

    def __eq__(self, other):
        if isinstance(other, Mirror):
            return self.index == other.index and self.direction == other.direction
        return False

    def __bool__(self):
        return self.index is not None

    def __hash__(self):
        return hash((self.index, self.direction))

    @property
    def points(self):
        if self.index and self.direction == Direction.HORIZONTAL:
            return self.index * 100
        elif self.index and self.direction == Direction.VERTICAL:
            return self.index

        return 0


def print_grid(grid: list[str]) -> None:
    for row in grid:
        print(row)


def parse_grid(input_text: str) -> list[str]:
    return input_text.splitlines()


def num_differences_between_grids(grid1: list[str], grid2: list[str]) -> int:
    total = 0
    for row1, row2 in zip(grid1, grid2):
        for char1, char2 in zip(row1, row2):
            if char1 != char2:
                total += 1

    return total


def find_mirror(grid: list[str], required_differences: int = 0) -> Mirror:
    def _find(grid: list[str], direction: Direction) -> Mirror:
        for i in range(1, len(grid)):
            # Flip the above portion so a direct comparison can be made
            # to the below portion.
            above = grid[:i][::-1]
            below = grid[i:]

            if num_differences_between_grids(above, below) == required_differences:
                return Mirror(i, direction)

        return Mirror()

    horizontal_mirror = _find(grid, Direction.HORIZONTAL)
    return horizontal_mirror if horizontal_mirror else _find(transpose(grid), Direction.VERTICAL)


def transpose(grid: list[str]) -> list[str]:
    return list(zip(*grid))


def part1(input_text: str) -> int:
    total = 0

    for chunk in helpers.split_text_on_blank_lines(input_text):
        grid = parse_grid(chunk)
        mirror = find_mirror(grid)
        total += mirror.points

    # Answer: 27664
    return total


def part2(input_text: str) -> int:
    total = 0

    for chunk in helpers.split_text_on_blank_lines(input_text):
        grid = parse_grid(chunk)
        mirror = find_mirror(grid, required_differences=1)
        total += mirror.points

    # Answer: 33991
    return total
