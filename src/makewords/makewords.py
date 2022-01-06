import os
import textwrap

import nltk
from nltk.corpus import words as nltklib 
from .config.const import ROOT_DIR


def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def _print_message(s):
    '''Handle terminal output consistently with nltk.'''
    prefix = '[makewords] '
    print(
        textwrap.fill(
            s,
            initial_indent=prefix
        )
    )


def possibleWords(letters, words=None):
    '''Identify the words that can be made from a list of letters.'''
    if words is None:
        _print_message('Using en wordlist sourced from nltk.')
        nltk_dir = os.path.join(ROOT_DIR, 'nltk_data')
        nltk.download('words', download_dir=nltk_dir, quiet=False)
        words = nltklib.words()
    else:
        _print_message('Using words provided by user.')
    mustHave = letters[0]
    for word in words:
        flag = 1
        chars = charCount(word)
        if mustHave not in word:
            continue
        if len(word) < 4:
            continue
        for key in chars:
            if key not in letters:
                flag = 0
            # else:
                # if letters.count(key) != chars[key]:
                    # flag = 0
        if flag == 1:
            print(word)
