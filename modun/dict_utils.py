import json
from collections import namedtuple
from collections.abc import MutableMapping
from pathlib import Path


def flatten_dict(d: MutableMapping, parent_key='', sep='__') -> dict:
    """
    Merge keys from a nested dict with '__'.
    All elements that only have one level are kept as they are.

    >>> d = {'a': {'b':1},'c':2}
    >>> flatten_dict(d)
    {'a__b': 1, 'c': 2}
    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def dict2pyobject(d: dict, name: str = 'mystruct') -> namedtuple:
    """Convert dict to an immutable object."""
    MyStruct = namedtuple(name, ' '.join(d))
    return MyStruct(**d)


def dict2object(d: dict) -> namedtuple:
    """Convert dict to an mutable object."""

    class MyClass:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    return MyClass(**d)


def write2json(json_fn: Path, parameters: list):
    """
    Load jsonfile, write values to it and save it.
    parameters: list of tuples. Example [('model.use_cuda',VALUE),] where VALUE is the parameter to be set
    """
    with open(json_fn) as file:
        d = json.load(file)

    for parameter, value in parameters:
        keys = parameter.split('.')

        if len(keys) == 1:
            d[keys[0]] = value
        else:
            split = parameter.split('.')
            key = d[split[0]]
            for idx in range(1, len(split) - 1):
                key = key[split[idx]]
            key[split[-1]] = value

    with open(json_fn, 'w') as outfile:
        json.dump(d, outfile, indent=4)
