import unittest
from pathlib import Path

import pytest

from modun.dict_utils import write2json
from modun.file_io import dict2json, json2dict

TOY_DICT1 = {
    "key1": {"key1_2": 1}
}


@pytest.mark.parametrize("toy_dict, param_key, result_dict", [
    (TOY_DICT1, "key1.key1_2",
     {"key1": {"key1_2": 12}}),
    (TOY_DICT1, "key1",
     {"key1": 12}),
    # todo this fails.
    # (TOY_DICT1, "key1.key1_2.key1_3",
    #  {"key1": {"key1_2": {"key1_3": 12}}}),
    ({}, "key1",
     {"key1": 12}),
])
def test_write2dict(toy_dict: dict, param_key: str, result_dict: dict):
    """
    Store toy json file, write to it and verify that the result looks as expected.
    """

    toy_json_fn = Path(__file__).parent / 'data/toy_json.json'
    dict2json(out_path=toy_json_fn, d=toy_dict)
    write2json(json_fn=toy_json_fn, parameters=[(param_key, 12)])

    new_toy_dict = json2dict(json_path=toy_json_fn)

    unittest.TestCase().assertDictEqual(new_toy_dict, result_dict)


if __name__ == '__main__':
    test_write2dict(param_key="key1", result_dict={"key1": 12})
    test_write2dict(param_key="key1.key1_2", result_dict={"key1": {"key1_2": 12}})
