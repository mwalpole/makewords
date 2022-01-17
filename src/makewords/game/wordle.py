# Simulate playing Wordle from CLI
# Choose a five letter word and build words corpus
# Apply rules, identify acceptable guess and provide feedback
# Score session
import random
import sys

import makewords.makewords as make
import makewords.util as util

N=5


class Wordle():
    def __init__(self, length=None):
        if length is None:
            length = N
        self.all_words = make.possible_words(length=length)
        self.target = random.choice(list(self.all_words)).upper()
        self.target_count = util.count_letters(self.target)

    def play(self):
        turn = 1
        while turn < 7:
            guess = self.guess(turn)
            result = self.assess(guess)
            self.respond(result, turn)
            turn += 1
        print("Done. The word is {}.".format(self.target))

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
        
        Print a capital letter for a letter in the correct place.
        Print a lower case letter for each appearance of that letter in the word.
        """
        result = {
            "guess": guess,
            "result": "",
            "exclude": ""
        }
        guess = guess.upper()
        letter_count = {}
        for i,letter in enumerate(guess):
            letter_count[letter] = letter_count.get(i, 0) + 1
            if letter == self.target[i]:
                result['result'] += letter
            elif letter in self.target and letter_count.get(letter) <= self.target_count[letter]:
                result['result'] += letter.lower()
            else:
                result['result'] += "."
                result['exclude'] += letter.lower()
        return result

    def respond(self, result, turn):
        print(
            "{turn}> {guess} -> {result}".format(
                turn=turn,
                guess=result["guess"].upper(),
                result=result["result"]
            )
        )


def main():
    wordle = Wordle()
    wordle.play()


if __name__ == "__main__":
    sys.exit(main())