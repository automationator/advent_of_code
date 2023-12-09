import math

from day8.part1.solution import (
    parse_nodes,
    parse_steps,
)


def traverse(input_text: str) -> int:
    nodes = parse_nodes(input_text)
    steps = parse_steps(input_text)

    starts = [nodes[n] for n in nodes if n.endswith("A")]
    all_num_steps = []
    for start in starts:
        current = start
        num_steps = 0
        while not current[0].endswith("Z"):
            for step in steps:
                num_steps += 1
                if step == "L":
                    current = nodes[current[1]]
                elif step == "R":
                    current = nodes[current[2]]

                if current[0].endswith("Z"):
                    all_num_steps.append(num_steps)
                    break

    return math.lcm(*all_num_steps)
