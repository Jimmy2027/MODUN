import json
from pathlib import Path


def json2dict(json_path: Path) -> dict:
    with open(json_path, 'rt') as json_file:
        json_config = json.load(json_file)
    return json_config
