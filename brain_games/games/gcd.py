from random import randint


def play():

    print('Find the greatest common divisor of given numbers.')

    a = int(randint(1, 100))
    b = int(randint(1, 100))

    correct_answer = 1
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            correct_answer = i
            break

    print(f'Question: {a} {b}')

    return correct_answer
