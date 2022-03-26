from enum import Enum

from app.utility.logging import e


class Card(Enum):
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

    def as_points(self, subtotal: int = 0):
        match self:
            case Card.ACE:
                if subtotal > 10:
                    return 1
                else:
                    return 11
            case Card.TWO:
                return 2
            case Card.THREE:
                return 3
            case Card.FOUR:
                return 4
            case Card.FIVE:
                return 5
            case Card.SIX:
                return 6
            case Card.SEVEN:
                return 7
            case Card.EIGHT:
                return 8
            case Card.NINE:
                return 9
            case Card.TEN | Card.JACK | Card.QUEEN | Card.KING:
                return 10
            case _:
                e(f'An unknown card type was found: {self}')

    def as_string(self):
        return f'[{self.name}]'
