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
    clean_words = set(filter(filters.word_is_ascii_lowercase, set(words)))
    return clean_words


def possible_words(
    words=None,
    include=None,
    only=False,
    match_count=False,
    exclude=None,
    length=None,
    mask=None,
):
    """Identify the words that can be made from a list of letters.

    Parameters
    ----------
    words   : [str], optional
        Set of words, superset of what will be returned.
    include : str, optional
        Letters to include in our search.
    only    : bool, optional, default is False
        Include only these letters or allow others.
    match_count : bool, optional, default is False
        Match the count of each letter from include exactly.
    exclude : str, optional
        Letters to exclude from our words.
    length  : int, optional
        Length of search words.
    mask    : str, optional
        Use . wildcard, e.g. "f...ar" will match "foobar".
    """
    words = get_clean_words(words=words)
    words = filters.apply(
        words,
        include=include,
        only=only,
        match_count=match_count,
        exclude=exclude,
        length=length,
        mask=mask,
    )
    return words
