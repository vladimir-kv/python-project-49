from random import randrange


def even():
    question = randrange(100)
    rigth_answer = ''
    if question % 2 == 0:
        rigth_answer = 'yes'
    else:
        rigth_answer = 'no'
    return question, rigth_answer
