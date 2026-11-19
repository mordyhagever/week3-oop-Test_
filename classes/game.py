from classes.card import Card
import random

class Game:
    def create_cards_box(self):
        cards_box = []
        for i in range(13):
            new_card_H = Card(i + 2, "♥")
            new_card_H.to_string()
            # new_card_H = new_card_H.__dict__
            cards_box.append(new_card_H)
            new_card_D = Card(i + 2, "♦")
            new_card_D.to_string()
            # new_card_D = new_card_D.__dict__
            cards_box.append(new_card_D)
            new_card_S = Card(i + 2, "♠")
            new_card_S.to_string()
            # new_card_S = new_card_S.__dict__
            cards_box.append(new_card_S)
            new_card_C = Card(i + 2, "♣")
            new_card_C.to_string()
            # new_card_C = new_card_C.__dict__
            cards_box.append(new_card_C)
        return cards_box

    def mix_cards(self):
        cards = self.create_cards_box()
        for _ in range(1000):
            first_index = random.randint(0,51)
            second_index = random.randint(0,51)
            while first_index == second_index:
                second_index = random.randint(0,51)
            switcher = cards[first_index]
            cards[first_index] = cards[second_index]
            cards[second_index] = switcher
        return cards

    def shuffle_to_players(self, all_cards):
        player1_cards = []
        player2_cards = []
        for i in range(52):
            if i % 2 == 0:
                player1_cards.append(all_cards[i])
            else:
                player2_cards.append(all_cards[i])
        return player1_cards, player2_cards


    def play_a_round(self, player_name, player1_cards, player2_cards):
        if not player1_cards or not player2_cards:
            return "Error, one of players don't have cards!"
        print("======== NEW ROUND IS ON ========")
        player1_turn = player1_cards.pop(0)
        print(f"{player_name}: {player1_turn.to_dict()}")
        player2_turn = player2_cards.pop(0)
        print(f"Computer's: {player2_turn.to_dict()}")
        player1_turn = player1_turn.from_string()
        player2_turn = player2_turn.from_string()
        if player1_turn > player2_turn:
            print(f"{player_name} won this round!")
            player1_cards.append(player1_turn)
            player1_cards.append(player2_turn)
        elif player2_turn > player1_turn:
            print("Computer won this round!")
            player2_cards.append(player2_turn)
            player2_cards.append(player1_turn)
        else:
            print("Tie, no one wins this round")
            player1_cards.append(player1_turn)
            player2_cards.append(player2_turn)
        print(f"{player_name} cards: {len(player1_cards)} | Computer's cards: {len(player2_cards)}")
        return self.safe_check_who_wins(player1_cards, player2_cards, player_name)

    def safe_check_who_wins(self, player1_cards, player2_cards, name):
        if not player1_cards:
            return f"{name} has not cards, computer wins!"
        if not player2_cards:
            return f"Computer has not cards, {name} wins!"
        return "Both have cards, game is on"

    def who_wins_if_ext(self, player1_cards, player2_cards, name):
        if len(player1_cards) > len(player2_cards):
            return "You win, computer lost!"
        elif len(player2_cards) > len(player1_cards):
            return "Sorry you lost!"
        return "Both have same amount, it's a tie!"

#
#
# new_game = Game()
# mix_cards = new_game.shuffle_to_players(new_game.mix_cards())
# player1_cards = mix_cards[0]
# player2_cards = mix_cards[1]
# # for card in player1_cards:
# #     print(card.to_dict())
# print(new_game.play_a_round("Mordy", player1_cards, player2_cards))




