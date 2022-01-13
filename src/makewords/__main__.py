import argparse
import sys

from makewords.makewords import possible_words


def main(args=None):
    args = sys.argv[1:] if args is None else args
    parser = argparse.ArgumentParser(description="Make words from letters.")
    parser.add_argument("letters", type=str, nargs="?", default="make")
    parser.add_argument("--words", dest="words", type=(str), nargs="?", default=None)
    parser.add_argument("--include", dest="include", type=str, nargs="?", default=None)
    parser.add_argument("--exclude", dest="exclude", type=str, nargs="?", default=None)
    parser.add_argument("--len", dest="length", type=int, nargs="?", default=None)
    parser.add_argument("--mask", dest="mask", type=str, nargs="?", default=None)
    args = parser.parse_args()
    letters = args.letters
    words = args.words.split(",") if args.words is not None else None
    include = args.include
    exclude = args.exclude
    length = args.length
    mask = args.mask
    possible_words(letters, words=words, length=length, mask=mask, include=include, exclude=exclude)


if __name__ == "__main__":  # pragma: no cov
    sys.exit(main())  # pragma: no cov
