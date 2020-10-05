from phrasehunter.game import Game

if __name__ == '__main__':
    rerun = 'Y'
    while rerun.upper() == 'Y':
        first_game = Game()
        first_game.start()
        rerun = input('Would you like to play again? [Y/N]\n')