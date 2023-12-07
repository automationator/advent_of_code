import os

from day7.part2.solution import count_total_winnings

with open(os.path.join(os.path.dirname(__file__), "..", "sample_input.txt")) as f:
    input_text = f.read()


def test_count_total_winnings():
    assert count_total_winnings(input_text) == 5905
