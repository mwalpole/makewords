import argparse
import sys

from makewords.makewords import possible_words


def main(args=None):
    args = sys.argv[1:] if args is None else args
    parser = argparse.ArgumentParser(description="Make words from letters.")
    parser.add_argument("--words", dest="words", type=(str), nargs="?", default=None)
    parser.add_argument("--include", dest="include", type=str, nargs="?", default=None)
    parser.add_argument("--only", dest="only", type=bool, nargs="?", default=False)
    parser.add_argument(
        "--match_count", dest="match_count", type=bool, nargs="?", default=False
    )
    parser.add_argument("--exclude", dest="exclude", type=str, nargs="?", default=None)
    parser.add_argument("--length", dest="length", type=int, nargs="?", default=None)
    parser.add_argument("--mask", dest="mask", type=str, nargs="?", default=None)
    parser.add_argument("--print", dest="print", type=bool, nargs="?", default=False)
    args = parser.parse_args()
    words = args.words.split(",") if args.words is not None else None
    include = args.include
    only = args.only
    match_count = args.match_count
    exclude = args.exclude
    length = args.length
    mask = args.mask
    words = possible_words(
        words=words,
        include=include,
        only=only,
        match_count=match_count,
        exclude=exclude,
        length=length,
        mask=mask,
    )
    if args.print:
        print(words)


if __name__ == "__main__":  # pragma: no cov
    sys.exit(main())  # pragma: no cov
