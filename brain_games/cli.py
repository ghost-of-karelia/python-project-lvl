import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def check_answer(answer, correct_answer, name, rounds_left):
    if answer != correct_answer:
        print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {name}!')
        rounds_left = 3
    else:
        rounds_left -= 1
        print('Correct!')
    
    return rounds_left
