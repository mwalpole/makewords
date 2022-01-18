import string

from nltk.corpus import words as nltklib

import makewords.filters as filters
import makewords.conf as conf
import makewords.util as util

import nltk

# os.environ['NLTK_DATA'] = NLTK_DIR not working
# in the meantime just append the path directly
nltk.data.path.append(conf.NLTK_DIR)


def get_clean_words(words=None):
    """Retrieve and clean words from NLTK or custom list.
    
    Cleaning here amounts to dropping words with captials 
    or non-ascii characters.
    """
    if words is None:
        util.print_message("Cleaning 'en' wordlist from nltk.")
        words = nltklib.words()
    else:
        util.print_message("Using words provided by user.")
    clean_words = set(
        filter(filters.word_is_ascii_lowercase, set(words))
    )
    return clean_words


def possible_words(
    words=None,
    include=None,
    only=False,
    exclude=None,
    length=None,
    mask=None,
    repeats=True,
):
    """Identify the words that can be made from a list of letters.

    Parameters
    ----------
    words   : [str], optional
        Set of words, superset of what will be returned.
    include : str, optional
        Letters to include in our search.
    only    : bool, optional
        Include only these letters or allow others.
    exclude : str, optional
        Letters to exclude from our words.
    length  : int, optional
        Length of search words.
    mask    : str, optional
        Use * wildcard, e.g. "f***ar" will match "foobar".
    repeats : bool, optional
        Allow included letters to be repeated or match exactly.
    """
    words = get_clean_words(words=words)
    include = include if include is not None else string.ascii_lowercase
    exclude = exclude if exclude is not None else ""
    allow = set(include).difference(exclude) if only else include
    words = filters.apply(
        words, include=allow, exclude=exclude, length=length, mask=mask, repeats=repeats
    )
    return words
