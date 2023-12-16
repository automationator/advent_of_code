# https://adventofcode.com/2023/day/12
#
# TODO: Understand this one better... had to heavily rely on some hints.
# I solved Part 1 by myself using an iterative brute force approach that took
# ~7 seconds, which would never work for Part 2. I ended up removing that
# approach and replaced it with one that works for both parts after looking
# at some hints. But I don't fully understand it (or dynamic programming) yet.
#
# See here for more info:
# https://advent-of-code.xavd.id/writeups/2023/day/12/
# https://www.youtube.com/watch?v=g3Ms5e7Jdqo&pp=ygUaYWR2ZW50IG9mIGNvZGUgMjAyMyBkYXkgMTI%3D
# https://old.reddit.com/r/adventofcode/comments/18ghux0/2023_day_12_no_idea_how_to_start_with_this_puzzle/kd0npmi/

import functools


def parse_lines(input_text: str, unfold_factor: int = 0) -> list[tuple[str, tuple[int, ...]]]:
    ret = []

    for line in input_text.splitlines():
        springs, lengths_str = line.split()
        lengths = [int(length) for length in lengths_str.split(",")]

        if unfold_factor:
            springs = "?".join([springs] * unfold_factor)
            lengths = lengths * unfold_factor

        ret.append((springs, tuple(lengths)))

    return ret


@functools.cache
def count_variations(springs: str, lengths: tuple[int, ...]) -> int:
    if springs == "":
        return 1 if lengths == () else 0

    if lengths == ():
        return 0 if "#" in springs else 1

    result = 0

    if springs[0] in ".?":
        result += count_variations(springs[1:], lengths)

    if springs[0] in "#?" and (
        lengths[0] <= len(springs)
        and "." not in springs[: lengths[0]]
        and (lengths[0] == len(springs) or springs[lengths[0]] != "#")
    ):
        result += count_variations(springs[lengths[0] + 1 :], lengths[1:])

    return result


def part1(input_text: str) -> int:
    total = 0

    for springs, lengths in parse_lines(input_text):
        total += count_variations(springs, lengths)

    # Answer: 7307
    return total


def part2(input_text: str) -> int:
    total = 0

    for springs, lengths in parse_lines(input_text, unfold_factor=5):
        total += count_variations(springs, lengths)

    # Answer: 3415570893842
    return total
