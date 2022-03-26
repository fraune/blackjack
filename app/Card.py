from enum import Enum

from app.utility.logging import e


class Pip(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def as_points(self):
        match self:
            case Pip.ACE:
                return 11
            case Pip.TWO:
                return 2
            case Pip.THREE:
                return 3
            case Pip.FOUR:
                return 4
            case Pip.FIVE:
                return 5
            case Pip.SIX:
                return 6
            case Pip.SEVEN:
                return 7
            case Pip.EIGHT:
                return 8
            case Pip.NINE:
                return 9
            case Pip.TEN | Pip.JACK | Pip.QUEEN | Pip.KING:
                return 10
            case _:
                e(f'An unknown card type was found: {self}')

    def as_string(self):
        return f'[{self.name}]'


class Card:
    pip: Pip
    score: int
    ace_high: bool = True

    def __init__(self, pip: Pip):
        self.pip = pip
        self.score = self.pip.as_points()
        self.ace_high = True

    def update_score(self, hand_subtotal: int):
        """
        Update this card's score, and return the amount it was changed by
        :param hand_subtotal: The subtotal of the other cards; affects the score of aces only
        :return: Amount that this card's value has changed
        """
        updated_by = 0
        if self.pip == Pip.ACE and hand_subtotal > 21 and self.ace_high:
            self.score = 1
            self.ace_high = False
            updated_by = -10
        return updated_by
