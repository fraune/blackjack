import random

import numpy
from numpy.typing import ArrayLike

from app.game.Game import Game, EndGameState
from app.simulator.policy import State, Action, get_current_state_from_score

"""
The epsilon determines the rate at which the algorithm chooses to explore rather than exploit the best known q-value.
"""
EPSILON = 0.1
LAMBDA = 0.1
ALPHA = 0.1


def determine_reward(state: State) -> int:
    if 0 <= state.value <= 20:
        return state.value + 1
    if state == State.PLAYER_HAS_LOST:
        return -1000
    if state == State.PLAYER_HAS_WON:
        return 1000
    raise ValueError(f'A reward was not determined from the following State: {state}')


def select_action(current_state: State, q_table: ArrayLike, allow_exploration: bool = True) -> Action:
    # Exploit - choose action with the highest q-value for the current state
    actions = q_table[current_state.value]
    best_action_index = numpy.argmax(actions)  # TODO: biased towards first action if the q_values are equal
    action = Action(best_action_index)

    if allow_exploration:
        # Explore - randomly choose from all possible actions in the current state with uniform probability
        r = random.randint(0, 1)
        if r < EPSILON:
            random_action_index = random.randint(0, len(Action) - 1)
            action = Action(random_action_index)

    return action


def optimize_policy() -> ArrayLike:
    """
    Initialize two-dimensional quality table:
      1. Current State
      2. Action

      The value in the cells is equal to the q-value.
    """
    q_table = numpy.zeros((len(State), len(Action)))
    episodes = 10000
    game = Game()

    for i in range(episodes):
        game.new_round()
        while game.player.round_over is False:
            current_state = get_current_state_from_score(game.player.hand.score_hand())
            action = select_action(current_state, q_table)
            match action:
                case Action.HIT:
                    game.player.hit()
                case Action.STAND:
                    game.player.stand()
                case _:
                    raise ValueError(f'Unknown Action: {action}')

            if game.player.round_over:
                match game.determine_winner():
                    case EndGameState.DEALER_WINS:
                        next_state = State.PLAYER_HAS_LOST
                    case EndGameState.PLAYER_WINS:
                        next_state = State.PLAYER_HAS_WON
                    case _:
                        next_state = get_current_state_from_score(game.player.hand.score_hand())
            else:
                next_state = get_current_state_from_score(game.player.hand.score_hand())
            reward = determine_reward(next_state)

            # Why do I need this? - Asking prof
            next_action = select_action(current_state, q_table, False)
            next_q = q_table[next_state.value, next_action.value]

            previous_q = q_table[current_state.value][action.value]
            updated_q = (1 - ALPHA) * previous_q + ALPHA * (reward + LAMBDA * next_q)
            q_table[current_state.value][action.value] = updated_q

    return q_table


def construct_policy(q_table: ArrayLike) -> list[Action]:
    policy_table = [None] * len(State)
    for state in State:
        action = select_action(state, q_table, False)
        policy_table[state.value] = action
    return policy_table
