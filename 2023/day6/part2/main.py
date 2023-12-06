import os

from day6.part2.solution import get_number_of_ways_to_win

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    # Answer: 42515755
    print(get_number_of_ways_to_win(input_text))
