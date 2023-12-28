import os
from typing import Callable, TypeVar

T = TypeVar("T")


def parse_grid(text: str) -> tuple[str, ...]:
    """
    Parse a grid of characters from a multi-line string.
    """
    return tuple(text.splitlines())


def print_grid(grid: tuple[str, ...]) -> None:
    """
    Print a grid of characters.
    """
    print(os.linesep.join(grid))


def split_text_on_blank_lines(text: str) -> tuple[str, ...]:
    """
    Split a string on blank lines.
    """
    return tuple(text.split(os.linesep + os.linesep))


def transpose_grid(grid: tuple[str, ...]) -> tuple[str, ...]:
    """
    Transpose a grid of characters.
    """
    return tuple("".join(row) for row in zip(*grid))


# Referenced https://mjc239.github.io/aoc23-day14/ for an example of
# how to implement the cycle detection algorithm.
def get_cycle_output(func: Callable[[T], T], arg: T, num_iterations: int) -> T:
    """
    Gets the output of a function after calling it a number of times.

    Args:
        func: The function to call
        arg: The argument to pass to the function
        num_iterations: The number of iterations to run the function

    Returns:
        The output of the function after the given number of iterations.
        If the function has cyclical output, the output will be calculated
        based on the number of iterations before the cycle is detected and
        the number of iterations within the cycle. If the function does not
        have cyclical output, the output will be the output of the function
        after the given number of iterations.
    """

    cycle_found = False
    num_iterations_before_cycle = 0
    num_iterations_in_cycle = 0
    seen = {arg: 0}
    for i in range(1, num_iterations):
        arg = func(arg)
        if arg in seen:
            num_iterations_before_cycle = seen[arg]
            num_iterations_in_cycle = i - num_iterations_before_cycle
            cycle_found = True
            break
        else:
            seen[arg] = i

    if cycle_found:
        remainder = (num_iterations - num_iterations_before_cycle) % num_iterations_in_cycle
        i_cycle = num_iterations_before_cycle + remainder
        final_arg = [k for k, v in seen.items() if v == i_cycle][0]
        return final_arg

    return arg
