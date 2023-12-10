# https://adventofcode.com/2023/day/1


def get_numbers_from_string(input_str: str) -> list[str]:
    """
    Given a string of letters and numbers, return a list of the numbers in the string.
    """

    return [x for x in input_str if x.isdigit()]


def get_first_and_last_numbers(input_str: str) -> int:
    """
    Given a string of letters and numbers, return a two-digit number consisting
    of the first and last numbers in the string.
    """

    all_numbers = get_numbers_from_string(input_str)

    first_number = all_numbers[0]
    last_number = all_numbers[-1]

    return int(f"{first_number}{last_number}")


def convert_spelled_numbers_to_digits(input_str: str) -> str:
    """
    Given a string of letters and numbers, return a string with the spelled-out
    numbers converted to digits. This needs to account for overlapping letters.

    For example, given the string "nineight", return "n9e8t".

    Then the code from Part 1 can be used to solve the problem.
    """

    number_mapping = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    for spelled_number in number_mapping:
        input_str = input_str.replace(spelled_number, number_mapping[spelled_number])

    return input_str


def part1(input_text: str) -> int:
    # Answer: 55816
    return sum(get_first_and_last_numbers(line) for line in input_text.splitlines())


def part2(input_text: str) -> int:
    # Answer: 54980
    return sum(
        get_first_and_last_numbers(convert_spelled_numbers_to_digits(line))
        for line in input_text.splitlines()
    )
