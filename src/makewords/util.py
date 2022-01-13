def letter_count(word):
    nchars = {}
    for i in word:
        nchars[i] = nchars.get(i, 0) + 1
    return nchars
