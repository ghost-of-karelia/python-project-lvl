from random import choice, randint


START_GAME_QUESTION = (
    'What is the result of the expression?'
)

NUM_MIN = 0
NUM_MAX = 100


def play():

    a = randint(NUM_MIN, NUM_MAX)
    b = randint(NUM_MIN, NUM_MAX)
    operator = choice(['+', '-', '*'])

    print(f'Question: {a} {operator} {b}')

    return get_correct_answer(operator, a, b)


def get_correct_answer(operator, a, b):

    if operator == '+':
        correct_answer = a + b
    if operator == '-':
        correct_answer = a - b
    if operator == '*':
        correct_answer = a * b

    return correct_answer
