import random

from app.Card import Card
from app.utility.logging import v


class Deck(object):
    cards: list[Card]
    SHUFFLE_PASSES: int = 7

    def __init__(self, number_suits: int = 4):
        self.cards = []
        for card in list(Card):
            for i in range(number_suits):
                print(f'  adding {card}')
                self.cards.append(card)

    def shuffle(self):
        for pazz in range(self.SHUFFLE_PASSES):
            first = random.randint(0, len(Card))
            second = random.randint(0, len(Card))
            aside = self.cards[first]
            self.cards[first] = self.cards[second]
            self.cards[second] = aside

    def as_string(self):
        deck = '('
        for card in self.cards:
            deck += card.as_string()
        deck += ')'
        return deck

    def print(self):
        v(self.as_string())
