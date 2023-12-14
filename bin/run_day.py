#!/usr/bin/env python3

import argparse
import datetime
import importlib
import os
import time

#
# Parse the arguments
#
parser = argparse.ArgumentParser(description="Initialize a new Advent of Code day")
parser.add_argument("-y", "--year", type=int, help="The year of the puzzle")
parser.add_argument("-d", "--day", type=int, help="The day of the puzzle")
args = parser.parse_args()

today = datetime.date.today()
year = args.year
day = args.day

if year > today.year or (year == today.year and day > today.day):
    print("You can't get the puzzle for a future day")
    exit(1)

if day < 1 or day > 25:
    print("There are only 25 days in Advent of Code")
    exit(1)

#
# Get the day solution path
#
solution_path = os.path.join("aoc", f"y{year}", f"day{day}", "solution.py")
if not os.path.exists(solution_path):
    print("You haven't solved this day yet")
    exit(1)

input_path = os.path.join("aoc", f"y{year}", f"day{day}", "input.txt")
if not os.path.exists(input_path):
    print("You do not have the input for this day")
    exit(1)

#
# Run the solution
#

solution_module = importlib.import_module(f"aoc.y{year}.day{day}.solution")
with open(input_path) as f:
    input_text = f.read()

start = time.time()
part1 = solution_module.part1(input_text)
end = time.time()
print(f"Part 1: {part1} ({end - start:.3f}s)")

start = time.time()
part2 = solution_module.part2(input_text)
end = time.time()
print(f"Part 2: {part2} ({end - start:.3f}s)")
