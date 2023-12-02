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
