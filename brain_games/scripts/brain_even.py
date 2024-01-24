#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.consts import ROUNDS_TO_PLAY


def main():
    
    name = welcome_user()
    rounds_left = ROUNDS_TO_PLAY

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while rounds_left > 0:
        number = randint(0, 100)
        print('Question:', number)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        answer = input('Your answer: ')

        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            rounds_left = 3
        else:
            rounds_left -= 1
            print('Correct!')

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
