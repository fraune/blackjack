from unittest import TestCase

from app.Card import Card, Pip
from app.Dealer import Dealer
from app.Deck import Deck


class TestDealer(TestCase):

    def test_draw_cards_will_not_bust(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.TEN), Card(Pip.JACK), Card(Pip.QUEEN)]
        dealer = Dealer(deck)
        # Act
        dealer.hit()
        # Assert
        assert dealer.round_over is True
        assert dealer.hand.score_hand() == 20
        assert len(dealer.hand.cards) == 2

    def test_draw_cards_until_end_of_deck(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.THREE), Card(Pip.SEVEN), Card(Pip.FOUR)]
        dealer = Dealer(deck)
        # Act
        dealer.hit()
        # Assert
        assert dealer.round_over is True
        assert dealer.hand.score_hand() == 14
        assert len(dealer.hand.cards) == 3

    def test_draw_cards_stands_on_21_with_ace(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.THREE), Card(Pip.TWO), Card(Pip.ACE), Card(Pip.JACK)]
        dealer = Dealer(deck)
        # Act
        dealer.hit()
        # Assert
        assert dealer.round_over is True
        assert dealer.hand.score_hand() == 21
        assert len(dealer.hand.cards) == 2

    def test_draw_cards_converts_ace_for_21(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.THREE), Card(Pip.ACE), Card(Pip.QUEEN), Card(Pip.JACK)]
        dealer = Dealer(deck)
        # Act
        dealer.hit()
        # Assert
        assert dealer.round_over is True
        assert dealer.hand.score_hand() == 21
        assert len(dealer.hand.cards) == 3

    def test_draw_cards_converts_ace_for_20_stops(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.TWO), Card(Pip.TWO), Card(Pip.TWO), Card(Pip.ACE), Card(Pip.FIVE), Card(Pip.JACK)]
        dealer = Dealer(deck)
        # Act
        dealer.hit()
        # Assert
        assert dealer.round_over is True
        assert dealer.hand.score_hand() == 20
        assert len(dealer.hand.cards) == 5

    def test_draw_cards_converts_ace_for_20_stops(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.TWO), Card(Pip.TWO), Card(Pip.ACE), Card(Pip.NINE), Card(Pip.ACE)]
        dealer = Dealer(deck)
        # Act
        dealer.hit()
        # Assert
        assert dealer.round_over is True
        assert dealer.hand.score_hand() == 21
        assert len(dealer.hand.cards) == 3

    def test_draw_cards_converts_ace_for_20_stops(self):
        # Arrange
        deck = Deck()
        deck.cards = [Card(Pip.TEN), Card(Pip.TWO), Card(Pip.FOUR), Card(Pip.FIVE), Card(Pip.ACE)]
        dealer = Dealer(deck)
        # Act
        dealer.hit()
        # Assert
        assert dealer.round_over is True
        assert dealer.hand.score_hand() == 12
        assert len(dealer.hand.cards) == 4
