#!/usr/bin/env python3

import prompt
from random import randint
from brain_games.cli import welcome_user
from math import sqrt


def play(rounds_left):

    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(rounds_left):

        number = randint(2, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes'

        for i in range(2, int(sqrt(number))):
            if number % i == 0:
                correct_answer = 'no'
                break

        if answer != correct_answer:
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'.'
            )
            print(f'Let\'s try again, {name}!')
            return None

        print('Correct!')

    print(f'Congratulations, {name}!')
