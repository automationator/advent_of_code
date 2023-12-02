import pytest
from part1.solution import (
    get_first_and_last_numbers,
    get_numbers_from_string,
)


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1abc2", ["1", "2"]),
        ("pqr3stu8vwx", ["3", "8"]),
        ("a1b2c3d4e5f", ["1", "2", "3", "4", "5"]),
        ("treb7uchet", ["7"]),
    ],
)
def test_get_numbers_from_string(input_text, expected):
    assert get_numbers_from_string(input_text) == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ],
)
def test_get_first_and_last_numbers(input_text, expected):
    assert get_first_and_last_numbers(input_text) == expected
