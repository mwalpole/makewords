import nltk
from nltk.corpus import words as nltklib

import makewords.filters as filters
import makewords.conf as conf
import makewords.util as util

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
    """Identify words that can be made from a list of letters.

    Parameters
    ----------
    words   : [str], optional
        list of words as baseline
    include : str, optional
        use these letters
    only    : bool, optional, default is False
        only use included letters
    match_count : bool, optional, default is False
        use the same count of included letters
    exclude : str, optional
        do not use these letters
    length  : int, optional
        make words of this many letters
    mask    : str, optional
        words should look like this, wildcard is "."
    """
    if include is not None and exclude is not None:
        shared = set(include).intersection(exclude)
        assert not shared, "Cannot include and exclude the same letter(s): {}".format(", ".join(shared)) 

    if mask is not None and length is None:
        length = len(mask)

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
