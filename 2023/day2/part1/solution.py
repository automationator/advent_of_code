import re

LIMITS = {"red": 12, "green": 13, "blue": 14}


def get_game_id(game: str) -> int:
    """
    Gets the game ID from the game.

    For example, if the game is:

    Game 10: 1 blue, 2 red, 19 green; 7 green, 5 blue, 7 red; 2 blue, 1 red, 3 green; 2 blue, 9 red, 10 green

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

    for count, color in get_game_pulls(game):
        if int(count) > LIMITS[color]:
            return False

    return True
