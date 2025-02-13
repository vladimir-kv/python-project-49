from brain_games.logic_games.even import even
from brain_games.logic_games.game import game

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    game(even, task)


if __name__ == '__main__':
    main()
