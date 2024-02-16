from random import choice, randint


def play():

    print('What is the result of the expression?')

    a = randint(0, 50)
    b = randint(0, 50)
    operator = choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = a + b
    if operator == '-':
        correct_answer = a - b
    if operator == '*':
        correct_answer = a * b

    print(f'Question: {a} {operator} {b}')

    return correct_answer
