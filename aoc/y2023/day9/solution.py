# https://adventofcode.com/2023/day/9


def parse_numbers(input_text: str) -> list[list[int]]:
    return list(list(int(n) for n in line.split()) for line in input_text.splitlines())


def get_differences(numbers: list[int]) -> list[int]:
    return list(numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1))


def get_next_number(history: list[list[int]]) -> int:
    """
    Starting with the final row of the history, get the final number and add it
    to the final number of the previous row. Append that number to the previous row.
    Repeat until the first row is reached. Return the final number of the first row.
    """

    for i in range(len(history) - 1, 0, -1):
        history[i - 1].append(history[i][-1] + history[i - 1][-1])

    return history[0][-1]


def get_previous_number(history: list[list[int]]) -> int:
    """
    Starting with the final row of the history, get the first number and subtract it
    from the first number of the previous row. Prepend that number to the previous row.
    Repeat until the first row is reached. Return the first number of the first row.
    """

    for i in range(len(history) - 1, 0, -1):
        history[i - 1].insert(0, history[i - 1][0] - history[i][0])

    return history[0][0]


def _build_history(numbers: list[int]) -> list[list[int]]:
    """
    Build a list of histories starting with the given numbers. Each history is a list
    of lists of numbers. The first list is the given numbers. Each subsequent list is
    the differences of the previous list. The final list is all zeroes.
    """

    history = [numbers]
    while set(history[-1]) != {0}:
        history.append(get_differences(history[-1]))

    return history


def part1(input_text: str) -> int:
    result = 0
    for numbers in parse_numbers(input_text):
        history = _build_history(numbers)
        result += get_next_number(history)

    return result


def part2(input_text: str) -> int:
    result = 0
    for numbers in parse_numbers(input_text):
        history = _build_history(numbers)
        result += get_previous_number(history)

    return result
