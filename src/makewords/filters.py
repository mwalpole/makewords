import string
from functools import partial

from makewords.conf import MIN_LENGTH
from makewords.util import letter_count


def word_length_equals(length, word):
    flag = True
    if length is not None:
        if len(word) != length:
            flag = False
    return flag


def word_length_at_least(length, word):
    flag = True
    if length is not None:
        if len(word) < length:
            flag = False
    return flag


def word_matches_mask(mask, word):
    flag = True
    if mask is not None:
        for i, j in enumerate(mask):
            if j == "*":
                continue
            else:
                if word[i] != j:
                    flag = False
                    break
    return flag


def word_contains_letter(include, word):
    flag = True
    if include is not None:
        for letter in include:
            if letter not in word:
                flag = False
                break
    return flag


def word_contains_excluded_letter(exclude, word):
    flag = True
    if exclude is not None:
        for letter in exclude:
            if letter in word:
                flag = False
                break
    return flag


def word_does_not_contain_nonascii_lowercase(word):
    return not set(word).difference(string.ascii_lowercase)


def word_includes_allowed_letters_only(include, repeats, word):
    flag = True
    letters = letter_count(word)
    for letter in letters:
        if letter not in include:
            flag = False
        else:
            if repeats and include.count(letter) != letters[letter]:
                flag = False
    return flag


def apply(words, length=None, mask=None, include=None, exclude=None, repeats=None):
    all_filters = (
        partial(word_length_at_least, MIN_LENGTH),
        partial(word_length_equals, length),
        partial(word_matches_mask, mask),
        partial(word_contains_letter, include),
        partial(word_contains_excluded_letter, exclude),
        partial(word_includes_allowed_letters_only, include, repeats)
    )
    for f in all_filters:
        words = filter(f, words)
    return set(words)
