"""Base helper class for connections to a MongoDB with python."""
import io
import pickle
from abc import abstractmethod
from pathlib import Path
from bson.binary import Binary
from modun.file_io import json2dict


class BaseMongodbClass(object):
    def __init__(self):
        self.mongodb_URI = self.get_mongodb_uri()

    @abstractmethod
    def get_mongodb_uri(self) -> str:
        pass

    @abstractmethod
    def connect(self):
        pass

    def new_entry(self, data: dict):
        """Add a new entry to the collection."""
        collection = self.connect()
        collection.insert_one(data)

    def add_gridfs_elem(self, filepath: Path, _id=None) -> None:
        fs = self.connect_with_gridfs()
        with io.FileIO(str(filepath), 'r') as fileObject:
            fs.put(fileObject, filename=str(filepath.stem), _id=_id)

    def add_array(self, npArray, filename: str, _id=None):
        fs = self.connect_with_gridfs()
        fs.put(Binary(pickle.dumps(npArray, protocol=2), subtype=128), filename=filename, _id=_id)

    def connect_with_gridfs(self):
        pass
