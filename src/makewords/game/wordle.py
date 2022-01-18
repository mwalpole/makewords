# Simulate playing Wordle from CLI
# Choose a five letter word and build words corpus
# Apply rules, identify acceptable guess and provide feedback
# Score session
import argparse
import random
import sys

import makewords.makewords as make
import makewords.util as util

N = 5


class Wordle:
    def __init__(self, length=None, word=None):
        self.length = length if length is not None else N
        self.all_words = make.possible_words(length=self.length)
        if word is None:
            self.target = random.choice(list(self.all_words)).upper()
        else:
            self.target = word.upper()
        self.target_count = util.count_letters(self.target)

    def play(self):
        turn = 1
        while turn < 7:
            guess = self.guess(turn)
            result = self.assess(guess)
            print("{0}> {1} -> {2}".format(turn, guess, result))
            turn += 1

    def guess(self, turn):
        guess = input("Guess {turn}: ".format(turn=turn))
        guess = self.clean(guess.lower(), turn)
        return guess

    def clean(self, guess, turn):
        ok = False
        if guess in self.all_words:
            ok = True
        if not ok:
            print("{} is not in wordlist. Try again.".format(guess))
            guess = self.guess(turn)
        return guess

    def assess(self, guess):
        """Provide hints based on assessment of latest guess.

        Rules
        -----
        #1 Print a capital letter for a letter in the correct place.
        #2 Print a lower case letter for each appearance of that letter in the word.
        """
        output = ["."] * self.length
        guess = guess.upper()
        # Rule #1 - Identify positions for which we have a full match
        answer = list(self.target)
        for i in reversed(range(self.length)):
            if guess[i] == answer[i]:
                output[i] = answer.pop(i)
        # Rule #2 - Identify positions that represent a letter match in the wrong position
        for i in range(self.length):
            if guess[i] in answer and not output[i].isalpha():
                output[i] = answer.pop(answer.index(guess[i])).lower()
        return "".join(output)


def main(args=None):
    args = sys.argv[1:] if args is None else args
    parser = argparse.ArgumentParser()
    parser.add_argument("--word", dest="word", type=str, nargs="?", default=None)
    args = parser.parse_args()
    word = args.word
    try:
        wordle = Wordle(word=word)
        wordle.play()
    except KeyboardInterrupt:
        print("\nUser exit.")
    finally:
        print("Done. Answer: {}".format(wordle.target))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cov
