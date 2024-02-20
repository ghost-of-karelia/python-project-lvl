from random import randint


START_GAME_QUESTION = (
    'What number is missing in the progression?'
)


NUM_MIN = 0
NUM_MAX = 12

STEP_MIN = 3
STEP_MAX = 8

PROGRESSION_LENGTH_MIN = 7
PROGRESSION_LENGTH_MAX = 12


def play():

    number = int(randint(NUM_MIN, NUM_MAX))
    step = int(randint(STEP_MIN, STEP_MAX))

    progression = []
    for _ in range(randint(PROGRESSION_LENGTH_MIN, PROGRESSION_LENGTH_MAX)):
        progression.append(number)
        number += step

    return get_correct_answer(progression)


def get_correct_answer(progression):

    correct_answer_position = randint(0, len(progression) - 1)
    correct_answer = progression[correct_answer_position]
    progression[correct_answer_position] = '..'

    print('Question:', *progression)   # Should it be located in play()?

    return correct_answer
