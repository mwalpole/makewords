import makewords


def test_output_is_not_always_empty():
    output = makewords.possibleWords('fobar', ('foobar','roof'))
    assert output == ['foobar', 'roof']


def test_output_can_be_empty():
    output = makewords.possibleWords('baz', ('foobar','roof'))
    assert output == []
