# https://adventofcode.com/2023/day/7

from collections import Counter
from dataclasses import dataclass
from enum import IntEnum


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
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


CARD_MAPPING_JACKS = {
    "2": Card.TWO,
    "3": Card.THREE,
    "4": Card.FOUR,
    "5": Card.FIVE,
    "6": Card.SIX,
    "7": Card.SEVEN,
    "8": Card.EIGHT,
    "9": Card.NINE,
    "T": Card.TEN,
    "J": Card.JACK,
    "Q": Card.QUEEN,
    "K": Card.KING,
    "A": Card.ACE,
}

CARD_MAPPING_JOKERS = {
    **CARD_MAPPING_JACKS,
    "J": Card.JOKER,
}


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


@dataclass
class Hand:
    cards: tuple[Card, Card, Card, Card, Card]
    bid: int
    with_jokers: bool = False

    _hand_type = None
    _upgraded_hand_type = None
    _len_set_cards = None

    def __lt__(self, other) -> bool:
        if self.with_jokers and other.with_jokers:
            this_type = self.upgraded_hand_type
            other_type = other.upgraded_hand_type
        else:
            this_type = self.hand_type
            other_type = other.hand_type

        if this_type < other_type:
            return True
        elif this_type == other_type:
            return self.cards < other.cards

        return False

    def __str__(self) -> str:
        return f"{self.hand_type.name} {[c.name for c in self.cards]} {self.bid}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(cards={self.cards}, bid={self.bid})"

    @property
    def len_set_cards(self):
        if self._len_set_cards is None:
            self._len_set_cards = len(set(self.cards))
        return self._len_set_cards

    @property
    def hand_type(self) -> HandType:
        if self._hand_type is None:
            if self._is_five_of_a_kind():
                self._hand_type = HandType.FIVE_OF_A_KIND
            # Determining full house must be done before four of a kind
            # because they both rely on the length of the set of cards
            # being 2, but full house has the additional requirement of
            # three of a kind.
            elif self._is_full_house():
                self._hand_type = HandType.FULL_HOUSE
            elif self._is_four_of_a_kind():
                self._hand_type = HandType.FOUR_OF_A_KIND
            elif self._is_three_of_a_kind():
                self._hand_type = HandType.THREE_OF_A_KIND
            elif self._is_two_pair():
                self._hand_type = HandType.TWO_PAIR
            elif self._is_one_pair():
                self._hand_type = HandType.ONE_PAIR
            else:
                self._hand_type = HandType.HIGH_CARD
        return self._hand_type

    @property
    def upgraded_hand_type(self) -> HandType:
        if self._upgraded_hand_type is None:
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
                self._upgraded_hand_type = HandType.FIVE_OF_A_KIND

            # Determining full house must be done before four of a kind
            # because they both rely on the length of the set of cards
            # being 2, but full house has the additional requirement of
            # three of a kind.
            elif self._is_full_house():
                self._upgraded_hand_type = (
                    HandType.FIVE_OF_A_KIND if Card.JOKER in self.cards else HandType.FULL_HOUSE
                )

            elif self._is_four_of_a_kind():
                self._upgraded_hand_type = (
                    HandType.FIVE_OF_A_KIND
                    if Card.JOKER in self.cards
                    else HandType.FOUR_OF_A_KIND
                )

            elif self._is_three_of_a_kind():
                self._upgraded_hand_type = (
                    HandType.FOUR_OF_A_KIND
                    if Card.JOKER in self.cards
                    else HandType.THREE_OF_A_KIND
                )

            elif self._is_two_pair():
                if Card.JOKER in self.cards:
                    counts = Counter(self.cards)
                    self._upgraded_hand_type = (
                        HandType.FOUR_OF_A_KIND if counts[Card.JOKER] == 2 else HandType.FULL_HOUSE
                    )
                else:
                    self._upgraded_hand_type = HandType.TWO_PAIR

            elif self._is_one_pair():
                self._upgraded_hand_type = (
                    HandType.THREE_OF_A_KIND if Card.JOKER in self.cards else HandType.ONE_PAIR
                )

            else:
                self._upgraded_hand_type = (
                    HandType.ONE_PAIR if Card.JOKER in self.cards else HandType.HIGH_CARD
                )

        return self._upgraded_hand_type

    def _is_five_of_a_kind(self) -> bool:
        return self.len_set_cards == 1

    def _is_four_of_a_kind(self) -> bool:
        return self.len_set_cards == 2

    def _is_full_house(self) -> bool:
        return self.len_set_cards == 2 and self._is_three_of_a_kind()

    def _is_three_of_a_kind(self) -> bool:
        return any(v == 3 for v in Counter(self.cards).values())

    def _is_two_pair(self) -> bool:
        return self.len_set_cards == 3

    def _is_one_pair(self) -> bool:
        return self.len_set_cards == 4


def _parse_hand(input_text: str, with_jokers: bool) -> Hand:
    cards_str, bid_str = input_text.split()

    map = CARD_MAPPING_JOKERS if with_jokers else CARD_MAPPING_JACKS
    return Hand(
        cards=tuple(map[c] for c in cards_str),
        bid=int(bid_str),
        with_jokers=with_jokers,
    )


def _parse_hands(input_text: str, with_jokers: bool) -> list[Hand]:
    return [_parse_hand(line, with_jokers) for line in input_text.splitlines()]


def _count_total_winnings(input_text: str, with_jokers: bool = False) -> int:
    total_winnings = 0
    sorted_hands = sorted(_parse_hands(input_text, with_jokers))
    for i, hand in enumerate(sorted_hands):
        total_winnings += hand.bid * (i + 1)
    return total_winnings


def part1(input_text: str) -> int:
    # Answer: 248422077
    return _count_total_winnings(input_text)


def part2(input_text: str) -> int:
    # Answer: 249817836
    return _count_total_winnings(input_text, with_jokers=True)
