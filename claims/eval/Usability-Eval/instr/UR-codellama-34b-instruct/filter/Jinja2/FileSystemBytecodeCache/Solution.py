
import jinja2

cache_dir = '/path/to/cache/directory'
pattern = 'bytecode_{{ filename }}.pyc'

class BytecodeCache(object):
    def __init__(self, cache_dir, pattern):
        self.cache_dir = cache_dir
        self.pattern = pattern

    def get(self, key):
        return self._read(key)

    def set(self, key, value):
        self._write(key, value)

    def _read(self, key):
        filename = self._get_filename(key)
        with open(filename, 'rb') as f:
            data = f.read()
        return data

    def _write(self, key, value):
        filename = self._get_filename(key)
        with open(filename, 'wb') as f:
            f.write(value)

    def _get_filename(self, key):
        return pattern.format(filename=key)
