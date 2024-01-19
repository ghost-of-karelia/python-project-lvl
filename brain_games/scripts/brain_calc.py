'''
#!/usr/bin/env python3
'''

from random import randint, choice
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print('What is the result of the expression?')

    rounds_left = 3

    operators = ['+', '-', '*']
    while rounds_left > 0:
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        operator = choice(operators)

        print(f'Question: {number1} {operator} {number2}')

        correct_answer = eval(str(number1) + operator + str(number2))
        answer = int(input('Your answer: '))

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
