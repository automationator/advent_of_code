import os

import pytest
from day7.part1.solution import (
    Card,
    Hand,
    HandType,
    count_total_winnings,
    parse_hands,
)

with open(os.path.join(os.path.dirname(__file__), "..", "sample_input.txt")) as f:
    input_text = f.read()


def test_parse_hands():
    assert parse_hands(input_text) == [
        Hand(cards=(Card.THREE, Card.TWO, Card.TEN, Card.THREE, Card.KING), bid=765),
        Hand(cards=(Card.TEN, Card.FIVE, Card.FIVE, Card.JACK, Card.FIVE), bid=684),
        Hand(cards=(Card.KING, Card.KING, Card.SIX, Card.SEVEN, Card.SEVEN), bid=28),
        Hand(cards=(Card.KING, Card.TEN, Card.JACK, Card.JACK, Card.TEN), bid=220),
        Hand(cards=(Card.QUEEN, Card.QUEEN, Card.QUEEN, Card.JACK, Card.ACE), bid=483),
    ]


@pytest.mark.parametrize(
    "hand, expected",
    [
        (
            Hand(cards=(Card.ACE, Card.ACE, Card.ACE, Card.ACE, Card.ACE), bid=1),
            HandType.FIVE_OF_A_KIND,
        ),
        (
            Hand(cards=(Card.ACE, Card.ACE, Card.ACE, Card.ACE, Card.KING), bid=1),
            HandType.FOUR_OF_A_KIND,
        ),
        (
            Hand(cards=(Card.ACE, Card.ACE, Card.ACE, Card.KING, Card.KING), bid=1),
            HandType.FULL_HOUSE,
        ),
        (
            Hand(cards=(Card.ACE, Card.ACE, Card.ACE, Card.KING, Card.QUEEN), bid=1),
            HandType.THREE_OF_A_KIND,
        ),
        (
            Hand(cards=(Card.ACE, Card.ACE, Card.KING, Card.KING, Card.QUEEN), bid=1),
            HandType.TWO_PAIR,
        ),
        (
            Hand(cards=(Card.ACE, Card.ACE, Card.KING, Card.QUEEN, Card.JACK), bid=1),
            HandType.ONE_PAIR,
        ),
        (
            Hand(cards=(Card.ACE, Card.KING, Card.QUEEN, Card.JACK, Card.TEN), bid=1),
            HandType.HIGH_CARD,
        ),
    ],
)
def test_hand_type(hand, expected):
    assert hand.hand_type == expected


def test_sort_hands():
    hands = parse_hands(input_text)
    assert sorted(hands) == [
        Hand(cards=(Card.THREE, Card.TWO, Card.TEN, Card.THREE, Card.KING), bid=765),
        Hand(cards=(Card.KING, Card.TEN, Card.JACK, Card.JACK, Card.TEN), bid=220),
        Hand(cards=(Card.KING, Card.KING, Card.SIX, Card.SEVEN, Card.SEVEN), bid=28),
        Hand(cards=(Card.TEN, Card.FIVE, Card.FIVE, Card.JACK, Card.FIVE), bid=684),
        Hand(cards=(Card.QUEEN, Card.QUEEN, Card.QUEEN, Card.JACK, Card.ACE), bid=483),
    ]


def test_count_total_winnings():
    assert count_total_winnings(input_text) == 6440
