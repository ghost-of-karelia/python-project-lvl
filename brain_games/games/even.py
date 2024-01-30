#!/usr/bin/env python3

import prompt
from random import randint
from brain_games.cli import welcome_user


def play(rounds_left):

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(rounds_left):

        number = randint(0, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer != correct_answer:
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'.'
            )
            print(f'Let\'s try again, {name}!')
            return None

        print('Correct!')

    print(f'Congratulations, {name}!')
