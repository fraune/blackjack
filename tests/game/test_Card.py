from unittest import TestCase

from app.game.Card import Pip


class TestPip(TestCase):

    def test_as_points_low(self):
        # Arrange
        expected = 5
        # Act
        actual = Pip.FIVE.as_points()
        # Assert
        assert actual == expected

    def test_as_points_high(self):
        # Arrange
        expected = 10
        # Act
        actual = Pip.JACK.as_points()
        # Assert
        assert actual == expected

    def test_as_points_ace(self):
        # Arrange
        expected = 11
        # Act
        actual = Pip.ACE.as_points()
        # Assert
        assert actual == expected
