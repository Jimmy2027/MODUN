import json
from collections import namedtuple
from pathlib import Path
from collections.abc import MutableMapping


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


def write_to_jsonfile(config_path: Path, parameters: list):
    """
    parameters: list of tuples. Example [('model.use_cuda',VALUE),] where VALUE is the parameter to be set
    """
    with open(config_path) as file:
        config = json.load(file)
    for parameter, value in parameters:
        split = parameter.split('.')
        key = config[split[0]]
        for idx in range(1, len(split) - 1):
            key = key[split[idx]]
        key[split[-1]] = value

    with open(config_path, 'w') as outfile:
        json.dump(config, outfile, indent=4)
