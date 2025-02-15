from brain_games.logic_games.prime import prime
from brain_games.logic_games.game import game

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game(prime, task)


if __name__ == '__main__':
    main()
