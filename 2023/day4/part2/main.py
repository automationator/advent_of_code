import os

from day4.part2.solution import StackOfScratchcards

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "..", "input.txt")) as f:
        input_text = f.read()

    stack = StackOfScratchcards(input_text)

    # Answer: 9881048
    print(stack.count_scratchcards())
