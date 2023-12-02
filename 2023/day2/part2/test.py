import pytest
from day2.part2.solution import (
    get_game_power,
    get_minimum_colors,
)


@pytest.mark.parametrize(
    "game, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", (4, 2, 6)),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", (1, 3, 4)),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", (20, 13, 6)),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", (14, 3, 15)),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", (6, 3, 2)),
    ],
)
def test_get_minimum_colors(game, expected):
    assert get_minimum_colors(game) == expected


@pytest.mark.parametrize(
    "game, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 48),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 12),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 1560),
        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 630),
        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", 36),
    ],
)
def test_get_game_power(game, expected):
    assert get_game_power(game) == expected
