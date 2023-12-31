# https://adventofcode.com/2023/day/16

from enum import Enum

from aoc.helpers import parse_grid


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def follow_beams(
    maze: tuple[str, ...], start: tuple[tuple[int, int], Direction] = ((0, 0), Direction.RIGHT)
) -> set[tuple[int, int]]:
    energized_cells: set[tuple[int, int]] = set()
    seen: set[tuple[int, int]] = set()
    beams: set[tuple[tuple[int, int], Direction]] = {start}
    while beams:
        beam = beams.pop()

        # The beam ends if it is out of the bounds of the maze.
        row, column = beam[0]
        if row < 0 or row >= len(maze) or column < 0 or column >= len(maze[0]):
            continue

        energized_cells.add((row, column))

        character = maze[row][column]
        direction = beam[1]
        new_beams = []
        if direction == Direction.UP:
            if character == "/":
                new_beams.append(((row, column + 1), Direction.RIGHT))
            elif character == "\\":
                new_beams.append(((row, column - 1), Direction.LEFT))
            elif character == "-":
                new_beams.append(((row, column - 1), Direction.LEFT))
                new_beams.append(((row, column + 1), Direction.RIGHT))
            else:
                new_beams.append(((row - 1, column), Direction.UP))

        elif direction == Direction.DOWN:
            if character == "/":
                new_beams.append(((row, column - 1), Direction.LEFT))
            elif character == "\\":
                new_beams.append(((row, column + 1), Direction.RIGHT))
            elif character == "-":
                new_beams.append(((row, column - 1), Direction.LEFT))
                new_beams.append(((row, column + 1), Direction.RIGHT))
            else:
                new_beams.append(((row + 1, column), Direction.DOWN))

        elif direction == Direction.LEFT:
            if character == "/":
                new_beams.append(((row + 1, column), Direction.DOWN))
            elif character == "\\":
                new_beams.append(((row - 1, column), Direction.UP))
            elif character == "|":
                new_beams.append(((row - 1, column), Direction.UP))
                new_beams.append(((row + 1, column), Direction.DOWN))
            else:
                new_beams.append(((row, column - 1), Direction.LEFT))

        elif direction == Direction.RIGHT:
            if character == "/":
                new_beams.append(((row - 1, column), Direction.UP))
            elif character == "\\":
                new_beams.append(((row + 1, column), Direction.DOWN))
            elif character == "|":
                new_beams.append(((row - 1, column), Direction.UP))
                new_beams.append(((row + 1, column), Direction.DOWN))
            else:
                new_beams.append(((row, column + 1), Direction.RIGHT))

        for new_beam in new_beams:
            if new_beam not in seen:
                seen.add(new_beam)
                beams.add(new_beam)

    return energized_cells


def part1(input_text: str) -> int:
    maze = parse_grid(input_text)
    energized_cells = follow_beams(maze)

    # Answer: 6883
    return len(energized_cells)


def part2(input_text: str) -> int:
    maze = parse_grid(input_text)

    max_energized_cells = 0
    for row in range(len(maze)):
        # Start the beam at each row on the left edge of the maze.
        start = ((row, 0), Direction.RIGHT)
        energized_cells = follow_beams(maze, start)

        if len(energized_cells) > max_energized_cells:
            max_energized_cells = len(energized_cells)

        # Start the beam at each row on the right edge of the maze.
        start = ((row, len(maze[0]) - 1), Direction.LEFT)
        energized_cells = follow_beams(maze, start)

        if len(energized_cells) > max_energized_cells:
            max_energized_cells = len(energized_cells)

    for column in range(len(maze[0])):
        # Start the beam at each column on the top edge of the maze.
        start = ((0, column), Direction.DOWN)
        energized_cells = follow_beams(maze, start)

        if len(energized_cells) > max_energized_cells:
            max_energized_cells = len(energized_cells)

        # Start the beam at each column on the bottom edge of the maze.
        start = ((len(maze) - 1, column), Direction.UP)
        energized_cells = follow_beams(maze, start)

        if len(energized_cells) > max_energized_cells:
            max_energized_cells = len(energized_cells)

    # Answer: 7228
    return max_energized_cells
