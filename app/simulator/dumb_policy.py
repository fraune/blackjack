from app.simulator.policy import Action

"""
Results of this policy table after 1000 episodes (dealer cheats)
  player losses = 244
  player wins   = 288
  player ties   = 468
"""

human_created_policy_table = [
    Action.HIT,  # Score is 1
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,
    Action.HIT,  # Score is 15
    Action.STAND,  # Score is 16
    Action.STAND,
    Action.STAND,
    Action.STAND,
    Action.STAND,
    Action.STAND,  # Score is 21
    Action.STAND,  # Player win
    Action.STAND,  # Player lost
]
