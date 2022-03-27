from app.game.Deck import Deck
from app.game.Hand import Hand
from app.utility.exceptions import RoundOverException


class Player:
    shared_deck: Deck
    hand: Hand
    round_over: bool = False

    def __init__(self, deck: Deck):
        self.shared_deck = deck
        self.hand = Hand()

    def reset_round(self):
        # TODO: Reset Deck
        self.hand.reset()
        self.round_over = False

    def deal_first_two_cards(self):
        self.hand.add_card(self.shared_deck.take_top_card())
        self.hand.add_card(self.shared_deck.take_top_card())
        # TODO: score and end round immediately if 21?

    def hit(self):
        if self.round_over:
            raise RoundOverException
        self.hand.add_card(self.shared_deck.take_top_card())
        if self.hand.score_hand() > 21:
            self.round_over = True

    def stand(self):
        self.round_over = True
