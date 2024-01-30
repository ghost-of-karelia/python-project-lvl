#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user, request_answer, verify_answer


def play(rounds_left):

    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    for _ in range(rounds_left):

        number1 = int(randint(0, 100))
        number2 = int(randint(0, 100))
        print(f'Question: {number1} {number2}')
        correct_answer = 1

        answer = int(request_answer())

        for i in range(min(number1, number2), 0, -1):
            if number1 % i == 0 and number2 % i == 0:
                correct_answer = i
                break

        if not verify_answer(answer, correct_answer, name):
            return None

    print(f'Congratulations, {name}!')
