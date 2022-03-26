from enum import Enum

from app.Dealer import Dealer
from app.Deck import Deck
from app.Player import Player
from app.utility.exceptions import UnknownGameStateException


class EndGameState(Enum):
    DEALER_WINS = 0
    PLAYER_WINS = 1
    TIE = 2


class Game:
    deck: Deck
    dealer: Dealer
    player: Player

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.player = Player(self.deck)

    def new_round(self):
        self.deck.reset()
        self.deck.shuffle()
        self.dealer.reset_round()
        self.player.reset_round()

    def determine_winner(self):
        dealer_score = self.dealer.hand.score_hand()
        player_score = self.dealer.hand.score_hand()

        if dealer_score > 21 and player_score > 21:
            return EndGameState.TIE

        if dealer_score > 21:
            return EndGameState.PLAYER_WINS

        if player_score > 21:
            return EndGameState.DEALER_WINS

        if dealer_score == player_score:
            return EndGameState.TIE

        if dealer_score > player_score:
            return EndGameState.DEALER_WINS

        if player_score > dealer_score:
            return EndGameState.PLAYER_WINS

        raise UnknownGameStateException()
