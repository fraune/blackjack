import random

from app.Card import Pip, Card
from app.utility.logging import v


class Deck(object):
    cards: list[Card]
    SHUFFLE_PASSES: int = 7

    def __init__(self, number_suits: int = 4):
        self.cards = []
        for suit in range(number_suits):
            for pip in list(Pip):
                v(f'  adding card to deck: {pip}')
                self.cards.append(Card(pip))

    def shuffle(self):
        for pazz in range(self.SHUFFLE_PASSES):
            first = random.randint(0, len(self.cards))
            second = random.randint(0, len(self.cards))
            aside = self.cards[first]
            self.cards[first] = self.cards[second]
            self.cards[second] = aside

    def take_top_card(self) -> Card:
        # TODO: Throws exception when deck is empty
        return self.cards.pop()

    def peek_top_card(self) -> Card:
        # TODO: Throws exception when deck is empty
        # TODO: This is cheating
        return self.cards[-1]

    def as_string(self):
        deck = '('
        for card in self.cards:
            deck += card.pip.as_string()
        deck += ')'
        return deck

    def print(self):
        v(self.as_string())
