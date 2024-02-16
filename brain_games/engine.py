import prompt
from brain_games.consts import ROUNDS_TO_PLAY


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play(name, game_function):

    for _ in range(ROUNDS_TO_PLAY):

        correct_answer = game_function()
        answer = prompt.string('Your answer: ')

        if str(answer) == str(correct_answer):
            print('Correct!')
        else:
            return print(
                f'\'{answer}\' is wrong answer ;(. '
                f'Correct answer was \'{correct_answer}\'. '
                f'Let\'s try again, {name}!'
            )

    print(f'Congratulations, {name}!')
