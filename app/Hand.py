from app.Card import Card
from app.utility.logging import v


class Hand:
    cards: list[Card]

    def __init__(self):
        self.cards = []

    def deal_card(self, card_to_add: Card):
        self.cards.append(card_to_add)

    def score_hand(self) -> int:
        # Count all cards, but count aces last
        score = 0
        while True:
            updated = False
            for card in self.cards:
                update = card.update_score(score)
                if update != 0:
                    updated = True
                    score += update
            if not updated:
                break
        return score

    def as_string(self):
        hand = '('
        for card in self.cards:
            hand += card.pip.as_string()
        hand += ')'
        return hand

    def print(self):
        v(self.as_string())
