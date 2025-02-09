from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    

if __name__ == '__main__':
    main()


#Запускается командой 'uv run python -m brain_games.scripts.brain_games' из консоли
#Или 'uv run brain-games'