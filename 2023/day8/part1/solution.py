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
