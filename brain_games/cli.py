import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def request_answer():
    answer = prompt.string('Your answer: ')
    return answer


def verify_answer(answer, correct_answer, name):
    if str(answer) != str(correct_answer):
        print(
            f'\'{answer}\' is wrong answer ;(. '
            f'Correct answer was \'{correct_answer}\'.'
        )
        print(f'Let\'s try again, {name}!')
        return False
    
    print('Correct!')
    return True
