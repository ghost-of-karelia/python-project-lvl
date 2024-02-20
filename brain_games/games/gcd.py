from random import randint
from math import gcd


START_GAME_QUESTION = (
    'Find the greatest common divisor of given numbers.'
)

NUM_MIN = 1
NUM_MAX = 100


def play():

    a = int(randint(NUM_MIN, NUM_MAX))
    b = int(randint(NUM_MIN, NUM_MAX))

    print(f'Question: {a} {b}')

    return get_correct_answer(a, b)


def get_correct_answer(a, b):

    correct_answer = gcd(a, b)
    return correct_answer
