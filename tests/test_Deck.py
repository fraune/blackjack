from unittest import TestCase

from app.Deck import Deck


class TestDeck(TestCase):

    def test_init_deck_size(self):
        # Arrange
        expected = 52
        deck1 = Deck()
        # Act
        actual = len(deck1.cards)
        # Assert
        assert actual == expected

    def test_init_deck_order(self):
        # Arrange
        expected = '([ACE][TWO][THREE][FOUR][FIVE][SIX][SEVEN][EIGHT][NINE][TEN][JACK][QUEEN][KING])'
        deck = Deck(1)
        # Act
        actual = deck.as_string()
        # Assert
        assert actual == expected
