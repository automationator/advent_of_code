from collections import Counter
from dataclasses import dataclass
from enum import IntEnum


class Card(IntEnum):
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


CARD_MAPPING = {
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

    _hand_type = None
    _len_set_cards = None

    def __lt__(self, other) -> bool:
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type == other.hand_type:
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
