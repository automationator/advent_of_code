from collections import Counter
from dataclasses import dataclass
from enum import IntEnum

from day7.part1.solution import Hand as HandPart1
from day7.part1.solution import HandType


class Card(IntEnum):
    JOKER = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    QUEEN = 11
    KING = 12
    ACE = 13


CARD_MAPPING = {
    "J": Card.JOKER,
    "2": Card.TWO,
    "3": Card.THREE,
    "4": Card.FOUR,
    "5": Card.FIVE,
    "6": Card.SIX,
    "7": Card.SEVEN,
    "8": Card.EIGHT,
    "9": Card.NINE,
    "T": Card.TEN,
    "Q": Card.QUEEN,
    "K": Card.KING,
    "A": Card.ACE,
}


@dataclass
class Hand(HandPart1):
    @property
    def hand_type(self) -> HandType:
        if self._hand_type is None:
            # Jokers can pretend to be any card for the purposes of determining
            # the type of the hand. How many Jokers the hand has determines
            # what type of hand it can be upgraded to. The possible upgrade
            # paths are:
            #
            # 5 OF A KIND -> 5 JOKERS -> 5 OF A KIND
            #
            # 4 OF A KIND -> 4 JOKERS -> 5 OF A KIND
            # 4 OF A KIND -> 1 JOKER -> 5 OF A KIND
            #
            # FULL HOUSE -> 3 JOKERS -> 5 OF A KIND
            # FULL HOUSE -> 2 JOKERS -> 5 OF A KIND
            #
            # 3 OF A KIND -> 3 JOKERS -> 4 OF A KIND
            # 3 OF A KIND -> 1 JOKER -> 4 OF A KIND
            #
            # TWO PAIR -> 2 JOKERS -> 4 OF A KIND
            # TWO PAIR -> 1 JOKER -> FULL HOUSE
            #
            # ONE PAIR -> 2 JOKERS -> 3 OF A KIND
            # ONE PAIR -> 1 JOKER -> 3 OF A KIND
            #
            # HIGH CARD -> 1 JOKER -> ONE PAIR

            if self._is_five_of_a_kind():
                self._hand_type = HandType.FIVE_OF_A_KIND

            # Determining full house must be done before four of a kind
            # because they both rely on the length of the set of cards
            # being 2, but full house has the additional requirement of
            # three of a kind.
            elif self._is_full_house():
                self._hand_type = (
                    HandType.FIVE_OF_A_KIND if Card.JOKER in self.cards else HandType.FULL_HOUSE
                )

            elif self._is_four_of_a_kind():
                self._hand_type = (
                    HandType.FIVE_OF_A_KIND
                    if Card.JOKER in self.cards
                    else HandType.FOUR_OF_A_KIND
                )

            elif self._is_three_of_a_kind():
                self._hand_type = (
                    HandType.FOUR_OF_A_KIND
                    if Card.JOKER in self.cards
                    else HandType.THREE_OF_A_KIND
                )

            elif self._is_two_pair():
                if Card.JOKER in self.cards:
                    counts = Counter(self.cards)
                    self._hand_type = (
                        HandType.FOUR_OF_A_KIND if counts[Card.JOKER] == 2 else HandType.FULL_HOUSE
                    )
                else:
                    self._hand_type = HandType.TWO_PAIR

            elif self._is_one_pair():
                self._hand_type = (
                    HandType.THREE_OF_A_KIND if Card.JOKER in self.cards else HandType.ONE_PAIR
                )

            else:
                self._hand_type = (
                    HandType.ONE_PAIR if Card.JOKER in self.cards else HandType.HIGH_CARD
                )

        return self._hand_type


def _parse_hand(input_text: str) -> Hand:
    cards_str, bid_str = input_text.split()
    return Hand(
        cards=tuple(CARD_MAPPING[c] for c in cards_str),
        bid=int(bid_str),
    )


def parse_hands(input_text: str) -> list[Hand]:
    return [_parse_hand(line) for line in input_text.splitlines()]


def count_total_winnings(input_text: str) -> int:
    total_winnings = 0
    sorted_hands = sorted(parse_hands(input_text))
    for i, hand in enumerate(sorted_hands):
        total_winnings += hand.bid * (i + 1)
    return total_winnings
