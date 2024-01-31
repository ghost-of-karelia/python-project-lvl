from random import randint
from brain_games.cli import request_answer, verify_answer


def play(rounds_left, name):

    print('Find the greatest common divisor of given numbers.')

    for _ in range(rounds_left):

        a = int(randint(0, 100))
        number2 = int(randint(0, 100))
        print(f'Question: {a} {number2}')
        correct_answer = 1

        answer = int(request_answer())

        for i in range(min(a, number2), 0, -1):
            if a % i == 0 and number2 % i == 0:
                correct_answer = i
                break

        if not verify_answer(answer, correct_answer, name):
            return None

    print(f'Congratulations, {name}!')
