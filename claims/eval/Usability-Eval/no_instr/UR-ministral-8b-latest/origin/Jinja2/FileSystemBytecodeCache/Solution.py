import os
import hashlib
import pickle
from jinja2 import Environment, FileSystemLoader

class BytecodeCache:
    def __init__(self, cache_dir, pattern):
        self.cache_dir = cache_dir
        self.pattern = pattern
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        self.env = Environment(loader=FileSystemLoader(cache_dir), trim_blocks=True, lstrip_blocks=True)

    def _build_filename(self, obj):
        obj_hash = hashlib.md5(pickle.dumps(obj)).hexdigest()
        return self.pattern.format(obj_hash=obj_hash)

    def get(self, obj):
        filename = self._build_filename(obj)
        cache_file = os.path.join(self.cache_dir, filename)

        if os.path.exists(cache_file):
            with open(cache_file, 'rb') as f:
                return pickle.load(f)

    def set(self, obj, bytecode):
        filename = self._build_filename(obj)
        cache_file = os.path.join(self.cache_dir, filename)

        with open(cache_file, 'wb') as f:
            pickle.dump(bytecode, f)
