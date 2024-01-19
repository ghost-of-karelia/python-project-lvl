from random import randint
from brain_games.cli import welcome_user


def main():
    
    name = welcome_user()
    print('What number is missing in the progression?')
    
    rounds_left = 3
    
    while rounds_left > 0:
        
        number1 = int(randint(0, 20))
        step = int(randint(1, 5))
        progression = []

        for i in range(number1, number1 + randint(5, 49), step):
            progression.append(i)
            
        correct_answer_position = randint(0, len(progression) - 1)
        correct_answer = progression[correct_answer_position]
        progression[correct_answer_position] = '..'

        print('Question:', *progression)
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
