import importlib.resources

import makewords.filters


def possible_words(
    words=None,
    include=None,
    only=False,
    match_count=False,
    exclude=None,
    length=None,
    mask=None,
):
    """Return words from that meet the filter criteria.

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
        assert not shared, f"Cannot both include and exclude: {','.join(shared)}"
    if mask is not None and length is None:
        length = len(mask)
    if words is None:
        words = importlib.resources.read_text("makewords.data", "words.dat").split("\n")
    words = makewords.filters.apply(
        words,
        include=include,
        only=only,
        match_count=match_count,
        exclude=exclude,
        length=length,
        mask=mask,
    )
    return words
