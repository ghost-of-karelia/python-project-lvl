from random import randint


def play():

    print('Answer "yes" if the number is even, otherwise answer "no".')

    number = randint(0, 100)
    print('Question:', number)

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer
