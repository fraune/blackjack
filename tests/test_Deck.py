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

    def test_unshuffled_decks_equivalent_order(self):
        # Arrange
        deck_unshuffled_1 = Deck()
        deck_unshuffled_2 = Deck()
        # Assert
        assert deck_unshuffled_2.as_string() == deck_unshuffled_1.as_string()

    def test_unshuffled_decks_equivalent_order(self):
        """
        A valid order for a shuffled deck can actually be the unshuffled order. We probably won't hit this edge case.
        """
        # Arrange
        deck_unshuffled = Deck()
        deck_shuffled = Deck()
        # Act
        deck_shuffled.shuffle()
        # Assert
        assert deck_shuffled.as_string() != deck_unshuffled.as_string()
