from brain_games.logic_games.game import game
from brain_games.logic_games.gcd import gcd

task = 'Find the greatest common divisor of given numbers.'


def main():
    game(gcd, task)


if __name__ == '__main__':
    main()
