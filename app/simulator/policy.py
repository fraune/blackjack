from enum import Enum

"""
The integers corresponding to each enum name represents the index that can be used to select that state/action from the
q-table or rewards table. Don't modify these numbers.
"""


class Action(Enum):
    HIT = 0
    STAND = 1


class State(Enum):
    SCORE_IS_1 = 0  # TODO: Remove? - Technically not possible if always dealt 2 cards to begin each round
    SCORE_IS_2 = 1
    SCORE_IS_3 = 2
    SCORE_IS_4 = 3
    SCORE_IS_5 = 4
    SCORE_IS_6 = 5
    SCORE_IS_7 = 6
    SCORE_IS_8 = 7
    SCORE_IS_9 = 8
    SCORE_IS_10 = 9
    SCORE_IS_11 = 10
    SCORE_IS_12 = 11
    SCORE_IS_13 = 12
    SCORE_IS_14 = 13
    SCORE_IS_15 = 14
    SCORE_IS_16 = 15
    SCORE_IS_17 = 16
    SCORE_IS_18 = 17
    SCORE_IS_19 = 18
    SCORE_IS_20 = 19
    SCORE_IS_21 = 20
    PLAYER_HAS_WON = 21
    PLAYER_HAS_LOST = 22


def get_current_state_from_score(score: int) -> State:
    if 1 <= score <= 21:
        return State(score - 1)
    else:
        raise ValueError(f'A State was not derived from the following score: {score}')
