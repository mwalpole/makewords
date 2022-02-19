import importlib.resources

import makewords.filters

MIN_WORD_LENGTH = 4


def possible_words(
    words=None,
    include=None,
    only=False,
    require=None,
    match_count=False,
    exclude=None,
    length=None,
    at_least=False,
    mask=None,
):
    """Return words from that meet the filter criteria.

    Parameters
    ----------
    words   : [str], optional
        list of words as baseline
    include : str, optional
        use any of these letters
    only    : bool, optional, default is False
        only use included letters
    require : str, optional
        must use these letters
    match_count : bool, optional, default is False
        use the same count of included letters
    exclude : str, optional
        do not use these letters
    length  : int, optional
        make words of this many letters
    at_least : bool, optional, default is False
        make words of at least {length} letters, default 4
    mask    : str, optional
        words should look like this, wildcard is "."
    """
    if include is not None and exclude is not None:
        shared = set(include).intersection(exclude)
        assert not shared, f"Cannot both include and exclude: {','.join(shared)}"
    if mask is not None and length is None:
        length = len(mask)
    if words is None:
        words = importlib.resources.read_text("makewords.data", "words.dat").split("\n")
    min_length = length if at_least else MIN_WORD_LENGTH
    words = makewords.filters.apply(
        words,
        include=include,
        only=only,
        require=require,
        match_count=match_count,
        exclude=exclude,
        length=length,
        min_length=min_length,
        mask=mask,
    )
    return words
