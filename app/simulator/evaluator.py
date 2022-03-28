from app.game.Game import Game, EndGameState
from app.simulator.policy import Action, get_current_state_from_score


def evaluate_policy_table(policy_table: list[Action]):
    episodes = 100000
    game = Game()

    player_lost = 0
    player_won = 0
    player_tied = 0

    for i in range(episodes):
        game.new_round()
        while game.player.round_over is False:
            current_score = game.player.hand.score_hand()
            current_state = get_current_state_from_score(current_score)
            action = policy_table[current_state.value]

            match action:
                case Action.HIT:
                    game.player.hit()
                case Action.STAND:
                    game.player.stand()
                case _:
                    raise ValueError(f'Unknown Action: {action}')

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
