from random import random

import numpy
from numpy.typing import ArrayLike

from app.simulator.policy import State, Action

"""
The epsilon determines the rate at which the algorithm chooses to explore rather than exploit the best known q-value.
"""
epsilon = 0.5

"""
Initialize three-dimensional rewards table:
  1. Current State
  2. Action
  3. Next State
  
  The value in the cells is equal to the Reward.
"""
rewards_table = numpy.zeros((len(State), len(Action), len(State)))

"""
Initialize two-dimensional quality table:
  1. Current State
  2. Action

  The value in the cells is equal to the q-value.
"""
q_table = numpy.zeros((len(State), len(Action), len(State)))


def determine_reward(state: State) -> int:
    if 0 <= state.value <= 20:
        return state.value + 1
    if state == State.PLAYER_HAS_LOST:
        return -1000
    if state.value == State.PLAYER_HAS_WON:
        return 1000
    raise ValueError(f'A reward was not determined from the following State: {state}')


def select_action(current_state: State, q_values: ArrayLike) -> Action:
    # Exploit - choose action with the highest q-value for the current state
    actions = q_values[current_state.value]
    best_action_index = numpy.argmax(actions)  # TODO: biased towards first action if the q_values are equal
    action = Action(best_action_index)

    # Explore - randomly choose from all possible actions in the current state with uniform probability
    r = random.randint(0, 1)
    if r < epsilon:
        random_action_index = random.randint(0, len(Action) - 1)
        action = Action(random_action_index)

    return action
