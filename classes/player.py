
class Player:
    def __init__(self, name, holding_cards):
        self.name = name
        self.holding_cards = holding_cards

    def show_next_card(self):
        return self.holding_cards[0]

