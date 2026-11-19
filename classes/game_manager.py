from classes.game import Game
from classes.valdations import Validation


class GameManager:
    def __init__(self):
        self.new_game = Game()
        self.cards = self.new_game.shuffle_to_players(self.new_game.mix_cards())
        self.player1_cards = self.cards[0]
        self.player2_cards = self.cards[1]

    def print_menu(self):
        valid = Validation()
        print("""
            =======================
                 GAME MANAGER
            ========================

            1. play_turn
            2. Exit
                """)
        choose = input()
        while not valid.main_choose_checker(choose):
            choose = input("Only a number from the menu: ")
        choose = int(choose)
        return choose

    def print_bonus_menu(self):
        valid = Validation()
        print("""
            =======================
                 GAME MANAGER
            ========================

            1. New game
            2. Exit
                        """)
        choose = input()
        while not valid.main_choose_checker(choose):
            choose = input("Only a number from the menu: ")
        choose = int(choose)
        return choose

    def run(self):
        valid = Validation()
        name = input("Please enter your name: ")
        while not valid.is_str(name):
            name = input("Only a non empty name: ")
        choose = self.print_menu()
        while choose != 2:
            print(self.new_game.play_a_round(name, self.player1_cards, self.player2_cards))
            if self.new_game.safe_check_who_wins(self.player1_cards, self.player2_cards, name) == "Both have cards, game is on":
                continue
            else:
                return
            choose = self.print_menu()
        print("You chose to exit the game!")
        return self.new_game.who_wins_if_ext(self.player1_cards, self.player2_cards, name)

    #Bonus

    def bonus_run(self):
        choose = self.print_bonus_menu()
        choose = int(choose)
        while choose != 2:
            print(self.run())
            choose = self.print_bonus_menu()

        return "You chose to exit, goodbye for now"









