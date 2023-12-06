from attr import frozen


@frozen
class Race:
    time: int
    distance_to_beat: int


def get_race(input_text: str) -> Race:
    lines = input_text.splitlines()
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return Race(time, distance)


def get_number_of_ways_to_win(input_text: str) -> int:
    race = get_race(input_text)
    for i in range(0, race.time + 1):
        distance = i * (race.time - i)
        if distance > race.distance_to_beat:
            num_losing_races = i * 2
            return (race.time + 1) - num_losing_races
