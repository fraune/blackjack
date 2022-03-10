import random

from app.Card import Card


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
        return deck

    def print(self):
        print(self.as_string())
