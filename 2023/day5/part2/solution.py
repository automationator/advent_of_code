import multiprocessing
import re


class Publisher:
    @classmethod
    def publish_almanac(cls, manuscript: str) -> "Almanac":
        sections = manuscript.split("\n\n")
        tables = [Table(section) for section in sections if "map:" in section]
        return Almanac(tables)


class Map:
    def __init__(self, destination_range_start: str, source_range_start: str, range_length: str):
        self._d_start = int(destination_range_start)
        self._s_start = int(source_range_start)
        self._r_length = int(range_length)
        self._d_range = range(self._d_start, self._d_start + self._r_length)
        self.source_range = range(self._s_start, self._s_start + self._r_length)

    def convert_source(self, source: int) -> int:
        source_index = source - self._s_start
        return self._d_range[source_index]


class Table:
    def __init__(self, input_text: str):
        self.maps = []
        for line in input_text.splitlines()[1:]:
            self.maps.append(Map(*line.split()))

    def identify_map(self, source: int) -> Map | None:
        return next((m for m in self.maps if source in m.source_range), None)


class Almanac:
    def __init__(self, tables: list[Table]):
        self._tables = tables

    def get_seed_location(self, seed: str | int) -> int:
        """
        To get the seed location, you need to map the seed through all the tables in the almanac.
        """

        source = int(seed)
        for table in self._tables:
            m = table.identify_map(source)
            if m:
                source = m.convert_source(source)

        return source

    def get_lowest_seed_location(self, seed_range: range) -> int:
        lowest_location = float("inf")
        for seed in seed_range:
            if (location := self.get_seed_location(seed)) < lowest_location:
                lowest_location = location
        return lowest_location


def get_seed_ranges(input_text: str) -> list[range]:
    seed_ranges = []
    for r in re.findall(r"(\d+ \d+)", input_text.splitlines()[0]):
        r_start, r_length = r.split()
        seed_ranges.append(range(int(r_start), int(r_start) + int(r_length)))
    return seed_ranges


def _get_lowest_seed_location(almanac: Almanac, seed_range: range) -> int:
    lowest_location = float("inf")
    for seed in seed_range:
        if (location := almanac.get_seed_location(seed)) < lowest_location:
            lowest_location = location
    return lowest_location


def split_range(r: range, n: int) -> list[range]:
    """
    Split a range into `n` ranges of equal length. The final range may be shorter than the others.
    """

    k, m = divmod(len(r), n)
    return [r[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n)]


def parallelize_get_lowest_seed_location(input_text: str) -> int:
    almanac = Publisher.publish_almanac(input_text)

    locations = []
    num_cores = multiprocessing.cpu_count()
    for seed_range in get_seed_ranges(input_text):
        with multiprocessing.Pool(num_cores) as pool:
            locations.extend(
                pool.starmap(
                    _get_lowest_seed_location,
                    [(almanac, r) for r in split_range(seed_range, num_cores)],
                )
            )

    return min(locations)
