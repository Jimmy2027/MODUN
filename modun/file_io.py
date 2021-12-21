import json
from pathlib import Path


def json2dict(json_path: Path) -> dict:
    with open(json_path, 'rt') as json_file:
        json_config = json.load(json_file)
    return json_config


def dict2json(out_path: Path, d: dict):
    with open(out_path, 'w') as outfile:
        json.dump(d, outfile, indent=2)


def ensure_dir(dirname: Path) -> None:
    """
    Create directory only if it does not exist yet.
    Throw an error otherwise.
    """
    dirname = Path(dirname)
    if not dirname.is_dir():
        dirname.mkdir(parents=True, exist_ok=False)
