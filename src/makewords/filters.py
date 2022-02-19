import collections
import string
from functools import partial


def word_length_equals(length, word):
    flag = True
    if length is not None:
        if len(word) != length:
            flag = False
    return flag


def word_length_at_least(min_length, word):
    flag = True
    if min_length is not None:
        if len(word) < min_length:
            flag = False
    return flag


def word_matches_mask(mask, word):
    flag = True
    if mask is not None:
        for i, j in enumerate(mask):
            if j == ".":
                continue
            else:
                if word[i] != j:
                    flag = False
                    break
    return flag


def word_contains_letter(include, only, require, word):
    flag = True
    if include is not None:
        if only:
            flag = set(word).issubset(include)
        else:
            for letter in include:
                if letter not in word:
                    flag = False
                    break
    if flag and require is not None:
        flag = set(require).issubset(word)
    return flag


def word_contains_excluded_letter(exclude, word):
    flag = True
    if exclude is not None:
        for letter in exclude:
            if letter in word:
                flag = False
                break
    return flag


def word_is_ascii_lowercase(word):
    return not set(word).difference(string.ascii_lowercase)


def word_matches_letter_count_from_include(include, match_count, word):
    flag = True
    if match_count:
        letter_count = collections.Counter(word)
        for letter in include:
            if include.count(letter) != letter_count[letter]:
                flag = False
    return flag


def many(filters, iterable):
    for f in filters:
        iterable = filter(f, iterable)
    return set(iterable)


def apply(
    words,
    include=None,
    only=False,
    require=None,
    match_count=False,
    exclude=None,
    length=None,
    min_length=None,
    mask=None,
):
    filters = (
        partial(word_length_equals, length),
        partial(word_length_at_least, min_length),
        partial(word_matches_mask, mask),
        partial(word_contains_letter, include, only, require),
        partial(word_contains_excluded_letter, exclude),
        partial(word_matches_letter_count_from_include, include, match_count),
    )
    return many(filters, words)
