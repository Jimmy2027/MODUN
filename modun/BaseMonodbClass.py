"""Base helper class for connections to a MongoDB with python."""
from pathlib import Path

from modun.file_io import json2dict


class BaseMongodbClass(object):
    @staticmethod
    def get_mongodb_uri():
        dbconfig = json2dict(Path('~/.config/mmvaedb.json').expanduser())
        return dbconfig['mongodb_URI']
