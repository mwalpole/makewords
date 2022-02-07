# Simulate playing Wordle from CLI
# Choose a five letter word and build words corpus
# Apply rules, identify acceptable guess and provide feedback
# Score session
import argparse
import random
import sys

import makewords.makewords as make

DEFAULT_LETTER_COUNT = 5
MAX_ATTEMPTS = 7

# Add session to pick up where we left off or start from particular state

class Wordle:
    def __init__(self, length=None, word=None):
        self.length = length if length is not None else DEFAULT_LETTER_COUNT
        self.all_words = make.possible_words(length=self.length)
        if word is None:
            self.target = random.choice(list(self.all_words)).upper()
        else:
            self.target = word.upper()
        self.max_attempts = MAX_ATTEMPTS
        self.attempts = {}

    def play(self):
        attempt = 1
        while attempt < self.max_attempts:
            guess = self.guess(attempt)
            result = self.check(guess)
            self.attempts[attempt] = result
            print("{0}> {1} -> {2}".format(attempt, guess, result))
            if result == self.target:
                break
            else:
                attempt += 1

    def guess(self, attempt):
        guess = input("Guess {attempt}: ".format(attempt=attempt))
        guess = self.clean(guess.lower(), attempt)
        return guess

    def clean(self, guess, attempt):
        ok = False
        if guess in self.all_words:
            ok = True
        if not ok:
            print("{} is not in wordlist. Try again.".format(guess))
            guess = self.guess(attempt)
        return guess

    def check(self, guess):
        """Provide hints based on the latest guess.

        Rules
        -----
        #1 Print a capital letter for a letter in the correct place.
        #2 Print a lower case letter for each appearance of that letter in the word.
        """
        output = ["."] * self.length
        guess = guess.upper()
        # Rule #1
        answer = list(self.target)
        for i in reversed(range(self.length)):
            if guess[i] == answer[i]:
                output[i] = answer.pop(i)
        # Rule #2
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


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())  # pragma: no cover
