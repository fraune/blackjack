from unittest import TestCase

from app.Card import Pip, Card
from app.Deck import Deck
from app.Player import Player
from app.utility.exceptions import RoundOverException


class TestPlayer(TestCase):

    def test_round_over_after_bust(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.TEN), Card(Pip.JACK), Card(Pip.QUEEN), Card(Pip.KING)]
        player = Player(deck)
        # Act
        player.hit()
        player.hit()
        player.hit()
        # Assert
        assert player.round_over is True
        with self.assertRaises(RoundOverException):
            player.hit()

    def test_round_over_after_stand(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.TEN), Card(Pip.JACK), Card(Pip.QUEEN), Card(Pip.KING)]
        player = Player(deck)
        # Act
        player.hit()
        player.hit()
        player.stand()
        # Assert
        assert player.round_over is True
        with self.assertRaises(RoundOverException):
            player.hit()

    def test_reset_round(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.TEN), Card(Pip.JACK)]
        player = Player(deck)
        # Act
        player.hit()
        player.stand()
        player.reset_round()
        # Assert
        assert player.round_over is False
        assert player.hand.score_hand() == 0
