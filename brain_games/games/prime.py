from random import randint
from math import sqrt


START_GAME_QUESTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


NUM_MIN = 2
NUM_MAX = 100


def play():

    number = randint(NUM_MIN, NUM_MAX)
    print('Question:', number)

    return get_correct_answer(number)


def get_correct_answer(number):

    correct_answer = 'yes'
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            correct_answer = 'no'
            break
    return correct_answer
