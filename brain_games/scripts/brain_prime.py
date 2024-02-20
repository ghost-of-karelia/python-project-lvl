#!/usr/bin/env python3

from brain_games.games import prime
from brain_games import engine


def main():

    name = engine.welcome_user()
    engine.play(name, prime)


if __name__ == '__main__':
    main()
