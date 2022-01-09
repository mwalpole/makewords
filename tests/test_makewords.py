import subprocess
import sys

import pytest

import makewords
from makewords.__main__ import main

LTRS_1 = "fobar"
WREF_1 = ["foobar", "foob"]
LTRS_2 = "baz"


def test_output_is_not_always_empty():
    output = makewords.possible_words(LTRS_1, WREF_1)
    assert output == WREF_1


def test_output_can_be_empty():
    output = makewords.possible_words(LTRS_2, WREF_1)
    assert output == []


def test_empty_string():
    with pytest.raises(AssertionError):
        makewords.possible_words("")


def test_nltk():
    output = makewords.possible_words("make")
    assert "make" in output


def test_main():
    process = subprocess.Popen(
        [sys.executable, "-m", "makewords"], stdout=subprocess.PIPE
    )
    out, _ = process.communicate()
    assert not process.returncode
    assert out


def test_main_args():
    pass
