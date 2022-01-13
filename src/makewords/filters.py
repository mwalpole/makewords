import string
from functools import partial

from makewords.conf import MIN_LENGTH


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


def apply(words, length=None, mask=None, include=None, exclude=None):
    all_filters = (
        partial(word_length_at_least, MIN_LENGTH),
        partial(word_length_equals, length),
        partial(word_matches_mask, mask),
        partial(word_contains_letter, include),
        partial(word_contains_excluded_letter, exclude),
    )
    for f in all_filters:
        words = filter(f, words)
    return set(words)
