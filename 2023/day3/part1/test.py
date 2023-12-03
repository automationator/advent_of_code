from day3.part1.solution import Schematic

TEST_SCHEMATIC = """467..114..
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
    part_numbers = schematic.get_part_numbers()
    assert len(part_numbers) == 8
    assert 114 not in part_numbers
    assert 58 not in part_numbers
    assert sum(part_numbers) == 4361
