#!/usr/bin/env python3

import prompt
from random import randint
from brain_games.cli import welcome_user


def play(rounds_left):

    name = welcome_user()
    print('What number is missing in the progression?')

    for _ in range(rounds_left):

        number1 = int(randint(0, 12))
        step = int(randint(3, 8))

        progression = []
        for i in range(randint(7, 12)):
            progression.append(number1)
            number1 += step

        correct_answer_position = randint(0, len(progression) - 1)
        correct_answer = progression[correct_answer_position]
        progression[correct_answer_position] = '..'

        print('Question:', *progression)
        answer = int(prompt.string('Your answer: '))

        if answer != correct_answer:
            print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'.'
            )
            print(f'Let\'s try again, {name}!')
            return None

        print('Correct!')

    print(f'Congratulations, {name}!')
