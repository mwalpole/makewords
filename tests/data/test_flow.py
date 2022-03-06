import re

import data.flow.util as util


def test_format_dir():
    assert util.format_dir("nltk_data").endswith("raw/en/nltk_data")


def test_format_loc():
    output = util.format_loc(task_name="store_something")
    convention = re.compile(".*/processed/en/store_something_[0-9-]+t[0-9-]+.dat")
    assert convention.match(output)
