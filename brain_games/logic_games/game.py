import prompt


def game(game_name, task):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(task)
    count = 0
    while count != 3:
        question, rigth_answer = game_name()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if str(rigth_answer) == str(answer):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{rigth_answer}'.\n"
                  f"Let's try again, {name}!")
            break
        if count == 3:
            print(f'Congratulations, {name}!')