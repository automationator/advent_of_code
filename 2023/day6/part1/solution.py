import math

from attr import frozen

"""
Time:      7  15   30
Distance:  9  40  200
"""


@frozen
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
