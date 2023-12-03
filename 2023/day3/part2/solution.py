import math
import re


def _ranges_overlap(a: range, b: range) -> bool:
    return a.start in b or b.start in a


class Schematic:
    def __init__(self, input_text: str):
        self.schematic = input_text.splitlines()

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
