from app.game.Game import Game, EndGameState
from app.simulator.policy import State, Action


def evaluate_policy_table(q_table: dict):
    episodes = 1000
    game = Game()

    player_lost = 0
    player_won = 0
    player_tied = 0

    for i in range(episodes):
        game.new_round()
        while game.player.round_over is False:
            current_score = game.player.hand.score_hand()
            actions = q_table[State(current_score)]
            best_action = max(actions, key=lambda x: actions[x])

            if best_action == Action.HIT:
                game.player.hit()
            else:
                game.player.stand()

        match game.determine_winner():
            case EndGameState.DEALER_WINS:
                player_lost += 1
            case EndGameState.PLAYER_WINS:
                player_won += 1
            case EndGameState.TIE:
                player_tied += 1

    print(f'Final Results:')
    print(f'  player losses = {player_lost}')
    print(f'  player wins   = {player_won}')
    print(f'  player ties   = {player_tied}')
