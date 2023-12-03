from day3.part2.solution import Schematic

TEST_SCHEMATIC = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_get_part_numbers():
    schematic = Schematic(TEST_SCHEMATIC)
    gear_ratios = schematic.get_gear_ratios()
    assert len(gear_ratios) == 2
    assert 16345 in gear_ratios
    assert 451490 in gear_ratios
