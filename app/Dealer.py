import copy

from app.Player import Player


class Dealer(Player):

    def hit(self):
        self.draw_cards()

    def draw_cards(self):
        """
        Dealer cheats and draws cards until the next card would cause bust
        :return:
        """
        while not self.round_over:
            hypothetical_hand = copy.deepcopy(self.hand)
            hypothetical_hand.add_card(self.shared_deck.peek_top_card())

            if hypothetical_hand.score_hand() > 21:
                self.round_over = True
            else:
                self.hand.add_card(self.shared_deck.take_top_card())
