import copy

from app.Player import Player
from app.utility.logging import w


class Dealer(Player):

    def hit(self):
        self.draw_cards()

    def draw_cards(self):
        """
        Dealer cheats and draws cards until the next card would cause bust.
        Dealer is flawed in that it will hit on 20 with an ace scored as 11.
        :return:
        """
        while not self.round_over:
            hypothetical_hand = copy.deepcopy(self.hand)
            try:
                hypothetical_hand.add_card(self.shared_deck.peek_top_card())
                hypothetical_score = hypothetical_hand.score_hand()
                if hypothetical_score > 21:
                    self.round_over = True
                elif hypothetical_score == 21:
                    self.hand.add_card(self.shared_deck.take_top_card())
                    self.round_over = True
                else:
                    self.hand.add_card(self.shared_deck.take_top_card())
            except IndexError:
                w("Ran out of cards")
                self.round_over = True
