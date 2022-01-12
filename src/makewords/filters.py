from functools import partial


def word_length_equals(length, word):
    flag = True
    if length is not None:
        if len(word) != length:
            flag = False
    return flag


def word_matches_mask(mask, word):
    flag = True
    if mask is not None:
        for i,j in enumerate(mask):
            if j == '*':
                continue
            else:
                if word[i] != j:
                    flag = False
    return flag


def word_contains_letter(letter, word):
    flag = True
    if letter is not None:
        if letter not in word:
            flag = False
    return flag


def word_contains_excluded_letter(exclude, word):
    flag = True
    if exclude is not None:
        for letter in exclude:
            if letter in word:
                flag = False
                break
    return flag


def apply(words, length=None, mask=None, letter=None, exclude=None):
    all_filters = (
        partial(word_length_equals, length),
        partial(word_matches_mask, mask),
        partial(word_contains_letter, letter),
        partial(word_contains_excluded_letter, exclude)
    )
    for f in all_filters:
        words = filter(f, words)
    return words
