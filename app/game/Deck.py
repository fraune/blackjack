import random

from app.game.Card import Pip, Card
from app.utility.logging import v


class Deck:
    _SHUFFLE_PASSES: int = 7
    number_suits: int
    cards: list[Card]

    def __init__(self, number_suits: int = 4):
        self.number_suits = number_suits
        self.reset()

    def reset(self):
        self.cards = []
        for suit in range(self.number_suits):
            for pip in list(Pip):
                v(f'  adding card to deck: {pip}')
                self.cards.append(Card(pip))

    def shuffle(self):
        for pazz in range(self._SHUFFLE_PASSES):
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
