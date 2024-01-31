#!/usr/bin/env python3

from brain_games.consts import ROUNDS_TO_PLAY
from brain_games.games import calc
from brain_games.cli import welcome_user


def main():

    name = welcome_user()
    calc.play(ROUNDS_TO_PLAY, name)


if __name__ == '__main__':
    main()
