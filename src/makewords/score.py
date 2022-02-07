import string

import makewords.util as util
import makewords.makewords as make


def lfreq(df, words=None):
    """Return letter frequency."""
    for word in words:
        for i, j in enumerate(word):
            df.loc[j]["total"] += 1  # total count per letter
            df.loc[j]["z{}".format(i)] += 1  # count of letter per register
        letter_count = util.count_letters(word)
        for letter, n in letter_count.items():
            df.loc[letter]["n{}".format(n)] += 1  # count of appearances per word
    return df


def top(df, k=5, l=5, m=12, additional=None):
    """Return top k l-character words based on top m letter frequency.
    
    Optionally explicitly include additional words for scoring.
    """
    # Take the M most common letters, e.g. ['a', 'e'...]
    chars = (
        df['total']
        .sort_values(axis='index', ascending=False)
        .head(m)
        .keys()
        .to_list()
    )
    exclude = set(string.ascii_lowercase).difference(chars)
    words = make.possible_words(exclude="".join(exclude), length=l)
    if additional is not None:
        words = words.union(additional.split(","))
    scores = {}
    for word in words:
        score = 0
        for i, letter in enumerate(word):
            score += df.get("z{}".format(i))[letter]
        scores[word] = score
    return scores
