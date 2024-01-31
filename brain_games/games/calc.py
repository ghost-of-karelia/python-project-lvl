from random import randint, choice
from brain_games.cli import request_answer, verify_answer


def play(rounds_left, name):

    print('What is the result of the expression?')

    for _ in range(rounds_left):

        operators = ['+', '-', '*']
        a = randint(0, 100)
        b = randint(0, 100)
        operator = choice(operators)

        print(f'Question: {a} {operator} {b}')
        answer = int(request_answer())

        if operator == '+':
            correct_answer = a + b
        if operator == '-':
            correct_answer = a - b
        if operator == '*':
            correct_answer = a * b

        if not verify_answer(answer, correct_answer, name):
            return None

    print(f'Congratulations, {name}!')
