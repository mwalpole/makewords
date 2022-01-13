import string
import textwrap

from nltk.corpus import words as nltklib

import makewords.filters as filters
from makewords.conf import NLTK_DIR

import nltk

# os.environ['NLTK_DATA'] = NLTK_DIR not working
# in the meantime just append the path directly
nltk.data.path.append(NLTK_DIR)


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
    words=None, length=None, mask=None, include=None, only=False, exclude=None, repeats=True
):
    """Identify the words that can be made from a list of letters."""
    words = get_clean_words(words=words)
    allow = set(string.ascii_lowercase).difference(exclude) if only else include
    words = filters.apply(words, length=length, mask=mask, include=allow, exclude=exclude, repeats=repeats)
    return words
