import random
from enum import Enum


class Card(Enum):
    ACE = 1,
    TWO = 2,
    THREE = 3,
    FOUR = 4,
    FIVE = 5,
    SIX = 6,
    SEVEN = 7,
    EIGHT = 8,
    NINE = 9,
    TEN = 10,
    JACK = 11,
    QUEEN = 12,
    KING = 13

    def as_string(self):
        return f'[{self.name}]'


class Deck:
    cards: list[Card] = []
    DUPLICATE_VALUES_PER_DECK: int = 1
    SHUFFLE_PASSES: int = 7

    def __init__(self):
        for card in list(Card):
            for i in range(self.DUPLICATE_VALUES_PER_DECK):
                self.cards.append(card)

        # self.shuffle()

    def shuffle(self):
        for pazz in range(self.SHUFFLE_PASSES):
            i = random.randint(0, len(Card))
            j = random.randint(0, len(Card))
            aside = self.cards[i]
            self.cards[i] = self.cards[j]
            self.cards[j] = aside

    def as_string(self):
        deck = '('
        for card in self.cards:
            deck += card.as_string()
        deck += ')'

    def print(self):
        print(self.as_string())
