import pytest
import re

import data.flow.util as util


def test_format_dir():
    assert util.format_dir("nltk_data").endswith("raw/en/nltk_data")


def test_format_loc():
    output = util.format_loc(task_name="store_something")
    convention = re.compile(".*/processed/en/store_something_[0-9-]+t[0-9-]+.dat")
    assert convention.match(output)


@pytest.fixture
def readable_list_serializer():
    return util.ReadableListSerializer()


def test_readable_list_deserialize(readable_list_serializer):
    output = readable_list_serializer.deserialize(b"test\ntest")
    assert output == ["test", "test"]


def test_readable_list_serialize(readable_list_serializer):
    output = readable_list_serializer.serialize(["test", "test"])
    assert output == b"test\ntest"


@pytest.fixture
def readable_dict_serializer():
    return util.ReadableDictSerializer()


def test_readable_dict_deserialize(readable_dict_serializer):
    output = readable_dict_serializer.deserialize(b"test,2\nother,1")
    assert output == {"test": 2, "other": 1}


def test_readable_dict_serialize(readable_dict_serializer):
    output = readable_dict_serializer.serialize({"test": 2, "other": 1})
    assert output == b"test,2\nother,1"
