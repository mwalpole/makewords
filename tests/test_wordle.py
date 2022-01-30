import pytest
from unittest.mock import patch

import makewords.game.wordle as wordle


@pytest.fixture
def game():
    return wordle.Wordle(word="benne")


def test_game_target_is_upper(game):
    assert game.target == game.target.upper()


def test_game_rule_one_only_caps(game):
    output = game.check("melee")
    assert output == ".E..E"


def test_game_rule_two_no_duplicates(game):
    output = game.check("meees")
    assert output == ".Ee.."


def test_game_win(game):
    output = game.check("benne")
    assert output == "BENNE"


def test_random_choice():
    config = {"possible_words.return_value": set(["foobar"])}
    patcher = patch("makewords.game.wordle.make", **config)
    mock_possible_words = patcher.start()
    output = wordle.Wordle()
    mock_possible_words.possible_words.assert_called_once_with(length=wordle.DEFAULT_LETTER_COUNT)
    assert output.target == "FOOBAR"