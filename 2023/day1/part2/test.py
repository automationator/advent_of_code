import pytest
from part2.solution import convert_spelled_numbers_to_digits


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("two1nine", "t2o1n9e"),
        ("eightwothree", "e8t2ot3e"),
        ("abcone2threexyz", "abco1e2t3exyz"),
        ("xtwone3four", "xt2o1e3f4r"),
        ("4nineeightseven2", "4n9ee8ts7n2"),
        ("zoneight234", "zo1e8t234"),
        ("7pqrstsixteen", "7pqrsts6xteen"),
    ],
)
def test_convert_spelled_numbers_to_digits(input_text, expected):
    assert convert_spelled_numbers_to_digits(input_text) == expected
