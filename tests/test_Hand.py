from unittest import TestCase

from app.Card import Pip, Card
from app.Hand import Hand


class TestHand(TestCase):

    def test_count_hand_1(self):
        # Arrange
        expected = 2
        hand = Hand()
        hand.deal_card(Card(Pip.TWO))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_2(self):
        # Arrange
        expected = 4
        hand = Hand()
        hand.deal_card(Card(Pip.TWO))
        hand.deal_card(Card(Pip.TWO))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_3(self):
        # Arrange
        expected = 17
        hand = Hand()
        hand.deal_card(Card(Pip.SEVEN))
        hand.deal_card(Card(Pip.KING))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_4(self):
        # Arrange
        expected = 22
        hand = Hand()
        hand.deal_card(Card(Pip.SEVEN))
        hand.deal_card(Card(Pip.KING))
        hand.deal_card(Card(Pip.FIVE))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_5(self):
        # Arrange
        expected = 18
        hand = Hand()
        hand.deal_card(Card(Pip.SEVEN))
        hand.deal_card(Card(Pip.ACE))
        hand.deal_card(Card(Pip.KING))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_6(self):
        # Arrange
        expected = 18
        hand = Hand()
        hand.deal_card(Card(Pip.SEVEN))
        hand.deal_card(Card(Pip.ACE))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_7(self):
        # Arrange
        expected = 12
        hand = Hand()
        hand.deal_card(Card(Pip.ACE))
        hand.deal_card(Card(Pip.ACE))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_8(self):
        # Arrange
        expected = 21
        hand = Hand()
        hand.deal_card(Card(Pip.JACK))
        hand.deal_card(Card(Pip.ACE))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected

    def test_count_hand_9(self):
        # Arrange
        expected = 12
        hand = Hand()
        hand.deal_card(Card(Pip.QUEEN))
        hand.deal_card(Card(Pip.ACE))
        hand.deal_card(Card(Pip.ACE))
        # Act
        actual = hand.score_hand()
        # Assert
        assert actual == expected
