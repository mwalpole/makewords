
import argparse
from itertools import permutations

import nltk
from nltk.corpus import words as nltklib 


def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def possibleWords(allWords, charSet):
    mustHave = charSet[0]
    for word in allWords:
        flag = 1
        chars = charCount(word)
        if mustHave not in word:
            continue
        if len(word) < 4:
            continue
        for key in chars:
            if key not in charSet:
                flag = 0
            # else:
                # if charSet.count(key) != chars[key]:
                    # flag = 0
        if flag == 1:
            print(word)
  

def runner(charSet):
    nltk.download('words')
    input = nltklib.words()
    charSet = list('ozngiat')
    possibleWords(input, charSet)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description='')
    parser.add_argument(
        'integers', metavar='int', nargs='+', type=int,
        help='an integer to be summed')
    parser.add_argument(
    '--log', default=sys.stdout, type=argparse.FileType('w'),
    help='the file where the sum should be written')
    args = parser.parse_args()

    charSet = args[0]
    runner(charSet)