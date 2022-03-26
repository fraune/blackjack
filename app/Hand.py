from app.Card import Card
from app.utility.logging import v


class Hand:
    cards: list[Card]

    def __init__(self):
        self.cards = []

    def deal_card(self, card_to_add: Card):
        self.cards.append(card_to_add)

    def count_hand(self) -> int:
        # Count all cards, but count aces last
        score = 0
        for card in self.cards:
            if card != Card.ACE:
                score += card.as_points()

        for card in self.cards:
            if card == Card.ACE:
                score += card.as_points(score)
        return score

    def as_string(self):
        hand = '('
        for card in self.cards:
            hand += card.as_string()
        hand += ')'
        return hand

    def print(self):
        v(self.as_string())
