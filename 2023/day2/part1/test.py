import pytest
from day2.part1.solution import (
    get_game_id,
    is_game_possible,
)


@pytest.mark.parametrize(
    "game, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
        ("Game 10: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 10),
    ],
)
def test_get_game_id(game, expected):
    assert get_game_id(game) == expected


@pytest.mark.parametrize(
    "game, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", False),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", False),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),
    ],
)
def test_is_game_possible(game, expected):
    assert is_game_possible(game) == expected
