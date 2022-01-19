import pytest

import makewords.filters as filters


def test_word_length_equals():
    assert filters.word_length_equals(4, "foob")


def test_word_length_at_least():
    assert filters.word_length_at_least(4, "foob")
    assert filters.word_length_at_least(4, "foobar")
    assert filters.word_length_at_least(None, "foobar")


def test_word_matches_mask():
    assert filters.word_matches_mask("fo.b", "foob")


def test_word_contains_letter():
    assert filters.word_contains_letter("b", False, "foob")


def test_word_contains_letter_include_none():
    assert filters.word_contains_letter(None, False, "foob")


def test_word_contains_excluded_letter():
    assert filters.word_contains_excluded_letter("z", "foobar")


def test_word_is_ascii_lowercase():
    assert filters.word_is_ascii_lowercase("foob")


def test_word_includes_allowed_letters_only():
    assert filters.word_includes_allowed_letters_only(
        include="fobaro", repeats=False, word="foobar"
    )


def test_fail_word_length_equals():
    with pytest.raises(AssertionError):
        assert filters.word_length_equals(4, "foobar")

    with pytest.raises(AssertionError):
        assert filters.word_length_equals(4, "baz")


def test_fail_word_length_at_least():
    with pytest.raises(AssertionError):
        assert filters.word_length_at_least(4, "foo")

    with pytest.raises(AssertionError):
        assert filters.word_length_at_least(7, "foobar")


def test_apply_iterative_filters():
    assert set() == filters.apply(["foo"])
    assert set(["foobar"]) == filters.apply(words=["foobar"], include="fobar")
    assert set() == filters.apply(["foobar"], include="fobar", length=5)
    assert set(["foobar"]) == filters.apply(["foobar"], include="fobar", length=6)
    assert set(["foobar"]) == filters.apply(["foobar"], include="fobar", mask="f.....")
    assert set(["foobar"]) == filters.apply(["foobar"], include="fobar", mask="......")
    assert set() == filters.apply(["foobar"], include="z")
    assert set() == filters.apply(["baz"], exclude="z")


def test_fail_word_matches_mask():
    with pytest.raises(AssertionError):
        assert filters.word_matches_mask("fo.b", "frob")


def test_fail_word_contains_letter():
    with pytest.raises(AssertionError):
        assert filters.word_contains_letter(include="x", only=True, word="foob")


def test_fail_word_contains_excluded_letter():
    with pytest.raises(AssertionError):
        assert filters.word_contains_excluded_letter("z", "baz")


def test_fail_word_is_ascii_lowercase():
    with pytest.raises(AssertionError):
        assert filters.word_is_ascii_lowercase("foo-bar")

    with pytest.raises(AssertionError):
        assert filters.word_is_ascii_lowercase("Foob")


def test_word_includes_allowed_letters_only():
    with pytest.raises(AssertionError):
        assert filters.word_includes_allowed_letters_only(
            include="fobar", repeats=False, word="foobar"
        )
