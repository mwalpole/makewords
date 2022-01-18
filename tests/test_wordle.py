import pytest

import makewords.game.wordle as wordle


@pytest.fixture
def game():
    return wordle.Wordle(word="benne")


def test_game_target_is_upper(game):
    assert game.target == game.target.upper()


def test_game_rule_one_only_caps(game):
    output = game.assess("melee")
    assert output == ".E..E"


def test_game_rule_two_no_duplicates(game):
    output = game.assess("meees")
    assert output == ".Ee.."


def test_game_win(game):
    output = game.assess("benne")
    assert output == "BENNE"
