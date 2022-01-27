import subprocess
import sys

import pytest 

import makewords
from makewords.__main__ import main

LTRS_1 = "fobar"
WREF_1 = set(["foobar", "foob"])
LTRS_2 = "baz"


def test_favor():
    output = makewords.possible_words(
        words=["favor", "fosta"], include="vfaro", exclude="clstdbhygn", length=5
    )
    assert "favor" in output


def test_output_is_not_always_empty():
    output = makewords.possible_words(words=WREF_1)
    assert output == WREF_1


def test_output_can_be_empty():
    output = makewords.possible_words(words=WREF_1, include=LTRS_2)
    assert output == set()


def test_include_empty_string():
    output = makewords.possible_words(words=WREF_1, include="")
    assert isinstance(output, set)


def test_nltk():
    output = makewords.possible_words(include="make", length=4)
    assert "make" in output


def test_main():
    process = subprocess.Popen(
        [sys.executable, "-m", "makewords", "--words=talo"], stdout=subprocess.PIPE
    )
    out, _ = process.communicate()
    assert not process.returncode
    assert out


def test_main_with_print():
    process = subprocess.Popen(
        [sys.executable, "-m", "makewords", "--words=talo", "--print=True"], stdout=subprocess.PIPE
    )
    out, _ = process.communicate()
    assert not process.returncode
    assert out


def test_main_arg_fail():
    with pytest.raises(AssertionError):
        process = subprocess.Popen(
            [sys.executable, "-m", "makewords", "unrecognized", "arguments"], stdout=subprocess.PIPE
        )
        out, _ = process.communicate()
        assert not process.returncode
