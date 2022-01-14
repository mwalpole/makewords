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
    words=None, include=None, only=False, exclude=None, length=None, mask=None, repeats=True
):
    """Identify the words that can be made from a list of letters.

    words   [str]   set of words, superset of what will be returned
    include str     letters to include in our search
    only    bool    include only these letters or allow others
    exclude str     letters to exclude from our words
    length  int     length of search words
    mask    str     use * wildcard, e.g. "f***ar" will match "foobar"
    repeats bool    allow included letters to be repeated or match exactly
    """
    words = get_clean_words(words=words)
    include = include if include is not None else string.ascii_lowercase
    exclude = exclude if exclude is not None else ''
    allow = set(include).difference(exclude) if only else include
    words = filters.apply(words, include=allow, exclude=exclude, length=length, mask=mask, repeats=repeats)
    return words
