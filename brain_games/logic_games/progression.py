from random import randrange


def progression():
    start = randrange(100)
    step = randrange(10)
    question = []
    highest_index = randrange(5, 14)
    hidden_index = randrange(highest_index)
    for i in range(highest_index + 1):
        question.append(start + step * i)
        if i == hidden_index:
            rigth_answer = str(question[i])
            question[i] = '..'
    question = ' '.join(map(str, question))
    return question, rigth_answer