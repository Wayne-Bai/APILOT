
import jinja2

class BytecodeCache:
    def __init__(self, cache_dir, pattern):
        self.cache_dir = cache_dir
        self.pattern = pattern

    def store(self, key, value):
        filename = self._get_filename(key)
        with open(filename, 'wb') as f:
            f.write(value)

    def load(self, key):
        filename = self._get_filename(key)
        if not os.path.exists(filename):
            return None
        with open(filename, 'rb') as f:
            return f.read()

    def _get_filename(self, key):
        hashed_key = hashlib.sha256(str(key).encode('utf-8')).hexdigest()
        filename = self.pattern % (hashed_key[:10],)
        return os.path.join(self.cache_dir, filename)
