#!/usr/bin/env python3

import prompt
from random import randint, choice
from brain_games.cli import welcome_user


def play(rounds_left):

    name = welcome_user()
    print('What is the result of the expression?')

    for _ in range(rounds_left):

        operators = ['+', '-', '*']
        a = randint(0, 100)
        b = randint(0, 100)
        operator = choice(operators)

        print(f'Question: {a} {operator} {b}')
        answer = int(prompt.string('Your answer: '))

        if operator == '+':
            correct_answer = a + b
        if operator == '-':
            correct_answer = a - b
        if operator == '*':
            correct_answer = a * b

        if answer != correct_answer:
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'.'
            )
            print(f'Let\'s try again, {name}!')
            return None

        print('Correct!')

    print(f'Congratulations, {name}!')
