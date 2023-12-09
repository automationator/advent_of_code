import os

from day8.part1.solution import traverse

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    # Answer: 14681
    print(traverse(input_text))
