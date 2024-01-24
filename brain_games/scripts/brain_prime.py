#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user
from brain_games.consts import ROUNDS_TO_PLAY

def play_brain_prime(rounds_left, name):
    
    if rounds_left == 0:
        return print(f'Congratulations, {name}!')

    number = randint(0, 100)
    print('Question:', number)
    answer = input('Your answer: ')

    for i in range(2, number):
        if number % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    if answer != correct_answer:        
        print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        return print(f'Let\'s try again, {name}!')
    else:
        print('Correct!')
        rounds_left -= 1
        play_brain_prime(rounds_left, name)

    print(f'Congratulations, {name}!')

def main():
    
    print('Answer "yes" if the number is prime, otherwise answer "no".')
    play_brain_prime(ROUNDS_TO_PLAY, welcome_user())


if __name__ == '__main__':
    main()
