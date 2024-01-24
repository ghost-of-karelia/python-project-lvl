#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.consts import ROUNDS_TO_PLAY


def main():
    
    name = welcome_user()
    rounds_left = ROUNDS_TO_PLAY

    print('Find the greatest common divisor of given numbers.')
    
    while rounds_left > 0:
        number1 = int(randint(0, 100))
        number2 = int(randint(0, 100))
        correct_answer = 1
        
        for i in range(min(number1, number2), 0, -1):
            if number1 % i == 0 and number2 % i == 0:
                correct_answer = i
                break
            i -= 1

        print(f'Question: {number1} {number2}')
        answer = int(input('Your answer: '))

        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            rounds_left = 3
        else:
            rounds_left -= 1
            print('Correct!')
    
    print(f'Congratulations, {name}!')


if __name__ == 'main':
    main()
