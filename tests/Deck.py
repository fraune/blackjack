from app.Deck import Deck


def test_deck():
    deck = Deck()
    x = deck.as_string()
    print(x, flush=True)
