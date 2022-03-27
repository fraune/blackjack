from unittest.mock import Mock

from app.Card import Pip, Card
from app.Deck import Deck
from app.Game import Game, EndGameState


def test_determine_winner_both_bust(mocker):
    # Arrange
    deck = Deck()
    deck.cards = [Card(Pip.TEN), Card(Pip.JACK), Card(Pip.QUEEN), Card(Pip.JACK), Card(Pip.TWO), Card(Pip.KING)]
    mocker.patch('app.Game.Deck', Mock(return_value=deck))
    mocker.patch('app.Deck.Deck.reset', Mock())
    mocker.patch('app.Deck.Deck.shuffle', Mock())

    # Act
    game = Game()
    game.new_round()
    game.dealer.hit()
    game.player.deal_first_two_cards()
    game.player.hit()

    # Assert
    actual = game.determine_winner()
    expected = EndGameState.TIE
    assert actual == expected


def test_determine_winner_dealer_bust(mocker):
    # Arrange
    deck = Deck()
    deck.cards = [Card(Pip.TEN), Card(Pip.JACK), Card(Pip.QUEEN), Card(Pip.JACK), Card(Pip.TWO), Card(Pip.KING)]
    mocker.patch('app.Game.Deck', Mock(return_value=deck))
    mocker.patch('app.Deck.Deck.reset', Mock())
    mocker.patch('app.Deck.Deck.shuffle', Mock())

    # Act
    game = Game()
    game.new_round()
    game.dealer.hit()
    game.player.deal_first_two_cards()

    # Assert
    actual = game.determine_winner()
    expected = EndGameState.PLAYER_WINS
    assert actual == expected

def test_determine_winner_player_bust(mocker):
    # Arrange
    deck = Deck()
    deck.cards = [Card(Pip.TEN), Card(Pip.JACK), Card(Pip.QUEEN), Card(Pip.JACK), Card(Pip.TWO), Card(Pip.KING)]
    mocker.patch('app.Game.Deck', Mock(return_value=deck))
    mocker.patch('app.Deck.Deck.reset', Mock())
    mocker.patch('app.Deck.Deck.shuffle', Mock())

    # Act
    game = Game()
    game.new_round()
    game.dealer.hit()
    game.player.deal_first_two_cards()

    # Assert
    actual = game.determine_winner()
    expected = EndGameState.PLAYER_WINS
    assert actual == expected
