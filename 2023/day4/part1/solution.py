import math
import re


def count_points(game: str) -> int:
    """
    Counts the points for a scratchcard game.
    """

    parsed_game = re.findall(r": ([\d\s]+) \| ([\d\s]+)", game)
    winning_numbers = set(parsed_game[0][0].split())
    my_numbers = set(parsed_game[0][1].split())
    my_winning_numbers = winning_numbers.intersection(my_numbers)
    return int(math.pow(2, len(my_winning_numbers) - 1))
