import math

from day2.part1.solution import get_game_pulls


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
