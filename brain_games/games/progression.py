from random import randint


def play():

    print('What number is missing in the progression?')

    number_0 = int(randint(0, 12))
    step = int(randint(3, 8))

    progression = []
    for i in range(randint(7, 12)):
        progression.append(number_0)
        number_0 += step

    correct_answer_position = randint(0, len(progression) - 1)
    correct_answer = progression[correct_answer_position]
    progression[correct_answer_position] = '..'

    print('Question:', *progression)

    return correct_answer
