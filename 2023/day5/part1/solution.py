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
            map = table.identify_map(source)
            if map:
                source = map.convert_source(source)

        return source


def get_seed_numbers(input_text: str) -> list[int]:
    return [int(s) for s in input_text.splitlines()[0].split(":")[1].split()]
