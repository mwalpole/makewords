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
    assert filters.word_contains_letter("b", False, None, "foob")


def test_word_contains_only_included_letters():
    assert filters.word_contains_letter("fobar", True, None, "foobar")
    assert not filters.word_contains_letter("fobar", True, None, "foobaz")


def test_word_must_include_required_letters():
    assert filters.word_contains_letter("b", False, "f", "foob")
    assert not filters.word_contains_letter("b", False, "r", "foob")


def test_word_contains_letter_include_none():
    assert filters.word_contains_letter(None, False, None, "foob")


def test_word_contains_excluded_letter():
    assert filters.word_contains_excluded_letter("z", "foobar")


def test_word_is_ascii_lowercase():
    assert filters.word_is_ascii_lowercase("foob")


def test_word_matches_letter_count_from_include():
    assert filters.word_matches_letter_count_from_include(
        include="fobaro", match_count=True, word="foobar"
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
        assert filters.word_contains_letter(
            include="foobar", only=True, require=None, word="foobaz"
        )


def test_fail_word_contains_excluded_letter():
    with pytest.raises(AssertionError):
        assert filters.word_contains_excluded_letter("z", "baz")


def test_fail_word_is_ascii_lowercase():
    with pytest.raises(AssertionError):
        assert filters.word_is_ascii_lowercase("foo-bar")

    with pytest.raises(AssertionError):
        assert filters.word_is_ascii_lowercase("Foob")


def test_fail_word_matches_specified_count_of_letters_to_include():
    with pytest.raises(AssertionError):
        assert filters.word_matches_letter_count_from_include(
            include="fobar", match_count=True, word="foobar"
        )
