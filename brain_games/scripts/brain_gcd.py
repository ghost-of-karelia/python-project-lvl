#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.consts import ROUNDS_TO_PLAY


def play_brain_dcg(rounds_left, name):

    if rounds_left == 0:
        return print(f'Congratulations, {name}!')

    number1 = int(randint(0, 100))
    number2 = int(randint(0, 100))
    correct_answer = 1
    print(f'Question: {number1} {number2}')
    answer = int(input('Your answer: '))

    for i in range(min(number1, number2), 0, -1):
        if number1 % i == 0 and number2 % i == 0:
            correct_answer = i
            break
        i -= 1

    if answer != correct_answer:
        print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        return print(f'Let\'s try again, {name}!')
    else:
        print('Correct!')
        rounds_left -= 1
        play_brain_dcg(rounds_left, name)


def main():

    print('Find the greatest common divisor of given numbers.')
    play_brain_dcg(ROUNDS_TO_PLAY, welcome_user())


if __name__ == 'main':
    main()
