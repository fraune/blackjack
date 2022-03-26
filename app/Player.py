from app.Deck import Deck
from app.Hand import Hand
from app.utility.exceptions import RoundOverException


class Player:
    shared_deck: Deck
    hand: Hand
    round_over: bool

    def __init__(self, deck: Deck):
        self.shared_deck = deck
        self.hand = Hand()

    def start_round(self):
        self.hand.reset()
        self.round_over = False

    def hit(self):
        if self.round_over:
            raise RoundOverException
        self.hand.add_card(self.shared_deck.take_top_card())
        if self.hand.score_hand() > 21:
            self.round_over = True

    def stand(self):
        self.round_over = True
