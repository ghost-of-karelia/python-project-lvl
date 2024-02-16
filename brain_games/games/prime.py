from random import randint
from math import sqrt


def play():

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    number = randint(2, 100)

    correct_answer = 'yes'
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            correct_answer = 'no'
            break

    print('Question:', number)

    return correct_answer
