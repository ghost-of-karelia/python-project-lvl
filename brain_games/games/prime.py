from random import randint
from brain_games.cli import request_answer, verify_answer
from math import sqrt


def play(rounds_left, name):

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(rounds_left):

        number = randint(2, 100)
        print('Question:', number)

        answer = request_answer()
        correct_answer = 'yes'

        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                correct_answer = 'no'
                break

        if not verify_answer(answer, correct_answer, name):
            return None

    print(f'Congratulations, {name}!')
