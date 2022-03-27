from app.simulator.policy import State, Action

"""
Results of this q-table after 1000 episodes (dealer cheats)
  player losses = 255
  player wins   = 256
  player ties   = 489
"""

human_created_q_table = {
    State.SCORE_IS_1: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_2: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_3: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_4: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_5: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_6: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_7: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_8: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_9: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_10: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_11: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_12: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_13: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_14: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_15: {
        Action.HIT: 100,
        Action.STAND: 0
    },
    State.SCORE_IS_16: {
        Action.HIT: 0,
        Action.STAND: 100
    },
    State.SCORE_IS_17: {
        Action.HIT: 0,
        Action.STAND: 100
    },
    State.SCORE_IS_18: {
        Action.HIT: 0,
        Action.STAND: 100
    },
    State.SCORE_IS_19: {
        Action.HIT: 0,
        Action.STAND: 100
    },
    State.SCORE_IS_20: {
        Action.HIT: 0,
        Action.STAND: 100
    },
    State.SCORE_IS_21: {
        Action.HIT: 0,
        Action.STAND: 100
    },
    State.PLAYER_HAS_WON: {
        Action.HIT: 0,
        Action.STAND: 100
    },
    State.PLAYER_HAS_LOST: {
        Action.HIT: 0,
        Action.STAND: 100
    }
}
