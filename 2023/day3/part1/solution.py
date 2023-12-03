import re


class Schematic:
    def __init__(self, input_text: str):
        self.schematic = input_text.splitlines()

    def get_part_numbers(self) -> list[int]:
        """
        Gets the part numbers from the schematic. A number is only a valid
        part number if it is adjacent to a symbol, even diagonally. However,
        a period does not count as a symbol.
        """

        part_numbers = []

        for y, line in enumerate(self.schematic):
            # Find the potential part numbers in this row
            for match in re.finditer(r"(\d+)", line):
                # If any of the digits in the number are adjacent to a symbol,
                # then it is a valid part number.
                for x in range(match.start(), match.end()):
                    if self._cell_has_adjacent_symbol(x, y):
                        part_numbers.append(int(match.group(1)))
                        break

        return part_numbers

    def _cell_has_adjacent_symbol(self, x: int, y: int) -> bool:
        """
        Checks the adjacent (including diagonal) cells to see if any of them
        are symbols (excluding periods).
        """

        invalid_symbols = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", None}

        # Check the cells above (including diagonals)
        if self._get_value_at(x - 1, y - 1) not in invalid_symbols:
            return True
        if self._get_value_at(x, y - 1) not in invalid_symbols:
            return True
        if self._get_value_at(x + 1, y - 1) not in invalid_symbols:
            return True

        # Check the cell to the left
        if self._get_value_at(x - 1, y) not in invalid_symbols:
            return True

        # Check the cell to the right
        if self._get_value_at(x + 1, y) not in invalid_symbols:
            return True

        # Check the cells below (including diagonals)
        if self._get_value_at(x - 1, y + 1) not in invalid_symbols:
            return True
        if self._get_value_at(x, y + 1) not in invalid_symbols:
            return True
        if self._get_value_at(x + 1, y + 1) not in invalid_symbols:
            return True

        return False

    def _get_value_at(self, x: int, y: int) -> str | None:
        """
        Gets the value at the given coordinates. If the coordinates are out of
        bounds, then None is returned.

        Note: This treats negative indexing as out of bounds.
        """

        if x < 0 or y < 0:
            return None

        try:
            return self.schematic[y][x]
        except IndexError:
            return None
