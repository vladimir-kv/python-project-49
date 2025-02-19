from brain_games.logic_games.game import game
from brain_games.logic_games.prime import prime

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game(prime, TASK)


if __name__ == '__main__':
    main()
