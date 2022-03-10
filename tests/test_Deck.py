from unittest import TestCase

from app.Deck import Deck


class TestDeck(TestCase):

    def test_init_deck_size(self):
        deck1 = Deck()
        assert len(deck1.cards) == 52

    def test_init_deck_order(self):
        deck = Deck(1)
        printout = deck.as_string()
        assert printout == '([ACE][TWO][THREE][FOUR][FIVE][SIX][SEVEN][EIGHT][NINE][TEN][JACK][QUEEN][KING])'
