#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.consts import ROUNDS_TO_PLAY


def play_brain_progression(rounds_left, name):

    if rounds_left == 0:
        return print(f'Congratulations, {name}!')

    number1 = int(randint(0, 12))
    step = int(randint(3, 7))
    progression = []

    for i in range(number1, number1 + randint(25, 72), step):
        progression.append(i)

    correct_answer_position = randint(0, len(progression) - 1)
    correct_answer = progression[correct_answer_position]
    progression[correct_answer_position] = '..'

    print('Question:', *progression)
    answer = int(input('Your answer: '))

    if answer != correct_answer:
        print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        return print(f'Let\'s try again, {name}!')
    else:
        print('Correct!')
        rounds_left -= 1
        play_brain_progression(rounds_left, name)


def main():

    print('What number is missing in the progression?')
    play_brain_progression(ROUNDS_TO_PLAY, welcome_user())


if __name__ == 'main':
    main()
  