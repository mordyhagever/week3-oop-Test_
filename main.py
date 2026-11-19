from os import name

from classes.game_manager import GameManager

def main():
    game = GameManager()
    print(game.run())


if __name__ == '__main__':
    main()


