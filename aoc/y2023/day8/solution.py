# https://adventofcode.com/2023/day/8

import math
import re


def parse_steps(input_text: str) -> list[str]:
    return [s for s in input_text.splitlines()[0]]


def parse_nodes(input_text: str) -> dict[str, tuple[str, str, str]]:
    nodes = {}

    for line in input_text.splitlines():
        if "=" in line:
            node, left, right = re.findall(r"(\w+) = \((\w+), (\w+)\)", line)[0]
            nodes[node] = (node, left, right)

    return nodes


def traverse(input_text: str) -> int:
    nodes = parse_nodes(input_text)
    steps = parse_steps(input_text)
    current_node = nodes["AAA"]
    end_node = nodes["ZZZ"]
    num_steps = 0
    while current_node != end_node:
        for step in steps:
            num_steps += 1
            left_node = nodes[current_node[1]]
            right_node = nodes[current_node[2]]
            if step == "L":
                current_node = left_node
            elif step == "R":
                current_node = right_node

    return num_steps


def traverse_like_a_ghost(input_text: str) -> int:
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


def part1(input_text: str) -> int:
    # Answer: 14681
    return traverse(input_text)


def part2(input_text: str) -> int:
    # Answer: 14321394058031
    return traverse_like_a_ghost(input_text)
