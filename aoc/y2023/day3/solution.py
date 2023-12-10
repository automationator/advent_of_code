# https://adventofcode.com/2023/day/3

import math
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

    def get_gear_ratios(self) -> list[int]:
        gear_ratios = []

        for y, line in enumerate(self.schematic):
            # Find the potential gears in this row
            for potential_gear in re.finditer(r"(\*)", line):
                gear_ratio_candidates = []

                # Find all numbers in the row above. If any of the numbers are positioned
                # such that their x coordinates overlap with the potential gear (including
                # diagonally), then it is a candidate for a gear ratio.
                if y > 0:
                    for above_part_number in re.finditer(r"(\d+)", self.schematic[y - 1]):
                        # If any of the digits in the number are adjacent to the potential
                        # gear, then it is a valid part number.
                        if _ranges_overlap(
                            range(potential_gear.start() - 1, potential_gear.end() + 1),
                            range(above_part_number.start(), above_part_number.end()),
                        ):
                            gear_ratio_candidates.append(int(above_part_number.group(1)))

                # Find all numbers in the current row. If any of them border the
                # potential gear, then it is a candidate for a gear ratio.
                for current_part_number in re.finditer(r"(\d+)", line):
                    # If any of the digits in the number are adjacent to the potential
                    # gear, then it is a valid part number.
                    if _ranges_overlap(
                        range(potential_gear.start() - 1, potential_gear.end() + 1),
                        range(current_part_number.start(), current_part_number.end()),
                    ):
                        gear_ratio_candidates.append(int(current_part_number.group(1)))

                # Find all numbers in the row below. If any of the numbers are positioned
                # such that their x coordinates overlap with the potential gear (including
                # diagonally), then it is a candidate for a gear ratio.
                if y < len(self.schematic) - 1:
                    for below_part_number in re.finditer(r"(\d+)", self.schematic[y + 1]):
                        # If any of the digits in the number are adjacent to the potential
                        # gear, then it is a valid part number.
                        if _ranges_overlap(
                            range(potential_gear.start() - 1, potential_gear.end() + 1),
                            range(below_part_number.start(), below_part_number.end()),
                        ):
                            gear_ratio_candidates.append(int(below_part_number.group(1)))

                # If there are exactly two gear ratio candidates, then we have a
                # valid gear ratio.
                if len(gear_ratio_candidates) == 2:
                    gear_ratios.append(math.prod(gear_ratio_candidates))

        return gear_ratios


def _ranges_overlap(a: range, b: range) -> bool:
    return a.start in b or b.start in a


def part1(input_text: str) -> int:
    schematic = Schematic(input_text)
    part_numbers = schematic.get_part_numbers()

    # Answer: 514969
    return sum(part_numbers)


def part2(input_text: str) -> int:
    schematic = Schematic(input_text)
    gear_ratios = schematic.get_gear_ratios()

    # Answer: 78915902
    return sum(gear_ratios)
