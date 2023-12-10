# https://adventofcode.com/2023/day/6

import math
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    distance_to_beat: int


def get_races(input_text: str) -> list[Race]:
    lines = input_text.splitlines()
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    return [Race(time, distance) for time, distance in zip(times, distances)]


def get_number_of_ways_to_win(race: Race) -> int:
    for i in range(0, race.time + 1):
        distance = i * (race.time - i)
        if distance > race.distance_to_beat:
            num_losing_races = i * 2
            return (race.time + 1) - num_losing_races


def num_ways_to_win_multiplied(input_text: str) -> int:
    races = get_races(input_text)
    return math.prod([get_number_of_ways_to_win(race) for race in races])


def get_race(input_text: str) -> Race:
    lines = input_text.splitlines()
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return Race(time, distance)


def part1(input_text: str) -> int:
    # Answer: 500346
    return num_ways_to_win_multiplied(input_text)


def part2(input_text: str) -> int:
    # Answer: 42515755
    race = get_race(input_text)
    for i in range(0, race.time + 1):
        distance = i * (race.time - i)
        if distance > race.distance_to_beat:
            num_losing_races = i * 2
            return (race.time + 1) - num_losing_races
