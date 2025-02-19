from brain_games.logic_games.game import game
from brain_games.logic_games.progression import progression

TASK = 'What number is missing in the progression?'


def main():
    game(progression, TASK)


if __name__ == '__main__':
    main()
