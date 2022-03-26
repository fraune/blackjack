from unittest import TestCase

from app.Card import Card
from app.Hand import Hand


class TestHand(TestCase):

    def test_count_hand_1(self):
        # Arrange
        expected = 2
        hand = Hand()
        hand.deal_card(Card.TWO)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_2(self):
        # Arrange
        expected = 4
        hand = Hand()
        hand.deal_card(Card.TWO)
        hand.deal_card(Card.TWO)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_3(self):
        # Arrange
        expected = 17
        hand = Hand()
        hand.deal_card(Card.SEVEN)
        hand.deal_card(Card.KING)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_4(self):
        # Arrange
        expected = 22
        hand = Hand()
        hand.deal_card(Card.SEVEN)
        hand.deal_card(Card.KING)
        hand.deal_card(Card.FIVE)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_5(self):
        # Arrange
        expected = 18
        hand = Hand()
        hand.deal_card(Card.SEVEN)
        hand.deal_card(Card.ACE)
        hand.deal_card(Card.KING)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_6(self):
        # Arrange
        expected = 18
        hand = Hand()
        hand.deal_card(Card.SEVEN)
        hand.deal_card(Card.ACE)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_7(self):
        # Arrange
        expected = 12
        hand = Hand()
        hand.deal_card(Card.ACE)
        hand.deal_card(Card.ACE)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_8(self):
        # Arrange
        expected = 21
        hand = Hand()
        hand.deal_card(Card.JACK)
        hand.deal_card(Card.ACE)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected

    def test_count_hand_9(self):
        # Arrange
        expected = 12
        hand = Hand()
        hand.deal_card(Card.QUEEN)
        hand.deal_card(Card.ACE)
        hand.deal_card(Card.ACE)
        # Act
        actual = hand.count_hand()
        # Assert
        assert actual == expected
