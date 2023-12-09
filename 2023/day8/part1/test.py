import os

from day8.part1.solution import (
    parse_nodes,
    parse_steps,
    traverse,
)

with open(os.path.join(os.path.dirname(__file__), "..", "sample_input.txt")) as f:
    input_text = f.read()


def test_parse_steps():
    assert parse_steps(input_text) == ["L", "L", "R"]


def test_parse_nodes():
    assert parse_nodes(input_text) == {
        "AAA": ("AAA", "BBB", "BBB"),
        "BBB": ("BBB", "AAA", "ZZZ"),
        "ZZZ": ("ZZZ", "ZZZ", "ZZZ"),
    }


def test_traverse():
    assert traverse(input_text) == 6
