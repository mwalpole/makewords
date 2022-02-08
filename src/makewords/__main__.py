import argparse
import sys

from makewords.makewords import possible_words


def main(args=None):
    args = sys.argv[1:] if args is None else args
    parser = argparse.ArgumentParser(description="Make words from letters.")
    parser.add_argument(
        "-w",
        "--words",
        dest="words",
        type=(str),
        nargs="?",
        default=None,
        help="list of words with comma",
    )
    parser.add_argument(
        "-i",
        "--include",
        dest="include",
        type=str,
        nargs="?",
        default=None,
        help="use these letters",
    )
    parser.add_argument(
        "-o",
        "--only",
        dest="only",
        type=bool,
        nargs="?",
        default=False,
        help="only use included letters",
    )
    parser.add_argument(
        "-c",
        "--match_count",
        dest="match_count",
        type=bool,
        nargs="?",
        default=False,
        help="use the same count of included letters",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        dest="exclude",
        type=str,
        nargs="?",
        default=None,
        help="do not use these letters",
    )
    parser.add_argument(
        "-l",
        "--length",
        dest="length",
        type=int,
        nargs="?",
        default=None,
        help="make words of this many letters",
    )
    parser.add_argument(
        "-m",
        "--mask",
        dest="mask",
        type=str,
        nargs="?",
        default=None,
        help="words should look like this, wildcard is '.'",
    )
    parser.add_argument("-v", "--verbose", action="count", default=0)
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
    print(words)


if __name__ == "__main__":
    sys.exit(main())
