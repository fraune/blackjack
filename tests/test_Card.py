from unittest import TestCase

from app.Card import Card


class TestCard(TestCase):

    def test_as_points_low(self):
        # Arrange
        expected = 5
        # Act
        actual = Card.FIVE.as_points()
        # Assert
        assert actual == expected

    def test_as_points_high(self):
        # Arrange
        expected = 10
        # Act
        actual = Card.JACK.as_points()
        # Assert
        assert actual == expected

    def test_as_points_ace_low(self):
        # Arrange
        expected = 1
        # Act
        actual = Card.ACE.as_points(11)
        # Assert
        assert actual == expected

    def test_as_points_ace_high(self):
        # Arrange
        expected = 11
        # Act
        actual = Card.ACE.as_points(10)
        # Assert
        assert actual == expected
