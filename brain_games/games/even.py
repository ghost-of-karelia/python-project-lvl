#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user, request_answer, verify_answer


def play(rounds_left):

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(rounds_left):

        x = randint(0, 100)
        print('Question:', x)

        answer = request_answer()

        if x % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if not verify_answer(answer, correct_answer, name):
            return None

    print(f'Congratulations, {name}!')
