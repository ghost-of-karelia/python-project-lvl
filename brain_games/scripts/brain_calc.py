#!/usr/bin/env python3

from random import randint, choice
from brain_games.cli import welcome_user, check_answer
from brain_games.consts import ROUNDS_TO_PLAY

def main():
    
    name = welcome_user()
    rounds_left = ROUNDS_TO_PLAY
    operators = ['+', '-', '*']
    
    print('What is the result of the expression?')

    while rounds_left > 0:

        number1 = randint(0, 100)
        number2 = randint(0, 100)
        operator = choice(operators)

        print(f'Question: {number1} {operator} {number2}')

        correct_answer = eval(str(number1) + operator + str(number2))
        answer = int(input('Your answer: '))

        rounds_left = check_answer(answer, correct_answer, name, rounds_left)

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
