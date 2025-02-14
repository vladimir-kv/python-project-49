from random import randrange


def gcd():
    a = randrange(100)
    b = randrange(100)
    question = (f"{a} {b}")
    rigth_answer = ''
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
        if a == b:
            rigth_answer = a
    return question, rigth_answer
