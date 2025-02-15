from random import randrange


def prime():
    question = randrange(100)
    denominator = 0
    rigth_answer = ''
    for i in range(1, question + 1):
        if question % i == 0:
            denominator += 1
    if denominator == 2:
        rigth_answer = 'yes'
    else:
        rigth_answer = 'no'
    return question, rigth_answer