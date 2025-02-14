from brain_games.logic_games.calc import calc
from brain_games.logic_games.game import game

task = 'What is the result of the expression?'


def main():
    game(calc, task)


if __name__ == '__main__':
    main()
