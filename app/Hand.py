from app.Card import Card
from app.utility.logging import v


class Hand:
    cards: list[Card]

    def __init__(self):
        self.reset()

    def reset(self):
        self.cards = []

    def add_card(self, card_to_add: Card):
        self.cards.append(card_to_add)

    def score_hand(self) -> int:
        while True:
            score = 0
            for card in self.cards:
                score += card.score

            new_score = score
            for card in self.cards:
                new_score += card.update_score(new_score)

            if score == new_score:
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
