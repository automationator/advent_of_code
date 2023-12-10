#!/usr/bin/env python3

import argparse
import datetime
import os
import webbrowser
from pathlib import Path

import requests


def _create_init_files(paths: tuple[str, ...]) -> None:
    """Create an __init__.py file in each directory"""
    init_dir = paths[0]
    Path(os.path.join(init_dir, "__init__.py")).touch()
    for p in paths[1:]:
        init_dir = os.path.join(init_dir, p)
        Path(os.path.join(init_dir, "__init__.py")).touch()


#
# Get the session token
#
session_token = os.environ.get("AOC_SESSION_TOKEN")
if not session_token:
    print("Please set the AOC_SESSION_TOKEN environment variable")
    exit(1)

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
# Open the puzzle in the browser
#
url = f"https://adventofcode.com/{year}/day/{day}"
webbrowser.open_new_tab(url)

#
# Fetch the puzzle input
#
response = requests.get(f"{url}/input", cookies={"session": session_token})
if response.status_code != 200:
    print("Error getting the day's input")
    exit(1)

#
# Scaffold the solution
#
day_path_tup = ("aoc", f"y{year}", f"day{day}")
day_path = Path(os.path.join(*day_path_tup))
os.makedirs(day_path, exist_ok=True)
_create_init_files(day_path_tup)

Path(os.path.join(day_path, "__init__.py")).touch()

with open(os.path.join(day_path, "input.txt"), "w") as f:
    f.write(response.text.strip())

with open(os.path.join(day_path, "solution.py"), "w") as f:
    f.write(
        f"""# {url}

def part1(input_text: str) -> int:
    return 0

def part2(input_text: str) -> int:
    return 0"""
    )

#
# Scaffold the tests
#
tests_path_tup = ("tests",) + day_path_tup
tests_path = Path(os.path.join(*tests_path_tup))
os.makedirs(tests_path, exist_ok=True)
_create_init_files(tests_path_tup)

with open(os.path.join(tests_path, "test_solution.py"), "w") as f:
    f.write(
        f'''# {url}

from aoc.y{year}.day{day}.solution import (
    part1,
    part2,
)

def test_part1():
    input_text = """"""

    assert part1(input_text) == 0

def test_part2():
    input_text = """"""

    assert part2(input_text) == 0'''
    )
