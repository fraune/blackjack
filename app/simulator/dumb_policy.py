from app.simulator.policy import Action

"""
Results of this policy table after 100,000 episodes (dealer cheats)
  player losses = 24948
  player wins   = 26786
  player ties   = 48266
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
