#! python3
import argparse

from src.makewords.makewords import possibleWords


def main(letters, words):
    possibleWords(letters, words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make words from letters.')
    parser.add_argument('letters', type=str, nargs='?', default='make')
    parser.add_argument('words', type=(str), nargs='?', default=None)
    args = parser.parse_args()
    letters = args.letters
    words = args.words.split(',') if args.words is not None else None
    main(letters, words)