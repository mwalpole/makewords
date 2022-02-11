import string
import subprocess
import sys

import pytest

import makewords
from makewords.__main__ import main

WORD_1 = "foobar"
WORD_2 = "foob"
WORDS = set([WORD_1, WORD_2])


def test_output_is_not_always_empty():
    output = makewords.possible_words(words=WORDS)
    assert output == WORDS


def test_no_words_output():
    others = set(string.ascii_lowercase).difference("".join(WORDS))
    output = makewords.possible_words(words=WORDS, include=others)
    assert output == set()


def test_include_empty_string():
    output = makewords.possible_words(words=WORDS, include="")
    assert isinstance(output, set)


def test_exclude_two_letters():
    output = makewords.possible_words(
        words=["foobar", "foobaz", "foobay", "bubbub"],
        include="faro",
        exclude="zy",
        length=6,
    )
    assert set(["foobar"]) == output


def test_include_and_exclude_same_letter_fails():
    with pytest.raises(AssertionError):
        makewords.possible_words(include="ab", exclude="bc")


def test_length_matches_mask():
    output = makewords.possible_words(words=WORDS, mask="." * len(WORD_1))
    assert output == set([WORD_1])


def test_random_word():
    output = makewords.possible_words(include="make", length=4)
    assert "make" in output


def test_main():
    process = subprocess.Popen(
        [sys.executable, "-m", "makewords", "--words=talo"], stdout=subprocess.PIPE
    )
    out, _ = process.communicate()
    assert not process.returncode
    assert out


def test_main_arg_fail():
    with pytest.raises(AssertionError):
        process = subprocess.Popen(
            [sys.executable, "-m", "makewords", "unrecognized", "arguments"],
            stdout=subprocess.PIPE,
        )
        out, _ = process.communicate()
        assert not process.returncode
