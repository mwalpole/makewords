# Simulate playing Wordle from CLI
# Choose a five letter word and build words corpus
# Apply rules, identify acceptable guess and provide feedback
# Score session
import argparse
import random
import string
import sys

import makewords.makewords as make

DEFAULT_LETTER_COUNT = 5
MAX_ATTEMPTS = 6
# Result states
FAIL = "Fail"
QUIT = "Quit"
SUCCESS = "Success"

# Add session to pick up where we left off or start from particular state


class Wordle:
    def __init__(self, length=None, answer=None):
        if length is not None and answer is not None:
            assert len(answer) == length, "Answer must match word length"
        length = len(answer) if answer is not None else length
        self.length = length if length is not None else DEFAULT_LETTER_COUNT
        self.all_words = make.possible_words(length=self.length)
        if answer is None:
            self.answer = random.choice(list(self.all_words)).upper()
        else:
            assert set(answer).issubset(
                string.ascii_lowercase
            ), "Answer must be lowecase ascii only"
            self.all_words = self.all_words.union(answer)
            self.answer = answer.upper()
        self.max_attempts = MAX_ATTEMPTS
        self.attempts = {}

    def play(self):
        attempt = 1
        result = FAIL
        while attempt <= self.max_attempts:
            guess = self.guess(attempt)
            response = self.check(guess)
            self.attempts[attempt] = response
            print("{0}> {1} -> {2}".format(attempt, guess, response))
            if response == self.answer:
                result = SUCCESS
                break
            else:
                attempt += 1
        return result

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
        answer = list(self.answer)
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
    parser.add_argument("-a", "--answer", dest="answer", type=str, default=None)
    args = parser.parse_args()
    try:
        wordle = Wordle(answer=args.answer)
        result = wordle.play()
    except KeyboardInterrupt:
        result = "\n" + QUIT
    finally:
        print("{}. Answer: {}".format(result, wordle.answer))


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())  # pragma: no cover
