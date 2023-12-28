# https://adventofcode.com/2023/day/14

from enum import StrEnum

from aoc.helpers import get_cycle_output, parse_grid, transpose_grid


class Direction(StrEnum):
    EAST = "east"
    WEST = "west"


def _tilt(grid: tuple[str, ...], direction: Direction) -> tuple[str, ...]:
    reverse = direction == Direction.WEST

    return tuple(
        "#".join(
            ["".join(sorted(movable_rocks, reverse=reverse)) for movable_rocks in row.split("#")]
        )
        for row in grid
    )


def tilt_north(grid: tuple[str, ...]) -> tuple[str, ...]:
    return transpose_grid(tilt_west(transpose_grid(grid)))


def tilt_south(grid: tuple[str, ...]) -> tuple[str, ...]:
    return transpose_grid(tilt_east(transpose_grid(grid)))


def tilt_east(grid: tuple[str, ...]) -> tuple[str, ...]:
    return _tilt(grid, Direction.EAST)


def tilt_west(grid: tuple[str, ...]) -> tuple[str, ...]:
    return _tilt(grid, Direction.WEST)


def spin_cycle(grid: tuple[str, ...]) -> tuple[str, ...]:
    grid = tilt_north(grid)
    grid = tilt_west(grid)
    grid = tilt_south(grid)
    grid = tilt_east(grid)
    return grid


def count_load(grid: tuple[str, ...]) -> int:
    load = 0
    num_rows = len(grid)
    for i, row in enumerate(grid):
        num_rocks_in_row = row.count("O")
        load += num_rocks_in_row * (num_rows - i)
    return load


def part1(input_text: str) -> int:
    grid = parse_grid(input_text)

    # Answer: 103614
    return count_load(tilt_north(grid))


def part2(input_text: str) -> int:
    grid = parse_grid(input_text)
    grid = get_cycle_output(spin_cycle, grid, 1000000000)

    # Answer: 83790
    return count_load(grid)
