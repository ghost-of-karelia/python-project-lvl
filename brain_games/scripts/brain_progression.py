#!/usr/bin/env python3

from brain_games.consts import ROUNDS_TO_PLAY
from brain_games.games import progression


def main():

    progression.play(ROUNDS_TO_PLAY)


if __name__ == '__main__':
    main()
