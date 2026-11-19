from os import name
from classes.game_manager import bonus_run

from classes.game_manager import GameManager

def main():
    game = GameManager()
    print(game.run())
    print(bonus_run())


if __name__ == '__main__':
    main()


