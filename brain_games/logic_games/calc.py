from random import choice, randrange


def calc():
    number_1 = randrange(100)
    number_2 = randrange(100)
    arithmetic_signs = choice(['+', '-', '*'])
    question = (f"{number_1} {arithmetic_signs} {number_2}")
    rigth_answer = eval(f"{number_1} {arithmetic_signs} {number_2}")
    return question, rigth_answer
