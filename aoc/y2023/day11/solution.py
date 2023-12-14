# https://adventofcode.com/2023/day/11

from typing import Generator

import numpy


def parse_universe(input_text: str) -> numpy.ndarray:
    return numpy.array([list(line) for line in input_text.splitlines()])


def calculate_empty_rows(galaxies: list[tuple[int, int]], height: int) -> set[int]:
    galaxy_rows = set(y for _, y in galaxies)
    return set(row for row in range(height) if row not in galaxy_rows)


def calculate_empty_columns(galaxies: list[tuple[int, int]], width: int) -> set[int]:
    galaxy_columns = set(x for x, _ in galaxies)
    return set(column for column in range(width) if column not in galaxy_columns)


def get_galaxy_coordinates(universe: numpy.ndarray) -> list[tuple[int, int]]:
    coords = numpy.where(universe == "#")
    return list(zip(coords[1], coords[0]))  # x, y


def get_galaxy_pairs(
    galaxies: list[tuple[int, int]],
) -> Generator[tuple[tuple[int, int], tuple[int, int]], None, None]:
    return ((g1, g2) for idx, g1 in enumerate(galaxies) for g2 in galaxies[idx + 1 :])


def get_distance_between_galaxies(galaxy_pair: tuple[tuple[int, int], tuple[int, int]]) -> int:
    galaxy1_x, galaxy1_y = galaxy_pair[0]
    galaxy2_x, galaxy2_y = galaxy_pair[1]
    return abs(galaxy1_x - galaxy2_x) + abs(galaxy1_y - galaxy2_y)


def expand_galaxies(input_text: str, expansion_factor: int = 2) -> list[tuple[int, int]]:
    universe = parse_universe(input_text)
    galaxies = get_galaxy_coordinates(universe)

    empty_rows = calculate_empty_rows(galaxies, universe.shape[0])
    empty_columns = calculate_empty_columns(galaxies, universe.shape[1])

    expanded_galaxies = []
    for galaxy in galaxies:
        num_empty_columns_before_galaxy = len([c for c in empty_columns if c < galaxy[0]])
        num_empty_rows_before_galaxy = len([r for r in empty_rows if r < galaxy[1]])
        expanded_galaxies.append(
            (
                galaxy[0] + (num_empty_columns_before_galaxy * (expansion_factor - 1)),
                galaxy[1] + (num_empty_rows_before_galaxy * (expansion_factor - 1)),
            )
        )

    return expanded_galaxies


def part1(input_text: str) -> int:
    expanded_galaxies = expand_galaxies(input_text)

    # Answer: 10490062
    return sum(map(get_distance_between_galaxies, get_galaxy_pairs(expanded_galaxies)))


def part2(input_text: str, expansion_factor: int = 1000000) -> int:
    expanded_galaxies = expand_galaxies(input_text, expansion_factor=expansion_factor)

    # Answer: 382979724122
    return sum(map(get_distance_between_galaxies, get_galaxy_pairs(expanded_galaxies)))
