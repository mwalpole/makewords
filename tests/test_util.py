from makewords.util import count_letters


def test_count_letters():
    output = count_letters('foobar')
    assert output == {'f': 1, 'o': 2, 'b': 1, 'a': 1, 'r': 1}


def test_count_letters_returns_empty_dict():
    output = count_letters('')
    assert output == {}
