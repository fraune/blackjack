from unittest import TestCase

from app.Card import Pip


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

    def test_as_points_ace_low(self):
        # Arrange
        expected = 1
        # Act
        actual = Pip.ACE.as_points(11)
        # Assert
        assert actual == expected

    def test_as_points_ace_high(self):
        # Arrange
        expected = 11
        # Act
        actual = Pip.ACE.as_points(10)
        # Assert
        assert actual == expected
