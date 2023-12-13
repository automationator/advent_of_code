# https://adventofcode.com/2023/day/10

from skimage.draw import polygon

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""


MAZE_TYPE = dict[tuple[int, int], list[tuple[int, int]]]

PIPE_MAPPING: dict[str, list[tuple[int, int]]] = {
    "|": [(0, -1), (0, 1)],  # North and south
    "-": [(-1, 0), (1, 0)],  # East and west
    "L": [(0, -1), (1, 0)],  # North and east
    "J": [(0, -1), (-1, 0)],  # North and west
    "7": [(0, 1), (-1, 0)],  # South and west
    "F": [(0, 1), (1, 0)],  # South and east
    ".": [],
    "S": [],
}


def is_valid_connection(connection: tuple[int, int]) -> bool:
    """Returns True if the connection is valid, False otherwise. An invalid
    connection is one that is outside the bounds of the maze."""

    return all(coordinate >= 0 for coordinate in connection)


def get_connecting_coordinates(value: str, x: int, y: int) -> list[tuple[int, int]]:
    """Returns a list of tuples containing the coordinates of the pipes that
    are connected to the pipe at the given coordinates."""

    connection_points = PIPE_MAPPING[value]
    connections = []
    for connection_point in connection_points:
        possible_connection = (x + connection_point[0], y + connection_point[1])
        if is_valid_connection(possible_connection):
            connections.append(possible_connection)

    return connections


def parse_maze(input_text: str) -> tuple[MAZE_TYPE, tuple[int, int]]:
    """Parses the input text maze into a dictionary where there is a key for
    every coordinate in the maze represented by a tuple in the form of
    (value, x, y) where value is the character at that position in the maze
    and x and y are the coordinates of the position in the maze.

    The values of the dictionary are lists containing up to two tuples in the
    form of [(x1, y1), (x2, y2)] where (x1, y1) is the position of the first
    connected pipe and (x2, y2) is the position of the second connected pipe.
    The value will be empty if the pipe is not connected to another pipe."""

    maze = {}
    start = (0, 0)
    for y, line in enumerate(input_text.splitlines()):
        for x, value in enumerate(line):
            maze[(x, y)] = get_connecting_coordinates(value, x, y)
            if value == "S":
                start = (x, y)

    # Fill in the connecting coordinates for the starting pipe
    maze[start] = [c for c in maze if (start[0], start[1]) in maze[c]]

    return maze, start


def get_maze_path(maze: MAZE_TYPE, start: tuple[int, int]) -> list[tuple[int, int]]:
    """Returns the path of the closed loop in the maze. The order of the path
    is the order in which the pipes are connected as if you were to pick a
    direction and walk the closed loop."""

    path = [start]
    seen = set()
    points_to_check = [start]
    while points_to_check:
        point = points_to_check.pop()
        next_point = next((p for p in maze[point] if p not in seen), None)
        if next_point:
            seen.add(point)
            path.append(next_point)
            points_to_check.append(next_point)

    return path


def part1(input_text: str) -> int:
    maze, start = parse_maze(input_text)

    # To have a closed loop, the length of the path will always be an even
    # number. The farthest you can get from the starting point is to go
    # halfway down the path, which is the length of the path divided by 2.
    return len(get_maze_path(maze, start)) // 2


def part2(input_text: str) -> int:
    maze, start = parse_maze(input_text)
    path = get_maze_path(maze, start)

    # Create a filled polygon from the path
    path_polygon = polygon(r=[p[1] for p in path], c=[p[0] for p in path])

    # The number of pixels fully enclosed by the path is equal to the number
    # of pixels in the polygon minus the number of pixels in the path
    return len(path_polygon[0]) - len(path)
