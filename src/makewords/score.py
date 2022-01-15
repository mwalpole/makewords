import makewords.util as util


def from_words(df, words=None):
    for word in words:
        for i,j in enumerate(word):
            df.loc[j]['total'] += 1          # total count per letter
            df.loc[j]['z{}'.format(i)] += 1  # count of letter per register
        letter_count = util.count_letters(word)
        for letter,n in letter_count.items():
            df.loc[letter]['n{}'.format(n)] += 1  # count of appearances per word
    return df
