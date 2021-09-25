from typing import Mapping, Union


def flatten_dict(d: Mapping[str, Union[dict, any]]) -> dict:
    """
    Merge keys from a two level nested dict with '__'.
    All elements that only have one level are kept as they are.

    >>> d = {'a': {'b':1},'c':2}
    >>> flatten_dict(d)
    {'a__b':1, 'c':2}
    """
    d_ = {}
    for k1, v1 in d.items():
        if isinstance(v1, dict):
            for k2, v2 in v1.items():
                d_[f'{k1}__{k2}'] = v2
        else:
            d_[k1] = v1
    return d_
