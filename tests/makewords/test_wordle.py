import pytest
from unittest.mock import patch

import makewords.game.wordle as wordle


@pytest.fixture
def game():
    return wordle.Wordle(answer="foobar", length=6)


def test_game_answer_is_upper(game):
    assert game.answer == game.answer.upper()


def test_game_rule_one_only_caps(game):
    output = game.check("oooooo")
    assert output == ".OO..."


def test_game_rule_two_no_duplicates(game):
    output = game.check("ooeeee")
    assert output == "oO...."


def test_game_win(game):
    output = game.check("foobar")
    assert output == "FOOBAR"


def test_answer_match_length_fail():
    with pytest.raises(AssertionError):
        wordle.Wordle(answer="foobar", length=5)


def test_answer_from_possible_words():
    config = {"possible_words.return_value": set(["foobar"])}
    patcher = patch("makewords.game.wordle.make", **config)
    mock_possible_words = patcher.start()
    game = wordle.Wordle()
    mock_possible_words.possible_words.assert_called_once_with(
        length=wordle.DEFAULT_LETTER_COUNT
    )
    assert game.answer == "FOOBAR"


@patch("makewords.game.wordle.Wordle.guess")
def test_game_play_success(guess):
    game = wordle.Wordle(answer="foobar")
    guess.side_effect = ["foofoo", "foobar"]
    result = game.play()
    assert result == wordle.SUCCESS
    assert len(game.attempts) == 2


@patch("makewords.game.wordle.Wordle.guess")
def test_game_play_fail(guess):
    game = wordle.Wordle(answer="foobar")
    guess.side_effect = ["foofoo"] * wordle.MAX_ATTEMPTS
    result = game.play()
    assert result == wordle.FAIL
    assert len(game.attempts) == wordle.MAX_ATTEMPTS
