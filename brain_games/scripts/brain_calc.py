#!/usr/bin/env python3

from brain_games.consts import ROUNDS_TO_PLAY
from brain_games.games import calc


def main():

    calc.play(ROUNDS_TO_PLAY)


if __name__ == '__main__':
    main()
