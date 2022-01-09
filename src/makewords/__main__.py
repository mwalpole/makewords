import argparse
import sys

from makewords.makewords import possible_words


def main(args=None):
    args = sys.argv[1:] if args is None else args
    parser = argparse.ArgumentParser(description="Make words from letters.")
    parser.add_argument("letters", type=str, nargs="?", default="make")
    parser.add_argument("words", type=(str), nargs="?", default=None)
    args = parser.parse_args()
    letters = args.letters
    words = args.words.split(",") if args.words is not None else None
    possible_words(letters, words)


if __name__ == "__main__":  # pragma: no cov
    sys.exit(main())  # pragma: no cov
