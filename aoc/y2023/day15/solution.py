# https://adventofcode.com/2023/day/15

from collections import defaultdict
from dataclasses import dataclass
from typing import Literal


@dataclass
class Step:
    label: str
    box: int
    operation: Literal["=", "-"]
    focal_length: int | None

    @classmethod
    def parse_step(cls, input_text: str) -> "Step":
        if "-" in input_text:
            label = input_text.split("-")[0]
            operation = "-"
            focal_length = None
        else:
            s = input_text.split("=")
            label = s[0]
            operation = "="
            focal_length = int(s[1])

        return cls(label=label, box=hash(label), operation=operation, focal_length=focal_length)


def perform_steps(steps: list[Step]) -> dict[int, dict[str, int]]:
    """
    Organize the lenses in each step into their boxes. For example, the final output
    for the test input would be:

    boxes = {
        0: {
            "rn": 1,
            "cm": 2,
        },
        1: {},
        3: {
            "ot": 7,
            "ab": 5,
            "pc": 6,
        }
    }
    """

    boxes = defaultdict(dict)
    for step in steps:
        if step.operation == "=":
            boxes[step.box][step.label] = step.focal_length
        else:
            boxes[step.box].pop(step.label, None)

    return boxes


def calculate_focusing_power(boxes: dict[int, dict[str, int]]) -> int:
    """
    Adds up the focusing power of all of the lenses. The focusing power of a
    single lens is the result of multiplying together:

    One plus the box number of the lens in question.
    The slot number of the lens within the box: 1 for the first lens, etc.
    The focal length of the lens.
    """

    total = 0
    for box, lenses in boxes.items():
        for idx, lense in enumerate(lenses.keys()):
            total += (box + 1) * (idx + 1) * lenses[lense]

    return total


def hash(input_text: str) -> int:
    """
    Determine the ASCII code for the current character of the string.
    Increase the current value by the ASCII code you just determined.
    Set the current value to itself multiplied by 17.
    Set the current value to the remainder of dividing itself by 256.
    """

    current_value = 0
    for char in input_text:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


def part1(input_text: str) -> int:
    total = 0
    for s in input_text.split(","):
        total += hash(s)

    assert total == 516804
    return total


def part2(input_text: str) -> int:
    steps = []
    for s in input_text.split(","):
        steps.append(Step.parse_step(s))

    boxes = perform_steps(steps)

    focusing_power = calculate_focusing_power(boxes)
    assert focusing_power == 231844
    return focusing_power
