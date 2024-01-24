#!/usr/bin/env python3

from random import randint, choice
from brain_games.cli import welcome_user
from brain_games.consts import ROUNDS_TO_PLAY

def play_brain_calc(rounds_left, name):
    
    if rounds_left == 0:
        return print(f'Congratulations, {name}!')
    
    operators = ['+', '-', '*']
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    operator = choice(operators)

    print(f'Question: {number1} {operator} {number2}')
    answer = int(input('Your answer: '))

    correct_answer = eval(str(number1) + operator + str(number2))

    if answer != correct_answer:        
        print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        return print(f'Let\'s try again, {name}!')
    else:
        print('Correct!')
        rounds_left -= 1
        play_brain_calc(rounds_left, name)


def main():
    
    print('What is the result of the expression?')
    play_brain_calc(ROUNDS_TO_PLAY, welcome_user())


if __name__ == '__main__':
    main()
