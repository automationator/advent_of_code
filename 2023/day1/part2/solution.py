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
