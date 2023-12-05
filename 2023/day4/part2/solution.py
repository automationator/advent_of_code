import re


class Scratchcard:
    def __init__(self, input_text: str):
        parsed_game = re.findall(r"(\d+): ([\d\s]+) \| ([\d\s]+)", input_text)

        self.card_number = parsed_game[0][0]

        winning_numbers = set(parsed_game[0][1].split())
        my_numbers = set(parsed_game[0][2].split())

        self.my_winning_numbers = winning_numbers.intersection(my_numbers)


class StackOfScratchcards:
    def __init__(self, input_text: str):
        self._scratchcards = [Scratchcard(game) for game in input_text.splitlines()]

    def count_scratchcards(self) -> int:
        total = 0
        stack = [s for s in self._scratchcards]
        while stack:
            total += 1
            s = stack.pop()
            # If card 10 has 4 winning numbers, then add cards 11-14,
            # which are indices 10-13.
            if s.my_winning_numbers:
                start_index = int(s.card_number)
                end_index = start_index + len(s.my_winning_numbers)
                stack.extend(self._scratchcards[start_index:end_index])
        return total
