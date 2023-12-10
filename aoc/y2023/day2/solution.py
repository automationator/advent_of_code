# https://adventofcode.com/2023/day/2

import math
import re


def get_game_id(game: str) -> int:
    """
    Gets the game ID from the game.

    For example, if the game is:

    Game 10: 1 blue, 2 red, 19 green

    Then the ID is 10.
    """

    return int(game.split(":")[0].split(" ")[1])


def get_game_pulls(game: str) -> list[tuple[int, str]]:
    """
    Gets the individual pulls from the game and returns them as a list of tuples.

    For example, if the game is:

    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red

    Then the pulls are:

    [
        (8, "green"),
        (6, "blue"),
        (20, "red"),
        (5, "blue"),
        (4, "red"),
        (13, "green"),
        (5, "green"),
        (1, "red"),
    ]
    """
    pulls = re.findall(r"(\d+ \w+)", game)

    result = []
    for pull in pulls:
        count, color = pull.split(" ")
        result.append((int(count), color))

    return result


def is_game_possible(game: str) -> bool:
    """
    Determines if the game is possible.

    For example, if the game is:

    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red

    Then the game is not possible because at one point there are 20 red,
    which is more than the limit of 12.
    """

    limits = {"red": 12, "green": 13, "blue": 14}

    return all(int(count) <= limits[color] for count, color in get_game_pulls(game))


def get_minimum_colors(game: str) -> tuple[int, int, int]:
    """
    Gets the minimum number of colors needed to play the game.

    For example, if the game is:

    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    Then the minimum number of red is 4, the minimum number of green is 2,
    and the minimum number of blue is 6.
    """

    min_colors = {"red": 0, "green": 0, "blue": 0}

    pulls = get_game_pulls(game)
    for count, color in pulls:
        if min_colors[color] < count:
            min_colors[color] = count

    return tuple(min_colors.values())


def get_game_power(game: str) -> int:
    """
    Gets the game power, where the power is the product of the minimum
    number of colors needed to play the game.
    """

    min_colors = get_minimum_colors(game)
    return math.prod(min_colors)


def part1(input_text: str) -> int:
    # Answer: 2105
    return sum(get_game_id(game) for game in input_text.splitlines() if is_game_possible(game))


def part2(input_text: str) -> int:
    # Answer: 72422
    return sum(get_game_power(game) for game in input_text.splitlines())
