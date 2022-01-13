import textwrap

from nltk.corpus import words as nltklib

import makewords.filters as filters
from makewords.conf import NLTK_DIR

import nltk

# os.environ['NLTK_DATA'] = NLTK_DIR not working
# in the meantime just append the path directly
nltk.data.path.append(NLTK_DIR)


def char_count(word):
    nchars = {}
    for i in word:
        nchars[i] = nchars.get(i, 0) + 1
    return nchars


def _print_message(s):
    """Handle terminal output consistently with nltk."""
    prefix = "[makewords] "
    print(textwrap.fill(s, initial_indent=prefix))


def get_clean_words(words=None):
    if words is None:
        _print_message("Cleaning 'en' wordlist from nltk.")
        words = nltklib.words()
    else:
        _print_message("Using words provided by user.")
    clean_words = set(
        filter(filters.word_does_not_contain_nonascii_lowercase, set(words))
    )
    return clean_words


def possible_words(
    letters, words=None, length=None, mask=None, include=None, exclude=None
):
    """Identify the words that can be made from a list of letters."""
    assert len(letters) > 0, "Must provide at least one letter."
    out = set()
    words = get_clean_words(words=words)
    words = filters.apply(words, length=length, mask=mask, include=include, exclude=exclude)
    for word in words:
        flag = 1
        chars = char_count(word)
        for key in chars:
            if key not in letters:
                flag = 0
            # else:
            #     if letters.count(key) != chars[key]:
            #         flag = 0
        if flag == 1:
            out.add(word)
            print(word)
    return out
