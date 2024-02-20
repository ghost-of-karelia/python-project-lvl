from random import randint


START_GAME_QUESTION = (
    'Answer "yes" if the number is even, otherwise answer "no".'
)

NUM_MIN = 0
NUM_MAX = 100


def play():

    number = randint(NUM_MIN, NUM_MAX)
    print('Question:', number)

    return get_correct_answer(number)


def get_correct_answer(number):

    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer
