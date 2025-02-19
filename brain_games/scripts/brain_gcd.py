from brain_games.logic_games.game import game
from brain_games.logic_games.gcd import gcd

TASK = 'Find the greatest common divisor of given numbers.'


def main():
    game(gcd, TASK)


if __name__ == '__main__':
    main()
